##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing_extensions as te

from atproto.xrpc_client.models import base


class Params(base.ParamsModelBase):

    """Parameters model for :obj:`com.atproto.sync.getCheckout`."""

    did: str  #: The DID of the repo.


class ParamsDict(te.TypedDict):
    did: str  #: The DID of the repo.


#: Response raw data type.
Response: te.TypeAlias = bytes
