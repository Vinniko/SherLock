from Interfaces.IListener import IListener
from Interfaces.IObservable import IObservable
import socket
import threading

class SocketListener(IListener, IObservable):

    def __init__(self, configModel):
        self.__configModel = configModel


    def Listen(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.__host, int(port)))
            while(True):
                sock.listen()
                conn, addr = sock.accept()
                addr += (port,)
                with self.__lock:
                    flag = True
                    for ip in self.__configModel.RemovedIps:
                        if(ip == addr[0]):
                            flag = False
                    if(flag):
                        self.NotifyObservers(addr)

    

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
    __observers = list()
    __lock = threading.Lock()


