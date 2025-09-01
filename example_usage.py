from debugtracer import DebugTracer

if __name__ == "__main__":
    tracer = DebugTracer(enabled=True)
    tracer.dprint("Hello, Debug!")
    tracer.log({"step": 1, "info": "First step"})
    tracer.print_section_header("TEST")
    print(tracer.records)
