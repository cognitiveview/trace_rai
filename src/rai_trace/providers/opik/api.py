import requests
from typing import Dict, Any, TYPE_CHECKING
from .keys import OpikGenerativeMetrics


if TYPE_CHECKING:
    from ...client import RaiTraceClient

class OpikProvider:
    """
    A client for submitting DeepEval metrics.
    """
    def __init__(self, client: 'RaiTraceClient'):
        self._client = client

    def submit(self, eval_metrics: Dict[str, Any], application_name: str, version: str = "1.0.0", use_case: str = "default"):
        """
        Submits DeepEval metrics to the TRACE API.

        Args:
            metric_results (Dict[str, Any]): A dictionary of metric scores.
            application_name (str): The name of your application.
            version (str): The application version.
            use_case (str): The use case for the evaluation.
        """

        try:
            eval_metrics = OpikGenerativeMetrics(**eval_metrics).model_dump()
        
        except Exception as e:
            print(f"Metric validation failed: {e}")
            raise

        url = self._client.base_url
        
        headers = {
            "Ocp-Apim-Subscription-Key": self._client.auth_token,
            "Content-Type": "application/json",
        }
        payload = {
            "metric_metadata": {
                "application_name": application_name,
                "version": version,
                "eval_provider": "opik",
                "use_case": use_case,
            },
            "metric_data": {
                "opik": eval_metrics
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response body: {response.text}")
            raise

