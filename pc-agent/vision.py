import pyautogui
from PIL import Image
import os
import time

class VisionEngine:
    """
    Handles visual perception for the PC Agent (Screenshots, OCR, etc.)
    """
    def __init__(self, output_dir="screenshots"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def take_screenshot(self, name=None):
        """
        Captures the primary monitor and saves it to a file.
        """
        try:
            if name is None:
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                name = f"jarvis_vision_{timestamp}.png"
            
            filepath = os.path.join(self.output_dir, name)
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            
            # Create a thumbnail for low-bandwidth transfer (optional)
            thumb_path = os.path.join(self.output_dir, f"thumb_{name}")
            thumb = screenshot.copy()
            thumb.thumbnail((400, 400))
            thumb.save(thumb_path)
            
            print(f"[*] Screenshot saved: {filepath}")
            return {
                "status": "success",
                "path": filepath,
                "thumb_path": thumb_path,
                "size": screenshot.size
            }
        except Exception as e:
            print(f"[ERROR] VisionEngine failed to take screenshot: {e}")
            return {"status": "error", "message": str(e)}

    def get_screen_size(self):
        return pyautogui.size()

    def get_mouse_pos(self):
        return pyautogui.position()
