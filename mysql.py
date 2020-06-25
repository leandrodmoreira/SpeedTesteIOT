
import speedtest
from datetime import datetime
import time
import pymysql.cursors

now = datetime.now()
host = 1
speed = speedtest.Speedtest()
speed.get_best_server()

download = repr(round(speed.download() / 1000 / 1000, 1))
upload = repr(round(speed.upload () / 1000 / 1000, 1))

# Connect to the database
connection = pymysql.connect(host='192.168.0.38',
                             user='root',
                             password='Wall@1979',
                             db='homeiot',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `iot_speedtest` (`timestamp`, `host` , `download` , `upload`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (now, host, download, upload))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

finally:
    connection.close()