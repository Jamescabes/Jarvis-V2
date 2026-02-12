import time
import socket
import os
import json
from executor import CommandExecutor

class PCAgent:
    def __init__(self, server_url="http://localhost:8000"):
        self.hostname = socket.gethostname()
        self.executor = CommandExecutor()
        self.server_url = server_url
        self.agent_id = None # To be assigned by backend

    def run(self):
        print(f"Jarvis PC Agent starting on {self.hostname}...")
        self.report_status()
        
        while True:
            if self.check_kill_switch():
                print("FATAL: Kill Switch active. Shutting down agent.")
                break
                
            print(f"[{time.strftime('%H:%M:%S')}] Agent heartbeat...")
            time.sleep(30)

    def check_kill_switch(self):
        # Placeholder for real API check
        # In production, this should be an extremely fast/reliable check
        return False

    def report_status(self):
        sys_info = self.executor.get_system_info()
        status_data = {
            "hostname": self.hostname,
            "status": "online",
            "info": sys_info
        }
        print(f"Reporting status: {json.dumps(status_data, indent=2)}")

if __name__ == "__main__":
    agent = PCAgent()
    agent.run()
