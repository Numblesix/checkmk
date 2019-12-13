# Stubs for kubernetes.client.models.v1_host_alias (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1HostAlias:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    hostnames: Any = ...
    ip: Any = ...
    def __init__(self, hostnames: Optional[Any] = ..., ip: Optional[Any] = ...) -> None: ...
    @property
    def hostnames(self): ...
    @hostnames.setter
    def hostnames(self, hostnames: Any) -> None: ...
    @property
    def ip(self): ...
    @ip.setter
    def ip(self, ip: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...