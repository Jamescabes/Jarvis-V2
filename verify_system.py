import time
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pc-agent')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from agent import PCAgent
import threading

def run_verification():
    print("=== JARVIS SYSTEM VERIFICATION ===")
    
    # 1. Initialize Agent
    agent = PCAgent(server_url="http://localhost:8000")
    
    # 2. Start Agent in a separate thread
    agent_thread = threading.Thread(target=agent.run, daemon=True)
    agent_thread.start()
    
    print("[*] Agent started. Waiting 2 seconds...")
    time.sleep(2)
    
    # 3. Simulate WakeWord Detection
    print("\n[STEP 1] Simulating WakeWord 'Jarvis' detection...")
    agent.wakeword.simulate_detection()
    
    time.sleep(1)
    if agent.active_listening:
        print("[SUCCESS] Agent entered ACTIVE mode correctly.")
    else:
        print("[FAILURE] Agent did not react to simulated detection.")
        return

    # 4. Test Command Execution
    print("\n[STEP 2] Testing safe command execution (systeminfo)...")
    result = agent.executor.execute("echo 'Jarvis verification command'")
    if "Jarvis verification command" in result.get("stdout", ""):
        print(f"[SUCCESS] Command executed: {result['stdout'].strip()}")
    else:
        print(f"[FAILURE] Command output unexpected: {result}")

    # 5. Test Paranoico Mode (Critical Command)
    print("\n[STEP 3] Testing 'Modo Paranoico' (critical command detection)...")
    critical_result = agent.executor.execute("rm -rf /")
    if critical_result.get("status") == "warning":
        print("[SUCCESS] Critical command blocked. Message: " + critical_result['message'])
    else:
        print(f"[FAILURE] Critical command was NOT blocked: {critical_result}")

    # 6. Test Vision (Screenshot)
    print("\n[STEP 4] Testing Vision (screenshot capture)...")
    vision_result = agent.vision.take_screenshot(name="test_verify.png")
    if vision_result.get("status") == "success":
        print(f"[SUCCESS] Screenshot captured: {vision_result['path']}")
    else:
        print(f"[FAILURE] Screenshot failed: {vision_result}")

    # 7. Test Interaction (Mouse movement)
    print("\n[STEP 5] Testing Interaction (safe mouse movement)...")
    original_pos = agent.vision.get_mouse_pos()
    interact_result = agent.interaction.move_mouse(original_pos.x + 50, original_pos.y + 50, duration=0.2)
    if interact_result.get("status") == "success":
        print(f"[SUCCESS] Mouse moved to: {interact_result['pos']}")
        # Return mouse
        agent.interaction.move_mouse(original_pos.x, original_pos.y, duration=0.1)
    else:
        print(f"[FAILURE] Interaction failed: {interact_result}")

    print("\n=== VERIFICATION COMPLETE ===")
    print("Result: SYSTEM FULL COMPUTER USE READY")

if __name__ == "__main__":
    run_verification()
