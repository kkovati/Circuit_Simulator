from simulator.circuit import Circuit
from simulator.components import Resistor, Capacitor, Inductor, OperationalAmplifier
from simulator.measurement import Voltmeter, ISenseResistor
from simulator.sources import SquareWaveSource


c = Circuit() 

c.add(SquareWaveSource(name='V1', v_hi=10, v_lo=2, t_period=20, 
                             duty_cycle=80, pos='1', neg='GND'))
c.add(Resistor(name='R1', r=100, pos='1', neg='2')) 
c.add(Resistor(name='R2', r=50, pos='2', neg='3'))
c.add(Resistor(name='R3', r=100, pos='3', neg='GND'))
c.add(OperationalAmplifier(name='OP_AMP', amp=1000, v_max=50, v_min=-50, 
                           non_inv='GND', inv='2', out='3'))
c.add(Voltmeter(name='VM1', pos='1', neg='GND'))
c.add(Voltmeter(name='VM2', pos='2', neg='GND'))
c.add(Voltmeter(name='VM3', pos='3', neg='GND'))
c.add(ISenseResistor(name='I1', resistor_name='R1'))

c.simulate(simulation_time=60)
    