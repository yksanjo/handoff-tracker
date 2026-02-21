import importlib


def test_main_exists():
    mod = importlib.import_module("handoff_tracker.cli")
    assert hasattr(mod, "main")
