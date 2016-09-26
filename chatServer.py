import socket, select, string, sys


if __name__ == "__main__":

	if(len(sys.argv) < 2) :
		print 'Usage : program port'
		sys.exit()
	     
	port = int(sys.argv[1]) #Read input from Command line argument

	CLIENT_LIST = [] #List to maintain connected clients
	
	# Create and Bind the UDP socket
	try:
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server_address = ('127.0.0.1', port)
		server_socket.bind(server_address)
		print 'Server Initialized on %s port %s' % server_address

	except:
		print 'Error in creating/binding socket'
		sys.exit()

	while True:
	    
	   try:
	   	#Recieve data and maintain client list 
		data, address = server_socket.recvfrom(4096)
		if 'greeting' in str(data):
			#register the client as active for broadacst of further message
			if address not in CLIENT_LIST:
				CLIENT_LIST.append(address)
			print "<" + str(address) + "> " + str(data)
		else:
 			#print any the message from client on server 
			broadcast_message = "<" + str(address) + "> " + str(data)
			print broadcast_message
		
			#broadcast message to all active clients . 
			for client in CLIENT_LIST:
				server_socket.sendto(broadcast_message, client)		
	   except:
		
		pass	    
		
	server_socket.close()
