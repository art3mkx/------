from datetime import datetime, timedelta

def get_future_date(days_ahead):
    current_time = datetime.today()
    
    if type(days_ahead) != int:
        return format_date(current_time)
    
    time_delta = timedelta(days=days_ahead)
    result_date = current_time + time_delta
    
    return format_date(result_date)

def format_date(dt):
    day = str(dt.day).zfill(2)
    month = str(dt.month).zfill(2)
    year = dt.year
    hour = str(dt.hour).zfill(2)
    minute = str(dt.minute).zfill(2)
    second = str(dt.second).zfill(2)
    
    return f"{day}-{month}-{year} {hour}:{minute}:{second}"
