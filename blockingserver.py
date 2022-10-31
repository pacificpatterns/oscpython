from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from dispatchermapping import dispatcher

ip = "0.0.0.0"
port = 1338


server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()  # Blocks forever