"""
Quick test script for rai-trace package
"""

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

        # Test deepeval import
        from rai_trace.providers.deepeval import submit
        print("✅ deepeval submodule imports work")

        # Mock the API call for testing
        try:
            import unittest.mock as mock
            with mock.patch('requests.post') as mock_post:
                mock_response = mock.Mock()
                mock_response.status_code = 200
                mock_response.json.return_value = {"status": "success"}
                mock_post.return_value = mock_response

                metrics = {
                    "dataset_drift": 0.1,
                    "data_quality": {
                        "feature1": "ok"
                    }
                }
                response = submit(metrics, api_key="dummy_key")
                print(f"✅ deepeval.submit(): {response}")
        except ImportError:
            print("Could not import mock, skipping deepeval test")
        
        print("\n🎉 All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_imports()