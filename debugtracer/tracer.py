# flake8: noqa: E501
from typing import Any, Dict, List


class DebugTracer:
    """Lightweight tracer to capture and print step-by-step debug info.

    - When enabled, dprint() emits to stdout and every log() is recorded.
    - Collected logs can be returned in the API's "debug" block for review.
    - Section headers can be printed to visually separate debug output.
    """

    def __init__(self, enabled: bool = False) -> None:
        self.enabled = enabled
        self.records: List[Dict[str, Any]] = []

    def dprint(self, message: str) -> None:
        if self.enabled:
            print(message)

    def log(self, entry: Dict[str, Any]) -> None:
        # Keep logs structured for post-run analysis
        self.records.append(entry)

    def print_section_header(self, section_title: str) -> None:
        """Print a formatted header for the section being processed.

        Creates large visual gaps before/after to clearly separate sections.
        Example: tracer.print_section_header("TEST")
        """
        if self.enabled:
            sep = "=" * 80
            # Large gap before
            print("\n\n")
            print(sep)
            print(f"{section_title:^80}")
            print(sep)
            # Gap after
            print("\n")
