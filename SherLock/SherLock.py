from Services.Guardian import Guardian
from Services.Loger import Loger
from Services.JSONParser import JSONParser
from Services.FileReader import FileReader
from Services.DataBaseWriter import DataBaseWriter
from Services.SocketListener import SocketListener
from Connections.DataBaseConnection import DataBaseConnection
from Models.ConfigModel import ConfigModel
import threading


loger = Loger()
guardian = Guardian(loger)
fileReader = guardian.Secure(FileReader)
jsonParser = guardian.Secure(JSONParser)
dataBaseConnection = guardian.Secure(DataBaseConnection, fileReader)
configModel = guardian.Secure(ConfigModel, fileReader)
dataBaseWriter = guardian.Secure(DataBaseWriter, dataBaseConnection)
socketListener = guardian.Secure(SocketListener, configModel)
guardian.Secure(socketListener.RegisterObserver, dataBaseWriter)
threadings = list()

for port in configModel.UsingPorts:
    threadings.append(threading.Thread(target=socketListener.Listen, args=(port,)))
for thread in threadings:
    thread.start()
    thread.join()