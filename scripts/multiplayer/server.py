import pickle
import socket
import _thread
from scripts.multiplayer.game import Game

server = "192.168.29.144"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen()
print("Waiting for connection")

connected = set()
games = {}
id_count = 0


def threaded_client(_conn, player, _game_id):
    global id_count
    _conn.send(str.encode(str(player)))
    while True:
        try:
            data = pickle.loads(_conn.recv(4096))
            if _game_id in games:
                game = games[_game_id]

                if not data:
                    break
                else:
                    reply = game
                    _conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Connection Lost")

    try:
        del games[_game_id]
        print("Closing Game", _game_id)
    except:
        pass
    id_count -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    id_count += 1
    p = 0
    game_id = (id_count - 1) // 2

    if id_count % 2 == 1:
        games[game_id] = Game()
    else:
        games[game_id].ready = True
        p = 1

    _thread.start_new_thread(threaded_client, (conn, p, game_id))
