# ⚡ Circuit Simulator
This tool is a time domain electrical circuit simulator written in **Python**.
It's main purpose is transient analysis of circuits containing basic components.<br> 
The simulator relies only on **NumPy**.<br> 
All simulation results were verified with **NI Multisim 10**.

Available components:
 - Resistor
 - Capacitor
 - Inductor
 - Operational amplifier
 
Sources:
 - DC voltage, DC current
 - AC voltage
 - Square wave

### Usage
Requires Python 3.7+ and dependencies from requirements.txt.<br>
```pip install -r requirements.txt```

## Examples

Check out more sample circuits [here](https://github.com/kkovati/Circuit_Simulator/tree/master/test).

### RLC Circuit

[This example](https://github.com/kkovati/Circuit_Simulator/blob/master/examples/RLC_circuit/example_RLC_circuit.py)
shows the simulation of the following RLC circuit.<br/> 
(This schematic diagram is made with NI Multisim, not with this Circuit Simulator tool.)

![RLC circuit](https://github.com/kkovati/Circuit_Simulator/blob/master/examples/RLC_circuit/RLC_circuit.png?raw=true)

The following code describes this RLC circuit and the simulation process, as the input for the program:
 - instantiate a circuit
 - instantiate components by defining names, electrical and functional parameters and connections
 - add the components to the circuit using `.add()`
 - start simulation with `.simulate()`
 
(Using GND is not necessary, see Hints)

```python
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
```

The next diagram is the output of the simulation, the measurement results.<br/> 
See the RLC oscillation at VM2 and I1.

![RLC results](https://github.com/kkovati/Circuit_Simulator/blob/master/examples/RLC_circuit/RLC_sim_results.png?raw=true)

### Inverting Operational Amplifier
 
[This example](https://github.com/kkovati/Circuit_Simulator/blob/master/examples/OpAmp_inverter/example_OpAmp_inverter.py) 
is an operational amplifier in inverting mode with a capacitor on its output. 
    
![OpAmp_inverter](https://github.com/kkovati/Circuit_Simulator/blob/master/examples/OpAmp_inverter/OpAmp_inverter.png?raw=true)

Define this circuit and run the simulation:

```python
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
```

Measurement results of the simulation. The output voltage is amplfied and inverted
(A = R2 / R1), and the capacitor charging can be observed at input switching. 

![OpAmp_inv_results](https://github.com/kkovati/Circuit_Simulator/blob/master/examples/OpAmp_inverter/OpAmp_results.png?raw=true)

### Operational Amplifier Switching Transient

[This example](https://github.com/kkovati/Circuit_Simulator/blob/master/examples/OpAmp_switching_transient/example_OpAmp_switching_transient.py)
is nearly the same circuit as in the former example without the capacitor on the 
amplifier's output and with a different, higher frequency input:

```python
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
```

Simulation produces the following results. Because of the smaller time scale
the switching transients of the amplifier and the virtual ground's voltage can be seen 
on the graph.

![OpAmp_switch_transient_results](https://github.com/kkovati/Circuit_Simulator/blob/master/examples/OpAmp_switching_transient/OpAmp_switching_transient_results.png?raw=true)
    
## Hints

Don't connect multiple capacitors directly into the same junction, use a small 
resistance between its pins.

Try to avoid using inductors under 10uH (when C_JUNCTION = 1e-9), else it will 
oscillate because of the junctions' parasitic capacitance. 
Alternatively use smaller C_JUNCTION but in parallel decrease the DELTA_TIME 
(Simulation step time interval) also.

Using GND signal (component) in not always necessary. If a junction is 
connected only to the 'neg' pins of sources, resistors and capacitors 
(and connected to at least to one source through its 'neg' pin), 
then it will remain at zero potential, thus becomes ground.

## Known Errors

A capacitor must be connected with correct polarity and the negative pin 
must be connected to GND or the junction which refers as ground (see Hints).






