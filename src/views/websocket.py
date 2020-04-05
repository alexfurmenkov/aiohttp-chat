from aiohttp import web, WSMsgType


class WebSocket(web.View):
    clients = []

    @staticmethod
    async def websocket_handler(request):
        print('Websocket connection starting')
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        print('Websocket connection ready')
        WebSocket.clients.append(ws)

        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                print(f'Client message: {msg.data}')
                if msg.data == 'close':
                    await ws.close()
                else:
                    for client in WebSocket.clients:
                        await client.send_str(msg.data)

        print('Websocket connection closed')
        return ws
