import uvicorn
from fastapi import FastAPI

from app.controller import sms, port
from app.modem import init_modem

app = FastAPI()  # 创建 api 对象
app.include_router(port, prefix='/port')
app.include_router(sms)

if __name__ == '__main__':
    init_modem()
    uvicorn.run(app, host="0.0.0.0", port=8085)
