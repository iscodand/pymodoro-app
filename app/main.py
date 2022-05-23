import threading
import time
import tkinter as tk
from tkinter import ttk
from playsound import playsound


class PomodoroTimer():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x425")
        self.root.title("Pymodoro Timer")
        self.root.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(
            file='app\icon\pymodoro-icon.png'))

        # Interface Layout
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", padding=6, font=("Unbutu", 12))
        self.s.configure("TButton", font=("Unbutu", 12))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=50, padx=50)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.pomodoro_timer_label = ttk.Label(
            self.tab1, text="25:00", font=("Ubuntu", 50))
        self.pomodoro_timer_label.pack(pady=50)

        self.short_break_timer_label = ttk.Label(
            self.tab2, text="05:00", font=("Ubuntu", 50))
        self.short_break_timer_label.pack(pady=50)

        self.long_break_timer_label = ttk.Label(
            self.tab3, text="15:00", font=("Ubuntu", 50))
        self.long_break_timer_label.pack(pady=50)

        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack()

        self.start_button = ttk.Button(
            self.grid_layout, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0, padx=10)

        self.reset_button = ttk.Button(
            self.grid_layout, text="Reset", command=self.reset_clock)
        self.reset_button.grid(row=0, column=1, padx=10)

        self.skip_button = ttk.Button(
            self.grid_layout, text="Skip", command=self.skip_clock)
        self.skip_button.grid(row=0, column=2, padx=10)

        self.pomodoros_count_label = ttk.Label(
            self.grid_layout, text="Pomodoros: 0", font=("Ubuntu", 12))
        self.pomodoros_count_label.grid(row=1, column=1, pady=20)

        self.pomodoros = 0
        self.stopped = False
        self.skipped = False
        self.running = False

        self.root.mainloop()

    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_seconds = 60 * 25

            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pomodoro_timer_label.config(
                    text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1

            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoros_count_label.config(
                    text=f"Pomodoros: {self.pomodoros}")

                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)

                else:
                    self.tabs.select(1)

                self.start_timer()

        elif timer_id == 2:
            full_seconds = 60 * 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.short_break_timer_label.config(
                    text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1

            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()

        elif timer_id == 3:
            full_seconds = 60 * 15

            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.long_break_timer_label.config(
                    text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1

            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()

        else:
            print('Invalid Timer ID!')

    def reset_clock(self):
        self.stopped = True
        self.skipped = False
        self.running = False
        self.pomodoros = 0
        self.pomodoro_timer_label.config(text="25:00")
        self.short_break_timer_label.config(text="05:00")
        self.long_break_timer_label.config(text="15:00")
        self.pomodoros_count_label.config(text="Pomodoros: 0")

    def skip_clock(self):
        current_tab = self.tabs.index(self.tabs.select())

        if current_tab == 0:
            self.pomodoro_timer_label.config(text="25:00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text="05:00")
        elif current_tab == 2:
            self.long_break_timer_label.config(text="15:00")

        self.skipped = True
        self.stopped = True


PomodoroTimer()
