from grpc import ServicerContext
import proto.greeting_pb2 as service_pb2
import proto.greeting_pb2_grpc as service_pb2_grpc
from delphai_utils.validation import validate


class Greeting(service_pb2_grpc.Greeting):
  async def greet(self, request: service_pb2.GreetRequest, context: ServicerContext) -> service_pb2.GreetResponse:
    await validate(service_pb2.GreetRequest, request, context)
    return service_pb2.GreetResponse(message=f'hello {request.name}')