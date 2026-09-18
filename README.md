# mc-pulse

A fast, pragmatic performance diagnostics and 20-TPS lag buster CLI for Minecraft Java servers (Paper, Purpur, Spigot).

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)

## Features

- **Automated Performance Audit**: Analyzes `server.properties`, `bukkit.yml`, `spigot.yml`, and `paper-world-defaults.yml`.
- **Lag Culprit Detection**: Catches simulation distance decoupling issues, excessive entity activation ranges, and hopper scanning overload.
- **Safe Auto-Patching**: Use `--fix` to generate automatic `.bak` backups and patch optimal settings with zero downtime.
- **Zero Heavy Dependencies**: Pure standard Python 3.

## Installation

```bash
git clone https://github.com/sixhen/mc-pulse.git
cd mc-pulse
pip install -e .
```

Or run directly without installing:

```bash
python3 bin/mcpulse --help
```

## Usage

Run inside your Minecraft server directory:

```bash
# Run diagnostics and score server settings
mcpulse

# Audit a specific server directory
mcpulse --dir /path/to/minecraft/server

# Automatically patch settings with safe backup
mcpulse --fix
```

## Example Output

```text
  __  __  _____      ____  _   _ _     ____  _____ 
 |  \/  |/ ____|    |  _ \| | | | |   / ___|| ____|
 | |\/| | |   ______| |_) | | | | |   \___ \|  _|  
 | |  | | |__|______|  __/| |_| | |___ ___) | |___ 
 |_|  |_|\_____|    |_|    \___/|_____|____/|_____|
  Minecraft TPS Optimizer v1.1.0 · by sixhen

:: Scanning server directory: /srv/minecraft

PERFORMANCE AUDIT RESULTS:
  Health Score: 66% (2/3 settings optimal)

DETECTED BOTTLENECKS:
  1. server.properties • simulation-distance
     Current:     10
     Recommended: 4
     Impact:      Active tick simulation distance. Decoupling saves up to 40% CPU.
```

## License

MIT License &copy; 2026 [sixhen](https://github.com/sixhen).
