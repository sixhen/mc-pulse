import argparse
import sys
import shutil
from pathlib import Path
from mcpulse import __version__
from mcpulse.rules import RULES

# ANSI Color formatting
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[38;5;48m"
RED = "\033[38;5;196m"
YELLOW = "\033[38;5;220m"
BLUE = "\033[38;5;39m"
PURPLE = "\033[38;5;141m"
GRAY = "\033[38;5;242m"

def print_banner():
    art = """
  __  __  _____      ____  _   _ _     ____  _____ 
 |  \\/  |/ ____|    |  _ \\| | | | |   / ___|| ____|
 | |\\/| | |   ______| |_) | | | | |   \\___ \\|  _|  
 | |  | | |__|______|  __/| |_| | |___ ___) | |___ 
 |_|  |_|\\_____|    |_|    \\___/|_____|____/|_____|
"""
    print(f"{PURPLE}{BOLD}{art}{RESET}{GRAY}  Minecraft TPS Optimizer v{__version__} · by sixhen{RESET}\n")

def parse_server_properties(filepath: Path) -> dict:
    props = {}
    if not filepath.is_file():
        return props
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                props[key.strip()] = val.strip()
    return props

def audit_directory(server_dir: Path):
    print_banner()
    print(f"{BLUE}::{RESET} Scanning server directory: {BOLD}{server_dir.resolve()}{RESET}\n")

    total_checks = 0
    passed_checks = 0
    issues = []

    # 1. Audit server.properties
    sp_path = server_dir / "server.properties"
    if sp_path.exists():
        props = parse_server_properties(sp_path)
        for key, info in RULES.get("server.properties", {}).items():
            total_checks += 1
            cur_val = props.get(key)
            rec_val = info["recommended"]
            if cur_val is not None and str(cur_val) == str(rec_val):
                passed_checks += 1
            else:
                issues.append({
                    "file": "server.properties",
                    "key": key,
                    "current": cur_val if cur_val is not None else "<missing>",
                    "recommended": rec_val,
                    "desc": info["desc"]
                })
    else:
        print(f"{YELLOW}!{RESET} server.properties not found in current directory.\n")

    # Display Report
    score = int((passed_checks / max(1, total_checks)) * 100) if total_checks else 0
    score_color = GREEN if score >= 80 else (YELLOW if score >= 50 else RED)

    print(f"{BOLD}PERFORMANCE AUDIT RESULTS:{RESET}")
    print(f"  Health Score: {score_color}{BOLD}{score}%{RESET} ({passed_checks}/{total_checks} settings optimal)\n")

    if issues:
        print(f"{BOLD}DETECTED BOTTLENECKS:{RESET}")
        for idx, item in enumerate(issues, 1):
            print(f"  {idx}. {YELLOW}{item['file']}{RESET} &bull; {BOLD}{item['key']}{RESET}")
            print(f"     Current:     {RED}{item['current']}{RESET}")
            print(f"     Recommended: {GREEN}{item['recommended']}{RESET}")
            print(f"     Impact:      {GRAY}{item['desc']}{RESET}\n")

        print(f"{GRAY}Run 'mcpulse --fix' to automatically patch server.properties with backup.{RESET}\n")
    else:
        print(f"{GREEN}✓ All scanned settings match optimal 20-TPS baselines!{RESET}\n")

def fix_server_properties(server_dir: Path):
    sp_path = server_dir / "server.properties"
    if not sp_path.exists():
        print(f"{RED}✗ server.properties not found in {server_dir}{RESET}")
        return

    # Create backup
    bak_path = sp_path.with_suffix(".properties.bak")
    shutil.copyfile(sp_path, bak_path)
    print(f"{GREEN}✓{RESET} Created backup: {bak_path.name}")

    props = parse_server_properties(sp_path)
    fixes_applied = 0

    for key, info in RULES.get("server.properties", {}).items():
        rec_val = str(info["recommended"])
        if props.get(key) != rec_val:
            props[key] = rec_val
            fixes_applied += 1
            print(f"  {GREEN}+ Patched{RESET} {key} = {rec_val}")

    # Write back
    with open(sp_path, "w", encoding="utf-8") as f:
        f.write("# Minecraft server properties - Optimized by mc-pulse\n")
        for k, v in sorted(props.items()):
            f.write(f"{k}={v}\n")

    print(f"\n{GREEN}✓ Optimization applied ({fixes_applied} settings updated).{RESET}")
    print(f"{GRAY}Restart your server to activate new parameters.{RESET}\n")

def main():
    parser = argparse.ArgumentParser(
        prog="mcpulse",
        description="Fast Minecraft Paper/Purpur performance diagnostics and 20-TPS lag buster."
    )
    parser.add_argument("-d", "--dir", default=".", help="Server root directory (default: current directory)")
    parser.add_argument("--fix", action="store_true", help="Automatically patch configurations with safe backups")
    parser.add_argument("-v", "--version", action="version", version=f"mc-pulse v{__version__}")

    args = parser.parse_args()
    target_dir = Path(args.dir)

    if args.fix:
        fix_server_properties(target_dir)
    else:
        audit_directory(target_dir)

if __name__ == "__main__":
    main()
