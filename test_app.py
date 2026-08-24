def test_app_file_exists():
    import os
    assert os.path.exists("wrong_app.py")
