import uvicorn,requests
from fastapi import FastAPI,Request

app = FastAPI()

@app.get('/')
async def default():
    return {'Hi'}

@app.get('/api/about')
async def About():
    return {'About':'This a simple Postman Clone created by Abhijith Venu ,which can handle the CRED operations'}


@app.post('/request/')
async def sended_requests(request:Request):
    data = await request.json()
    print(data)
    method = data['method']
    url = data['url']
    headers = data.get('headers',{})
    body = data.get('body',{})
    token = data.get('token')
    return 0