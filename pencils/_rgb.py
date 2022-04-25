from __future__ import annotations
from dataclasses import dataclass


@dataclass
class RGB:
    red: int
    green: int
    blue: int

    @property
    def r(self) -> int:
        return self.red

    @property
    def g(self) -> int:
        return self.green

    @property
    def b(self) -> int:
        return self.blue

    @property
    def red_hex(self) -> str:
        return f'{self.red:02x}'

    @property
    def green_hex(self) -> str:
        return f'{self.green:02x}'

    @property
    def blue_hex(self) -> str:
        return f'{self.blue:02x}'

    @property
    def red_float(self) -> float:
        return self.red / 255

    @property
    def green_float(self) -> float:
        return self.green / 255

    @property
    def blue_float(self) -> float:
        return self.blue / 255

    @property
    def hex(self) -> str:
        return f'{self.red:02x}{self.green:02x}{self.blue:02x}'

    @property
    def hash(self) -> str:
        return f'#{self.hex}'

    @property
    def ints(self) -> tuple[int, int, int]:
        return (self.red, self.green, self.blue)

    @property
    def floats(self) -> tuple[float, float, float]:
        return (self.red / 255, self.green / 255, self.blue / 255)

    @property
    def css(self) -> str:
        return f'rgb({self.red}, {self.green}, {self.blue})'
