import os

from fastapi import FastAPI, Request, Response

app = FastAPI()


async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    if 'added' not in request.scope:
        response.headers["x-my-header"] = 'keke'
        request.scope['added'] = 1
    return response

@app.get('/')
async def root():
    return 'OK'

for i in range(int(os.getenv('M', 1))):
    app.middleware("http")(add_custom_header)
