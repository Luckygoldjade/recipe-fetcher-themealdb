#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#
import time
import zmq
import json
context = zmq.Context()
print(f"Current libzmq version is {zmq.zmq_version()}")
print(f"Current  pyzmq version is {zmq.__version__}")


#  Socket to talk to server
def receive_message():
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        #  Wait for next request from client
        message = socket.recv()
        print(f"Received request: {message}")
        print(type(message))
        message_str = message.decode('utf-8')
        print(f"Received request: {message_str}")
        print(type(message_str))
        message_json = json.loads(message_str)
        print(f"Received request: {message_json}")

        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        socket.send(b"Received data")


if __name__ == "__main__":
    receive_message()
    print("Done")
