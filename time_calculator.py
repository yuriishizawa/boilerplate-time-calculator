ddef add_time(start, duration, day=None):
    hour_increment = 0
    n_days = 0
    string_days = str()
    days_week = {"Sunday": 0, "Monday": 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}

    start_time = start.split()[0].split(":")
    start_AMPM = start.split()[1]
    duration_time = duration.split(":")

    sum_minutes = int(start_time[1]) + int(duration_time[1])

    if sum_minutes < 60:
        pass
    else:
        sum_minutes = sum_minutes - 60
        hour_increment = 1

    sum_hour = int(duration_time[0]) + hour_increment
    total_hour = int(start_time[0]) + sum_hour

    if total_hour < 12:
        new_hour = total_hour
        new_AMPM = start_AMPM
        new_time = f'{new_hour}:{sum_minutes:02} {new_AMPM}'

    else:
        n = (total_hour)//12
        if total_hour%12 == 0:
            new_hour = 12
        else:
            new_hour = (total_hour)%12

        if n>2 and n%2 == 0:
            n_days = n/2
            string_days = f'({n_days} days later)'
            new_time = f'{new_hour}:{sum_minutes:02} {start_AMPM} {string_days}'
        elif n>2 and n%2 != 0:
            n_days = n//2 + 1
            if start_AMPM == "PM":
                new_AMPM = "AM"
            else:
                new_AMPM = "PM"
            new_time = f'{new_hour}:{sum_minutes:02} {new_AMPM} ({n_days} days later)'
        elif (n<=2 and start_AMPM == "PM") or (n==2 and start_AMPM == "AM"):
            n_days = 1
            new_AMPM = "AM"
            new_time = f'{new_hour}:{sum_minutes:02} {new_AMPM} (next day)'
        elif n<2 and start_AMPM == "AM":
            new_AMPM = "PM"
            new_time = f'{new_hour}:{sum_minutes:02} {new_AMPM}'


    if day != None:
        start_day = day
        end_day_id = (days_week[start_day.capitalize()] + n_days)%7
        end_day = [k for k,i in days_week.items() if i == end_day_id]
        if n_days == 0:
            new_time = f'{new_hour}:{sum_minutes:02} {new_AMPM}, {end_day[0]}'
        elif n_days == 1:
            new_time = f'{new_hour}:{sum_minutes:02} {new_AMPM}, {end_day[0]} (next day)'
        else:
            new_time = f'{new_hour}:{sum_minutes:02} {new_AMPM}, {end_day[0]} ({n_days} days later)'
            
    return new_time