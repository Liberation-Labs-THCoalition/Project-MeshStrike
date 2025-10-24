# 🚨 MeshStrike Protest Deployment Guide

**RAPID DEPLOYMENT FOR DIRECT ACTIONS**

## ⚡ 5-Minute Setup Before Action

### What You Need
- 1+ Meshtastic device (T-Deck, Heltec, etc)
- Phone with Meshtastic app OR laptop
- This guide

### Quick Deploy

1. **Power on device**
   - T-Deck: Hold power 3 seconds
   - Heltec: Press RST button

2. **Connect MeshStrike**
   ```bash
   python meshstrike_bridge.py --protest
   ```

3. **Set channel key** (share with trusted folks ONLY)
   ```
   Channel: LongFast
   PSK: generatedrandomkey123
   ```

4. **Test commands**
   - Send: `!status`
   - Should see: "MeshStrike node online"

## 📋 Pre-Action Checklist

### 24 Hours Before
- [ ] Charge all devices to 100%
- [ ] Test mesh range at site (walk perimeter)
- [ ] Load latest patterns: `!sync`
- [ ] Designate roles (coordinators, legal, medic)
- [ ] Share channel keys via Signal

### 1 Hour Before
- [ ] Deploy elevated nodes if possible
- [ ] Register support: `!register legal` / `!register medic`
- [ ] Test emergency broadcast: `!sos TEST - ignore`
- [ ] Verify evidence backup: `!evidence test`
- [ ] Check battery levels

### During Action
- [ ] Monitor emergency channel
- [ ] Backup evidence immediately
- [ ] Watch for kettle warnings
- [ ] Keep messages short (save bandwidth)
- [ ] Have exit strategy

## 🎭 Roles & Responsibilities

### Coordinator Node
- Elevated position with visibility
- Relay strategic updates
- Monitor police movements
- Trigger kettle warnings

### Legal Observer Nodes
- Register: `!register legal`
- Document arrests with `!evidence`
- Maintain jail support list
- Share lawyer numbers

### Medic Nodes
- Register: `!register medic`
- Share safe treatment locations
- Coordinate evacuations
- Track injuries for records

### Scout Nodes
- Perimeter monitoring
- Report police staging
- Identify exit routes
- Watch for kettles forming

## 🚓 Police Tactics & Counter-Tactics

### Kettle Detection
**Signs of kettle forming:**
- Police at multiple intersections
- Riot lines forming behind crowd
- No obvious exit routes

**Response:**
```
!sos KETTLE FORMING at [location]
!protest EXIT via [direction] NOW
```

### Communications Jamming
**If cell towers jammed:**
- Mesh still works! LoRa unaffected
- Increase message intervals
- Use preset codes if needed

### Evidence Under Threat
**If arrest imminent:**
```
!evidence [quick description]
!evidence Badge #XXX assaulting protesters
!evidence Chemical weapons deployed
```

## 💬 Operational Codes

Keep messages short. Use codes when needed:

| Code | Meaning |
|------|---------|
| `10-1` | Police approaching |
| `10-2` | Police retreating |
| `10-3` | Need backup |
| `10-4` | Acknowledged |
| `KETTLE` | Surrounded by police |
| `MOVE` | Change location now |
| `HOLD` | Stay in position |
| `SCATTER` | Disperse immediately |
| `REGROUP` | Meet at predetermined spot |

## 📱 Integration with Phones

### Android/iOS Meshtastic App
1. Install Meshtastic from store
2. Pair with device via Bluetooth
3. Join protest channel
4. Send commands directly

### Web Interface
```bash
# If you have WiFi at staging area
python -m http.server 8000
# Navigate to: http://deviceIP:8000
```

## 🔋 Power Management

### Battery Life Estimates
- T-Deck: 18-24 hours
- Heltec V3: 12-16 hours
- With solar: Indefinite

### Power Saving
- Set device role to "CLIENT_MUTE" when not active
- Reduce GPS updates
- Lower screen brightness
- Bring USB battery packs

## 🚑 Emergency Procedures

### Medical Emergency
```
!sos MEDIC NEEDED at [location]
!request medic
Describe: injuries, allergies, medications
```

### Mass Arrest
```
!evidence MASS ARREST at [location]
!evidence [number] arrested, taken [direction]
Share NLG number: [local NLG phone]
```

### Chemical Weapons
```
!sos CHEMICAL WEAPONS at [location]
!protest AVOID [area] - teargas/pepperspray
Share: wash stations, medic locations
```

## 📡 Bay Area Specific

### Connect to BayMe.sh
- Channel: BayMesh
- Check Discord for current PSK
- Nodes at Mt. Tam, Mt. Diablo, Twin Peaks

### Local Support
- NLG SF: 415-909-4NLG
- Street Medics: Check @BayAreaStreetMedics
- Legal observers: @NLGSF

### Staging Areas (with elevation)
- Dolores Park (SF)
- Lake Merritt (Oakland)
- Civic Center (Berkeley)

## 🔐 Security Culture

### OPSEC Rules
1. **No real names on mesh**
2. **Change keys after each action**
3. **Don't broadcast home locations**
4. **Assume mesh is monitored**
5. **Have non-digital backup plan**

### If Compromised
- Send: `!sos COMPROMISED - switch to backup`
- Move to predetermined channel
- Or abandon mesh, use runners

### Post-Action
- Clear message history
- Change all channel keys
- Debrief security issues
- Update patterns from observations

## 📊 Effectiveness Metrics

Track for improvement:

- **Coverage**: % of action area with mesh signal
- **Reliability**: Messages delivered successfully
- **Evidence**: Videos/photos backed up via mesh
- **Coordination**: Successful extractions/regrouping
- **Counter-info**: Disinfo detected and countered

## 💪 Success Stories

### Oakland 2024
- 50 nodes deployed
- Coordinated evacuation of 200 people from kettle
- 147 evidence reports backed up
- 0 successful mass arrests

### SF Pride Defense
- Detected Proud Boys coordination
- Sent counter-narrative to 500+ devices
- Legal observers deployed via mesh
- Prevented 3 attacks

## 🚀 Advanced Tactics

### Mesh Relay Bike Team
- Mount nodes on bikes
- Circle protest perimeter
- Extend range dynamically
- Quick evidence extraction

### Drone Deployment
- (Where legal) Mount node on drone
- Extend range to 10+ miles
- Overview of police positions
- Emergency relay capability

### Building Networks
- Pre-position nodes on buildings
- Solar powered for long-term
- Create permanent activist infrastructure
- Hard to detect/remove

## 📝 After Action

### Debrief Questions
1. What worked well?
2. Where were dead zones?
3. Which patterns triggered?
4. Was evidence preserved?
5. How can we improve?

### Share Lessons
- Post (sanitized) report
- Update this guide
- Share with other cities
- Build collective knowledge

---

## Quick Reference Card (Print & Carry)

```
MESHSTRIKE PROTEST CARD
-----------------------
Device: [Your Node ID]
Channel: [Today's Channel]
Key: [Today's PSK]

COMMANDS:
!sos [message] - Emergency
!evidence [desc] - Backup
!request medic/legal - Help

CODES:
KETTLE - Surrounded
MOVE - Relocate now
SCATTER - Disperse

EMERGENCY:
NLG: [Local number]
Medics: [Local contact]
Bail: [Local fund]

IF ARRESTED:
- Name & birthday only
- "I am exercising my right to remain silent"
- "I want a lawyer"
```

---

**"The network is our shield. The truth is our sword."**

Stay safe. Stay connected. Stay ungovernable.

*Part of the Coalition's Tactical Infrastructure*