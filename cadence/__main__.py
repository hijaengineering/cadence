import time
import tkinter as tk
from tkinter import messagebox

import keyboard

MED_KPM = 300
MAX_KPM = 400
GEOMETRY = "200x150"
TEXT_COLOR = "white"
RESET_INTERVAL = 10  # Reset every 10 seconds


class TypingSpeedTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("cadence")
        self.root.geometry(GEOMETRY)
        self.root.attributes("-topmost", True)  # Always on top
        self.root.overrideredirect(True)  # Hide window decorations

        self.label = tk.Label(
            self.root,
            text="0 KPM",
            font=("Arial", 16),
            bg="white",
            fg=TEXT_COLOR,  # This controls the text color
        )
        self.label.pack(fill=tk.BOTH, expand=True)

        self.start_time = time.time()
        self.keystrokes = 0

        keyboard.on_press(self.key_pressed)
        self.update_speed()

        # Add window close event handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.root.mainloop()

    def key_pressed(self, event):
        self.keystrokes += 1

    def update_speed(self):
        elapsed_time = time.time() - self.start_time
        kpm = int((self.keystrokes / elapsed_time) * 60) if elapsed_time > 0 else 0

        self.label.config(text=f"{kpm} KPM")

        if kpm > MAX_KPM:
            self.label.config(bg="red")
        elif (kpm > MED_KPM) and (kpm < MAX_KPM):
            self.label.config(bg="yellow")
        else:
            self.label.config(bg="white")

        if elapsed_time > RESET_INTERVAL:
            self.start_time = time.time()
            self.keystrokes = 0

        self.root.after(1000, self.update_speed)  # Update every second

    def on_close(self):
        # Show warning before closing the window
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()


if __name__ == "__main__":
    TypingSpeedTracker()
