from math import pi


#error: 0 means too high, 1 means too low, 2 means no error
def turbine_power(rho, length, velocity, cP):
    #velocity greater than 20
    if velocity > 20:
        power = 0
        print("Error, velocity is too high, no power generated")
    #velocity less than 4
    elif velocity < 4:
        power = 0
        print("Error, velocity is too low, no power generated")
    #reasonable velocity
    else:
        power = 1/2 * rho * pi * length**2 * velocity**3 * cP
    return power