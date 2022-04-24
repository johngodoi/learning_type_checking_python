from dataclasses import dataclass
import typic
from pytypes import typechecked


@dataclass
@typic.al(strict=True, always=True)  # type: ignore
@typechecked  # type: ignore
class Greater:
    name: str

    def print_hi(self, other: str) -> None:
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {self.name+other}')  # Press Ctrl+F8 to toggle the breakpoint.
