import speedtest
from datetime import datetime
import time
import csv

speed = speedtest.Speedtest()
speed.get_best_server()


while True:

    now = datetime.now()

    file = open('Log_SpeedTest.csv','a')

    reader = "Timestamp, Download(Mbs), Upload(Mbps) \n"

    download = repr(round(speed.download() / 1000 / 1000, 1))
    upload = repr(round(speed.upload () / 1000 / 1000, 1))

    textoBruto = now.strftime('%Y-%m-%d %H:%M') + ';' + download + ';' + upload + "\n"

    texto = textoBruto.replace(".",",")

    #file.write(reader)
    file.write(texto)

    file.close()

    print(texto)

    time.sleep(3600)

   