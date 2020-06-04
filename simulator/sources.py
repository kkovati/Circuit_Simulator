import math
from .components import Component


class Source():
    """Base model of voltage and current sources"""
    
    def reset_current(self):
        self.pos.reset_current()
        self.neg.reset_current()
        
        
class DCVoltageSource(Component, Source):
    """Constant voltage source"""
    
    def __init__(self, name, v, pos, neg):
        """
        name : str - name of source
        v : float - output voltage value
        pos : str - junction name connected to positive pin
        neg : str - junction name connected to negative pin
        """
        Component.__init__(self, name, pos=pos, neg=neg)
        self.v = v
        
    def simulation_step(self, *args):
        """Outputs constant voltage"""
        self.pos.set_voltage(self.neg.v + self.v)    


class SquareWaveSource(Component, Source):
    "Square wave source with configurable duty cycle"
    
    def __init__(self, name, v_hi, v_lo, t_period, duty_cycle, pos, neg):
        """
        name : str - name of source
        v_hi : float - output voltage high value
        v_lo : float - output voltage low value
        t_period : float - period time of a cycle in usec
        duty_cycle : float - ratio in percentage of high and low voltage 
                            signal during one cycle in percentage
        pos : str - junction name connected to positive pin
        neg : str - junction name connected to negative pin
        """
        Component.__init__(self, name, pos=pos, neg=neg)
        self.v_hi = v_hi
        self.v_lo = v_lo
        self.t_period = t_period * 1e-6
        self.duty_cycle = duty_cycle / 100
        
    def simulation_step(self, time):
        if time % self.t_period <= self.t_period * self.duty_cycle:
            v = self.v_hi  
        else:
            v = self.v_lo
        self.pos.set_voltage(self.neg.v + v)
        
        
class ACVoltageSource(Component, Source):
    """Sinusoidal voltage source with DC bias"""
    
    def __init__(self, name, v_rms, t_period, dc, pos, neg):
        """
        name : str - name of source
        v_rms : float - output voltage root mean square value
        t_period : float - period time of a cycle in usec
        dc : float - DC bias voltage of output signal
        pos : str - junction name connected to positive pin
        neg : str - junction name connected to negative pin
        """
        Component.__init__(self, name, pos=pos, neg=neg)
        self.v_rms = v_rms
        self.t_period = t_period * 1e-6
        self.dc = dc
    
    def simulation_step(self, time):
        v = math.sin((time % self.t_period) * 2 * math.pi / self.t_period)
        v *= self.v_rms
        v += self.dc
        self.pos.set_voltage(self.neg.v + v)
        
        
class DCCurrentSource(Component, Source):
    """Constant current source"""
    
    def __init__(self, name, i, pos, neg):
        """
        name : str - name of source
        i : float - output current value
        pos : str - junction name connected to positive pin
        neg : str - junction name connected to negative pin
        """
        Component.__init__(self, name, pos=pos, neg=neg)
        self.i = i
        
    def simulation_step(self, *args):
        """Outputs constant current"""
        self.pos.add_current(-self.i)
        self.neg.add_current(self.i)
    
    # overwrite
    def reset_current(self):
        """
        Current source must not supply current the way voltage sources do,
        therefore this function is overwritten and left empty
        """        
        pass


class GND(Component, Source):
    """Ground"""
    
    def __init__(self, name, gnd):
        Component.__init__(self, name, gnd=gnd)
        
    def simulation_step(self, *args):
        self.gnd.set_voltage(0)  
        
    def reset_current(self):
        self.gnd.reset_current()
    