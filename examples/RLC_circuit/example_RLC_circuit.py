from simulator.circuit import Circuit
from simulator.components import Resistor, Capacitor, Inductor
from simulator.measurement import Voltmeter, ISenseResistor
from simulator.sources import SquareWaveSource

    
circuit = Circuit()  

circuit.add(SquareWaveSource(name='V1', v_hi=10, v_lo=0, t_period=500, 
                             duty_cycle=50, pos='1', neg='GND'))
circuit.add(Resistor(name='R1', r=3, pos='1', neg='2')) 
circuit.add(Resistor(name='R2', r=50, pos='2', neg='GND'))
circuit.add(Capacitor(name='C1', c=10e-6, pos='2', neg='GND'))
circuit.add(Inductor(name='L1', l=10e-6, pos='2', neg='GND'))
circuit.add(Voltmeter(name='VM1', pos='1', neg='GND'))
circuit.add(Voltmeter(name='VM2', pos='2', neg='GND'))
circuit.add(ISenseResistor(name='I1', resistor_name='R1')) 

circuit.simulate(simulation_time=1000)