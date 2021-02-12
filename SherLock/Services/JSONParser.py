from Interfaces.IParser import IParser
import json

class JSONParser(IParser):
    

    def Pars(self, data):
        return json.dumps(data)

    def Unpars(self, data):
        return json.loads(data)


