import requests
from unittest.mock import Mock
from datetime import datetime


def isweekday():
    today = datetime.today()
    day_of_the_week = today.weekday()
    return (0 <= day_of_the_week < 5) # 0 Monday 6 Sunday 
    
def getholidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None
