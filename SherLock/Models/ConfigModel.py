from Interfaces.IModel import IModel
from Exceptions.FileNotExistsException import FileNotExistsException
import os
import json

class ConfigModel(IModel):
    
    def __init__(self, fileReader):
        self.__fileReader = fileReader
        if(os.path.exists(self.__filePath)):
            tmp = json.loads(self.__fileReader.Read(self.__filePath))
            self.__removedIps = tmp['removedIps']
            self.__usingPorts = tmp['usingPorts']
        else:
            raise FileNotExistsException(self.__fileErrorString)

    @property
    def RemovedIps(self):
        return self.__removedIps

    @RemovedIps.setter
    def RemovedIps(self, data):
        self.__removedIps = data

    @property
    def UsingPorts(self):
        return self.__usingPorts

    @UsingPorts.setter
    def UsingPorts(self, data):
        self.__usingPorts = data


    __removedIps = list()
    __usingPorts = list()
    __fileReader = 0


