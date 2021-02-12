from Interfaces.IWriter import IWriter
from Interfaces.IObserver import IObserver
from datetime import datetime

class DataBaseWriter(IWriter, IObserver):

    def __init__(self, dataBaseConnection):
        self.__dataBaseConnection = dataBaseConnection


    def Write(self, data):
        with self.__dataBaseConnection.connection.cursor() as cursor:
            qyery = "INSERT polls(destinationIp, port, date) VALUES({0}, {1}, {2});".format(data[0], data[1], datetime.now)
            cursor.execute(query)

    def Update(self, data):
        """ Updating some information when method is called """
        self.Write(data) 

    __dataBaseConnection = 0