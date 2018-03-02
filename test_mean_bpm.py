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

    x1 = [1, 2, 3, 4]
    f1 = [1, 2, 3]
    x2 = []
    f2 = []
    test_answer1 = 120.
    test_answer2 = None
    assert test_answer1 == mean_bpm(x1, f1)
    assert test_answer2 == mean_bpm(x2, f2)
    with pytest.raises(TypeError):
        mean_bpm(5, 6)
    with pytest.raises(TypeError):
        mean_bpm('abc', [1, 2, 3])
    with pytest.raises(TypeError):
        mean_bpm({1: 4}, [1, 2, 3])
    with pytest.raises(ValueError):
        mean_bpm(['s', 's'], [1, 2, 3])
