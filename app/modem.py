import re
import sys
import time

from gsmmodem import GsmModem
from gsmmodem.modem import SentSms

from .config import refresh_sms_used
from .db import SessionLocal
from .db import Sms

"""
初始化 ec20 
"""
def init_modem():
    print("初始化SMS模块")
    modem.smsTextMode = False
    modem.connect(PIN)
    print("等待网络覆盖...")
    modem.waitForNetworkCoverage(10)
    print("Waiting for SMS message...")
    # print(modem.__dict__)
    print(modem.networkName)


def handle_sms(sms):
    # print(sms.__dict__)
    message = u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\nSmsc:{3}\n'.format(sms.number,
                                                                                                    sms.time, sms.text,
                                                                                                    sms.smsc)
    print(message)
    timestamp = int(sms.time.timestamp())
    #
    db_sms = Sms()
    db_sms.type = 2
    db_sms.timestamp = timestamp
    db_sms.smsc = sms.smsc
    db_sms.number, db_sms.text, = sms.number, sms.text
    #
    db_session = SessionLocal()
    db_session.add(db_sms)
    db_session.commit()
    db_session.refresh(db_sms)
    # 刷新短信使用情况
    refresh_sms_used(sms)

# https://www.jianshu.com/p/ca0d29b6e127
def send_sms(destination=str, text=str):
    if destination is None or len(destination) == 0:
        print('Error: Please change the tel_num variable\'s value before running this example.')
        sys.exit(1)

    response = modem.sendSms(destination, text)
    print(response.__dict__)
    print(type(response))
    if type(response) == SentSms:
        print('SMS Delivered.')
        db_sms = Sms()
        db_sms.type = 1
        # db_sms.hash_pwd = hashlib.new('md5', user.pwd.encode()).hexdigest()
        db_sms.timestamp = int(time.time())
        db_sms.smsc = ''
        db_sms.number, db_sms.text, = destination, text

        db_session = SessionLocal()
        db_session.add(db_sms)
        db_session.commit()
        db_session.refresh(db_sms)
        db_session.close()
        return db_sms
    else:
        print('SMS Could not be sent')


PORT = '/dev/ttyUSB2'
BAUDRATE = 115200
PIN = None
modem = GsmModem(PORT, BAUDRATE, smsReceivedCallbackFunc=handle_sms)
