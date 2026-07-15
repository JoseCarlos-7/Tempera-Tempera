import random
import datetime as dt

def get_date(
        date_type:str,
        min_year:int = 1960,
        max_year:int = 2002):
    
    assert date_type in ['now','today','custom','random'] ,\
          "Date_type must be one of these: 'now','today','custom','random'"

    if date_type == 'random':
        year = random.randint(min_year,max_year)
        month = random.randint(1,12)
        day = random.randint(1,30) if month != 2 else random.randint(1,28)
        return f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}'

    if date_type == 'today':

        return dt.date.today().strftime('%Y-%m-%d')
