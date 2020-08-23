import socket
import _thread
from scripts.multiplayer.game import Game

server = "192.168.29.235"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(server, port)
except socket.error as e:
    str(e)

s.listen()
print("Waiting for connection")


def threaded_client(conn, game_id):
    pass


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    _thread.start_new_thread(threaded_client, (conn, 0))
