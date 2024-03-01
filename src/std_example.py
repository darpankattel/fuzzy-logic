"""
CSV Headers:    No,1,2,3,4,Learning Level
Example Value:  1,16,24,28,32,ADVANCE
Mappings:       1 = Listening
                2 = Vocabulary
                3 = Structure
                4 = Reading
"""
import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Read the dataset
df = pd.read_csv('data/dataset.csv')

# Define input variables
listening = ctrl.Antecedent(np.arange(0, 17, 1), 'listening')
vocabulary = ctrl.Antecedent(np.arange(0, 25, 1), 'vocabulary')
structure = ctrl.Antecedent(np.arange(0, 29, 1), 'structure')
reading = ctrl.Antecedent(np.arange(0, 33, 1), 'reading')

# Define output variable
learning_level = ctrl.Consequent(np.arange(0, 101, 1), 'learning_level')

# Define membership functions for input variables
listening['low'] = fuzz.trimf(listening.universe, [0, 5, 7])
listening['medium'] = fuzz.trimf(listening.universe, [5, 7, 10])
listening['average'] = fuzz.trimf(listening.universe, [8, 10, 12])
listening['high'] = fuzz.trimf(listening.universe, [12, 14, 16])
listening.view()

vocabulary['low'] = fuzz.trimf(vocabulary.universe, [0, 7, 10])
vocabulary['medium'] = fuzz.trimf(vocabulary.universe, [7, 10, 15])
vocabulary['average'] = fuzz.trimf(vocabulary.universe, [12, 15, 21])
vocabulary['high'] = fuzz.trimf(vocabulary.universe, [19, 21, 24])

structure['low'] = fuzz.trimf(structure.universe, [0, 8, 10])
structure['medium'] = fuzz.trimf(structure.universe, [8, 10, 17])
structure['average'] = fuzz.trimf(structure.universe, [14, 17, 24])
structure['high'] = fuzz.trimf(structure.universe, [22, 24, 28])

reading['low'] = fuzz.trimf(reading.universe, [0, 9, 12])
reading['medium'] = fuzz.trimf(reading.universe, [9, 12, 19])
reading['average'] = fuzz.trimf(reading.universe, [16, 19, 26])
reading['high'] = fuzz.trimf(reading.universe, [23, 26, 32])

# Define membership functions for output variable
learning_level['foundation'] = fuzz.trimf(learning_level.universe, [0, 10, 27])
learning_level['basic'] = fuzz.trimf(learning_level.universe, [27, 38.5, 50])
learning_level['elementary'] = fuzz.trimf(
    learning_level.universe, [50, 60, 70])
learning_level['intermediate'] = fuzz.trimf(
    learning_level.universe, [70, 80, 90])
learning_level['advanced'] = fuzz.trimf(
    learning_level.universe, [90, 95, 100])

# Define rules
# Rule 1
rule1 = ctrl.Rule(listening['low'] & vocabulary['low'] &
                  structure['low'] & reading['low'], learning_level['foundation'])

# Rule 2
rule2 = ctrl.Rule(listening['low'] & vocabulary['low'] &
                  structure['low'] & reading['medium'], learning_level['foundation'])

# Rule 3
rule3 = ctrl.Rule(listening['low'] & vocabulary['low'] &
                  structure['low'] & reading['average'], learning_level['foundation'])

# Rule 4
rule4 = ctrl.Rule(listening['low'] & vocabulary['low'] &
                  structure['low'] & reading['high'], learning_level['foundation'])

# Rule 5
rule5 = ctrl.Rule(listening['low'] & vocabulary['low'] &
                  structure['medium'] & reading['low'], learning_level['foundation'])

# Rule 6
rule6 = ctrl.Rule(listening['low'] & vocabulary['low'] &
                  structure['average'] & reading['low'], learning_level['foundation'])

# Rule 7
rule7 = ctrl.Rule(listening['low'] & vocabulary['low'] &
                  structure['high'] & reading['low'], learning_level['foundation'])

# Rule 8
rule8 = ctrl.Rule(listening['low'] & vocabulary['medium'] &
                  structure['low'] & reading['low'], learning_level['foundation'])

# Rule 9
rule9 = ctrl.Rule(listening['low'] & vocabulary['average'] &
                  structure['low'] & reading['low'], learning_level['foundation'])

# Rule 10
rule10 = ctrl.Rule(listening['low'] & vocabulary['high'] &
                   structure['low'] & reading['low'], learning_level['foundation'])

# Rule 11
rule11 = ctrl.Rule(listening['medium'] & vocabulary['low'] &
                   structure['low'] & reading['low'], learning_level['foundation'])

# Rule 12
rule12 = ctrl.Rule(listening['average'] & vocabulary['low'] &
                   structure['low'] & reading['low'], learning_level['foundation'])

