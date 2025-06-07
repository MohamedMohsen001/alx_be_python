from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"{current_date.date().year}-{current_date.date().month}-{current_date.date().day} {current_date.time().hour}-{current_date.time().minute}-{current_date.time().second}")
    
def calculate_future_date():
    number_of_days = int(input("Enter Number Of Days:"))
    future_date = datetime.now().date() + timedelta(number_of_days)
    print(f"{future_date.year}-{future_date.month}-{future_date.day}")