import sys
sys.path.append('gen-py')
sys.path.append('vendored')
from thrift.protocol import TBinaryProtocol, TJSONProtocol
from thrift.server import TServer
from thrift.transport import TTransport
from lambda_thrift_service import MultiplicationService

class MultiplicationServiceHandler(object):
    def multiply(self, i, j):
        return i * j

handler = MultiplicationServiceHandler()
processor = MultiplicationService.Processor(handler)
protocol_factory = TJSONProtocol.TJSONProtocolFactory()
server = TServer.TServer(processor, None, None, None, protocol_factory, protocol_factory)

def multiply(event, context):
    body = event['body']
    itrans = TTransport.TMemoryBuffer(body)
    otrans = TTransport.TMemoryBuffer()
    iprot = server.inputProtocolFactory.getProtocol(itrans)
    oprot = server.outputProtocolFactory.getProtocol(otrans)
    server.processor.process(iprot, oprot)
    return {'statusCode': 200, 'body': otrans.getvalue()}
