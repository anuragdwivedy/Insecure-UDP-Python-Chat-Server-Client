import socket, select, string, sys, getpass
 
#function to get prompt for clients with thier username
def prompt() :
    myvariable = getpass.getuser()
    sys.stdout.write(myvariable+':')
    sys.stdout.flush()
 
#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : program hostname port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. Send message'
    prompt()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #read incoming message from remote server
            if sock == s:
                data = s.recvfrom(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    sys.stdout.write(data[0])
                    prompt()
             
            #when user enteres a message send it to server
            else :
                msg = sys.stdin.readline()
             	s.sendto(msg, (host, port))
                prompt()
