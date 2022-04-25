"""A collection of color palettes.
"""
from ._palette import Palette
from ._palettes import (
    DefoPalette,
    NLPalette,
    TRPalette,
    INPalette,
    SEPalette,
    CAPalette,
    AUPalette,
    RUPalette,
    FRPalette,
    ESPalette,
    DEPalette,
    CNPalette,
    USPalette,
    GBPalette,
    SocialPalette,
    MetroPalette,
    CSSPalette,
    TailwindPalette,
    BootstrapPalette,
)
from ._color import Color
from ._colors import Colors
from ._hsl import HSL
from ._rgb import RGB
from ._registry import random_palette, PALETTES


__version__ = "0.1.0"
__all__ = [
    'DefoPalette',
    'NLPalette',
    'TRPalette',
    'INPalette',
    'SEPalette',
    'CAPalette',
    'AUPalette',
    'RUPalette',
    'FRPalette',
    'ESPalette',
    'DEPalette',
    'CNPalette',
    'USPalette',
    'GBPalette',
    'SocialPalette',
    'MetroPalette',
    'CSSPalette',
    'TailwindPalette',
    'BootstrapPalette',

    'Palette',
    'Color',
    'Colors',
    'Palettes',
    'HSL',
    'RGB',
    'random_palette',
    'PALETTES',
]
