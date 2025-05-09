
#!/bin/bash
sleep 10
export DISPLAY=:0
chromium-browser --kiosk http://localhost:5000 &
