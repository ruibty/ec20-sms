# 针对ec20的一个收发短信的模块

https://github.com/ruibty/ec20-sms

https://hub.docker.com/repository/docker/ruibty/ec20-sms

- python3

- 需要的依赖

```
pip install sqlalchemy pymysql python-gsmmodem-new fastapi uvicorn -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Linux下试一下

```
docker run --privileged=true --rm \
    -v /dev/ttyUSB2:/dev/ttyUSB2 \
    -p 8085:8085 \
    -e MYSQL_HOST=192.168.1.60 \
    -e MYSQL_DATABASE=test \
    -e MYSQL_USERNAME=test \
    -e MYSQL_PASSWORD=123456 \
    ruibty/ec20-sms:1.0.20220818
```

## 一共两个接口

### 发送短信

`post`方式

```
http://0.0.0.0:8085/sms/
```

| 参数名     | 传参方式 | 是否必须 | 说明       |
|---------|------|------|----------|
| tel_num | body | 是    | 收信人的电话号码 |
| content | body | 是    | 短信内容     |

### 查看短信

`get`方式

```
http://0.0.0.0:8085/sms/by-type/{type}}?page=1&row=50
```

| 参数名  | 传参方式   | 是否必须 | 说明            |
|------|--------|------|---------------|
| type | url    | 是    | 1 代表发出 2 代表收到 |
| page | params | 是    | 页码            |
| row  | params | 否    | 数据量           |