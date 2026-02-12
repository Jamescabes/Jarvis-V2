import time
import socket
import os

class PCAgent:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.status = "Idle"

    def run(self):
        print(f"Jarvis PC Agent starting on {self.hostname}...")
        while True:
            # Placeholder for command listener
            time.sleep(10)

if __name__ == "__main__":
    agent = PCAgent()
    agent.run()
