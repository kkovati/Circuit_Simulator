from simulator.circuit import Circuit
from simulator.components import Resistor, Capacitor, OperationalAmplifier
from simulator.measurement import Voltmeter, ISenseResistor
from simulator.sources import SquareWaveSource


circuit = Circuit()  

circuit.add(SquareWaveSource(name='V1', v_hi=10, v_lo=0, t_period=500, 
                             duty_cycle=50, pos='1', neg='GND'))
circuit.add(Resistor(name='R1', r=100, pos='1', neg='2')) 
circuit.add(Resistor(name='R2', r=200, pos='2', neg='3'))
circuit.add(Resistor(name='R3', r=10, pos='3', neg='4'))
circuit.add(Resistor(name='R4', r=100, pos='5', neg='GND'))
circuit.add(Capacitor(name='C1', c=1e-6, pos='4', neg='GND'))
circuit.add(OperationalAmplifier(name='OP_AMP', amp=1000, v_max=50, 
                                 v_min=-50, non_inv='5', inv='2',out='3'))
circuit.add(Voltmeter(name='V_IN', pos='1', neg='GND'))
circuit.add(Voltmeter(name='V_OUT', pos='4', neg='GND'))
circuit.add(ISenseResistor(name='I2', resistor_name='R2')) 

circuit.simulate(simulation_time=1000)
    
    