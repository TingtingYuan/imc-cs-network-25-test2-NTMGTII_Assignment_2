from rpc import RPCServer



def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid input")
    if n in (0, 1):
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def checksum(byte_array):
    if not isinstance(byte_array, (list, bytes, bytearray)):
        raise ValueError("Invalid input type")
    return sum(byte_array) % 256

if __name__ == "__main__":
    server = RPCServer()
    server.registerMethod(add)
    server.registerMethod(sub)
    server.registerMethod(fibonacci)
    server.registerMethod(checksum)
    print("RPC server starting...")
    server.run()