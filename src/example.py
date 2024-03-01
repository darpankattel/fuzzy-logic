# main.py
from src.fuzzy import FuzzySystem


class Example:
    def run(self):
        # Define fuzzy rules, variables, and system
        rules = []  # List of fuzzy rules
        fuzzy_system = FuzzySystem(rules)

        # Define input values (temperature and humidity)
        inputs = {'temperature': 40, 'humidity': 70}

        # Compute the output (fan speed) using the fuzzy system
        output = fuzzy_system.compute_output(inputs)

        print("Computed fan speed:", output)
