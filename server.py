import socket
import pickle
from game import Game
from _thread import *

server = "10.11.250.207"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn, playerId ,p, gameId):

    conn.send(str.encode(str(p))) # Send PlayerId 0 or 1

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode() # Client will send paddle x position and ball position

            if gameId in games:
                game = games[gameId] # choose the correct game

                if not data:
                    break
                else:
                    if p == 0 :



                    else :


                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    conn.close()


players = []
IdCount = 0
gameId = 1
games = {

}
while True :
    conn, addr = s.accept()
    print("Connected to:", addr)
    IdCount += 1
    p = 0
    currentGameId = gameId
    players.append(IdCount)
    if len(players) % 2 == 1 :
        games[gameId] = Game(gameId)
        games[gameId].player1 = IdCount
        p = 1


    else :
        games[gameId] = Game(gameId)
        p = 2
        gameId += 1

    start_new_thread(threaded_client, (conn, IdCount , p , currentGameId))


















    start_new_thread(threaded_client, (conn, IdCount ,total_players % 2, gameId))











