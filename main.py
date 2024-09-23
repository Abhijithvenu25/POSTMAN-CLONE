import uvicorn,requests,httpx
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5501",
    "http://localhost:5501",
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows these origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


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

    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, headers=headers, json=body)
    
    return response.json()