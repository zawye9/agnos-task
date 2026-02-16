from datetime import datetime

database = {}

def get_today_date():
    return datetime.utcnow().strftime("%Y-%m-%d")

def update_today_timestamp():
    today = get_today_date()

    if today not in database:
        database[today] = {
            "date": today,
            "updatedAt": datetime.utcnow().isoformat()
        }
    else:
        database[today]["updatedAt"] = datetime.utcnow().isoformat()

    print("Updated timestamp:", database[today]["updatedAt"])
    return database[today]

def get_today_record():
    today = get_today_date()
    return database.get(today, {})
