from Interfaces.IWriter import IWriter
from Interfaces.IObserver import IObserver
from datetime import datetime

class DataBaseWriter(IWriter, IObserver):

    def __init__(self, dataBaseConnection):
        self.__dataBaseConnection = dataBaseConnection


    def Write(self, data):
        with self.__dataBaseConnection.Connection.cursor() as cursor:
            query = "INSERT polls(destinationIp, port, date) VALUES('{0}', '{1}', '{2}');".format(data[0], data[2], datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            cursor.execute(query)
            self.__dataBaseConnection.Connection.commit()

    def Update(self, data):
        """ Updating some information when method is called """
        self.Write(data) 

    __dataBaseConnection = 0