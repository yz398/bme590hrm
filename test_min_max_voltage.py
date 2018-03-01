def test_min_max_voltage():
    """
    Tests the min_max_voltage function
    """
    try:
        import pytest
        from list_module.min_max_voltage import min_max_voltage
    except ImportError:
        print("Necessary imports for this test function failed")
        return
    test_data1 = [0, -3, -1.2, 10]
    test_data2 = [1, 3, 2, 5]
    test_data3 = [-3/2, -9, -3, -7, -1]
    test_data4 = []
    test_answer1 = (-3, 10)
    test_answer2 = (1, 5)
    test_answer3 = (-9, -1)
    test_answer4 = (None, None)
    assert test_answer1 == min_max_voltage(test_data1)
    assert test_answer2 == min_max_voltage(test_data2)
    assert test_answer3 == min_max_voltage(test_data3)
    assert test_answer4 == min_max_voltage(test_data4)
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