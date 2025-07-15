import requests
from typing import Dict, Any

class OpikProvider:
    """
    A client for submitting DeepEval metrics.
    """
    def __init__(self, client: 'RaiTraceClient'):
        self._client = client

    def submit(self, metric_results: Dict[str, Any], application_name: str, version: str = "1.0.0", use_case: str = "default"):
        """
        Submits DeepEval metrics to the TRACE API.

        Args:
            metric_results (Dict[str, Any]): A dictionary of metric scores.
            application_name (str): The name of your application.
            version (str, optional): The application version. Defaults to "1.0.0".
            use_case (str, optional): The use case for the evaluation. Defaults to "default".
        """
        url = f"{self._client.base_url}/cv/v1/metrics"
        headers = {
            "Authorization": self._client.auth_token,
            "Content-Type": "application/json",
            "X-User-Id": self._client.user_id,
        }
        payload = {
            "metric_metadata": {
                "application_name": application_name,
                "version": version,
                "provider": "deepeval",
                "use_case": use_case,
            },
            "metric_data": {
                "deepeval": metric_results
            }
        }
        
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
