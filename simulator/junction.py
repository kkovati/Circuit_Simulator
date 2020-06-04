from .simulation_settings import DELTA_TIME, C_JUNCTION


class Junction: 
    """
    Model of a junction 
    Represents an equipotential electrical wire with no resistance, but
    with parasitic capacitance
    """    
    
    def __init__(self, name):
        self.name = name
        self.v = 0
        self.i = 0
        
    def set_voltage(self, v):
        self.v = v
        
    def reset_current(self):        
        self.i = 0
        
    def add_current(self, i):
        """
        Net current flows in and out from the junction
        Current which flows out from the junction is positive
        """
        self.i += i
        
    def simulation_step(self):
        """
        Updates it's voltage according to the following equatation:
        I = C * dV / dt
        """    
        dv = -self.i * DELTA_TIME / C_JUNCTION        
        self.v += dv
        
            

        
        
