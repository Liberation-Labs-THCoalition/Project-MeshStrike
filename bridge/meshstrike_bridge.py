#!/usr/bin/env python3
"""
MeshStrike Bridge - TruthStrike for Meshtastic Networks
Compatible with Cyber Pony Express and Bay Area mesh networks
Enables counter-propaganda and protest coordination without internet
"""

import asyncio
import json
import sqlite3
import hashlib
import time
from datetime import datetime
from typing import Dict, List, Optional
import logging

# Meshtastic imports (pip install meshtastic)
try:
    import meshtastic
    import meshtastic.serial_interface
    import meshtastic.tcp_interface
    from pubsub import pub
except ImportError:
    print("Install meshtastic: pip install meshtastic")
    exit(1)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MeshStrike")

class MeshStrike:
    """
    Bridge between TruthStrike counter-propaganda and Meshtastic mesh networks
    """

    def __init__(self, port=None, host=None):
        """
        Initialize MeshStrike bridge
        Args:
            port: Serial port for USB-connected Meshtastic device
            host: IP address for WiFi-connected device
        """
        self.patterns = {}
        self.evidence_cache = {}
        self.protest_coords = {}
        self.emergency_alerts = []
        self.interface = None
        self.db = None

        # Meshtastic channel config
        self.PATTERN_CHANNEL = 2  # Distribute patterns
        self.EVIDENCE_CHANNEL = 3  # Backup evidence
        self.PROTEST_CHANNEL = 4  # Coordination
        self.EMERGENCY_CHANNEL = 5  # SOS broadcasts

        self.init_database()
        self.load_patterns()
        self.connect_mesh(port, host)

    def init_database(self):
        """Initialize local database for offline operation"""
        self.db = sqlite3.connect('meshstrike.db')
        c = self.db.cursor()

        # Patterns table
        c.execute('''CREATE TABLE IF NOT EXISTS patterns
                    (id TEXT PRIMARY KEY,
                     category TEXT,
                     pattern TEXT,
                     severity TEXT,
                     counter_narrative TEXT,
                     funders TEXT,
                     timestamp INTEGER)''')

        # Evidence table
        c.execute('''CREATE TABLE IF NOT EXISTS evidence
                    (id TEXT PRIMARY KEY,
                     location TEXT,
                     description TEXT,
                     hash TEXT,
                     sender_id TEXT,
                     timestamp INTEGER,
                     verified_count INTEGER DEFAULT 0)''')

        # Protest coordination
        c.execute('''CREATE TABLE IF NOT EXISTS protests
                    (id TEXT PRIMARY KEY,
                     location TEXT,
                     time INTEGER,
                     description TEXT,
                     safety_info TEXT,
                     participant_count INTEGER DEFAULT 0)''')

        self.db.commit()

    def connect_mesh(self, port=None, host=None):
        """Connect to Meshtastic device"""
        try:
            if port:
                logger.info(f"Connecting via serial: {port}")
                self.interface = meshtastic.serial_interface.SerialInterface(port)
            elif host:
                logger.info(f"Connecting via TCP: {host}")
                self.interface = meshtastic.tcp_interface.TCPInterface(host)
            else:
                # Auto-detect
                logger.info("Auto-detecting Meshtastic device...")
                self.interface = meshtastic.serial_interface.SerialInterface()

            # Subscribe to received messages
            pub.subscribe(self.on_receive, "meshtastic.receive")
            pub.subscribe(self.on_connection, "meshtastic.connection.established")

            logger.info("Connected to Meshtastic network!")
            self.announce_presence()

        except Exception as e:
            logger.error(f"Failed to connect: {e}")
            logger.info("Running in offline mode")

    def on_connection(self, interface, topic=pub.AUTO_TOPIC):
        """Handle connection established"""
        logger.info("Mesh connection established")
        self.sync_patterns()

    def on_receive(self, packet, interface):
        """Handle received mesh messages"""
        try:
            if 'decoded' in packet:
                data = packet['decoded']

                # Check message type
                if 'text' in data:
                    self.process_text_message(packet)
                elif 'data' in data:
                    self.process_data_message(packet)

        except Exception as e:
            logger.error(f"Error processing packet: {e}")

    def process_text_message(self, packet):
        """Process text messages for commands and alerts"""
        text = packet['decoded']['text']
        sender = packet.get('fromId', 'unknown')

        # Command processing
        if text.startswith('!'):
            self.process_command(text, sender)

        # Emergency detection
        emergency_keywords = ['help', 'sos', 'emergency', 'injured', 'arrest']
        if any(keyword in text.lower() for keyword in emergency_keywords):
            self.handle_emergency(text, sender, packet)

        # Pattern detection (even over mesh!)
        detected = self.detect_disinformation(text)
        if detected:
            self.send_counter_narrative(detected, sender)

    def process_data_message(self, packet):
        """Process data packets (patterns, evidence, etc)"""
        try:
            data = json.loads(packet['decoded']['data'].decode())
            msg_type = data.get('type')

            if msg_type == 'pattern_sync':
                self.receive_pattern(data)
            elif msg_type == 'evidence':
                self.receive_evidence(data)
            elif msg_type == 'protest_update':
                self.receive_protest_update(data)

        except Exception as e:
            logger.error(f"Error processing data: {e}")

    def load_patterns(self):
        """Load TruthStrike patterns for offline detection"""
        # Load from database
        c = self.db.cursor()
        c.execute('SELECT * FROM patterns ORDER BY timestamp DESC')

        for row in c.fetchall():
            pattern_id, category, pattern, severity, counter, funders, _ = row
            if category not in self.patterns:
                self.patterns[category] = []

            self.patterns[category].append({
                'id': pattern_id,
                'pattern': pattern,
                'severity': severity,
                'counter_narrative': counter,
                'funders': funders
            })

        # Load default patterns if empty
        if not self.patterns:
            self.load_default_patterns()

        logger.info(f"Loaded {len(self.patterns)} pattern categories")

    def load_default_patterns(self):
        """Load default counter-propaganda patterns"""
        defaults = {
            'fascist_recruiting': [
                {
                    'pattern': 'great replacement',
                    'severity': 'critical',
                    'counter_narrative': 'Immigration has always strengthened America. This is white nationalist propaganda.',
                    'funders': 'FAIR, CIS, NumbersUSA'
                },
                {
                    'pattern': 'cultural marxism',
                    'severity': 'high',
                    'counter_narrative': 'Recycled Nazi conspiracy theory. Originally "Cultural Bolshevism" from 1930s Germany.',
                    'funders': 'Heritage Foundation, Turning Point USA'
                }
            ],
            'police_propaganda': [
                {
                    'pattern': 'outside agitators',
                    'severity': 'high',
                    'counter_narrative': 'Same excuse used against Civil Rights movement. Local people demanding justice.',
                    'funders': 'Police unions, Fox News'
                },
                {
                    'pattern': 'antifa',
                    'severity': 'medium',
                    'counter_narrative': 'Anti-fascism is self-defense. Fascists killed millions, antifa has killed zero.',
                    'funders': 'Right-wing media ecosystem'
                }
            ],
            'protest_safety': [
                {
                    'pattern': 'kettle',
                    'severity': 'critical',
                    'counter_narrative': 'KETTLE WARNING: Police surrounding protesters. Find exits immediately.',
                    'funders': 'N/A - Safety alert'
                }
            ]
        }

        for category, patterns_list in defaults.items():
            self.patterns[category] = patterns_list
            for pattern in patterns_list:
                self.store_pattern(category, pattern)

    def detect_disinformation(self, text):
        """Detect disinformation patterns in text"""
        text_lower = text.lower()

        for category, patterns_list in self.patterns.items():
            for pattern_dict in patterns_list:
                if pattern_dict['pattern'].lower() in text_lower:
                    return {
                        'category': category,
                        'pattern': pattern_dict,
                        'detected_text': text
                    }

        return None

    def send_counter_narrative(self, detection, recipient):
        """Send counter-narrative over mesh"""
        pattern = detection['pattern']
        message = f"⚠️ DISINFO DETECTED: {detection['category']}\n"
        message += f"TRUTH: {pattern['counter_narrative']}\n"
        message += f"FUNDED BY: {pattern['funders']}"

        self.send_message(message, recipient)

    def process_command(self, text, sender):
        """Process mesh commands"""
        parts = text.split()
        command = parts[0].lower()

        commands = {
            '!help': self.send_help,
            '!patterns': self.send_pattern_list,
            '!evidence': self.backup_evidence,
            '!protest': self.send_protest_info,
            '!sos': self.broadcast_emergency,
            '!status': self.send_status,
            '!sync': self.sync_patterns
        }

        if command in commands:
            if len(parts) > 1:
                commands[command](sender, ' '.join(parts[1:]))
            else:
                commands[command](sender)

    def send_help(self, sender, args=None):
        """Send help message"""
        help_text = """MeshStrike Commands:
!help - This message
!patterns - Get disinfo patterns
!evidence <description> - Backup evidence
!protest <info> - Share protest info
!sos <message> - Emergency broadcast
!status - Network status
!sync - Sync patterns"""

        self.send_message(help_text, sender)

    def backup_evidence(self, sender, description):
        """Backup evidence across the mesh"""
        evidence_id = hashlib.sha256(
            f"{sender}{description}{time.time()}".encode()
        ).hexdigest()[:16]

        # Store locally
        c = self.db.cursor()
        c.execute('''INSERT INTO evidence (id, description, sender_id, timestamp)
                     VALUES (?, ?, ?, ?)''',
                  (evidence_id, description, sender, int(time.time())))
        self.db.commit()

        # Broadcast to mesh for backup
        evidence_packet = {
            'type': 'evidence',
            'id': evidence_id,
            'description': description,
            'sender': sender,
            'timestamp': time.time()
        }

        self.broadcast_data(evidence_packet, self.EVIDENCE_CHANNEL)

        response = f"Evidence backed up: {evidence_id}\n"
        response += "Distributed across mesh network"
        self.send_message(response, sender)

    def broadcast_emergency(self, sender, message):
        """Broadcast emergency alert to all nodes"""
        alert = f"🚨 SOS from {sender}: {message}"

        # Store emergency
        self.emergency_alerts.append({
            'sender': sender,
            'message': message,
            'timestamp': time.time()
        })

        # Broadcast on emergency channel
        self.broadcast_message(alert, self.EMERGENCY_CHANNEL)

        logger.warning(f"Emergency broadcast: {alert}")

    def send_protest_info(self, sender, args=None):
        """Share protest coordination info"""
        if not self.protest_coords:
            self.send_message("No active protests logged", sender)
            return

        info = "📍 Active Protests:\n"
        for protest_id, details in self.protest_coords.items():
            info += f"{details['location']}: {details['description']}\n"
            info += f"Safety: {details.get('safety_info', 'Stay together')}\n"

        self.send_message(info, sender)

    def sync_patterns(self, sender=None):
        """Sync patterns across mesh network"""
        logger.info("Syncing patterns across mesh...")

        for category, patterns_list in self.patterns.items():
            for pattern in patterns_list:
                sync_packet = {
                    'type': 'pattern_sync',
                    'category': category,
                    'pattern': pattern
                }

                self.broadcast_data(sync_packet, self.PATTERN_CHANNEL)
                time.sleep(0.5)  # Don't flood the mesh

        if sender:
            self.send_message(f"Synced {len(self.patterns)} pattern categories", sender)

    def announce_presence(self):
        """Announce MeshStrike node to network"""
        announcement = "⚔️ MeshStrike node online - Counter-propaganda mesh bridge active"
        self.broadcast_message(announcement)

    def send_message(self, text, recipient='^all'):
        """Send text message over mesh"""
        if self.interface:
            self.interface.sendText(text, destinationId=recipient)
            logger.info(f"Sent: {text[:50]}...")

    def broadcast_message(self, text, channel=0):
        """Broadcast message to all nodes"""
        self.send_message(text, '^all')

    def broadcast_data(self, data, channel=0):
        """Broadcast data packet to mesh"""
        if self.interface:
            data_bytes = json.dumps(data).encode()
            self.interface.sendData(data_bytes, destinationId='^all',
                                   portNum=256, channelIndex=channel)

    def store_pattern(self, category, pattern_dict):
        """Store pattern in database"""
        pattern_id = hashlib.sha256(
            f"{category}{pattern_dict['pattern']}".encode()
        ).hexdigest()[:16]

        c = self.db.cursor()
        c.execute('''INSERT OR REPLACE INTO patterns
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (pattern_id, category, pattern_dict['pattern'],
                   pattern_dict['severity'], pattern_dict['counter_narrative'],
                   pattern_dict.get('funders', ''), int(time.time())))
        self.db.commit()

    def receive_pattern(self, data):
        """Receive and store pattern from mesh"""
        category = data['category']
        pattern = data['pattern']

        if category not in self.patterns:
            self.patterns[category] = []

        # Check if we already have this pattern
        existing = any(p['pattern'] == pattern['pattern']
                      for p in self.patterns[category])

        if not existing:
            self.patterns[category].append(pattern)
            self.store_pattern(category, pattern)
            logger.info(f"Received new pattern: {category}/{pattern['pattern']}")

    def receive_evidence(self, data):
        """Receive and verify evidence from mesh"""
        evidence_id = data['id']

        # Check if we have it
        c = self.db.cursor()
        c.execute('SELECT verified_count FROM evidence WHERE id = ?', (evidence_id,))
        result = c.fetchone()

        if result:
            # Increment verification count
            c.execute('''UPDATE evidence SET verified_count = verified_count + 1
                        WHERE id = ?''', (evidence_id,))
        else:
            # Store new evidence
            c.execute('''INSERT INTO evidence
                        (id, description, sender_id, timestamp, verified_count)
                        VALUES (?, ?, ?, ?, 1)''',
                     (evidence_id, data.get('description', ''),
                      data.get('sender', 'mesh'), int(time.time())))

        self.db.commit()
        logger.info(f"Evidence {evidence_id} backed up")

    def run(self):
        """Run MeshStrike bridge"""
        logger.info("MeshStrike bridge running...")
        logger.info("Commands: !help, !patterns, !evidence, !protest, !sos")

        try:
            while True:
                time.sleep(1)

                # Periodic sync (every hour)
                if int(time.time()) % 3600 == 0:
                    self.sync_patterns()

        except KeyboardInterrupt:
            logger.info("Shutting down MeshStrike bridge...")
            if self.interface:
                self.interface.close()
            self.db.close()

# Protest coordination extensions
class ProtestCoordinator(MeshStrike):
    """
    Extended MeshStrike for protest coordination
    Compatible with Cyber Pony Express infrastructure
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.legal_observers = set()
        self.medics = set()
        self.safe_houses = []

    def register_support(self, sender, role, location=None):
        """Register support roles (legal, medic, etc)"""
        if role == 'legal':
            self.legal_observers.add(sender)
            self.broadcast_message(f"📋 Legal observer available: {sender}")
        elif role == 'medic':
            self.medics.add(sender)
            self.broadcast_message(f"🏥 Street medic available: {sender}")
        elif role == 'safehouse' and location:
            self.safe_houses.append({'node': sender, 'location': location})
            # Don't broadcast safehouses publicly

    def request_support(self, sender, support_type):
        """Request support during protest"""
        if support_type == 'legal' and self.legal_observers:
            observer = next(iter(self.legal_observers))
            self.send_message(f"Legal support requested by {sender}", observer)
            self.send_message(f"Legal observer {observer} notified", sender)
        elif support_type == 'medic' and self.medics:
            medic = next(iter(self.medics))
            self.send_message(f"Medical support requested by {sender}", medic)
            self.send_message(f"Medic {medic} notified", sender)

    def broadcast_kettle_warning(self, location):
        """Warn about police kettling"""
        warning = f"⚠️ KETTLE WARNING at {location}!\n"
        warning += "Police surrounding protesters. Find exits NOW.\n"
        warning += "Stay calm, stay together, record everything."

        self.broadcast_message(warning, self.EMERGENCY_CHANNEL)

        # Log for evidence
        self.backup_evidence('SYSTEM', f"Kettle warning at {location}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='MeshStrike - Counter-propaganda mesh bridge')
    parser.add_argument('--port', help='Serial port for USB Meshtastic device')
    parser.add_argument('--host', help='IP address for WiFi Meshtastic device')
    parser.add_argument('--protest', action='store_true',
                       help='Enable protest coordination features')

    args = parser.parse_args()

    print("""
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║     ███╗   ███╗███████╗███████╗██╗  ██╗            ║
    ║     ████╗ ████║██╔════╝██╔════╝██║  ██║            ║
    ║     ██╔████╔██║█████╗  ███████╗███████║            ║
    ║     ██║╚██╔╝██║██╔══╝  ╚════██║██╔══██║            ║
    ║     ██║ ╚═╝ ██║███████╗███████║██║  ██║            ║
    ║     ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝            ║
    ║                                                      ║
    ║     S T R I K E   v1.0                              ║
    ║     Counter-Propaganda Mesh Network                 ║
    ║     Compatible with Cyber Pony Express              ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝

    The network cannot be cut. The truth cannot be stopped.
    """)

    # Create appropriate bridge
    if args.protest:
        bridge = ProtestCoordinator(port=args.port, host=args.host)
    else:
        bridge = MeshStrike(port=args.port, host=args.host)

    # Run the bridge
    bridge.run()