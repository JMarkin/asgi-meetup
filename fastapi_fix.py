import os

from fastapi import FastAPI, Request, Response
from starlette.types import ASGIApp, Message, Receive, Scope, Send

app = FastAPI()

class CustomHeaderMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):

        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        async def send_wrapper(message: Message):
            if message['type'] == 'http.response.start' and not 'added' in message:
                message['headers'].append((b'x-my-header', b'keke'))
                message['added'] = 1
            return await send(message)

        await self.app(scope, receive, send_wrapper)

@app.get('/')
async def root():
    return 'OK'

for i in range(int(os.getenv('M', 1))):
    app.add_middleware(CustomHeaderMiddleware)
