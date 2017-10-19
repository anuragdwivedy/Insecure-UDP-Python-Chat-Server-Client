# Insecure-UDP-Python-Chat-Server-Client
Simple python client-server broadcast chat application using UDP

# Usage of Server:
	python chatServer.py <portnumber>
# Usage of Clients:
	python chatClient.py <server ip> <server portnumber>

Server excepts all messages from clients and broadcast to all registred active clients
For a client to be registered as active, the client must send 'greeting' message.  
