from simulator.circuit import Circuit
from simulator.components import Resistor
from simulator.measurement import Voltmeter, VSenseResistor, ISenseResistor
from simulator.sources import ACVoltageSource


c = Circuit()        

c.add(ACVoltageSource(name='V1', v_rms=3, t_period=50, dc=5, pos='1', 
                      neg='GND'))
c.add(Resistor(name='R1', r=100, pos='1', neg='2')) 
c.add(Resistor(name='R2', r=100, pos='2', neg='GND'))
c.add(Voltmeter(name='VM1', pos='1', neg='GND'))
c.add(VSenseResistor(name='VR1', resistor_name='R1'))
c.add(Voltmeter(name='VM2', pos='2', neg='GND'))
c.add(VSenseResistor(name='VR2', resistor_name='R2'))
c.add(ISenseResistor(name='I1', resistor_name='R1'))

c.simulate(simulation_time=100)