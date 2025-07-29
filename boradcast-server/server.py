import asyncio
import websockets
from typing import Set

connected_clients: Set[websockets.WebSocketServerProtocol] = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(message, websocket)
    except websocket.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def broadcast(message: str, sender):
    for client in connected_clients:
        if client != sender:
            try:
                await client.send(message)
            except Exception:
                pass

def start_server(host: str, port: int):
    print(f'[Server] Statring on {host}:{port}')
    loop = asyncio.get_event_loop()
    server = websockets.serve(handler, host, port)
    loop.run_until_complete(server)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("\n[Server] Shutting down")


