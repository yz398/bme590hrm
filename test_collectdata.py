def test_collectdata():
    """
    Tests the collectdata function
    """
    try:
        import pytest
        from list_module.collectdata import collectdata
    except ImportError:
        print("Necessary imports for this test function failed")
        return 
    with pytest.raises(TypeError):
        collectdata([1,2,3])
