Usage of Server:
	python chatServer.py <portnumber>
usage of Clients:
	python chatClient.py <server ip> <server portnumber>

Server excepts all messages from clients and broadcast to all registred active clients

For a client to be registered as active, the client must send 'greeting' message.  
