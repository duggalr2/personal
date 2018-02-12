from pushbullet import PushBullet


def send_notification(reminder):
    apiKey = "o.KyxljpIYKkRPnUvzyNIgDZvKsVObqkFN"
    p = PushBullet(apiKey)
    # print(p.devices)
    motog = p.devices[-1]
    motog.push_note('REMINDER', reminder)
