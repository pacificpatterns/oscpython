import abletonKeyFunctions as akf
import blockingserver
from pythonosc.osc_server import BlockingOSCUDPServer
from dispatchermapping import dispatcher, open

print(open)
akf.openAbleton()
print(open)

# ip = "0.0.0.0"
# port = 1337

# server = BlockingOSCUDPServer((ip, port), dispatcher)
# server.serve_forever()  # Blocks forever
