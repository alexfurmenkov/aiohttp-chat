import aiohttp
from aiohttp import web


class WebSocket(web.View):

    async def get(self):
        websocket = web.WebSocketResponse()
        await websocket.prepare(self.request)

        async for msg in websocket:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == 'close':
                    await websocket.close()
                else:
                    await websocket.send_str(msg.data + '/answer')
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print('ws connection closed with exception %s' %
                      websocket.exception())

        print('websocket connection closed')

        return websocket
