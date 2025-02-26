from datetime import datetime

# Get today's date
today_date = datetime.now().strftime("%d-%m-%Y")
print(type(today_date), today_date)