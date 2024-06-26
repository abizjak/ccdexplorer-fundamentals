# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: health.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class NodeHealthRequest(betterproto.Message):
    """
    Parameters to the node health query. The default message gives a good
    default.
    """

    pass


@dataclass(eq=False, repr=False)
class NodeHealthResponse(betterproto.Message):
    """
    Response to the health check. A return code of "OK" is used for success,
    and errors are handled via RPC status codes
    """

    pass


class HealthStub(betterproto.ServiceStub):
    async def check(
        self,
        node_health_request: "NodeHealthRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "NodeHealthResponse":
        return await self._unary_unary(
            "/concordium.health.Health/Check",
            node_health_request,
            NodeHealthResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class HealthBase(ServiceBase):
    async def check(
        self, node_health_request: "NodeHealthRequest"
    ) -> "NodeHealthResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_check(
        self, stream: "grpclib.server.Stream[NodeHealthRequest, NodeHealthResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.check(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/concordium.health.Health/Check": grpclib.const.Handler(
                self.__rpc_check,
                grpclib.const.Cardinality.UNARY_UNARY,
                NodeHealthRequest,
                NodeHealthResponse,
            ),
        }
