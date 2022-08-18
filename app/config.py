import os
import re

db = {
    'mysql_host': 'localhost',
    'mysql_port': '3306',
    'mysql_database': 'test',
    'mysql_username': 'test',
    'mysql_password': '123456'
}

sms_used = {
    'total': 300,
    'used': 0,
    'surplus': 300
}


def init_db():
    # for key in os.environ:
    # print(key, os.environ[key])
    db['mysql_host'] = os.getenv('MYSQL_HOST', '192.168.1.60')
    db['mysql_port'] = os.getenv('MYSQL_PORT', '3306')
    db['mysql_database'] = os.getenv('MYSQL_DATABASE', 'test')
    db['mysql_username'] = os.getenv('MYSQL_USERNAME', 'test')
    db['mysql_password'] = os.getenv('MYSQL_PASSWORD', '123456')


def refresh_sms_used(sms):
    if sms.number == '10010' and '短信' in sms.text:
        # print(sms.text)
        # 共300条, 已用15条
        key_word_str_list = re.findall(r"共[0-9]\d*条, 已用[0-9]\d*条", sms.text)
        # print(key_word_str_list)
        # ['共300条, 已用15条']
        if len(key_word_str_list) > 0:
            print(sms.time)
            # 2022-07-22 11:33:12+08:00
            # print(type(sms.time))
            # <class 'datetime.datetime'>
            # print(sms.time.time())
            # 11:56:56

            key_word_str = re.findall(r"[0-9]\d*", key_word_str_list[0])
            print(key_word_str)
            # ['300', '15']
            if len(key_word_str) == 2:
                total, used = key_word_str
                surplus = int(total) - int(used)
                sms_used['total'] = total
                sms_used['used'] = used
                sms_used['surplus'] = surplus
