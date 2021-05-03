# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pgcapture_pb2 as pgcapture__pb2


class DBLogGatewayStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Capture = channel.stream_stream(
                '/pgcapture.DBLogGateway/Capture',
                request_serializer=pgcapture__pb2.CaptureRequest.SerializeToString,
                response_deserializer=pgcapture__pb2.CaptureMessage.FromString,
                )


class DBLogGatewayServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Capture(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DBLogGatewayServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Capture': grpc.stream_stream_rpc_method_handler(
                    servicer.Capture,
                    request_deserializer=pgcapture__pb2.CaptureRequest.FromString,
                    response_serializer=pgcapture__pb2.CaptureMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pgcapture.DBLogGateway', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DBLogGateway(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Capture(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/pgcapture.DBLogGateway/Capture',
            pgcapture__pb2.CaptureRequest.SerializeToString,
            pgcapture__pb2.CaptureMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DBLogControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PullDumpInfo = channel.stream_stream(
                '/pgcapture.DBLogController/PullDumpInfo',
                request_serializer=pgcapture__pb2.DumpInfoRequest.SerializeToString,
                response_deserializer=pgcapture__pb2.DumpInfoResponse.FromString,
                )
        self.Schedule = channel.unary_unary(
                '/pgcapture.DBLogController/Schedule',
                request_serializer=pgcapture__pb2.ScheduleRequest.SerializeToString,
                response_deserializer=pgcapture__pb2.ScheduleResponse.FromString,
                )


class DBLogControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PullDumpInfo(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Schedule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DBLogControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PullDumpInfo': grpc.stream_stream_rpc_method_handler(
                    servicer.PullDumpInfo,
                    request_deserializer=pgcapture__pb2.DumpInfoRequest.FromString,
                    response_serializer=pgcapture__pb2.DumpInfoResponse.SerializeToString,
            ),
            'Schedule': grpc.unary_unary_rpc_method_handler(
                    servicer.Schedule,
                    request_deserializer=pgcapture__pb2.ScheduleRequest.FromString,
                    response_serializer=pgcapture__pb2.ScheduleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pgcapture.DBLogController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DBLogController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PullDumpInfo(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/pgcapture.DBLogController/PullDumpInfo',
            pgcapture__pb2.DumpInfoRequest.SerializeToString,
            pgcapture__pb2.DumpInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Schedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pgcapture.DBLogController/Schedule',
            pgcapture__pb2.ScheduleRequest.SerializeToString,
            pgcapture__pb2.ScheduleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AgentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Configure = channel.unary_unary(
                '/pgcapture.Agent/Configure',
                request_serializer=pgcapture__pb2.AgentConfigRequest.SerializeToString,
                response_deserializer=pgcapture__pb2.AgentConfigResponse.FromString,
                )
        self.Dump = channel.unary_unary(
                '/pgcapture.Agent/Dump',
                request_serializer=pgcapture__pb2.AgentDumpRequest.SerializeToString,
                response_deserializer=pgcapture__pb2.AgentDumpResponse.FromString,
                )


class AgentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Configure(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Dump(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Configure': grpc.unary_unary_rpc_method_handler(
                    servicer.Configure,
                    request_deserializer=pgcapture__pb2.AgentConfigRequest.FromString,
                    response_serializer=pgcapture__pb2.AgentConfigResponse.SerializeToString,
            ),
            'Dump': grpc.unary_unary_rpc_method_handler(
                    servicer.Dump,
                    request_deserializer=pgcapture__pb2.AgentDumpRequest.FromString,
                    response_serializer=pgcapture__pb2.AgentDumpResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pgcapture.Agent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Agent(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Configure(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pgcapture.Agent/Configure',
            pgcapture__pb2.AgentConfigRequest.SerializeToString,
            pgcapture__pb2.AgentConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Dump(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pgcapture.Agent/Dump',
            pgcapture__pb2.AgentDumpRequest.SerializeToString,
            pgcapture__pb2.AgentDumpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
