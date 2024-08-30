from math import pi


################ formulas for rectangular profiles #################### 

def I_rect(h:float, b:float) -> float:
    """
    calcultat I (treghetsmoment) for a rectangular profile
    """
    I = 1/12 * b * h*h*h
    return I

def W_pl_rect(h:float, b:float) -> float:
    W = 1/4 * b * h*h
    return W

def W_el_rect(h:float, b:float) -> float:
    W = 1/6 * b * h*h
    return W

############### formulas for H - profiles ####################

def I_H(h: float, t_steg:float, b:float, t_flens:float, r:float = 0) -> float:
    """
    calaculat I for dobbel symetrical H-profiles
    """
    h_steg = h - t_flens*2
    d_flens = h/2 - t_steg/2
    d_rad = h_steg/2 - 0.223*r
    a_runding = 4*r*r - pi*r*r

    I_steg = I_rect(h_steg, t_steg)
    I_flens = I_rect(t_flens, b)
    I_rad = 0.0075*r**4

    Iy = I_steg + 2*(I_flens + b*t_flens*d_flens*d_flens) + 4*I_rad + 2*(a_runding/2*d_rad*d_rad) #denne må kontrollerast
    return Iy

##noe er feil her

k =I_H(990, 16.5, 300, 31, 30)
print(k)
    