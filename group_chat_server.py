import threading
import socket 

s = socket.socket( socket.AF_INET , socket.SOCK_STREAM) 

s.bind(('localhost' , 9999) ) 

s.listen() 

clients = []
nicknames = [] 

def broadcast(msg):
    for c in  clients:
        c.send(msg)


# Handling Messages From Clients
def handle(client):
    while True: 
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = s.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

        

receive()

        
import socket 
import threading 

s = socket.socket(socket.AF_INET  , socket.SOCK_STREAM) 

s.bind(('localhost' , 9999)) 

s.listen() 

#  create list for clients and nickname 
clients = []
nicknames = [] 

def broadcast(msg):
    for c in clients:
        c.send(msg)
        

def handle(client ):
    while True :
        try:
            msg = client.recv(1024) 
            broadcast(msg)
        except:
            idx = clients.index(client)
            clients.remove(client)
            client.close()
            
            nickname  = nicknames[idx]
            broadcast('{} left the chat' .format(nickname).encode('ascii') )
            nicknames.remove(nickname)
            

def recive():
    
    while True:
        
        c , add = s.accept() 
        print('connected to ' , add )
        
        #get the nickname  
        c.send('Nick'.encode('ascii')) 
        nickname = c.recv(1024).decode('ascii')
       
        nickname.append(nickname)
        clients.append(c) 
        
        #broadcast nickname 
        broadcast('{} joined the chat '.format(nickname).encode('ascii'))  
        print('nickname is ', nickname)
        
        #thread for each client 
        thread = threading.Thread(target=handle, args = c )
        thread.start() 
        
        
recive() 
        
        
        