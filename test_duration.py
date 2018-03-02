def test_duration():
    """
    Tests the duration function
    """
    try:
        import pytest
        from list_module.duration import duration
    except ImportError:
        print("Necessary imports for this test function failed")
        return
    test_data1 = [0, -3, -1.2, 10]
    test_data2 = []
    test_answer1 = 10
    test_answer2 = None
    assert test_answer1 == duration(test_data1)
    assert test_answer2 == duration(test_data2)

    with pytest.raises(TypeError):
        duration(5)
    with pytest.raises(TypeError):
        duration('abc')
    with pytest.raises(TypeError):
        duration({1: 4})
    with pytest.raises(ValueError):
        duration(['s', 's'])
    with pytest.raises(ValueError):
        duration(['-inf', 5])
    with pytest.raises(ValueError):
        duration(['+inf', 5])
    with pytest.raises(ValueError):
        duration([float('inf'), 5])
    with pytest.raises(ValueError):
        duration([float('-inf'), 5])