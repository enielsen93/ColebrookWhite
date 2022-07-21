# ColebrookWhite
Python Package for calculating QFull for a circular pipe using Colebrook Whites formula

<b>To install:</b>

```
python -m pip install https://github.com/enielsen93/ColebrookWhite/tarball/master
```

## Example:
```
import ColebrookWhite
pipe_diameter = 0.2 # m
slope = 10e-3 # m/m
pipe_material = "Plastic"

print(ColebrookWhite.QFull(pipe_diameter, slope, pipe_material))
```
