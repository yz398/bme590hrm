def test_detect_peak():
    """
    Tests the detect_peak function
    """
    try:
        import pytest
        from list_module.detect_peak import detect_peak
    except ImportError:
        print("Necessary imports for this test function failed")
        return

    test_data1 = [0, 3, -2, 7, 1,4]
    test_data2 = []
    test_answer1 = [[3, 7], [1, 3]]
    test_answer2 = None
    assert test_answer1 == detect_peak(test_data1)
    assert test_answer2 == detect_peak(test_data2)
    with pytest.raises(TypeError):
        detect_peak(5)
    with pytest.raises(TypeError):
        detect_peak('abc')
    with pytest.raises(TypeError):
        detect_peak({1: 4})
    with pytest.raises(ValueError):
        detect_peak(['s', 's'])
    with pytest.raises(ValueError):
        detect_peak(['-inf', 5])
    with pytest.raises(ValueError):
        detect_peak(['+inf', 5])
    with pytest.raises(ValueError):
        detect_peak([float('inf'), 5])
    with pytest.raises(ValueError):
        detect_peak([float('-inf'), 5])