from aiohttp import web, WSMsgType
from src.models.message import Message
import datetime


class WebSocket(web.View):
    clients = []

    @staticmethod
    async def broadcast(message):
        for client in WebSocket.clients:
            await client.send_json(message)

    @staticmethod
    async def websocket_handler(request):
        print('Websocket connection starting')
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        print('Websocket connection ready')
        WebSocket.clients.append(ws)
        await WebSocket.broadcast({'type': 'service',
                                   'message': f'{request.user.login} joined',
                                   'time': f'{datetime.datetime.now().hour}:'
                                           f'{datetime.datetime.now().minute}'})

        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                print(f'Client message: {msg.data}')
                if msg.data == 'close':
                    await ws.close()
                else:
                    message = Message(author_id=request.user, message=msg.data, created_at=datetime.datetime.now())
                    message.save()
                    returned_data = dict(
                        type='message',
                        user_login=request.user.login,
                        message=msg.data,
                        time=f'{datetime.datetime.now().year}-{datetime.datetime.now().hour}-'
                             f'{datetime.datetime.now().day} at {datetime.datetime.now().hour}'
                             f':{datetime.datetime.now().minute}'
                    )
                    await WebSocket.broadcast(returned_data)

        print('Websocket connection closed')
        return ws
