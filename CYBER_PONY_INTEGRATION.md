# 🐴 MeshStrike + Cyber Pony Express Integration

**Joining the Bay Area's Uncuttable Network**

## What is Cyber Pony Express?

Cyber Pony Express is the Bay Area's Meshtastic network promoting "text walkie-talkies" for disaster preparedness and community autonomy. MeshStrike adds counter-propaganda and protest coordination capabilities to this infrastructure.

## 🌉 Bay Area Mesh Networks

### Active Networks
- **BayMe.sh**: Primary Bay Area network
- **SacValley Mesh**: Sacramento Valley coverage
- **Central Valley Mesh**: Extended regional network
- **NorCal Mesh**: Northern California backbone

### Key Infrastructure

**Mountain Repeaters** (High-power nodes with solar):
- Mt. Tamalpais (North Bay coverage)
- Mt. Diablo (East Bay coverage)
- Twin Peaks (SF coverage)
- Mt. Hamilton (South Bay coverage)

## 🔧 Hardware Compatibility

### Cyber Pony Express Recommended Devices

MeshStrike works with ALL Cyber Pony hardware:

| Device | Price | MeshStrike Features | Best For |
|--------|-------|-------------------|----------|
| **T-Deck Plus** | $75-90 | Full keyboard input, screen for patterns | Coordinators |
| **Heltec V3** | $17-23 | Compact, long battery | Scouts |
| **RAK Wireless** | $38 | Modular, expandable | Base stations |
| **DIY ESP32+LoRa** | ~$15 | Customizable | Bulk deployment |

## 📡 Channel Configuration

### Join Existing Channels

**BayMesh Public Channel:**
```
Name: BayMesh
Region: US
Modem: LongFast
PSK: [Check Discord for current]
```

**MeshStrike Protest Channel:**
```
Name: MeshStrike
Region: US
Modem: LongFast
PSK: Generate per action
Channel: 4
```

### Frequency Settings

US ISM Band (license-free):
- **915 MHz** (US/Canada)
- **868 MHz** (Europe)
- **433 MHz** (Asia)

## 🚀 Quick Integration

### Step 1: Flash Meshtastic Firmware

```bash
# Install flasher
pip install meshtastic-flasher

# Flash device (automatic detection)
meshtastic-flasher
```

### Step 2: Configure for Bay Area

```bash
# Set region
meshtastic --set region US

# Set modem preset
meshtastic --set modem_config.preset LONG_FAST

# Join BayMesh
meshtastic --ch-set name "BayMesh" --ch-index 0
```

### Step 3: Launch MeshStrike Bridge

```bash
# Connect to your device
python meshstrike_bridge.py --port /dev/ttyUSB0

# Or via WiFi (if device supports)
python meshstrike_bridge.py --host 192.168.1.100
```

## 🏘️ Community Integration

### Cyber Pony Express Events

MeshStrike features for CPE events:

**Workshops:**
- Demo counter-propaganda detection
- Train on evidence backup
- Practice emergency protocols

**Disaster Drills:**
- Test mesh coverage
- Coordinate via MeshStrike
- Document with evidence system

**Hardware Distribution:**
- Pre-load MeshStrike patterns
- Configure protest channels
- Include quick reference cards

### Contributing Back

Share with Cyber Pony Express:

1. **Coverage Maps**: Document mesh dead zones
2. **Pattern Updates**: Local fascist groups
3. **Range Tests**: Real-world performance
4. **Success Stories**: Effective deployments

## 📊 Network Topology

```
Cyber Pony Express Infrastructure
              ↓
    [Mountain Repeaters]
         ↙    ↓    ↘
[Oakland]  [SF]  [San Jose]
    ↓        ↓        ↓
[Local Mesh Networks]
         ↓
[MeshStrike Nodes]
    ↙    ↓    ↘
[Patterns] [Evidence] [Coordination]
```

## 🔐 Security Alignment

### Shared Principles

Both MeshStrike and CPE emphasize:
- **No surveillance**: Mesh avoids corporate tracking
- **Community control**: Nodes run by activists
- **Resilience**: Works when internet is cut
- **Accessibility**: No license required

### Enhanced Security

MeshStrike adds:
- Pattern-based disinformation detection
- Distributed evidence backup
- Emergency broadcast system
- Legal/medic coordination

