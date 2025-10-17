from rpc import RPCClient

server = RPCClient('127.0.0.1', 8080)

server.connect()

print(server.add(5, 6))
print(server.sub(5, 6))


server.disconnect()
