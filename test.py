import sys
import glob
sys.path.append('gen-py')
from thrift import Thrift
from thrift.transport import THttpClient
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TJSONProtocol
from lambda_thrift_service import MultiplicationService

URL = '' #Replace this
transport = THttpClient.THttpClient(URL)
transport = TTransport.TBufferedTransport(transport)
protocol = TJSONProtocol.TJSONProtocol(transport)

client = MultiplicationService.Client(protocol)
transport.open()

print client.multiply(100, 50)
