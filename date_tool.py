from datetime import datetime

def calculate_days(purchase_date):
    purchase = datetime.strptime(purchase_date, "%Y-%m-%d")
    today = datetime.today()
    return (today - purchase).days

