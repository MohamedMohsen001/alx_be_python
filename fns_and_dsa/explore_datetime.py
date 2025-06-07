from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    
def calculate_future_date():
    number_of_days = int(input("Enter Number Of Days:"))
    future_date = datetime.now().date() + timedelta(number_of_days)
    print(f"{future_date.year}-{future_date.month:02d}-{future_date.day:02d}")