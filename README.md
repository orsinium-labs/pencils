# pencils

Pancils is a Python library with a colletion of color palettes.

Currently available palettes:

+ Everything from [flatuicolors.com](https://flatuicolors.com/)
+ Most of the palettes from [materialui.co](https://materialui.co/)
+ [Tailwind](https://tailwindcss.com/) color palette.
+ [Bootstrap](https://getbootstrap.com/) color palette.
+ CSS (HTML) color names.

Features:

+ A lot of colors from manually picked palettes.
+ 100% type safe.
+ Best integration with IDEs, autocomplete all the way down.
+ Includes multiple representations (HEX, [RGB](https://en.wikipedia.org/wiki/RGB_color_model), [HSL](https://en.wikipedia.org/wiki/HSL_and_HSV)) for each color.
+ Zero-dependency.

Installatiion:

```bash
python3 -m pip install pencils
```

## Usage

Get the hex representation of "Sunflower" color from [Dutch Palette](https://flatuicolors.com/palette/nl) of [Flat UI Colors](https://flatuicolors.com/):

```python
import pencils

pencils.NLPalette.colors.sunflower.value.hex
# 'FFC312'
```

The color: <span style="color:#FFC312">◼◼◼</span>

That's a lot of attributes and each one of them has a meaning:

1. `NLPalette` is an instance of the `pencils.Palette` class which holds information about palette name, author, source URL, and even emojis associated with the palette.
1. `colors` attribute is an [enum](https://docs.python.org/3/library/enum.html), a subclass of `pencils.Colors`.
1. `sunflower` is the color ID.
1. `value` is used to get the value of the enum. The value is an instance of `pencils.Color` class which contains operations on colors.
1. `hex` is a lowercase hex representaion of the color without `#`.

Make the color darker:

```python
color = pencils.NLPalette.colors.sunflower.value.hsl
color.lightness = .2
color.hex
# '664c00'
```

The color: <span style="color:#664c00">◼◼◼</span>

Get random color from a random palette:

```python
pencils.random_palette().random_color()
# Color(name='Unmellow Yellow', hex='fffa65')
```

The color: <span style="color:#fffa65">◼◼◼</span>
