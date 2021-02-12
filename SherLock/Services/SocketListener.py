from Interfaces.IListener import IListener
from Interfaces.IObservable import IObservable
import socket

class SocketListener(IListener, IObservable):

    def __init__(self, configModel):
        __configModel = configModel


    def Listen(self, port):
        while(true):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind((self.__host, port))
                sock.listen()
                conn, addr = sock.accept()
                for ip in __configModel.RemovedIps:
                    if(ip != addr[0]):
                        NotifyObservers(addr)

    

    def NotifyObservers(self, data):
        """ Notifying observers """
        for observer in self.__observers:
            observer.Update(data)

    def RegisterObserver(self, observer):
        """ Registration of the new observer
       
        Keywords arguments:
        observer - object, wchich realization IObserver

        """
        self.__observers.append(observer)

    def RemoveObserver(self, observer):
        """ Removing of the certain observer
       
        Keywords arguments:
        observer - observer, wcich will be removed 

        """
        self.__observers.remove(observer)

    __host = "127.0.0.1"
    __configModel = 0


