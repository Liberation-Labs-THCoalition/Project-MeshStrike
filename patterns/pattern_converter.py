#!/usr/bin/env python3
"""
Pattern Converter - Bridge TruthStrike and MeshStrike patterns
Converts between browser extension and mesh network formats
"""

import json
import sqlite3
import hashlib
import time
from typing import Dict, List

class PatternConverter:
    """Convert patterns between TruthStrike and MeshStrike formats"""

    def __init__(self):
        self.truthstrike_patterns = {}
        self.meshstrike_patterns = {}

    def load_truthstrike_patterns(self, filepath='../../PROJECT_TRUTHSTRIKE/patterns.json'):
        """Load patterns from TruthStrike browser extension"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)

            # Convert TruthStrike format
            for category, info in data.items():
                self.truthstrike_patterns[category] = {
                    'patterns': info.get('patterns', []),
                    'severity': info.get('severity', 'medium'),
                    'category': info.get('category', category),
                    'funders': info.get('funders', []),
                    'counterPoints': info.get('counterPoints', [])
                }

            print(f"Loaded {len(self.truthstrike_patterns)} categories from TruthStrike")
            return True

        except FileNotFoundError:
            print("TruthStrike patterns not found, using defaults")
            self.load_default_truthstrike()
            return False

    def load_default_truthstrike(self):
        """Default patterns from TruthStrike"""
        self.truthstrike_patterns = {
            'election_fraud': {
                'patterns': [
                    'stolen\\s+election',
                    'dominion\\s+voting',
                    'rigged\\s+election'
                ],
                'severity': 'high',
                'category': 'election_integrity',
                'funders': ['Heritage Foundation', 'ALEC', 'True the Vote'],
                'counterPoints': [
                    'No evidence found in 60+ court cases',
                    'Confirmed secure by Trump\'s own DHS',
                    'Paper audits confirmed electronic tallies'
                ]
            },
            'climate_denial': {
                'patterns': [
                    'climate\\s+hoax',
                    'global\\s+warming\\s+scam',
                    'co2\\s+is\\s+plant\\s+food'
                ],
                'severity': 'high',
                'category': 'climate',
                'funders': ['Koch Industries', 'ExxonMobil', 'Heartland Institute'],
                'counterPoints': [
                    '99.9% scientific consensus on human cause',
                    'Fossil companies knew since 1970s',
                    'Extreme weather increasing as predicted'
                ]
            },
            'anti_trans': {
                'patterns': [
                    'groomer',
                    'trans.*agenda',
                    'biological\\s+man'
                ],
                'severity': 'high',
                'category': 'civil_rights',
                'funders': ['Alliance Defending Freedom', 'Family Research Council'],
                'counterPoints': [
                    'Trans people 4x more likely to be victims',
                    'Medical consensus supports gender-affirming care',
                    'Bathroom predator myth debunked by stats'
                ]
            }
        }

    def convert_to_meshstrike(self):
        """Convert TruthStrike patterns to MeshStrike format"""
        self.meshstrike_patterns = {}

        for category, data in self.truthstrike_patterns.items():
            self.meshstrike_patterns[category] = []

            for pattern in data['patterns']:
                # Create simplified pattern for mesh (bandwidth limited)
                mesh_pattern = {
                    'pattern': pattern.replace('\\s+', ' '),  # Simplify regex
                    'severity': data['severity'],
                    'counter_narrative': data['counterPoints'][0] if data['counterPoints'] else 'Disinformation detected',
                    'funders': ', '.join(data['funders'][:3])  # Limit to 3 for bandwidth
                }

                self.meshstrike_patterns[category].append(mesh_pattern)

        return self.meshstrike_patterns

    def add_protest_patterns(self):
        """Add protest-specific patterns for mesh network"""
        protest_patterns = {
            'police_tactics': [
                {
                    'pattern': 'kettle',
                    'severity': 'critical',
                    'counter_narrative': 'KETTLE ALERT: Police surrounding. Find exits immediately.',
                    'funders': 'N/A'
                },
                {
                    'pattern': 'disperse',
                    'severity': 'high',
                    'counter_narrative': 'Dispersal order given. Know your rights. Document everything.',
                    'funders': 'N/A'
                },
                {
                    'pattern': 'antifa',
                    'severity': 'medium',
                    'counter_narrative': 'Antifa means anti-fascist. Fascists killed millions, antifa zero.',
                    'funders': 'Right-wing media'
                },
                {
                    'pattern': 'outside agitators',
                    'severity': 'medium',
                    'counter_narrative': 'Same lie used against Civil Rights movement. Locals demanding justice.',
                    'funders': 'Police unions'
                }
            ],
            'fascist_symbols': [
                {
                    'pattern': 'proud boys',
                    'severity': 'high',
                    'counter_narrative': 'Designated terrorist organization in Canada. Known for violence.',
                    'funders': 'Dark money networks'
                },
                {
                    'pattern': 'three percenter',
                    'severity': 'high',
                    'counter_narrative': 'Militia movement linked to Jan 6 insurrection. Armed and dangerous.',
                    'funders': 'Gun lobby'
                },
                {
                    'pattern': 'boogaloo',
                    'severity': 'high',
                    'counter_narrative': 'Accelerationist movement seeking civil war. Multiple murders committed.',
                    'funders': 'Online extremism'
                }
            ],
            'safety_alerts': [
                {
                    'pattern': 'tear gas',
                    'severity': 'critical',
                    'counter_narrative': 'CHEMICAL WEAPONS: Move upwind. Don\'t rub eyes. Use water/LAW.',
                    'funders': 'N/A'
                },
                {
                    'pattern': 'rubber bullets',
                    'severity': 'critical',
                    'counter_narrative': 'LESS-LETHAL WEAPONS: Can kill. Protect head/eyes. Document injuries.',
                    'funders': 'N/A'
                },
                {
                    'pattern': 'mass arrest',
                    'severity': 'high',
                    'counter_narrative': 'MASS ARREST: Write NLG number on arm. Name only. Remain silent.',
                    'funders': 'N/A'
                }
            ]
        }

        # Add to mesh patterns
        for category, patterns in protest_patterns.items():
            if category not in self.meshstrike_patterns:
                self.meshstrike_patterns[category] = []
            self.meshstrike_patterns[category].extend(patterns)

        print(f"Added {len(protest_patterns)} protest-specific categories")

    def save_meshstrike_db(self, db_path='meshstrike.db'):
        """Save patterns to MeshStrike SQLite database"""
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS patterns
                    (id TEXT PRIMARY KEY,
                     category TEXT,
                     pattern TEXT,
                     severity TEXT,
                     counter_narrative TEXT,
                     funders TEXT,
                     timestamp INTEGER)''')

        # Insert patterns
        count = 0
        for category, patterns_list in self.meshstrike_patterns.items():
            for pattern_dict in patterns_list:
                pattern_id = hashlib.sha256(
                    f"{category}{pattern_dict['pattern']}".encode()
                ).hexdigest()[:16]

                c.execute('''INSERT OR REPLACE INTO patterns
                            VALUES (?, ?, ?, ?, ?, ?, ?)''',
                         (pattern_id,
                          category,
                          pattern_dict['pattern'],
                          pattern_dict['severity'],
                          pattern_dict['counter_narrative'],
                          pattern_dict.get('funders', ''),
                          int(time.time())))
                count += 1

        conn.commit()
        conn.close()
        print(f"Saved {count} patterns to {db_path}")

    def save_meshstrike_json(self, filepath='mesh_patterns.json'):
        """Save patterns as JSON for distribution"""
        with open(filepath, 'w') as f:
            json.dump(self.meshstrike_patterns, f, indent=2)
        print(f"Saved patterns to {filepath}")

        # Also create compressed version for bandwidth
        compressed = {}
        for cat, patterns in self.meshstrike_patterns.items():
            compressed[cat[:8]] = []  # Shorten category names
            for p in patterns:
                compressed[cat[:8]].append({
                    'p': p['pattern'][:20],  # Limit pattern length
                    's': p['severity'][0],  # Just first letter
                    'c': p['counter_narrative'][:100],  # Limit counter narrative
                    'f': p.get('funders', '')[:30]  # Limit funders
                })

        with open('mesh_patterns_compressed.json', 'w') as f:
            json.dump(compressed, f, separators=(',', ':'))
        print(f"Saved compressed patterns (for mesh distribution)")

    def generate_qr_codes(self):
        """Generate QR codes for pattern distribution"""
        try:
            import qrcode

            # Create QR code for each category
            for category in self.meshstrike_patterns:
                data = json.dumps(self.meshstrike_patterns[category])

                if len(data) > 2953:  # QR code size limit
                    data = data[:2953]

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(data)
                qr.make(fit=True)

                img = qr.make_image(fill_color="black", back_color="white")
                img.save(f'qr_{category}.png')
                print(f"Generated QR code for {category}")

        except ImportError:
            print("Install qrcode: pip install qrcode[pil]")

    def export_for_protest(self, event_name='action'):
        """Export patterns optimized for specific protest"""
        protest_pack = {
            'event': event_name,
            'generated': time.strftime('%Y-%m-%d %H:%M'),
            'critical_patterns': [],
            'commands': {
                '!sos': 'Emergency broadcast',
                '!evidence': 'Backup evidence',
                '!request legal': 'Get legal support',
                '!request medic': 'Get medical support'
            }
        }

        # Add only critical patterns for bandwidth
        for category, patterns in self.meshstrike_patterns.items():
            for pattern in patterns:
                if pattern['severity'] in ['critical', 'high']:
                    protest_pack['critical_patterns'].append({
                        'p': pattern['pattern'],
                        'c': pattern['counter_narrative'][:100]
                    })

        # Save protest pack
        filename = f'protest_pack_{event_name}_{time.strftime("%Y%m%d")}.json'
        with open(filename, 'w') as f:
            json.dump(protest_pack, f, separators=(',', ':'))

        print(f"Created protest pack: {filename}")
        print(f"Size: {len(json.dumps(protest_pack))} bytes")
        print(f"Patterns: {len(protest_pack['critical_patterns'])}")

        return filename

def main():
    """Run pattern conversion"""
    print("""
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║  PATTERN CONVERTER - TruthStrike ↔ MeshStrike        ║
    ║  Bridge browser and mesh counter-propaganda           ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
    """)

    converter = PatternConverter()

    # Load TruthStrike patterns
    print("\n[1] Loading TruthStrike patterns...")
    converter.load_truthstrike_patterns()

    # Convert to mesh format
    print("\n[2] Converting to MeshStrike format...")
    converter.convert_to_meshstrike()

    # Add protest-specific patterns
    print("\n[3] Adding protest patterns...")
    converter.add_protest_patterns()

    # Save in various formats
    print("\n[4] Saving patterns...")
    converter.save_meshstrike_db()
    converter.save_meshstrike_json()

    # Generate QR codes for offline sharing
    print("\n[5] Generating QR codes...")
    converter.generate_qr_codes()

    # Create protest pack
    print("\n[6] Creating protest pack...")
    converter.export_for_protest('oakland_action')

    print("\n✅ Pattern conversion complete!")
    print("\nFiles created:")
    print("  - meshstrike.db (SQLite database)")
    print("  - mesh_patterns.json (Full patterns)")
    print("  - mesh_patterns_compressed.json (For mesh)")
    print("  - qr_*.png (QR codes for offline sharing)")
    print("  - protest_pack_*.json (Event-specific)")

    print("\n🚀 Ready for deployment to mesh network!")

if __name__ == "__main__":
    main()