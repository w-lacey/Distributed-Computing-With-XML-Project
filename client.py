import sys
import xmlrpc.client

#Setting console for the host/port addresses and for the two values for performing operations on the server.
HOST = sys.argv[1]
PORT = sys.argv[2]
x = int(sys.argv[3])
y = int(sys.argv[4])

#Creating the URI with the previously entered host and port
URI = 'http://' + HOST + ':' + PORT

#Creating instance of server using URI
s = xmlrpc.client.ServerProxy(URI)

#Calling server methods
print("Name: " + s.name())
print(s.help())
print("Addition: " + str(s.add(x, y)))
print("Subtraction: " + str(s.sub(x, y)))
print("Multiplication: " + str(s.mult(x, y)))
print("Division: " + str(s.div(x, y)))
print(s.time())