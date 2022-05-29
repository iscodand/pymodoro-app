from notifypy import Notify

class PymodoroNotifications():
    def code_time_notification(self):
        notification = Notify()
        notification.application_name = "Pymodoro App"
        notification.title = "Code Time End!"
        notification.message = "Work time end! Get some coffee!"
        notification.icon = "app/assets/icons/pymodoro-icon.png"
        notification.send()

    def short_break_time_notification(self):
        notification = Notify()
        notification.application_name = "Pymodoro App"
        notification.title = "Coffee Time End!"
        notification.message = "Coffee Time End! Let's go and Code!"
        notification.icon = "app/assets/icons/pymodoro-icon.png"
        notification.send()

    def long_break_time_notification(self):
        notification = Notify()
        notification.application_name = "Pymodoro App"
        notification.title = "Social Time End!"
        notification.message = "Social time end! Let's go and Code!"
        notification.icon = "app/assets/icons/pymodoro-icon.png"
        notification.send()