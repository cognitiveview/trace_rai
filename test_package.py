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
        print(f"An error occurred: {e}")

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
        
        result = add_numbers(10, 5)
        print(f"✅ add_numbers(10, 5): {result}")


        print("\n🎉 All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_send_metrics()