import asyncio
import websockets
import logging

log_file_path = "/temp/ws-server.log"

async def echo(websocket, path):
    # print("websocket all data is:", vars(websocket))
    logger = logging.getLogger("websocket-app")
    # logger.info("websocket all data is: {}".format(vars(websocket)) )
    logger.info("Client connected from {}".format(websocket.remote_address))
    print("Client connected from {}".format(websocket.remote_address))  # Added print statement
    async for message in websocket:
        logger.info("Received message from client {}: {}".format(websocket.remote_address, message))
        print("Received message from client {}: {}".format(websocket.remote_address, message))  # Added print statement
        # sent_msg = input("Enter your message: ")
        # await websocket.send(sent_msg)
        await websocket.send(message + " from server")
        logger.info("Sent message back to client {}: {}".format(websocket.remote_address, message))
        # print("Sent message back to client {}: {}".format(websocket.remote_address, message))  # Added print statement

async def main():
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    server = await websockets.serve(echo, "0.0.0.0", 8819)
    logging.info("Server started.")
    print("Server started.")  # Added print statement
    await server.wait_closed()

asyncio.run(main())
