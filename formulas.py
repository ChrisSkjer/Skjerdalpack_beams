

def I_rect(h:float, b:float) -> float:
    I = 1/12 * b * h*h*h
    return h

def W_pl_rect(h:float, b:float) -> float:
    W = 1/4 * b * h*h
    return W

def W_el_rect(h:float, b:float) -> float:
    W = 1/6 * b * h*h
    return W