from simulator.circuit import Circuit
from simulator.components import Resistor, Capacitor, Inductor, OperationalAmplifier
from simulator.measurement import Voltmeter, ISenseResistor
from simulator.sources import DCCurrentSource


c = Circuit()        

c.add(DCCurrentSource(name='I1', i=1, pos='1', neg='GND'))
c.add(Resistor(name='R1', r=100, pos='1', neg='2')) 
c.add(Resistor(name='R2', r=100, pos='2', neg='GND'))
c.add(Voltmeter(name='VM1', pos='1', neg='GND'))
c.add(Voltmeter(name='VM2', pos='2', neg='GND'))
c.add(ISenseResistor(name='I1', resistor_name='R1'))

c.simulate(simulation_time=50)

