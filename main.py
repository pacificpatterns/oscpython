print('hello')
import abletonKeyFunctions as akf
import blockingserver
from pythonosc.osc_server import BlockingOSCUDPServer
from dispatchermapping import dispatcher, open

ip = "0.0.0.0"
port = 1339

dispatchermapping.openAbleton()
server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()  # Blocks forever
