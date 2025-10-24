# ⚔️ MeshStrike: Counter-Propaganda for Mesh Networks

**TruthStrike meets Meshtastic - Fighting fascism even when they cut the internet**

Compatible with [Cyber Pony Express](https://themultiverse.school/x/cyberpony) and Bay Area mesh networks.

## 🌐 What Is MeshStrike?

MeshStrike bridges counter-propaganda capabilities with decentralized mesh networks. When authorities cut internet during protests, when disasters knock out cell towers, or when you just need untraceable coordination - MeshStrike keeps the truth flowing.

### Core Features

- **Offline Counter-Propaganda**: Detect and counter disinformation without internet
- **Pattern Distribution**: Share detection patterns across the mesh
- **Evidence Backup**: Distributed storage across multiple nodes
- **Protest Coordination**: Encrypted coordination during actions
- **Emergency Broadcast**: SOS system with automatic relay
- **Legal/Medic Support**: Connect protesters with observers and medics

## 🛠️ Hardware Requirements

### Compatible with Cyber Pony Express Hardware

- **T-Deck Plus** ($75-90): Standalone with keyboard and screen
- **Heltec V3** ($17-23): Budget option
- **RAK Wireless** ($38): Modular kit
- **DIY Build** (~$15): ESP32 + RFM95 LoRa module

### Recommended Setup

1. **Base Station**: Raspberry Pi + RAK Wireless (elevated location)
2. **Mobile Units**: T-Deck Plus or Heltec V3
3. **Range**: 1 mile urban, several miles line-of-sight

## 📦 Installation

### Quick Start

```bash
# Install dependencies
pip install meshtastic pubsub

# Clone MeshStrike
git clone https://github.com/coalition/meshstrike.git
cd meshstrike

# Run the bridge
python bridge/meshstrike_bridge.py --port COM3  # Windows
python bridge/meshstrike_bridge.py --port /dev/ttyUSB0  # Linux
```

### Protest Mode

```bash
# Enable enhanced protest coordination
python bridge/meshstrike_bridge.py --protest
```

## 📡 Mesh Commands

Send these commands via Meshtastic chat:

| Command | Description | Example |
|---------|-------------|---------|
| `!help` | Show all commands | `!help` |
| `!patterns` | Get disinfo patterns | `!patterns` |
| `!evidence <desc>` | Backup evidence | `!evidence Police using teargas at 5th and Main` |
| `!protest <info>` | Share protest info | `!protest March at City Hall 3pm` |
| `!sos <message>` | Emergency broadcast | `!sos Need medic at fountain` |
| `!status` | Network status | `!status` |
| `!sync` | Sync patterns | `!sync` |

### Support Roles

- `!register legal` - Register as legal observer
- `!register medic` - Register as street medic
- `!request legal` - Request legal support
- `!request medic` - Request medical support

## 🎯 Pattern Detection (Offline!)

MeshStrike detects disinformation even without internet:

### Pre-Loaded Patterns

- **Fascist Recruiting**: "great replacement", "cultural marxism"
- **Police Propaganda**: "outside agitators", "antifa terrorists"
- **Protest Safety**: Kettle warnings, dispersal orders

### Adding Custom Patterns

Edit `patterns.json` or use the API:

```json
{
  "category": "local_fascists",
  "pattern": "proud boys",
  "severity": "critical",
  "counter_narrative": "Designated terrorist group in Canada",
  "funders": "Various dark money"
}
```

## 🚨 Emergency Features

### Kettle Warning System

Automatic detection and broadcast when police surround protesters:

```python
# Triggered by keywords or manual alert
"⚠️ KETTLE WARNING at [location]!
Police surrounding protesters. Find exits NOW.
Stay calm, stay together, record everything."
```

### Evidence Backup

All evidence is distributed across the mesh with verification:

1. User reports incident: `!evidence Cops attacking peaceful protesters`
2. System generates hash: `Evidence ID: a4f3b2c1`
3. Distributes to all nodes for backup
4. Multiple nodes verify receipt
5. Evidence preserved even if original device seized

## 🔐 Security & Privacy

- **End-to-end encryption** for direct messages
- **Channel encryption** with pre-shared keys
- **No internet required** - completely offline operation
- **No phone numbers** - uses node IDs only
- **Distributed storage** - no single point of failure

## 🌉 Bay Area Integration

MeshStrike is designed to work with existing Bay Area mesh infrastructure:

### Compatible Networks

- **BayMe.sh**: Bay Area Meshtastic network
- **SacValley Mesh**: Sacramento Valley coverage
- **Central Valley Mesh**: Extended regional network

### Repeater Nodes

Connect to community repeaters for extended range:

1. Mt. Tam repeater (covers North Bay)
2. Mt. Diablo repeater (covers East Bay)
3. Twin Peaks repeater (covers SF)

## 📊 Network Topology

```
[Protest Site] ←→ [Mobile Nodes] ←→ [Repeaters] ←→ [Base Stations]
     ↓                   ↓                              ↓
[Evidence Backup]  [Coordination]              [Pattern Updates]
```

## 🚀 Deployment Scenarios

### Protest/Direct Action

1. Deploy MeshStrike nodes before action
2. Distribute T-Decks to coordinators
3. Register legal observers and medics
4. Share channel keys with trusted participants
5. Monitor emergency channel for SOS

### Disaster Response

1. Establish base station at coordination center
2. Deploy mobile nodes with first responders
3. Share resource locations via mesh
4. Coordinate mutual aid without cell service

### Community Defense

1. Install permanent nodes in neighborhoods
2. Create local pattern database
3. Share security alerts via mesh
4. Build resilient communication network

## 🛡️ Operational Security

### DO:
- Use code names/handles, not real names
- Change pre-shared keys regularly
- Keep spare batteries charged
- Test range before actions
- Have backup communication plans

### DON'T:
- Broadcast sensitive locations publicly
- Leave devices unattended
- Use default channel keys
- Assume messages are private from all
- Rely solely on mesh during critical moments

## 🤝 Contributing

### Help Needed

- **Pattern Writers**: Document local fascist propaganda
- **Node Operators**: Host repeater nodes
- **Developers**: Improve bridge code
- **Testers**: Field test during actions
- **Translators**: Localize for other regions

### Testing Checklist

- [ ] Range test in your area
- [ ] Pattern detection accuracy
- [ ] Evidence backup verification
- [ ] Emergency broadcast reach
- [ ] Battery life under load

## 📚 Resources

### Hardware

- [Meshtastic Devices](https://meshtastic.org/docs/hardware)
- [Cyber Pony Express](https://themultiverse.school/x/cyberpony)
- [DIY LoRa Guide](https://meshtastic.org/docs/hardware/diy)

### Software

- [Meshtastic Python API](https://github.com/meshtastic/python)
- [TruthStrike Patterns](https://github.com/coalition/truthstrike)
- [Protest Safety Guide](https://protesthandbook.org)

### Networks

- [BayMe.sh Discord](https://discord.gg/baymesh)
- [NorCal Mesh](https://norcalmesh.net)
- [Disaster.radio](https://disaster.radio)

## ⚠️ Disclaimer

MeshStrike is for legitimate protest, emergency response, and community defense. Users are responsible for compliance with local laws. The Coalition provides this tool for defensive purposes against fascism and disinformation.

## 🔥 Philosophy

**"When they cut the internet, we build our own network."**

The state thinks they can blind us by cutting communications during protests. They think they can isolate communities during disasters. They think centralized control gives them power.

They're wrong.

Every MeshStrike node is a middle finger to censorship. Every relayed message is resistance. Every backed-up video of police brutality is accountability they can't delete.

The network cannot be cut. The truth cannot be stopped.

## 📝 License

GNU General Public License v3.0 - Free as in freedom

## 💪 Support

- **Code Issues**: [GitHub](https://github.com/coalition/meshstrike)
- **Hardware Help**: [Cyber Pony Express](https://themultiverse.school/x/cyberpony)
- **Protest Support**: [Coalition](https://thcoalition.net)

---

**Part of the Coalition's Uncuttable Infrastructure**

*Built with rage against surveillance and love for autonomous networks*

**The revolution will be decentralized.**