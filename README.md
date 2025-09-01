
# DebugTracer

**DebugTracer** is a lightweight, generic, and dynamic debug tracing utility for Python projects. It helps you capture, print, and structure debug information step-by-step, making it easy to review and analyze your application's behavior.

---

## Features

- **Lightweight**: Minimal dependencies, easy to add/remove.
- **Structured Logging**: Collects logs as structured dictionaries for later analysis.
- **Dynamic Printing**: Print debug messages and section headers only when enabled.
- **Reusable**: Package and use across multiple projects.

---

## Installation

Install locally in your project directory:

```sh
pip install .
```

Or install in development mode:

```sh
pip install -e .
```

---

## Basic Usage

```python
from debugtracer import DebugTracer

tracer = DebugTracer(enabled=True)
tracer.dprint("Hello, Debug!")
tracer.log({"step": 1, "info": "First step"})
tracer.print_section_header("TEST")
print(tracer.records)
```

**Output:**

```
Hello, Debug!



================================================================================
									TEST                                       
================================================================================


[{'step': 1, 'info': 'First step'}]
```

---

## Example: Tracing Steps in a Function

```python
from debugtracer import DebugTracer

def process_items(items, tracer=None):
	tracer = tracer or DebugTracer()
	tracer.print_section_header("PROCESS ITEMS")
	for idx, item in enumerate(items):
		tracer.dprint(f"Processing item {idx}: {item}")
		tracer.log({"step": idx, "item": item, "status": "processed"})
	return tracer.records

if __name__ == "__main__":
	tracer = DebugTracer(enabled=True)
	records = process_items(["apple", "banana", "cherry"], tracer)
	print(records)
```

---

## Example: Conditional Debugging

```python
from debugtracer import DebugTracer

def compute(x, y, debug=False):
	tracer = DebugTracer(enabled=debug)
	tracer.dprint(f"Computing sum of {x} and {y}")
	result = x + y
	tracer.log({"operation": "add", "x": x, "y": y, "result": result})
	return result, tracer.records

res, logs = compute(5, 7, debug=True)
print("Result:", res)
print("Debug logs:", logs)
```

---

## Example: Integrating with FastAPI (or any API)

```python
from fastapi import FastAPI
from debugtracer import DebugTracer

app = FastAPI()

@app.get("/add")
def add(x: int, y: int, debug: bool = False):
	tracer = DebugTracer(enabled=debug)
	tracer.dprint(f"Adding {x} + {y}")
	result = x + y
	tracer.log({"x": x, "y": y, "result": result})
	return {"result": result, "debug": tracer.records if debug else None}
```

---

## API Reference

### `DebugTracer(enabled: bool = False)`
Create a new tracer. If `enabled` is `True`, debug prints and headers are shown.

### `dprint(message: str)`
Print a debug message if enabled.

### `log(entry: dict)`
Add a structured log entry to the tracer's records.


### `print_section_header(section_title: str)`
Print a visually separated header for a new debug section (e.g., "TEST", "PROCESS", etc).

### `records`
List of all structured log entries collected during the run.

---

## License

MIT License
