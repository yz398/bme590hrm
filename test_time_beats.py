def test_time_beats():
    """
    Tests the time_beats function
    """
    try:
        import pytest
        from list_module.time_beats import time_beats
        import numpy
    except ImportError:
        print("Necessary imports for this test function failed")
        return    
    x1 = []
    f1 = []
    x2 = [1, 3, 5, 7]
    f2 = [1, 2, 3, 4, 4, 5, 6, 7]
    test_answer1 = None
    test_answer2 = [[2., 2.], [2., 4.], [2., 5.]]
    assert test_answer1 == time_beats(x1, f1)
    assert (test_answer2 == time_beats(x2, f2)).all() == True
    with pytest.raises(TypeError):
        time_beats(5, 6)
    with pytest.raises(TypeError):
        time_beats('abc', [1, 2, 3])
    with pytest.raises(TypeError):
        time_beats({1: 4}, [1, 2, 3])
    with pytest.raises(ValueError):
        time_beats(['s', 's'], [1, 2, 3]) 
        