from abc import ABCMeta, abstractmethod

class IListener(object):
    
    @abstractmethod
    def Listen(self, port):
        pass


