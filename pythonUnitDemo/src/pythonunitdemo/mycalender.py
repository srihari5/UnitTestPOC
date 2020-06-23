import requests
from unittest.mock import Mock
from datetime import datetime


def isweekday():
    """
    Checks whether today is weekday and returns true 

    Returns:
      bool: true if current day is Monday - Frday , false if saturday or sunday

    """
    today = datetime.today()
    day_of_the_week = today.weekday()
    return (0 <= day_of_the_week < 5) # 0 Monday 6 Sunday 


def getholidays():
    """
    Will get all holidays from api

    Returns:
        Dictionary : holiday's retruned from api        
  
    """  
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None
"""
Sample Text
"""