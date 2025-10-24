#!/bin/bash
# MeshStrike Installer - Get mesh-ready in minutes
# Compatible with Cyber Pony Express infrastructure

echo "╔════════════════════════════════════════════════════════╗"
echo "║                                                        ║"
echo "║     MESHSTRIKE INSTALLER v1.0                         ║"
echo "║     Counter-Propaganda Mesh Network                   ║"
echo "║     Compatible with Cyber Pony Express                ║"
echo "║                                                        ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    OS="windows"
else
    OS="unknown"
fi

echo "[*] Detected OS: $OS"

# Check Python
echo "[*] Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "[!] Python not found. Please install Python 3.8+"
    exit 1
fi

echo "[*] Using Python: $($PYTHON_CMD --version)"

# Create virtual environment
echo "[*] Creating virtual environment..."
$PYTHON_CMD -m venv venv

# Activate virtual environment
echo "[*] Activating virtual environment..."
if [[ "$OS" == "windows" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install dependencies
echo "[*] Installing dependencies..."
pip install --upgrade pip
pip install meshtastic pubsub

# Optional dependencies
echo "[*] Installing optional dependencies..."
pip install qrcode[pil] 2>/dev/null || echo "   QR code generation not available"

# Check for Meshtastic device
echo ""
echo "[*] Checking for Meshtastic devices..."

if [[ "$OS" == "linux" ]]; then
    DEVICES=$(ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null)
elif [[ "$OS" == "macos" ]]; then
    DEVICES=$(ls /dev/tty.usbserial* /dev/tty.usbmodem* 2>/dev/null)
elif [[ "$OS" == "windows" ]]; then
    echo "   Please check Device Manager for COM ports"
    DEVICES=""
else
    DEVICES=""
fi

if [ -z "$DEVICES" ]; then
    echo "[!] No Meshtastic device detected"
    echo "    Connect your device and run: python bridge/meshstrike_bridge.py --port <PORT>"
else
    echo "[✓] Found devices:"
    echo "$DEVICES" | while read -r device; do
        echo "    $device"
    done
    FIRST_DEVICE=$(echo "$DEVICES" | head -n 1)
fi

# Create database
echo ""
echo "[*] Initializing database..."
$PYTHON_CMD -c "
import sqlite3
conn = sqlite3.connect('meshstrike.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS patterns
            (id TEXT PRIMARY KEY,
             category TEXT,
             pattern TEXT,
             severity TEXT,
             counter_narrative TEXT,
             funders TEXT,
             timestamp INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS evidence
            (id TEXT PRIMARY KEY,
             location TEXT,
             description TEXT,
             hash TEXT,
             sender_id TEXT,
             timestamp INTEGER,
             verified_count INTEGER DEFAULT 0)''')
c.execute('''CREATE TABLE IF NOT EXISTS protests
            (id TEXT PRIMARY KEY,
             location TEXT,
             time INTEGER,
             description TEXT,
             safety_info TEXT,
             participant_count INTEGER DEFAULT 0)''')
conn.commit()
conn.close()
print('[✓] Database initialized')
"

# Generate default patterns
echo "[*] Generating default patterns..."
cd patterns
$PYTHON_CMD pattern_converter.py > /dev/null 2>&1
cd ..
echo "[✓] Patterns generated"

# Create launch scripts
echo ""
echo "[*] Creating launch scripts..."

# Linux/Mac launch script
cat > start_meshstrike.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
echo "Starting MeshStrike bridge..."
python bridge/meshstrike_bridge.py --protest $@
EOF
chmod +x start_meshstrike.sh

# Windows launch script
cat > start_meshstrike.bat << 'EOF'
@echo off
call venv\Scripts\activate
echo Starting MeshStrike bridge...
python bridge\meshstrike_bridge.py --protest %*
EOF

echo "[✓] Launch scripts created"

# Test installation
echo ""
echo "[*] Testing installation..."
$PYTHON_CMD -c "
import meshtastic
import pubsub
print('[✓] All modules loaded successfully')
"

# Print instructions
echo ""
echo "════════════════════════════════════════════════════════"
echo "                    INSTALLATION COMPLETE!"
echo "════════════════════════════════════════════════════════"
echo ""
echo "TO START MESHSTRIKE:"
echo ""

if [ ! -z "$FIRST_DEVICE" ]; then
    echo "  ./start_meshstrike.sh --port $FIRST_DEVICE"
else
    echo "  ./start_meshstrike.sh --port <YOUR_DEVICE_PORT>"
fi

echo ""
echo "QUICK START COMMANDS:"
echo "  !help     - Show all commands"
echo "  !patterns - Get counter-propaganda patterns"
echo "  !evidence - Backup evidence"
echo "  !sos      - Emergency broadcast"
echo ""
echo "JOIN THE BAY AREA MESH:"
echo "  1. Install Meshtastic app on phone"
echo "  2. Connect to device via Bluetooth"
echo "  3. Join channel: BayMesh"
echo "  4. Check Discord for current PSK"
echo ""
echo "PROTEST MODE:"
echo "  ./start_meshstrike.sh --protest"
echo ""
echo "════════════════════════════════════════════════════════"
echo "    The network cannot be cut. The truth cannot be stopped."
echo "════════════════════════════════════════════════════════"