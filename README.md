# net_watchdog

A lightweight Python tool for sysadmins to monitor remote network endpoints in hostile environments.

## Features
- Periodic ping monitoring of configured hosts
- Simple HTTP health checks
- Logs alerts to local file
- Minimal dependencies (Python 3.x)

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/syriaobserver/net_watchdog.git
cd net_watchdog
pip install -r requirements.txt

Usage
Edit config.yaml to add your target hosts and monitoring interval.
Run the watchdog script:
python3 watchdog.py config.yaml
Example config.yaml


# Target hosts to monitor for availability
hosts:
  - http://192.168.10.1   # local router
  - http://10.0.0.254     # VPN gateway
  - https://relay.opsnet.org
  - https://control.silentchain.net
interval: 300  # check interval in seconds (5 minutes)
Known Issues
Limited error handling for unreachable hosts.

No TLS verification for HTTPS endpoints (consider patching).

Logs are not rotated automatically.




##Disclaimer
This project is provided as-is for educational and demonstration purposes only.
The author accepts no responsibility for misuse or any damage resulting from its use in production environments.

