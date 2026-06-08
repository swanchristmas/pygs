def test_import() -> None:
    import pygs as _pygs

    assert _pygs.__name__ == "pygs"
