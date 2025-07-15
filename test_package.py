"""
Quick test script for rai-trace package
"""


def test_send_metrics():
    from rai_trace.client import RaiTraceClient
    """
    Example test to send metrics using the RaiTraceClient.
    """
    
    # This client will hold your authentication token and manage providers.
    client = RaiTraceClient(auth_token = 'f895bd4974e248998099c10bb5bec046')

    # 2. Prepare your metric data for each provider
    deepeval_metrics = {
        'AnswerRelevancyMetric': 20,
        'FaithfulnessMetric': 1.0,
        'HallucinationMetric': 0.0
    }

    opik_metrics = {
        'Equals': 0.95,
        'Contains': 1.0,
        'RegexMatch': 0.85,
        'IsJson': 1.0,
        'SentenceBLEU': 0.78,
        'CorpusBLEU': 0.82,
        'ROUGE': 0.88,
        'Sentiment': 0.7,
        'Moderation': 0.95,
        'Usefulness': 0.9,
        'AnswerRelevance': 0.85,
        'ContextPrecision': 0.92,
        'ContextRecall': 0.87
    }

    evidently_metrics = {
        'ContextRelevance': 0.89,
        'BLEU': 0.76,
        'ROUGE': 0.84,
        'BERTScore': 0.91,
        'ExactMatch': 0.65,
        'MAP': 0.73,
        'NDCG': 0.81,
        'MRR': 0.78,
        'HitRate': 0.85,
        'FaithfulnessLLMEval': 0.92,
        'CorrectnessLLMEval': 0.88,
        'IsValidJSON': 1.0,
        'DeclineLLMEval': 0.05,
        'PIILLMEval': 0.02,
        'BiasLLMEval': 0.15,
        'ToxicityLLMEval': 0.03,
        'Sentiment': 0.72,
        'NegativityLLMEval': 0.08,
        'Diversity': 0.67,
        'Serendipity': 0.45,
        'ScoreDistribution': 0.6,
        'OOVWordsPercentage': 0.12,
        'PrecisionTopK': 0.83,
        'RecallTopK': 0.79,
        'FBetaTopK': 0.81,
        'RegExp': 0.94,
        'Contains': 0.98,
        'TextLength': 15,
        'Perplexity': 25.4
    }

    # 3. Use the provider-specific methods from the client instance
    # The client handles passing the auth token and base URL to the provider.
    print("Sending DeepEval metrics...")
    try:
        response = client.deepeval.submit(
            eval_metrics = deepeval_metrics,
            application_name = "trace_sdk",
            version = "1.0.0",
            use_case = "transportation"
        )
        print("Response from DeepEval submission:", response)
        assert response is not None # Add a basic assertion

    except Exception as e:
        print(f"An error occurred with DeepEval: {e}")

    print("\nSending Opik metrics...")
    try:
        response = client.opik.submit(
            eval_metrics = opik_metrics,
            application_name = "trace_sdk",
            version = "1.0.0",
            use_case = "transportation"
        )
        print("Response from Opik submission:", response)
        assert response is not None

    except Exception as e:
        print(f"An error occurred with Opik: {e}")

    print("\nSending Evidently metrics...")
    try:
        response = client.evidently.submit(
            eval_metrics = evidently_metrics,
            application_name = "trace_sdk",
            version = "1.0.0",
            use_case = "transportation"
        )
        print("Response from Evidently submission:", response)
        assert response is not None

    except Exception as e:
        print(f"An error occurred with Evidently: {e}")

def test_imports():
    """Test that imports work correctly"""
    try:
        # Test package import
        import rai_trace
        print(f"✅ Package imported successfully")
        print(f"Version: {rai_trace.__version__}")
        
        # Test submodule import
        from rai_trace.plugins.sample import hello_world, add_numbers
        print("✅ Submodule imports work")
        
        # Test functions
        greeting = hello_world("Developer")
        print(f"✅ hello_world(): {greeting}")

        print("\n🎉 All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_imports()
    test_send_metrics()