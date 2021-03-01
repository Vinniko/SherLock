# SherLock
---------------------------------------------------------------------------------------------
1. Подготовка к установке скрипта
---------------------------------------------------------------------------------------------
Необходимые пакеты для работы скрипта:
>python3 (apt-get install python3)

>pymysql (pip install pymysql)

Файл Connections/Connections.json содержит в себе реквизиты для подключения скрипта к базе 
данных(перед началом работы следует заменить тестовые данные на реальные, т.е. имя хостинга, 
имя самой базы, пользователь и пароль. Порт не меняется!)

Пример:
<br>{<br>"DataBaseName": "имя_базы_данных",
  <br>"DataBaseUser": "имя_пользователя",
  <br>"DataBasePassword": "пароль",
  <br>"DataBaseHost": "имя_хоста",
  <br>"DataBasePort": "3306"
<br>}

Файл Configs/Configs.json содержит в себе настройки, которые учитываются при непосредственной 
работе скрипта:
-игнорируемые ip адреса (обращение на эти ip адреса не будут записываться в базу)
-прослушиваемые порты (обращение на эти порты будут записываться в базу)
Редактирование данного файла также следует осуществлять перед запуском скрипта.
Количество адресов и портов не ограничено.

Пример:<br>
{<br>
  "removedIps": ["ip-address1","ip-address2",...,"ip-address..."],
  <br>"usingPorts": [ "port1", "port2",...,"port..."]
<br>}

---------------------------------------------------------------------------------------------
2. Установка скрипта
---------------------------------------------------------------------------------------------
Работу скрипта можно проверить запустив файл SherLock.py, используя следующую команду:
> python3 SherLock.py

(Однако, в таком случае программа будет работать только на время текущей сессии)

По-этому для удобства запишем его в cron:
>crontab -e

После, в открывшемся файле вводим необходимые данные о частоте запуска программы.
 
Параметр:	Допустимый интервал<br>
минуты:	        0-59<br>
часы:	          0-23<br>
день месяца:    1-31<br>
месяц:          1-12<br>
день недели:    0-7 (0-Вс,1-Пн,2-Вт,3-Ср,4-Чт,5-Пт,6-Сб,7-Вс)

Поле может быть задано явно или шаблоном:<br>
1)* — любая цифра;<br>
2)целое число;<br>
3)целые числа через запятую — задание дискретного множества значений, например 1,2,5;<br>
4)два целых числа, разделенные дефисом, соответствующие диапазону значений, например 3-6.

Пример готовой строки сценария cron:
 
Выполнять задание в 18 часов 7 минут 13 мая если это пятница
>7 18 13 5 5 .../SherLock/SherLock/SherLock.py

Выполнять задание раз в час в 0 минут
>0 */1 * * * .../SherLock/SherLock/SherLock.py

Выполнять задание каждые семь часов в 0 минут
>0 */7 * * * .../SherLock/SherLock/SherLock.py

Выполнять задание по воскресеньям в 10 час 30 минут
>30 10 * * 0 .../SherLock/SherLock/SherLock.py

P.S. <br>1) вместо {...} вводится полный путь к папке
     <br>2) папка скрипта может находиться в любом месте, главное, чтобы все файлы, 
        нахощиеся в папке никуда не перемещались и не удалялись.
