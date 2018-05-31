import socket

class Robot:
    state = ''
    def __init__(self, host='35.187.230.213', port='50007'):
        self.host=host
        self.port=port


    def calNextMove(self, instate):
        if(self.state == instate):
            pass
        else:
            self.socserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socserv.connect((self.host, int(self.port)))

            sentstring = self.serializeState(instate)

            self.socserv.sendall(bytes(sentstring,encoding='utf-8'));

            nextmove = self.socserv.recv(2048)
            print('Recv', repr(nextmove))

    def serializeState(self, instate):
        ## protocol = "boardsize, board[0][0] board[0][1] board[0]..."
        serialized = ''
        for i in range(len(instate)):
            for j in range(len(instate)):
                serialized = serialized+" "+str(instate[i][j])

        serialized = str(len(instate))+","+serialized

        return serialized



