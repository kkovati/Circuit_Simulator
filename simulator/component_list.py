from .components import (Component, Resistor, Capacitor, Inductor, 
                        OperationalAmplifier)
from .measurement import MeasuringInstrument
from .sources import Source


class ComponentList:
    """Sorting and handling different types of component"""
    
    def __init__(self):
        self.components = []
        self.sources = []
        self.measuring_instruments = []
        self.resistors = []
        self.capacitors = []
        self.inductors = []
        self.amplifiers = []
        
    def add(self, component):
        if Component in component.__class__.__bases__:
            self.components.append(component)
            
        if Source in component.__class__.__bases__:
            self.sources.append(component)
            
        if MeasuringInstrument in component.__class__.__bases__:
            self.measuring_instruments.append(component)
            
        if Resistor is component.__class__:
            self.resistors.append(component)
        
        if Capacitor is component.__class__:
            self.capacitors.append(component)
            
        if Inductor is component.__class__:
            self.inductors.append(component)
            
        if OperationalAmplifier is component.__class__:
            self.amplifiers.append(component)
            