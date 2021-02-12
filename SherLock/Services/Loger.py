from Interfaces.ILogger import ILoger
import os
from contextlib import closing
from datetime import datetime


class Loger(ILoger):
    """  Class for loging exceptions and actions  
        
        Open methods:
        Logg

        Interfaces:
        ILogger
    """
   
    def __init__(self):
        """ Init Loger object """
        if(not os.path.exists(os.path.dirname(os.path.abspath(__file__)).replace("\\Services", "\\Logering"))):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)).replace("\\Services", "\\Logering"))
        self.__logFilePath = os.path.dirname(os.path.abspath(__file__)).replace("\\Services", "\\Logering/Log.txt")

    def Log(self, text):
        """ Loging the text in the log file
       
        Keywords arguments:
        text - text wchich write in file

        """
        with closing(open(self.__logFilePath, "a")) as file:
            file.write("\n" + str(datetime.now()) + ": " + text)


    __logFilePath = ""


