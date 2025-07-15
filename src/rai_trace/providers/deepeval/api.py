import requests
from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ...client import RaiTraceClient

class DeepevalProvider:
    """
    A client for submitting DeepEval metrics.
    """
    def __init__(self, client: 'RaiTraceClient'):
        self._client = client

    def submit(self, eval_metrics: Dict[str, Any], application_name: str, version: str, use_case: str):
        """
        Submits DeepEval metrics to the TRACE API.

        Args:
            metric_results (Dict[str, Any]): A dictionary of metric scores.
            application_name (str): The name of your application.
            version (str, optional): The application version. Defaults to "1.0.0".
            use_case (str, optional): The use case for the evaluation. Defaults to "default".
        """

        # url = f"{self._client.base_url}/cv/v1/metrics"
        url = self._client.base_url

        
        headers = {
            "Ocp-Apim-Subscription-Key": self._client.auth_token,
            "Content-Type": "application/json",
        }
        
        payload = {
            "metric_metadata": {
                "application_name": application_name,
                "version": version,
                "eval_provider": "deepeval",
                "use_case": use_case,
            },
            "metric_data": {
                "deepeval": eval_metrics
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            # Print the detailed error response from the server
            print(f"Response body: {response.text}")
            raise
