from math import pi

#Standard pool shape
def standard(l_one, l_two, ds, dd):
    #calculations
    volume = ((ds * l_one) + ((dd - ds) * l_one/3)) * l_two #(top rectangle + bottom triangle) * width
    vol_in_G = volume * 1728 / 231

    #conditional and return
    if any(val < 0 for val in (l_one, l_two, ds, dd)):
        print("Please enter valid dimensions.")
        return None
    else:
        print(f"The volume of the Standard pool with your dimensions is {vol_in_G:,.2f} gallons.")
        return vol_in_G
    

def ramp(l_one, l_two, ds, dd):
    #calculations
    volume = (0.5 * ds * (l_one/3 + 2 * l_one/3) + (0.5 * l_one/3 * (ds + dd))) * l_two #(left trapezoid + right trapezoid) * width
    vol_in_G = volume * 1728 / 231

    #conditional and return
    if any(val < 0 for val in (l_one, l_two, ds, dd)):
        print("Please enter valid dimensions.")
        return None
    else:
        print(f"The volume of the Ramp pool with your dimensions is {vol_in_G:,.2f} gallons.")
        return vol_in_G
    

def round(l_one, l_two, ds, dd):    
    #calculations
    volume = (pi * l_one**2 * ds) + (pi * (dd - ds) / 3 * (l_one**2 + l_two**2 + (l_one * l_two))) #above cylinder + bottom frustum
    vol_in_G = volume * 1728 / 231

    #conditional and return
    if any(val < 0 for val in (l_one, l_two, ds, dd)):
        print("Please enter valid dimensions.")
        return None
    else:
        print(f"The volume of the Round pool with your dimensions is {vol_in_G:,.2f} gallons.")
        return vol_in_G