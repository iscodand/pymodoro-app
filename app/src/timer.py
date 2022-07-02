import threading
import time
import winsound
from interface import PymodoroInterface
from notifications import PymodoroNotifications


class PymodoroTimer(PymodoroInterface, PymodoroNotifications):
    def __init__(self):
        self.pomodoros = 1
        self.stopped = False
        self.skipped = False
        self.running = False
        self.pymodoro_interface()

    # Config of Thread Timer
    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    # Defining main timer loop
    def timer_loop(self, full_seconds):
        timer_id = self.tabs.index(self.tabs.select()) + 1

        while full_seconds > 0 and not self.stopped:
            minutes, seconds = divmod(full_seconds, 60)

            if timer_id == 1:
                self.pomodoro_timer_label.config(
                    text=f"{minutes:02d} {seconds:02d}")

            elif timer_id == 2:
                self.short_break_timer_label.config(
                    text=f"{minutes:02d} {seconds:02d}")

            elif timer_id == 3:
                self.long_break_timer_label.config(
                    text=f"{minutes:02d} {seconds:02d}")

            self.root.update()
            time.sleep(1)
            full_seconds -= 1

    # Here is the pre start timer, a 5 seconds timer before the Pomodoro timer starts
    def pre_start_timer(self):
        full_seconds = 5

        self.timer_loop(full_seconds)

    # Here is the main logic of the timer, simple, but powerful
    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        full_seconds = 60 * 25
        short_break_seconds = 60 * 5
        long_break_seconds = 60 * 15

        if timer_id == 1:
            self.pre_start_timer()
            
            self.timer_loop(full_seconds)

            if not self.stopped or self.skipped or self.running:
                self.code_time_notification()
                winsound.PlaySound(sound="app/assets/sounds/sound.wav",
                                   flags=winsound.SND_FILENAME)
                self.pomodoros += 1
                self.pomodoros_count_label.config(
                    text=f"Pomodoro #{self.pomodoros}")

                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)

                else:
                    self.tabs.select(1)

                self.start_timer()

        elif timer_id == 2:
            self.pre_start_timer()

            self.timer_loop(short_break_seconds)

            if not self.stopped or self.skipped:
                self.short_break_time_notification()
                winsound.PlaySound(sound="app/assets/sounds/sound.wav",
                                   flags=winsound.SND_FILENAME)
                self.tabs.select(0)
                self.start_timer()

        elif timer_id == 3:
            self.pre_start_timer()

            self.timer_loop(long_break_seconds)

            if not self.stopped or self.skipped:
                self.long_break_time_notification()
                winsound.PlaySound(sound="app/assets/sounds/sound.wav",
                                   flags=winsound.SND_FILENAME)
                self.tabs.select(0)
                self.start_timer()

        else:
            print('Invalid Timer ID!')
    
    def reset_clock(self):
        self.stopped = True
        self.skipped = False
        self.running = False
        self.pomodoros = 0
        self.pomodoro_timer_label.config(text="25 00")
        self.short_break_timer_label.config(text="05 00")
        self.long_break_timer_label.config(text="15 00")
        self.pomodoros_count_label.config(text="Pomodoro #1")

    def skip_clock(self):
        current_tab = self.tabs.index(self.tabs.select())

        if current_tab == 0:
            self.pomodoro_timer_label.config(text="25 00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text="05 00")
        elif current_tab == 2:
            self.long_break_timer_label.config(text="15 00")

        self.skipped = True
        self.stopped = True
