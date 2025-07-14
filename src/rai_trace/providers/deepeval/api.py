import requests
from typing import Dict, Any
from providers.deepeval.keys import DEEPEVAL_METRIC_KEYS

class DeepEvalClient:
    def __init__(self, api_key: str, api_url: str = "https://api.deepeval.com"):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def submit_metrics(self, metrics: Dict[str, Any]):
        """
        Submits metrics to the DeepEval API.
        Validates metrics against Evidently keys before submitting.
        """
        validated_metrics = {key: metrics[key] for key in metrics if key in EVIDENTLY_METRIC_KEYS}

        if not validated_metrics:
            print("No valid metrics to submit.")
            return None

        endpoint = f"{self.api_url}/metrics"

        try:
            response = requests.post(endpoint, json = validated_metrics, headers = self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error submitting metrics to DeepEval: {e}")
            return None


