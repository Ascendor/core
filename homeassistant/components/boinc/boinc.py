"""Boinc Remote class wrapping boinc_client as RemoteEntity."""

from boinc_client import Boinc
from boinc_client.clients.rpc_client import RpcClient

from homeassistant.components.remote import RemoteEntity


class BoincRemote(RemoteEntity):
    """Boinc Remote class wrapping boinc_client as RemoteEntity."""

    def __init__(self, host, name, port, api_key, logger) -> None:
        """__init__ takes Hostname, Port and API-Key of the to-be-controlled BOINC PC, plus a free name and a logger."""
        self.host = host
        self._name = name
        self.port = port
        self.api_key = api_key
        self.logger = logger
        # Hostname or IP of the running BOINC client
        # Create an RPC client to connect to the BOINC socket
        self.rpc_client = RpcClient(
            hostname=self.host, port=self.port, password=self.api_key
        )
        self.rpc_client.authenticate()

        # Create a BOINC client to interact with the RPC socket
        self.boinc_client = Boinc(rpc_client=self.rpc_client)

    def turn_on(self, activity: str = "None", **kwargs):
        """Send the power on command."""

    async def async_turn_on(self, activity: str = "None", **kwargs):
        """Send the power on command."""

    @property
    def is_on(self) -> bool | None:
        """Return True if entity is on."""
        clientstate = self.boinc_client.get_client_state()
        self.logger.info(clientstate)
        return self._attr_is_on
