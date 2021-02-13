from Interfaces.IConnection import IConnection
from Exceptions.FileNotExistsException import FileNotExistsException
import pymysql
import os
import json

class DataBaseConnection(IConnection):
    
    def __init__(self, fileReader):
        """  Creating connection """
        self.__fileReader = fileReader
        if(os.path.exists(self.__filePath)):
            tmp = json.loads(self.__fileReader.Read(self.__filePath))
            self.__dataBaseName = tmp['DataBaseName']
            self.__dataBaseUser = tmp['DataBaseUser']
            self.__dataBasePassword = tmp['DataBasePassword']
            self.__dataBaseHost = tmp['DataBaseHost']
            self.__dataBasePort = tmp['DataBasePort']
        else:
            raise FileNotExistsException(self.__fileErrorString)
        self.__connection = pymysql.connect(host=self.__dataBaseHost, database=self.__dataBaseName, user=self.__dataBaseUser, password=self.__dataBasePassword, port=int(self.__dataBasePort))
        self.__connection.autocommit_mode = True

    @property
    def Connection(self):
        """ Geting connection """
        return self.__connection

    def __del__(self):
        """ Close connection """
        self.__connection.close()

    __dataBaseName = ''
    __dataBaseUser = ''
    __dataBasePassword = ''
    __dataBaseHost = ''
    __dataBasePort = ''
    __filePath = os.path.dirname(os.path.abspath(__file__)) + "/Connections.json"
    __fileErrorString = "Отсутсвует файл в дирректории ../Connections/Connections.json"
    __fileReader = 0
    __connection = 0


