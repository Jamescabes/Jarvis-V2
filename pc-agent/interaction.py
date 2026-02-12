import pyautogui
import time

class InteractionEngine:
    """
    Handles physical interaction with the PC (Mouse, Keyboard).
    """
    def __init__(self):
        # Safety feature: move mouse to corner to abort
        pyautogui.FAILSAFE = True

    def move_mouse(self, x: int, y: int, duration: float = 0.5):
        """Moves mouse to coordinates."""
        pyautogui.moveTo(x, y, duration=duration)
        return {"status": "success", "pos": (x, y)}

    def click(self, x: int = None, y: int = None, button: str = 'left'):
        """Clicks at coordinates or current position."""
        pyautogui.click(x=x, y=y, button=button)
        return {"status": "success", "button": button, "pos": (x, y) if x else pyautogui.position()}

    def type_text(self, text: str, interval: float = 0.05):
        """Types text on keyboard."""
        pyautogui.write(text, interval=interval)
        return {"status": "success", "text": text}

    def press_key(self, key: str):
        """Presses a specific key (e.g., 'enter', 'esc')."""
        pyautogui.press(key)
        return {"status": "success", "key": key}

    def hotkey(self, *args):
        """Executes a hotkey combination (e.g., 'ctrl', 'c')."""
        pyautogui.hotkey(*args)
        return {"status": "success", "keys": args}
