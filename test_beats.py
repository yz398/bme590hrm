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
        beats(5)
    with pytest.raises(TypeError):
        beats('abc')
    with pytest.raises(TypeError):
        beats({1: 4})
    with pytest.raises(ValueError):
        beats(['s', 's'])
    with pytest.raises(ValueError):
        beats(['-inf', 5])
    with pytest.raises(ValueError):
        beats(['+inf', 5])
    with pytest.raises(ValueError):
        beats([float('inf'), 5])
    with pytest.raises(ValueError):
        beats([float('-inf'), 5])
