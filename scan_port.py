import socket

socket.setdefaulttimeout(1)
ip=raw_input("enter ip:")
for i in range (21,81):
    try:
        ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#        socket.setdefaulttimeout(1)
        a=ss.connect((ip,int(i)))
        if a==None:
            print ip,i,"  [open]"
#        else:
#            print ""
        ss.close()
    except:
        print i,"port close"
