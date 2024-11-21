import time
from datetime import datetime
from plyer import notification

notification_times = [
    "9:30",
    "11:20",
    "12:50",
    "14:20",
    "15:50",
]

notification_title = "Reminder"
notification_message = "This message must be important!"


def show_notification(title, message):
    notification.notify(title=title, message=message, timeout=10)


if __name__ == "__main__":
    print("Notification script is running...")
    while True:
        current_time = datetime.now().strftime("%H:%M")

        if current_time in notification_times:
            show_notification(current_time, notification_message)
            # notification_times.remove(current_time)

        time.sleep(60)
