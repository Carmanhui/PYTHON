import time
import _thread
import serial
import threading


class myserial:
    recdata = ""

    def __init__(self, port, baudrate, timeout):
        self.port = serial.Serial(port, baudrate)

        if (self.port.is_open):
            print("打开", self.port.portstr)
        else:
            print("打开端口失败")

    def receivemsg(self):
        # print("rec")
        while True:
            size = self.port.in_waiting

            if size:
                self.recdata = self.port.read_all().decode('utf-8')
                if self.recdata != "":
                    print("rec at", time.ctime(), '\n', str(self.recdata))
                    self.recdata = ""

    def sendmsg(self):
        while True:
            senddata = input("plz input:")
            senddata = senddata.encode('utf-8')
            self.port.write(senddata)


if __name__ == '__main__':

    print("starting")
    # 实例化
    mport = myserial('COM2', baudrate=9600, timeout=1)
    # 线程开启
    _thread.start_new_thread(mport.sendmsg, ())
    # _thread.start_new_thread(mport.receivemsg,())
    print("here")
    while True:
        time.sleep(1)
        mport.receivemsg()
