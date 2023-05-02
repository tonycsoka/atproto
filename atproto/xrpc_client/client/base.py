import dataclasses
from enum import Enum
from typing import Optional

from xrpc_client.request import AsyncRequest, Request, Response

# TODO(MarshalX): Generate async version automatically!


class InvokeType(Enum):
    QUERY = 'query'
    PROCEDURE = 'procedure'


_BASE_API_URL = 'https://bsky.social/xrpc'


class ClientBase:
    """Low level methods are here"""

    def __init__(self, base_url: Optional[str] = None, request: Optional[Request] = None):
        if request is None:
            request = Request()
        if base_url is None:
            base_url = _BASE_API_URL

        self._request = request
        self._base_url = base_url

    @property
    def request(self) -> Request:
        return self._request

    def _build_url(self, nsid: str) -> str:
        return f'{self._base_url}/{nsid}'

    def invoke_query(self, nsid: str, params: Optional[dict] = None, data: Optional[dict] = None, **kwargs) -> Response:
        return self._invoke(InvokeType.QUERY, url=self._build_url(nsid), params=params, data=data, **kwargs)

    def invoke_procedure(
        self, nsid: str, params: Optional[dict] = None, data: Optional[dict] = None, **kwargs
    ) -> Response:
        return self._invoke(InvokeType.PROCEDURE, url=self._build_url(nsid), params=params, data=data, **kwargs)

    def _invoke(self, invoke_type: InvokeType, **kwargs) -> Response:
        # TODO(MarshalX): write proper serialization. Add support of more kwargs!
        if 'data' in kwargs and kwargs['data']:
            kwargs['json'] = dataclasses.asdict(kwargs['data'])
            kwargs.pop('data')
        if 'params' in kwargs and kwargs['params']:
            kwargs['params'] = dataclasses.asdict(kwargs['params'])

        if invoke_type is InvokeType.QUERY:
            return self.request.get(**kwargs)
        else:
            return self.request.post(**kwargs)


class AsyncClientBase:
    """Low level methods are here"""

    def __init__(self, base_url: Optional[str] = None, request: Optional[AsyncRequest] = None):
        if request is None:
            request = AsyncRequest()
        if base_url is None:
            base_url = _BASE_API_URL

        self._request = request
        self._base_url = base_url

    @property
    def request(self) -> AsyncRequest:
        return self._request

    def _build_url(self, nsid: str) -> str:
        return f'{self._base_url}/{nsid}'

    async def invoke_query(
        self, nsid: str, params: Optional[dict] = None, data: Optional[dict] = None, **kwargs
    ) -> Response:
        return await self._invoke(InvokeType.QUERY, url=self._build_url(nsid), params=params, data=data, **kwargs)

    async def invoke_procedure(
        self, nsid: str, params: Optional[dict] = None, data: Optional[dict] = None, **kwargs
    ) -> Response:
        return await self._invoke(InvokeType.PROCEDURE, url=self._build_url(nsid), params=params, data=data, **kwargs)

    async def _invoke(self, invoke_type: InvokeType, **kwargs) -> Response:
        # TODO(MarshalX): write proper serialization. Add support of more kwargs!
        if 'data' in kwargs and kwargs['data']:
            kwargs['json'] = dataclasses.asdict(kwargs['data'])
            kwargs.pop('data')
        if 'params' in kwargs and kwargs['params']:
            kwargs['params'] = dataclasses.asdict(kwargs['params'])

        if invoke_type is InvokeType.QUERY:
            return await self.request.get(**kwargs)
        else:
            return await self.request.post(**kwargs)
