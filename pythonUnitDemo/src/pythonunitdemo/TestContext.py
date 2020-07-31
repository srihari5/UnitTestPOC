import logging
import sys

dict_obj = {'fields': {'color': 'yellow', 'api_endpoint': '/results', 'host': 'app01', 'index':'hec'},
            'user': 'foobar', 'app': 'my demo', 'severity': 'low', 'error codes': [1, 23, 34, 456]}
 
class CustomAdapter(logging.LoggerAdapter):
    """
    This example adapter expects the passed in dict-like object to have a
    'connid' key, whose value in brackets is prepended to the log message.
    """
    def process(self, msg, kwargs):        
        return '[%s] %s' % (self.extra['first'], msg), kwargs
logger = logging.getLogger(__name__)
kwars ={'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel(logging.DEBUG)
adapter = CustomAdapter(logger,kwars)

logger.info('hai')
adapter.debug('hello')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-100:-3])
