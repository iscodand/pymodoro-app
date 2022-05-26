import tkinter as tk
import sv_ttk
import time
from tkinter import ttk


class PomodoroInterface():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x550")
        self.root.title("Pymodoro Timer")
        self.root.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(
            file="app/assets/icons/pymodoro-icon.png"))

        # Setting Style
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", padding=6, font=("Montserrat", 12))
        self.s.configure("TButton", font=("Montserrat", 12))

        sv_ttk.set_theme("dark")

        # Setting Tabs with ttk.Notebook
        self.tabs = ttk.Notebook(self.root, width=150)
        self.tabs.pack(pady=50, padx=50, ipadx=85)

        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tab3 = ttk.Frame(self.tabs)

        self.pomodoro_timer_label = ttk.Label(
            self.tab1, text="25 00", font=("Montserrat SemiBold", 60))
        self.pomodoro_timer_label.pack(pady=50)

        self.short_break_timer_label = ttk.Label(
            self.tab2, text="05 00", font=("Montserrat SemiBold", 60))
        self.short_break_timer_label.pack(pady=50)

        self.long_break_timer_label = ttk.Label(
            self.tab3, text="15 00", font=("Montserrat SemiBold", 60))
        self.long_break_timer_label.pack(pady=50)

        self.pomodoros_count_label = ttk.Label(
            self.tab1, text="Pomodoro #1", font=("Montserrat Thin", 9))
        self.pomodoros_count_label.pack(pady=20)

        self.short_break_note_label = ttk.Label(
            self.tab2, text="Coffee Time!", font=("Montserrat Thin", 9))
        self.short_break_note_label.pack(pady=20)

        self.long_break_note_label = ttk.Label(
            self.tab3, text="Long Rest Time!", font=("Montserrat Thin", 9))
        self.long_break_note_label.pack(pady=20)

        self.tabs.add(self.tab1, text="  Code Time   ")
        self.tabs.add(self.tab2, text="   Coffee   ")
        self.tabs.add(self.tab3, text="   Social   ")

        # Set the buttons and his respective positions
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack()

        self.start_button = ttk.Button(
            self.grid_layout, text="Start", command=self.start_timer_thread, width=20)
        self.start_button.grid(row=0, column=1, padx=10)

        self.reset_button = ttk.Button(
            self.grid_layout, text="Reset", command=self.reset_clock)
        self.reset_button.grid(row=0, column=0, padx=10)

        self.skip_button = ttk.Button(
            self.grid_layout, text="Skip", command=self.skip_clock)
        self.skip_button.grid(row=0, column=2, padx=10)

        self.choose_theme_icon = tk.PhotoImage(file="app/assets/icons/light_icon.png")
        self.choose_theme_icon_sample = self.choose_theme_icon.subsample(
            10, 10)

        self.choose_theme_button = ttk.Button(
            self.grid_layout,
            image=self.choose_theme_icon_sample,
            compound="center",
            command=self.choose_theme)
        self.choose_theme_button.grid(row=2, column=1, pady=30)

        self.root.resizable(False, False)
        self.root.mainloop()

    def choose_theme(self):
        time.sleep(0.25)
        return sv_ttk.toggle_theme()
