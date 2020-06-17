import matplotlib.pyplot as plt
import numpy as np
from .component_list import ComponentList
from .junction import Junction
from .misc import LoadingBar
from .simulation_settings import DELTA_TIME


class Circuit:
    """Model of an electrical circuit"""
    
    def __init__(self):
        self.comp_list = ComponentList()
    
    def add(self, component):
        """
        Adds a component, source or measuring instrument to the ciruit's 
        component list
        component : child class of Component, Source or MeasuringInstrument
        """
        self.comp_list.add(component)
     
    def simulate(self, simulation_time):
        """
        Starts simlation and plots measuremnt results
        simulation_time : float - simulation time length in usec
        """
        self.connect_circuit()
        self.init_measuring_instruments()
        
        time = np.arange(simulation_time * 1e-6, step=DELTA_TIME) 
        lb = LoadingBar(len(time), 'Simulation')
        for t in time:
            self.simulation_step(t)
            lb()
            
        self.plot_measurements(time)
        
    def connect_circuit(self):
        """Initialize junctions and connects components to junctions"""
        
        self.junctions = {}        
        for component in self.comp_list.components:
            for junction_name in component.get_junction_names():
                if not junction_name in self.junctions:
                    self.junctions[junction_name] = Junction(junction_name)                    
        
        for component in self.comp_list.components:
            component.connect(self.junctions)
            
    def init_measuring_instruments(self):                
        for mi in self.comp_list.measuring_instruments:
            mi.set_measured_component(self.comp_list.components)                
                    
    def simulation_step(self, time):
        """
        Single step of simulation. All components modify its' internal 
        values and effect their connected junctions
        """
        # reset junction currents to zero
        for j in self.junctions.values():
            j.reset_current()
        
        # voltage sources set voltages, current sources set currents
        for s in self.comp_list.sources:
            s.simulation_step(time)
         
        # amplifier sources set voltages
        for a in self.comp_list.amplifiers:
            a.simulation_step()
          
        # resistors set junction currents
        for r in self.comp_list.resistors:
            r.simulation_step() 
            
        # set inductor currents according to junction voltages
        for i in self.comp_list.inductors:
            i.simulation_step()  
            
        # set capacitor voltages according to junction currents
        for c in self.comp_list.capacitors:
            c.simulation_step()  
        
        # measurements recorded
        for mi in self.comp_list.measuring_instruments:
            mi.simulation_step()
         
        # voltage sources provide the current difference of junctions
        for s in self.comp_list.sources:
            s.reset_current()
          
        # amplifiers' output provide the current difference of junctions
        for a in self.comp_list.amplifiers:
            a.reset_current()
            
        # set junction voltages according to current
        for junction in self.junctions.values():
            junction.simulation_step()
        
    def plot_measurements(self, time):
        """Plots voltage and current measurement results"""
        
        time = np.divide(time, 1e-6)
        # plt.figure(dpi=300) # for high resolution graphs
        
        plt.subplot(2, 1, 1)
        plt.title('Measurements')
        plt.xlabel('time [usec]')
        plt.ylabel('voltage [V]')
        for mi in self.comp_list.measuring_instruments:
            if mi.measurement_type == 'V':        
                plt.plot(time, mi.get_measurements(), label=mi.name)
        plt.legend()
        
        plt.subplot(2, 1, 2)
        plt.xlabel('time [usec]')
        plt.ylabel('current [A]')
        for mi in self.comp_list.measuring_instruments:
            if mi.measurement_type == 'I':
                plt.plot(time, mi.get_measurements(), label=mi.name)
        plt.legend()
        plt.gcf().align_ylabels()               
        
        plt.show()   

        
                
            