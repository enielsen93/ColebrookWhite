import numpy as np
def QFull(diameter, slope, material, resolution = 1e-6):
    if material[0].lower() == "p":
        k = 0.001
    else:
        k = 0.0015

    g = 9.82 #m2/s
    kinematicViscosity = 0.0000013 #m2/s
    R = diameter / 4.0

    Vmin = 0.001
    Vmax = 500
    I = 1E+40
    while abs(slope - I) > resolution and Vmax-Vmin > resolution:
        V = 10**((np.log10(Vmax) + np.log10(Vmin)) / 2.0)

        Re = V * R / kinematicViscosity
        f = 0.01 #Initial Guess
        fOld = 1000
        while abs(f - fOld) > resolution:
            fOld = f
            f = 2 / (6.4 - 2.45 * np.log(k / R + 4.7 / (Re * np.sqrt(f)))) ** 2
        I = f * (V ** 2 / (2 * g * R))
        if slope > I:
            Vmin = V
        else:
            Vmax = V
    if Vmax-Vmin <= resolution:
        return None
    else:
        return V * (diameter / 2.0) ** 2 * np.pi