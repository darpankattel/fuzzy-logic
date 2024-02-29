import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create input variables
"""
An Antecedent representa the input variables in a fuzzy logic system.
"""
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

# Create output variable
"""
A Consequent represents the output variable in a fuzzy system.
"""
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define membership functions
"""
trimf generates a triangular membership function.
"""
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['medium'] = fuzz.trimf(temperature.universe, [25, 50, 75])
temperature['high'] = fuzz.trimf(temperature.universe, [50, 100, 100])

humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['medium'] = fuzz.trimf(humidity.universe, [25, 50, 75])
humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Define rules
"""
Rule in a fuzzy system, connecting antecedent(s) to consequent(s).
"""

rule1 = ctrl.Rule(temperature['low'] & humidity['low'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['medium'] &
                  humidity['medium'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['high'] & humidity['high'], fan_speed['high'])

# Define control system and its simulation

fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

# Pass inputs and compute output
fan_sim.input['temperature'] = 40
fan_sim.input['humidity'] = 70
fan_sim.compute()

# Output
print(fan_sim.output['fan_speed'])
