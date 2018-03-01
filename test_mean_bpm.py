def test_mean_bpm():
    """
    Tests the mean_bpm function
    """
    try:
        import pytest
        from list_module.mean_bpm import mean_bpm 
        from list_module.beats import beats
    except ImportError:
        print("Necessary imports for this test function failed")
        return

    x1 = [1,2,3,4]
    f1 = [1,2,3]
    x2=[]
    f2 =[]
    test_answer1 = 120.0
    test_answer2 = None
    assert test_answer1 == mean_bpm(test_data1)
    assert test_answer2 == mean_bpm(test_data2)
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