## 📱 App Integration

### Meshtastic App + MeshStrike

1. Install Meshtastic (iOS/Android)
2. Pair with device via Bluetooth
3. Send MeshStrike commands:
   - Type `!help` in any channel
   - Use `!evidence` to backup
   - Send `!sos` for emergencies

### Web Interface

```python
# Serve web interface locally
cd meshstrike
python -m http.server 8000
# Navigate to: http://localhost:8000
```

## 🌐 Regional Expansion

### Starting Your City's Network

Using CPE + MeshStrike model:

1. **Hardware**: Order 10+ Heltec V3 devices ($200)
2. **Firmware**: Flash with Meshtastic
3. **Patterns**: Load local propaganda patterns
4. **Deploy**: Place nodes at strategic locations
5. **Grow**: Host workshops, share devices

### Connect Regions

**NorCal Backbone:**
- Eureka ↔ Redding ↔ Sacramento ↔ Bay Area

**Central Valley Link:**
- Sacramento ↔ Stockton ↔ Modesto ↔ Fresno

**Coastal Chain:**
- Eureka ↔ Bay Area ↔ Santa Cruz ↔ Monterey

## 📚 Resources

### Cyber Pony Express
- Website: https://themultiverse.school/x/cyberpony
- Discord: [Join BayMesh Discord](https://discord.gg/baymesh)
- Events: Check Discord for workshops

### MeshStrike
- GitHub: https://github.com/coalition/meshstrike
- Patterns: Updated weekly
- Support: https://thcoalition.net

### Hardware
- Meshtastic: https://meshtastic.org
- US Suppliers: Rokland, Amazon
- Bulk Orders: Contact CPE for group buys

## 🤝 Joint Operations

### Protest Scenarios

**Before Action:**
1. Coordinate with CPE node operators
2. Ensure repeater coverage at site
3. Share channel keys via Signal
4. Test MeshStrike commands

**During Action:**
- CPE provides communication backbone
- MeshStrike adds tactical features
- Both systems remain independent
- Redundancy through multiple channels

**After Action:**
- Share coverage maps with CPE
- Update MeshStrike patterns
- Document effectiveness
- Plan improvements

## 💡 Innovation Ideas

### Future Integration

**Mesh-to-Internet Bridge:**
- CPE nodes with internet share updates
- MeshStrike patterns sync automatically
- Evidence uploads when possible

**Solar Repeater Network:**
- Permanent protest infrastructure
- CPE hardware + MeshStrike software
- Community-maintained nodes

**Regional Pattern Exchange:**
- Bay Area patterns → Portland
- LA patterns → Bay Area
- Seattle patterns → Everyone

## 🚨 Emergency Protocols

### If Internet Cut

1. **Switch to Mesh**: All devices auto-connect
2. **Join Emergency Channel**: Pre-agreed channel
3. **Send Status**: `!status [location] [situation]`
4. **Coordinate**: Use MeshStrike commands

### If Mesh Jammed

1. **Change Channel**: Move to backup
2. **Reduce Power**: Lower transmit strength
3. **Go Mobile**: Use bikes/cars as relays
4. **Physical Runners**: Last resort

## 📝 Quick Reference

### Essential Info

**CPE Discord**: https://discord.gg/baymesh
**Emergency Channel**: 5
**Protest Channel**: 4
**Default Region**: US
**Frequency**: 915 MHz

### MeshStrike Commands

```
!help - Show commands
!patterns - Get patterns
!evidence [desc] - Backup
!sos [msg] - Emergency
!protest [info] - Coordinate
```

### Bay Area Nodes

**Always Online:**
- Mt. Tam Repeater
- Mt. Diablo Repeater
- Twin Peaks Node

**Contact** (via Discord):
- BayMesh Admins
- CPE Organizers
- MeshStrike Support

---

## Final Thoughts

Cyber Pony Express built the roads. MeshStrike provides the weapons.

Together, we create infrastructure that:
- **Cannot be cut** by authorities
- **Cannot be bought** by corporations
- **Cannot be stopped** by fascists

Every node strengthens both networks. Every user increases resilience. Every deployment is an act of collective defense.

**"From the mountains to the streets, the mesh will set us free."**

---

*Part of the Coalition's Autonomous Infrastructure Initiative*

**The revolution will be decentralized. The network will be uncuttable.**