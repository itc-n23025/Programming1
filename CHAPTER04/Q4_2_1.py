from datetime import datetime, timedelta


def classify_days(days=0):
    today = datetime.now().date()
    target_date = today + timedelta(days=days)

    if target_date == today:
        return "今日"
    elif target_date == today + timedelta(days=1):
        return "明日"
    elif target_date == today - timedelta(days=1):
        return "昨日"
    else:
        return "今日より1日を超えて離れた日"


print(classify_days(-1))
print(classify_days())
print(classify_days(1))
print(classify_days(10))
