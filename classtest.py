import json
from json import JSONEncoder
class COLog:
    """[Summary]
    Cloud Operations custom log 
    :property [current_timestamp]: [current_timestamp of the orginating server], defaults to [none] 
    :property [major_workflow_class]: [major workflow], defaults to [none] 
    :property [minor_workflow_method]: [minor workflow], defaults to [none]
    :property [launch_timestamp]: [launch_timestamp], defaults to [none] 
    :property [role]: [UDA role], defaults to [none]
    :property [step]: [Current step in execution], defaults to [none]
    :property [process_user]: [servive account or user executing this process], defaults to [none]
    :property [requester]: [user triggered this action], defaults to [none]
    :property [site_url]: [site_url], defaults to [none]
    :property [customer_name]: [customer name], defaults to [none]
    :property [site_key]: [site key (Tennat key)], defaults to [none]
    :property [environment]: [Tier (Prod/Stage/Test/Dev)], defaults to [none]
    :property [source_system]: [source system orginating this execution], defaults to [none]
    :property [process_service]: [ windows/linux service name], defaults to [none] 
    :property [global_transaction_id]: [Guid which will be used to tie events together from various processes], defaults to [none]
    :property [local_transaction_id]: [Guid which will be used to tie events together with in this process], defaults to [none] 
    :property [destination_system]: [Target server or device in case of remote execution], defaults to [none] 
    :property [message]: [log message], defaults to [none]        
    :property [severity]: [log severity], defaults to [none]
    :property [exception_trace]: [detailed stack trace in case of expection], defaults to [none]   
    """   
    @property
    def current_timestamp(self):      
        return self.__current_timestamp
    @current_timestamp.setter
    def current_timestamp(self,val):
        self.__current_timestamp = val
    
    @property
    def major_workflow_class(self):      
        return self.__major_workflow_class   
    @major_workflow_class.setter
    def major_workflow_class(self,val):
        self.__major_workflow_class = val

    @property
    def minor_workflow_method(self):
        return self.__minor_workflow_method
    @minor_workflow_method.setter
    def minor_workflow_method(self,val):
        self.minor_workflow_method = val

    @property
    def launch_timestamp(self):      
        return self.__launch_timestamp 
    @launch_timestamp.setter
    def launch_timestamp(self,val):
        self.__launch_timestamp = val

    @property
    def role(self):      
        return self.__role 
    @role.setter
    def role(self,val):
        self.__role = val

    @property
    def step(self):      
        return self.__step 
    @step.setter
    def step(self,val):
        self.__step = val

    @property
    def process_user(self):      
        return self.__process_user 
    @process_user.setter
    def process_user(self,val):
        self.__process_user = val

class COLogEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

         
colog=COLog()

colog.current_timestamp=10
colog.launch_timestamp=120
colog.major_workflow_class=130
colog.process_user=50

cologJSONData = json.dumps(colog, indent=4, cls=COLogEncoder)
print(cologJSONData)
d=json.loads(cologJSONData)
print(d)
dd=COLogEncoder()
