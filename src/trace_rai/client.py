from .providers.deepeval.api import DeepevalProvider
from .providers.evidently.api import EvidentlyProvider
from .providers.opik.api import OpikProvider

class RaiTraceClient:
    """
    The main client for interacting with the TRACE API.
    """
    def __init__(self, auth_token: str, base_url: str = "https://qa-api-manager.azure-api.net/trace/metrics"):
        """
        Initializes the client with authentication credentials.

        Args:
            auth_token (str): Your authorization token.
            base_url (str, optional): The base URL of the API. Defaults to "https://api.cognitiveview.com".
        """
        self.auth_token = auth_token
        self.base_url = base_url

        # Instantiate and attach provider-specific clients
        self.deepeval = DeepevalProvider(self)
        self.evidently = EvidentlyProvider(self)
        self.opik = OpikProvider(self)
