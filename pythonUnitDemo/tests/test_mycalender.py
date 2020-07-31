__author__ = "Srihari"
__copyright__ = "Srihari"
__license__ = "mit"

import pytest
from datetime import datetime
from unittest.mock import Mock
from unittest.mock import patch
from requests.exceptions import Timeout
from requests.exceptions import ConnectTimeout
from pythonunitdemo.mycalender import getholidays,isweekday,requests


@pytest.fixture 
def jsonholidaydata():  
    """
    Example for fixture
    """
    return { 
        '25/12' : 'Christmas',
        '01/01' : 'New Year'
        }
 
@patch('pythonunitdemo.mycalender.datetime')
def test_isweekday_withWeekday(mocked_datetime):
    wednesday = datetime(year=2020,month=6,day=17)
    mocked_datetime.today.return_value = wednesday
    assert isweekday()
    
def test_isweekday_withWweekend():
    with patch('pythonunitdemo.mycalender.datetime') as mocked_datetime:
        sunday = datetime(year=2020,month=6,day=14)
        mocked_datetime.today.return_value = sunday
        assert isweekday() == False

def test_getholidays_timeout():
    with patch('pythonunitdemo.mycalender.requests') as mocked_requests:
        mocked_requests.get.side_effect = Timeout
        with pytest.raises(Timeout):
            getholidays()
            assert mocked_requests.get.call_count > 0

@patch.object(requests,'get',side_effect=ConnectTimeout)
def test_getholidays_connecttimeout(mockConnectTimeoutrequest):
   # with patch('pythonunitdemo.mycalender.requests') as mocked_requests:
   with pytest.raises(ConnectTimeout):
    assert  getholidays() == None
   


@patch('pythonunitdemo.mycalender.requests.get')
def test_getholidays_status200(mocked_get,jsonholidaydata):
    mocked_get.return_value = Mock()
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value= jsonholidaydata
    assert jsonholidaydata == getholidays()

"""
Test case example with patch decorator for mock get method status_code 200 and retrun_value with jsonholidaydata

As we are not validating the return value this test may pass even the funtionality is broken 

This kind of tests will show good scrore in code coverage, but will not help in validating actaul code . We should be avoid this kind of tests.
"""
@patch('pythonunitdemo.mycalender.requests.get')
def test_getholidays_status200BadEx(mocked_get,jsonholidaydata):
    mocked_get.return_value = Mock()
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value= jsonholidaydata
    assert jsonholidaydata != None    

"""
Test case example with patch decorator for mock get method status_code 400 and retrun_value with jsonholidaydata

"""
@patch('pythonunitdemo.mycalender.requests.get')
def test_getholidays_status400(mocked_get):
    mocked_get.return_value = Mock()
    mocked_get.return_value.status_code = 400
    mocked_get.return_value.json.return_value=jsonholidaydata
    assert getholidays() == None

 

