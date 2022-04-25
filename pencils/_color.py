from __future__ import annotations
from colorsys import rgb_to_hls
from dataclasses import dataclass
from functools import cached_property
from ._rgb import RGB
from ._hsl import HSL


@dataclass
class Color:
    name: str
    hex: str

    @cached_property
    def rgb(self) -> RGB:
        """The color representation as a tuple of ints from 0 to 255.
        """
        assert len(self.hex) == 6
        return RGB(
            int(self.hex[:2], 16),
            int(self.hex[2:4], 16),
            int(self.hex[4:], 16),
        )

    @cached_property
    def hsl(self) -> HSL:
        rgb = self.rgb
        hue, ls, sat = rgb_to_hls(rgb.red_float, rgb.green_float, rgb.blue_float)
        return HSL(hue, sat, ls)

    @property
    def hls(self) -> HSL:
        return self.hsl
