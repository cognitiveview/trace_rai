import json
import os
import sys
from rai_trace.client import RaiTraceClient

def load_env_variable(key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise EnvironmentError(f"Missing required environment variable: {key}")
    return value

def load_metrics(filepath: str) -> dict:
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Metrics file not found at path: {filepath}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in metrics file: {filepath}")

def evaluate_and_submit(metrics: dict, client: RaiTraceClient) -> dict:
    return client.deepeval.submit(
        eval_metrics=metrics,
        application_name="my-chatbot-app",
        version="1.2.0",
        use_case="customer-support"
    )

def check_evaluation_result(response: dict):
    result = response.get("result") or response.get("status")
    if result and result.lower() == "fail":
        print("Evaluation failed. TRACE result:", result)
        sys.exit(1)
    print("Evaluation passed. TRACE result:", result or "unknown")

def main():
    try:
        auth_token = load_env_variable("TRACE_TOKEN")
        metrics_path = os.environ.get("TRACE_METRICS_FILE", "trace_inputs/metrics.json")

        print(f"Loading metrics from: {metrics_path}")
        metrics = load_metrics(metrics_path)

        print("Submitting metrics to TRACE...")
        client = RaiTraceClient(auth_token=auth_token)
        response = evaluate_and_submit(metrics, client)

        print("TRACE response received:")
        print(json.dumps(response, indent=2))

        check_evaluation_result(response)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()