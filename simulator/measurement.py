from .components import Component


class MeasuringInstrument:
    
    def __init__(self, measurement_type):
        """
        Initializes an empty list of measurements
        measurement_type : str - 'V' for voltage, 'I' for current
        """
        self.measurements = []
        self.measurement_type = measurement_type 
        
    def set_measured_component(self, components):
        # left empty on purpose, child class must overwrite
        pass
        
    def get_measurements(self):
        return self.measurements


class Voltmeter(Component, MeasuringInstrument):
    
    def __init__(self, name, pos, neg):
        """
        name : str - name of component, this name will be used on the legend 
                    of the measurement result chart
        resistor_name : str - name of measured resistor
        pos : str - junction name connected to positive pin
        neg : str - junction name connected to negative pin
        """
        Component.__init__(self, name, pos=pos, neg=neg)
        MeasuringInstrument.__init__(self, measurement_type='V')        
        
    def simulation_step(self):        
        """Single measurement"""        
        self.measurements.append(self.pos.v - self.neg.v) 
        
        
class VSenseResistor(MeasuringInstrument):
    """Measures voltage on a resistor"""  
    
    def __init__(self, name, resistor_name):
        """
        name : str - name of component, this name will be used on the legend 
                    of the measurement result chart
        resistor_name : str - name of measured resistor
        """
        MeasuringInstrument.__init__(self, measurement_type='V')
        self.name = name
        self.resistor_name = resistor_name 
        
    #override 
    def set_measured_component(self, components):
        """
        Chooses and saves the appropriate component from the component list to 
        measure
        components : list - list of components
        """
        for component in components:
            if component.name == self.resistor_name:
                self.resistor = component
        
    def simulation_step(self): 
        """Single measurement"""
        self.measurements.append(self.resistor.pos.v - self.resistor.neg.v)
                
class _Ammeter(Component, MeasuringInstrument):
    """IMPLEMENTATION IS NOT READY!"""
    
    def __init__(self, name, pos, neg):
        """NOT READY"""
        Component.__init__(self, name, pos=pos, neg=neg)
        MeasuringInstrument.__init__(self, measurement_type='I')
        
    def simulation_step(self):
        """NOT READY"""
        pass
        
class ISenseResistor(MeasuringInstrument):
    """Measures current through a resistor"""
    
    def __init__(self, name, resistor_name):
        """
        name : str - name of component, this name will be used on the legend 
                    of the measurement result chart
        resistor_name : str - name of measured resistor
        """
        MeasuringInstrument.__init__(self, measurement_type='I')
        self.name = name
        self.resistor_name = resistor_name
        
    #override 
    def set_measured_component(self, components):
        """
        Chooses and saves the appropriate component from the component list to 
        measure
        components : list - list of components
        """
        for component in components:
            if component.name == self.resistor_name:
                self.resistor = component
        
    def simulation_step(self): 
        """Single measurement"""
        self.measurements.append(self.resistor.i)
        

        
        
        
