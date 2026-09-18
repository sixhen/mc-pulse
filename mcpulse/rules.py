# Optimization rules & recommended baseline settings for Paper/Purpur 1.20+
# Designed to maintain steady 20 TPS under heavy player and redstone load.

RULES = {
    "server.properties": {
        "view-distance": {
            "recommended": 7,
            "desc": "Player view distance. Values > 10 drastically increase tick chunk generation.",
            "type": "int"
        },
        "simulation-distance": {
            "recommended": 4,
            "desc": "Active tick simulation distance. Decoupling from view distance saves up to 40% CPU.",
            "type": "int"
        },
        "network-compression-threshold": {
            "recommended": 256,
            "desc": "Payload compression threshold to minimize bandwidth overhead.",
            "type": "int"
        }
    },
    "spigot.yml": {
        "entity-activation-range.monsters": {
            "recommended": 24,
            "desc": "Tick range for hostile mobs. Reduces useless entity AI ticks when far from players.",
            "type": "int"
        },
        "entity-activation-range.animals": {
            "recommended": 16,
            "desc": "Tick range for passive animals.",
            "type": "int"
        },
        "entity-tracking-range.monsters": {
            "recommended": 48,
            "desc": "Tracking distance sent to client packets.",
            "type": "int"
        },
        "ticks-per.hopper-check": {
            "recommended": 8,
            "desc": "Ticks between empty hopper scans. Drastically reduces hopper lag.",
            "type": "int"
        }
    },
    "paper-world-defaults.yml": {
        "entities.spawning.despawn-ranges.monster.hard": {
            "recommended": 96,
            "desc": "Hard despawn radius. Default 128 is too large for modern mob farms.",
            "type": "int"
        },
        "chunks.auto-save-interval": {
            "recommended": 6000,
            "desc": "World save interval (5 mins). Prevents frequent disk I/O lag spikes.",
            "type": "int"
        },
        "tick-rates.mob-spawner": {
            "recommended": 2,
            "desc": "Spawner block tick interval.",
            "type": "int"
        },
        "redstone-implementation": {
            "recommended": "ALTERNATE_CURRENT",
            "desc": "Modern low-overhead redstone calculation engine.",
            "type": "str"
        }
    }
}
