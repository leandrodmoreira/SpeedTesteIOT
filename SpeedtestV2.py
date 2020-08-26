
import speedtest
from datetime import datetime
import time
import csv
import pymysql.cursors

speed = speedtest.Speedtest()
speed.get_best_server()


while True:

    #Criação das variáveis
    now = datetime.now()

    file = open('Log_SpeedTest.csv','a')

    timestamp =  now.strftime('%Y-%m-%d %H:%M')
    print("Date/Time:")
    print(timestamp)

    host = 1
    print("Host:")
    print(host)

    download = repr(round(speed.download() / 1000 / 1000, 1))
    upload = repr(round(speed.upload () / 1000 / 1000, 1))

    downloadComma = download.replace(".",",")
    print("Download:")
    print(downloadComma)
    uploadComma = upload.replace(".",",")
    print("Upload:")
    print(uploadComma)

    #Gravando dados no banco de dados

    # Connect to the database
    connection = pymysql.connect(host='192.168.0.38',
                             user='root',
                             password='Wall@1979',
                             db='homeiot',
                             cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `iot_speedtest` (`timestamp`, `host` , `download` , `upload`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (now, host, downloadComma, uploadComma))

        connection.commit()

    finally:
        connection.close()

    #Gravando dados no arquivo de log
    reader = "Timestamp, Download(Mbs), Upload(Mbps) \n"

    textoBruto = now.strftime('%Y-%m-%d %H:%M') + ';' + download + ';' + upload + "\n"

    texto = textoBruto.replace(".",",")

    #file.write(reader)
    file.write(texto)

    file.close()

    print("Valor armazenado no banco de dados e gravado no arquivo:")
    print(texto)

    time.sleep(3600)

   