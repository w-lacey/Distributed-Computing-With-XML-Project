import sys
from datetime import *
from xmlrpc.server import SimpleXMLRPCServer

#Setting the host and port values to console inputs
HOST = sys.argv[1]
PORT = sys.argv[2]

#Create server
server = SimpleXMLRPCServer((HOST, int(PORT)))

#Returns host name
def name():
    return HOST

#Returns a list of all available methods
def help():
    return ('All methods: name, time, add, sub, div, help')

#Returns the current time in 24 hour format
def time():
    today = datetime.today()
    currentTime = today.strftime("%H:%M:%S")
    return "The current time is: " + currentTime

#Returns the sum of the values passed in through console
def add(x, y):
    return x+y

#Returns the subtraction using the values entered in console
def sub(x, y):
    return x-y

#Returns the multiplication using the values entered in console
def mult(x, y):
    return x * y

#Returns the division using the values entered in console while checking the value entering and throwing an error if division by zero is attempted
def div(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        "You cannot divide by zero"


server.register_function(name)
server.register_function(help)
server.register_function(time)
server.register_function(add)
server.register_function(sub)
server.register_function(mult)
server.register_function(div)
server.serve_forever()