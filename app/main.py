import threading
import time
import winsound
from interface import PomodoroInterface


class PomodoroTimer(PomodoroInterface):
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
            full_seconds = 5

            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pomodoro_timer_label.config(
                    text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1

            if not self.stopped or self.skipped:
                winsound.PlaySound(sound="app\sounds\sound.wav",
                                   flags=winsound.SND_FILENAME)
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
            full_seconds = 5

            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.short_break_timer_label.config(
                    text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1

            if not self.stopped or self.skipped:
                winsound.PlaySound(sound="app\sounds\sound.wav",
                                    flags=winsound.SND_FILENAME)
                self.tabs.select(0)
                self.start_timer()

        elif timer_id == 3:
            full_seconds = 60 * 15
            full_seconds = 5

            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.long_break_timer_label.config(
                    text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1

            if not self.stopped or self.skipped:
                winsound.PlaySound(sound="app\sounds\sound.wav",
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
