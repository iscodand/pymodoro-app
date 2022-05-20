import threading
import time
import tkinter as tk
from tkinter import ttk


class PomodoroTimer():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x400")
        self.root.title("Pymodoro Timer")

        # Interface Layout
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Unbutu", 12))
        self.s.configure("TButton", font=("Unbutu", 12))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, padx=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=200)

        self.pomodoro_timer_label = ttk.Label(
            self.tab1, text="25:00", font=("Ubuntu", 30))
        self.pomodoro_timer_label.pack(pady=20)

        self.short_break_timer_label = ttk.Label(
            self.tab2, text="05:00", font=("Ubuntu", 30))
        self.short_break_timer_label.pack(pady=20)

        self.long_break_timer_label = ttk.Label(
            self.tab3, text="15:00", font=("Ubuntu", 30))
        self.long_break_timer_label.pack(pady=20)

        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=20)

        self.start_button = ttk.Button(
            self.grid_layout, text="Start", command=self.start_timer_thread())
        self.start_button.grid(row=0, column=0)

        self.reset_button = ttk.Button(
            self.grid_layout, text="Reset", command=self.reset_clock())
        self.reset_button.grid(row=0, column=1)

        self.skip_button = ttk.Button(
            self.grid_layout, text="Skip", command=self.skip_clock())
        self.skip_button.grid(row=0, column=2)

        self.pomodoros_count_label = ttk.Label(
            self.grid_layout, text="Pomodoros: 0", font=("Ubuntu", 12))
        self.pomodoros_count_label.grid(row=1, column=1, pady=20)

        self.pomodoros = 0
        self.stopped = False
        self.skipped = False

        self.root.mainloop()

    def start_timer_thread(self):
        t = threading.Thread(target=self.start_timer)
        t.start()

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
                self.pomodoros_counter_label.config(
                    text=f"Pomodoros {self.pomodoros}")

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
        pass

    def skip_clock(self):
        pass


PomodoroTimer()
