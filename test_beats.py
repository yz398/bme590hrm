def test_beats():
    """
    Tests the beats function
    """
    try:
        import pytest
        from list_module.beats import beats
    except ImportError:
        print("Necessary imports for this test function failed")
        return
    test_data1 = [0, -3, -1.2, 10]
    test_data2 = []
    test_answer1 = 4
    test_answer2 = None
    assert test_answer1 == beats(test_data1)
    assert test_answer2 == beats(test_data2) 
    with pytest.raises(TypeError):
        min_max_list(5)
    with pytest.raises(TypeError):
        min_max_list('abc')
    with pytest.raises(TypeError):
        min_max_list({1: 4})
    with pytest.raises(ValueError):
        min_max_list(['s', 's'])
    with pytest.raises(ValueError):
        min_max_list(['-inf', 5])
    with pytest.raises(ValueError):
        min_max_list(['+inf', 5])
    with pytest.raises(ValueError):
        min_max_list([float('inf'), 5])
    with pytest.raises(ValueError):
        min_max_list([float('-inf'), 5])