# Rule 13
rule13 = ctrl.Rule(listening['high'] & vocabulary['low'] &
                   structure['low'] & reading['low'], learning_level['foundation'])

# Rule 14
rule14 = ctrl.Rule(listening['medium'] & vocabulary['medium'] &
                   structure['medium'] & reading['low'], learning_level['basic'])

# Rule 15
rule15 = ctrl.Rule(listening['medium'] & vocabulary['medium'] &
                   structure['medium'] & reading['medium'], learning_level['basic'])

# Rule 16
rule16 = ctrl.Rule(listening['medium'] & vocabulary['medium'] &
                   structure['medium'] & reading['average'], learning_level['basic'])

# Rule 17
rule17 = ctrl.Rule(listening['medium'] & vocabulary['medium'] &
                   structure['medium'] & reading['high'], learning_level['basic'])

# Rule 18
rule18 = ctrl.Rule(listening['medium'] & vocabulary['medium'] &
                   structure['average'] & reading['low'], learning_level['basic'])

# Rule 19
rule19 = ctrl.Rule(listening['medium'] & vocabulary['medium'] &
                   structure['high'] & reading['medium'], learning_level['basic'])

# Rule 20
rule20 = ctrl.Rule(listening['medium'] & vocabulary['high'] &
                   structure['medium'] & reading['medium'], learning_level['basic'])

# Rule 21
rule21 = ctrl.Rule(listening['average'] & vocabulary['medium'] &
                   structure['medium'] & reading['medium'], learning_level['basic'])

# Rule 22
rule22 = ctrl.Rule(listening['high'] & vocabulary['medium'] &
                   structure['medium'] & reading['medium'], learning_level['basic'])

# Rule 23
rule23 = ctrl.Rule(listening['medium'] & vocabulary['average'] &
                   structure['medium'] & reading['medium'], learning_level['basic'])

# Rule 24
rule24 = ctrl.Rule(listening['average'] & vocabulary['average'] &
                   structure['average'] & reading['average'], learning_level['elementary'])

# Rule 25
rule25 = ctrl.Rule(listening['average'] & vocabulary['average'] &
                   structure['average'] & reading['high'], learning_level['elementary'])

# Rule 26
rule26 = ctrl.Rule(listening['average'] & vocabulary['average'] &
                   structure['high'] & reading['average'], learning_level['elementary'])

# Rule 27
rule27 = ctrl.Rule(listening['average'] & vocabulary['high'] &
                   structure['average'] & reading['average'], learning_level['elementary'])

# Rule 28
rule28 = ctrl.Rule(listening['high'] & vocabulary['average'] &
                   structure['average'] & reading['average'], learning_level['elementary'])

# Rule 29
rule29 = ctrl.Rule(listening['high'] & vocabulary['average'] &
                   structure['average'] & reading['high'], learning_level['intermediate'])

# Rule 30
rule30 = ctrl.Rule(listening['average'] & vocabulary['high'] &
                   structure['high'] & reading['average'], learning_level['intermediate'])

# Rule 31
rule31 = ctrl.Rule(listening['average'] & vocabulary['average'] &
                   structure['high'] & reading['high'], learning_level['intermediate'])

# Rule 32
rule32 = ctrl.Rule(listening['high'] & vocabulary['high'] &
                   structure['average'] & reading['high'], learning_level['intermediate'])

# Rule 33
rule33 = ctrl.Rule(listening['low'] & vocabulary['high'] &
                   structure['high'] & reading['high'], learning_level['elementary'])

# Rule 34
rule34 = ctrl.Rule(listening['high'] & vocabulary['low'] &
                   structure['low'] & reading['high'], learning_level['basic'])

# Rule 35
rule35 = ctrl.Rule(listening['high'] & vocabulary['high'] &
                   structure['high'] & reading['average'], learning_level['advanced'])

# Rule 36
rule36 = ctrl.Rule(listening['high'] & vocabulary['high'] &
                   structure['high'] & reading['high'], learning_level['advanced'])


# Define control system
# learning_level_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16,
#                                          rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36])
# learning_level_sim = ctrl.ControlSystemSimulation(learning_level_ctrl)

# # Iterate over dataset rows and determine learning level
# learning_levels = []
# for index, row in df.iterrows():
#     learning_level_sim.input['listening'] = row['1']
#     learning_level_sim.input['vocabulary'] = row['2']
#     learning_level_sim.input['structure'] = row['3']
#     learning_level_sim.input['reading'] = row['4']

#     learning_level_sim.compute()
#     learning_level_value = learning_level_sim.output['learning_level']
#     learning_levels.append(learning_level_value)

# df['Learning Level'] = learning_levels

# # Save results to a new CSV file
# df.to_csv('data/output_dataset.csv', index=False)
input("")
