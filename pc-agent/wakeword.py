import os
import threading
import time
import sounddevice as sd
import numpy as np

class WakeWordEngine:
    """
    WakeWord engine using SoundDevice instead of PyAudio for better compatibility on Windows.
    """
    def __init__(self, keyword="jarvis"):
        self.keyword = keyword
        self.is_listening = False
        self._on_detected_callback = None
        self.sample_rate = 16000 # Standard for most STT engines

    def start(self, callback):
        """
        Starts the listening thread using SoundDevice.
        """
        self._on_detected_callback = callback
        self.is_listening = True
        self.thread = threading.Thread(target=self._listen_loop, daemon=True)
        self.thread.start()
        print(f"[*] Wakeword Engine started (SoundDevice). Listening for '{self.keyword}'...")

    def stop(self):
        self.is_listening = False
        if hasattr(self, 'thread') and self.thread.is_alive():
            self.thread.join()

    def _listen_loop(self):
        """
        Real audio capture loop using sounddevice.
        """
        try:
            with sd.InputStream(samplerate=self.sample_rate, channels=1, dtype='int16') as stream:
                while self.is_listening:
                    # Capture a chunk of audio
                    audio_chunk, overflowed = stream.read(512)
                    if overflowed:
                        print("[!] Audio overflow")
                    
                    # Placeholder: Process audio_chunk with Porcupine/PocketSphinx
                    # For now, just keep the loop alive
                    time.sleep(0.01)
        except Exception as e:
            print(f"[ERROR] WakeWord Engine failed to access microphone: {e}")
            self.is_listening = False
            
    def simulate_detection(self):
        if self._on_detected_callback:
            print(f"[!] Wakeword detected: {self.keyword}")
            self._on_detected_callback()
