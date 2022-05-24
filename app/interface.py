import tkinter as tk
import sv_ttk
from tkinter import TOP, ttk


class PomodoroInterface():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Pymodoro Timer")
        self.root.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(
            file='app\icon\pymodoro-icon.png'))

        # Interface Layout
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", padding=6, font=("Unbutu", 12))
        self.s.configure("TButton", font=("Unbutu", 12))
        
        sv_ttk.set_theme("dark")

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=50, padx=50)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.pomodoro_timer_label = ttk.Label(
            self.tab1, text="25:00", font=("Unbutu", 50))
        self.pomodoro_timer_label.pack(pady=50)

        self.short_break_timer_label = ttk.Label(
            self.tab2, text="05:00", font=("Unbutu", 50))
        self.short_break_timer_label.pack(pady=50)

        self.long_break_timer_label = ttk.Label(
            self.tab3, text="15:00", font=("Unbutu", 50))
        self.long_break_timer_label.pack(pady=50)

        self.tabs.add(self.tab1, text="Code Time")
        self.tabs.add(self.tab2, text="Coffee")
        self.tabs.add(self.tab3, text="Social")

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
            self.grid_layout, text="Pomodoros: 0", font=("Ubuntu Bold", 14))
        self.pomodoros_count_label.grid(row=1, column=1, pady=30)

        self.choose_theme_button = ttk.Button(
            self.grid_layout, text="Theme", command=self.choose_theme)
        self.choose_theme_button.grid(row=2, column=1, pady=30)

        self.pomodoros = 0
        self.stopped = False
        self.skipped = False
        self.running = False

        self.root.resizable(False, False)
        self.root.mainloop()

    def choose_theme(self):
        return sv_ttk.toggle_theme()
