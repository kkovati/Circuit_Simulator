from simulator.circuit import Circuit
from simulator.components import Resistor, Capacitor
from simulator.measurement import Voltmeter, ISenseResistor
from simulator.sources import DCVoltageSource


c1 = Circuit() 

c1.add(DCVoltageSource(name='V1', v=10, pos='1', neg='GND'))
c1.add(Resistor(name='R1', r=50, pos='1', neg='2')) 
c1.add(Capacitor(name='C1', c=1e-7, pos='2', neg='3'))
c1.add(Resistor(name='R1', r=50, pos='3', neg='GND')) 
c1.add(Voltmeter(name='VM1', pos='1', neg='GND'))
c1.add(Voltmeter(name='VM2', pos='2', neg='GND'))
c1.add(Voltmeter(name='VM3', pos='3', neg='GND'))
c1.add(ISenseResistor(name='I1', resistor_name='R1'))

c1.simulate(simulation_time=100)
    
    