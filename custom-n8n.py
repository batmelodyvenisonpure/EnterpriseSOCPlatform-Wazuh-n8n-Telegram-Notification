#!/usr/bin/env python3

import sys
import json
import requests
import os
import logging
from datetime import datetime

# Setup logging
log_file = '/var/ossec/logs/integrations.log'
logging.basicConfig(filename=log_file, level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Log what we received
    logging.info(f"Python script started with {len(sys.argv)} args")
    
    # Need at least alert file and URL
    if len(sys.argv) < 3:
        logging.error("Not enough arguments")
        sys.exit(1)
    
    # First arg is alert file
    alert_file = sys.argv[1]
    logging.info(f"Alert file: {alert_file}")
    
    # Find the URL - look for http:// or https://
    webhook_url = None
    for arg in sys.argv:
        if arg.startswith('http://') or arg.startswith('https://'):
            webhook_url = arg
            logging.info(f"Found URL: {webhook_url}")
            break
    
    if not webhook_url:
        logging.error("No URL found in arguments")
        sys.exit(1)
    
    # Check if alert file exists
    if not os.path.exists(alert_file):
        logging.error(f"File not found: {alert_file}")
        sys.exit(1)
    
    # Read the alert
    try:
        with open(alert_file, 'r') as f:
            alert_data = json.load(f)
        logging.info("Alert file read successfully")
    except Exception as e:
        logging.error(f"Failed to read alert: {e}")
        sys.exit(1)
    
    # Add timestamp
    alert_data['received_at'] = datetime.utcnow().isoformat()
    
    # Send to n8n
    try:
        r = requests.post(webhook_url, json=alert_data, timeout=10)
        
        if r.status_code in [200, 201, 202]:
            logging.info(f"Sent successfully - Status: {r.status_code}")
            sys.exit(0)
        else:
            logging.error(f"Failed - Status: {r.status_code}")
            logging.error(f"Response: {r.text}")
            sys.exit(1)
            
    except requests.exceptions.ConnectionError:
        logging.error(f"Could not connect to {webhook_url}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
