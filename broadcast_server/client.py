import asyncio
import websockets
import sys

async def listen_messages(websocket):
    async for message in websocket:
        print(f"\n[Broadcast] {message}")

async def send_messages(websocket):
    loop = asyncio.get_event_loop()
    while True:
        message = await loop.run_in_executor(None, sys.stdin.readline)
        if message.strip():
            await websocket.send(message.strip())

async def run_client(uri):
    try:
        async with websockets.connect(uri) as websocket:
            print(f"[Client] Connected to server {uri}")
            await asyncio.gather(
                listen_messages(websocket),
                send_messages(websocket,)
            )
    except Exception as e:
        print(f"[Client] Connection failed: {e}")

def start_client(host: str, port: int):
    uri = f"ws://{host}:{port}"
    asyncio.run(run_client(uri))