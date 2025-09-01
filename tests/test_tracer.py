import pytest
from debugtracer import DebugTracer

def test_dprint_enabled(capsys):
    tracer = DebugTracer(enabled=True)
    tracer.dprint("Hello, Test!")
    captured = capsys.readouterr()
    assert "Hello, Test!" in captured.out

def test_dprint_disabled(capsys):
    tracer = DebugTracer(enabled=False)
    tracer.dprint("Should not print")
    captured = capsys.readouterr()
    assert "Should not print" not in captured.out

def test_log_and_records():
    tracer = DebugTracer(enabled=False)
    tracer.log({"step": 1, "msg": "test"})
    assert tracer.records == [{"step": 1, "msg": "test"}]

def test_print_section_header(capsys):
    tracer = DebugTracer(enabled=True)
    tracer.print_section_header("TEST SECTION")
    captured = capsys.readouterr()
    assert "TEST SECTION" in captured.out
