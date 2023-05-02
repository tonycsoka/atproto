from xrpc_client import models
from xrpc_client.client.raw import AsyncClientRaw, ClientRaw

# TODO(MarshalX): Generate async version automatically


class Client(ClientRaw):
    """High-level client for XRPC of ATProtocol."""

    def login(self, login: str, password: str) -> models.GetProfileResponseRef:
        session = self.com.atproto.server.create_session(models.CreateSessionData(login, password))
        self.request.set_additional_headers({'Authorization': f'Bearer {session.accessJwt}'})
        return self.bsky.actor.get_profile(models.GetProfileParams(session.handle))


class AsyncClient(AsyncClientRaw):
    """High-level client for XRPC of ATProtocol."""

    async def login(self, login: str, password: str) -> models.GetProfileResponseRef:
        session = await self.com.atproto.server.create_session(models.CreateSessionData(login, password))
        self.request.set_additional_headers({'Authorization': f'Bearer {session.accessJwt}'})
        return await self.bsky.actor.get_profile(models.GetProfileParams(session.handle))
