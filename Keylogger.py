import json
import time
import os
from datetime import datetime
from pynput import keyboard

class KeyloggerEngine:
    def __init__(self):
        self.log_data = []
        self.listener = None
        self.callback = None
        self.start_time = None

    def set_callback(self, callback):
        self.callback = callback

    def on_press(self, key):
        try:
            k = key.char if key.char is not None else str(key)
        except AttributeError:
            k = str(key)
        
        # Real-time human-readable timestamp
        readable_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        entry = {
            "event": "pressed", 
            "key": k, 
            "timestamp": readable_time
        }
        self.log_data.append(entry)

        if self.callback:
            self.callback(k)

    def start(self):
        self.log_data = []
        self.start_time = time.time()
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop(self):
        if self.listener:
            self.listener.stop()
            duration = time.time() - self.start_time
            self.save_logs()
            return self.get_session_stats(duration)
        return None

    def get_session_stats(self, duration):
        total_keys = len(self.log_data)
        # Calculate Words Per Minute (Average 5 characters = 1 word)
        wpm = round((total_keys / 5) / (duration / 60), 2) if duration > 0 else 0
        return {
            "total_keys": total_keys,
            "wpm": wpm,
            "duration": round(duration, 2)
        }

    def save_logs(self):
        with open("log_data.json", "w") as jf:
            json.dump(self.log_data, jf, indent=4)
        
        with open("log_raw.txt", "w") as tf:
            for item in self.log_data:
                key = item["key"]
                if key == "Key.space": tf.write(" ")
                elif key == "Key.enter": tf.write("\n")
                elif "Key" not in key: tf.write(key)

    def open_log_folder(self):
        os.startfile(os.getcwd())