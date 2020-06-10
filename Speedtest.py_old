import speedtest
from datetime import datetime
import time

speedtester = speedtest.Speedtest()
speedtester.get_best_server()


while True:

    now = datetime.now()

    file = open('file.csv','a')

    #reader = "Timestamp, Download(Mbs), Upload(Mbps) \n"

    download = repr(round(speedtester.download() / 1000 / 1000, 1))
    upload = repr(round(speedtester.upload () / 1000 / 1000, 1))

    texto = now.strftime('%Y-%m-%d %H:%M') + ' , ' + download + ' , ' + upload + "\n"

    #file.write(reader)
    file.write(texto)

    file.close()

    print(texto)

    time.sleep(1800)

   