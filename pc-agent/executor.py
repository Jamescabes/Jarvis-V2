import subprocess
import os
import platform

class CommandExecutor:
    def __init__(self):
        self.os_type = platform.system()

    def assess_command(self, command: str):
        # Local risk assessment (synchronized with backend logic)
        critical_keywords = ["rm ", "format", "del /s", "drop table"]
        if any(kw in command.lower() for kw in critical_keywords):
            return "critical"
        return "safe"

    def execute(self, command: str, confirmed: bool = False):
        """
        Executes a system command with risk assessment.
        """
        risk = self.assess_command(command)
        if risk == "critical" and not confirmed:
            return {"status": "warning", "message": "Action requires double confirmation"}

    def get_system_info(self):
        return {
            "os": self.os_type,
            "release": platform.release(),
            "cpu": platform.processor(),
            "cwd": os.getcwd()
        }
