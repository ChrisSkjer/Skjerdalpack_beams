from formulas import I_rect, W_pl_rect, W_el_rect

class Rect_profile:
    def __init__(self, hight:float, width:float) -> None:
        self.hight = hight
        self.width = width
    
    def get_Iy(self):
        return I_rect(self.hight, self.width)
        
    def get_Ix(self):
        return I_rect(self.width, self.hight) 
    
    def get_Wy_pl(self):
        return W_pl_rect(self.hight, self.width)

    def get_Wy_el(self):
        return W_el_rect(self.hight, self.width)
    
    def get_Wx_pl(self):
        return W_pl_rect(self.width, self.hight)
        
    def get_Wx_el(self):
        return W_el_rect(self.width, self.hight)
        
        
class H_profile:
    def __init__(self) -> None:
        pass
