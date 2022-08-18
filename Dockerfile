FROM python:3.10.6-alpine

# RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
# && apt update \

ENV MYSQL_HOST 192.168.1.60
ENV MYSQL_PORT 3306
ENV MYSQL_DATABASE test
ENV MYSQL_USERNAME test
ENV MYSQL_PASSWORD 123456

ENV REDIS_HOST 192.168.1.50
ENV REDIS_PORT 6379
ENV REDIS_DATABASE 1
ENV REDIS_PASSWORD Blqkn3Tj5gUDoiUK

ENV RABBITMQ_HOST 192.168.1.50
ENV RABBITMQ_PORT 5672
ENV RABBITMQ_USERNAME shr
ENV RABBITMQ_PASSWORD passWord

RUN pip install python-gsmmodem-new fastapi uvicorn sqlalchemy pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./app /app
COPY ./main.py /main.py

WORKDIR /

CMD ["python", "/main.py"]
