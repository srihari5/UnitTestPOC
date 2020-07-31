import logging
from splunk_hec_handler import SplunkHecHandler
logger = logging.getLogger(__name__)
splunk_handler = SplunkHecHandler('splunk-dev.sumtotallab.host',
                   '434634f0-d60a-4592-9959-ba14b3bdccb5',
                    port=443,proto='https',
                    ssl_verify=False,
                    source="HEC_example",
                    index="HecTest",
                    sourcetype="_json")
logger.addHandler(splunk_handler)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')