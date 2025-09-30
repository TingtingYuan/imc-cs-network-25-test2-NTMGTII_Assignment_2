import pytest
import time

from rpc import RPCClient, RPCServer
from rpc_server import fibonacci

from multiprocessing import Process

@pytest.fixture
def setup_server():
    server = RPCServer()
    server.registerMethod(fibonacci)

    server_process = Process(target=server.run)
    server_process.start()

    time.sleep(1)

    server_address = '127.0.0.1'
    yield server_address

    server_process.terminate()
    server_process.join()


def test_fibonacci(setup_server):
    client = RPCClient(setup_server, 8080)
    client.connect()
    assert client.add(2, 8) == 10
    assert client.add(3, 9) == 12
    assert client.sub(6, 3) == 3
    client.disconnect()



    
