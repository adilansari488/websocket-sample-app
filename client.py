import asyncio
import websockets

async def hello():
    ws_URL = "ws://localhost:8819"
    # msg_to_send = "Hello, WebSocket!"
    async with websockets.connect(ws_URL) as websocket:
        while True:
            try:
                msg_to_send = input("Enter your message: ")
                await websocket.send(msg_to_send)
                response = await websocket.recv()
                print(f"Received: {response}")
            except websockets.exceptions.ConnectionClosedError:
                print("Connection closed. Reconnecting...")
            await asyncio.sleep(1)
if __name__ == "__main__":
    try:
        asyncio.run(hello())
    except KeyboardInterrupt:
        print("keyboard interrupt. Exiting...")

