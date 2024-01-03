import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Chrono")

        self.state = False
        self.minutes = 25
        self.seconds = 0

        self.display = tk.Label(master, text="25:00", font=("Helvetica", 48), fg="red")
        self.display.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

    def reset_timer(self):
        self.stop_timer()
        self.minutes = 25
        self.seconds = 0
        self.display.config(text="25:00")

    def tick(self):
        if self.state:
            if self.seconds == 0:
                if self.minutes == 0:
                    messagebox.showinfo("Time's up!", "Take a break!")
                    self.reset_timer()
                    return
                else:
                    self.minutes -= 1
                    self.seconds = 59
            else:
                self.seconds -= 1
            time_format = '{:02d}:{:02d}'.format(self.minutes, self.seconds)
            self.display.config(text=time_format)
            self.master.after(1000, self.tick)

    def start_timer(self):
        self.state = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.tick()

    def stop_timer(self):
        self.state = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()