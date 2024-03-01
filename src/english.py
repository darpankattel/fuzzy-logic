"""
Fuzzy Logic Recommended Student Learning Levels 
"""
import numpy as np
import matplotlib.pyplot as plt

# Define the universe of discourse
marks_listening = np.arange(0, 17, 1)
marks_vocabulary = np.arange(0, 24, 1)
marks_structure = np.arange(0, 28, 1)
marks_reading = np.arange(0, 32, 1)

# Define triangular membership functions for each category


class Student:
    """
    Represents a student with a name and marks
    """

    def __init__(self, name: str, marks: np.array) -> None:
        self.name = name
        self.marks = marks


class FuzzyVariable:
    def __init__(self, universe=None, label=None):
        self.universe = universe
        self.label = label

    def get_fuzzy_var(self, mark, obj):
        fuzzy_values = [obj._low(mark), obj._medium(
            mark), obj._average(mark), obj._high(mark)]
        return fuzzy_values


class MF:
    """
    A class to represent membership functions for a given category
    Args:
        label (str): The label of the category
        x (np.array): The universe of discourse
        lows (tuple): The low points of the membership function
        mediums (tuple): The medium points of the membership function
        averages (tuple): The average points of the membership function
        highs (tuple): The high points of the membership function
    Returns:
        None
    """

    def __init__(self, label: str, x: np.array, lows: tuple, mediums: tuple, averages: tuple, highs: tuple) -> None:
        self.label = label
        self.x = x
        self.lows = lows
        self.mediums = mediums
        self.averages = averages
        self.highs = highs

    def _low(self, x):
        a, b = self.lows
        if x <= a:
            return (1)
        elif a <= x <= b:
            return ((b-x)/(b-a))
        else:
            return (0)

    def low(self):
        x = self.x
        points = []
        for i in x:
            points.append(self._low(x[i]))
        return np.array(points)

    def _medium(self, x):
        a, b, c = self.mediums
        if x <= a or x > c:
            return (0)
        elif a < x <= b:
            return ((x - a) / (b-a))
        elif b < x <= c:
            return ((c - x) / (c-b))
        else:
            return (0)

    def medium(self):
        x = self.x
        points = []
        for i in x:
            points.append(self._medium(x[i]))
        return np.array(points)

    def _average(self, x):
        a, b, c = self.averages
        if x <= a or x > c:
            return (0)
        elif a < x <= b:
            return ((x - a) / (b-a))
        elif b < x <= c:
            return ((c - x) / (c-b))
        else:
            return (0)

    def average(self):
        x = self.x
        points = []
        for i in x:
            points.append(self._average(x[i]))
        return np.array(points)

    def _high(self, x):
        a, b = self.highs
        if x <= a:
            return (0)
        elif a < x <= b:
            return ((x - a) / (b-a))
        else:
            return (1)

    def high(self):
        x = self.x
        points = []
        for i in x:
            points.append(self._high(x[i]))
        return np.array(points)

    def plot(self):
        x = self.x
        a, b = self.lows


# Plot the membership functions
plt.figure(figsize=(10, 6))

lmf = MF('Listening', marks_listening, (3, 7),
         (5, 8, 10), (8, 12, 14), (12, 15))
vmf = MF("Vocaboalry", marks_vocabulary, (5, 10),
         (7, 12, 15), (12, 18, 21), (19, 22))
smf = MF("Structure", marks_structure, (5, 10),
         (8, 13, 17), (14, 18, 24), (22, 26))
rmf = MF("Reading", marks_reading, (5, 12),
         (9, 14, 19), (16, 22, 26), (23, 28))
# output = MF("output", marks_output, (10, 27), (27, 39, 50), (0, 0), (0, 0))

plt.plot(marks_listening, lmf.low(), label='Low')
plt.plot(marks_listening, lmf.medium(), label='Medium')
plt.plot(marks_listening, lmf.average(), label='Average')
plt.plot(marks_listening, lmf.high(), label='High')

plt.title('Triangular Membership Functions for Listening Test Marks')
plt.xlabel('Marks')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid(True)
# plt.show()

plt.plot(marks_vocabulary, vmf.low(), label='Low')
plt.plot(marks_vocabulary, vmf.medium(), label='Medium')
plt.plot(marks_vocabulary, vmf.average(), label='Average')
plt.plot(marks_vocabulary, vmf.high(), label='High')

plt.title('Triangular Membership Functions for Vocabulary Test Marks')
plt.xlabel('Marks')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid(True)
# plt.show()

plt.plot(marks_structure, smf.low(), label='Low')
plt.plot(marks_structure, smf.medium(), label='Medium')
plt.plot(marks_structure, smf.average(), label='Average')
plt.plot(marks_structure, smf.high(), label='High')

plt.title('Triangular Membership Functions for Structure Test Marks')
plt.xlabel('Marks')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid(True)
# plt.show()

plt.plot(marks_reading, rmf.low(), label='Low')
plt.plot(marks_reading, rmf.medium(), label='Medium')
plt.plot(marks_reading, rmf.average(), label='Average')
plt.plot(marks_reading, rmf.high(), label='High')

plt.title('Triangular Membership Functions for Reading Test Marks')
plt.xlabel('Marks')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid(True)
# plt.show()

# bishnu = Student("Bishnu", np.array([16, 24, 28, 32]))  # ramro
bishnu = Student("Bishnu", np.array([8, 12, 20, 10]))  # ramro
# bishnu = Student("Bishnu", np.array([1, 2, 2, 3]))  # naramro

fuzzy_var_listening = FuzzyVariable(
    universe=marks_listening, label="Listening")
fuzzy_var_vocabulary = FuzzyVariable(
    universe=marks_vocabulary, label="Vocabulary")
fuzzy_var_structure = FuzzyVariable(
    universe=marks_structure, label="Structure")
fuzzy_var_reading = FuzzyVariable(universe=marks_reading, label="Reading")

fuzzy_vars = [fuzzy_var_listening.get_fuzzy_var(bishnu.marks[0], lmf), fuzzy_var_vocabulary.get_fuzzy_var(bishnu.marks[1], vmf), fuzzy_var_structure.get_fuzzy_var(bishnu.marks[2], smf), fuzzy_var_reading.get_fuzzy_var(bishnu.marks[3], rmf)
              ]

print("Fuzzy values for mark", bishnu.name, ":")
print(fuzzy_vars)


def rule(fuzzy_vars):
    list, voca, stru, read = fuzzy_vars


def compare(tc1, tc2):
    tc = 0
    if tc1 > tc2 and tc1 != 0 and tc2 != 0:
        tc = tc2
    else:
        tc = tc1

    if tc1 == 0 and tc2 != 0:
        tc = tc2

    if tc2 == 0 and tc1 != 0:
        tc = tc1

    return tc


def rule(fuzzy_vars):
    list, voca, stru, read = fuzzy_vars
    list_l, list_m, list_a, list_h = list
    voca_l, voca_m, voca_a, voca_h = voca
    stru_l, stru_m, stru_a, stru_h = stru
    read_l, read_m, read_a, read_h = read

    fd_op1 = min(min(min(list_l, voca_l), stru_l), read_l)
    fd_op2 = min(min(min(list_l, voca_l), stru_l), read_m)
    fd_op3 = min(min(min(list_l, voca_l), stru_l), read_a)
    fd_op4 = min(min(min(list_l, voca_l), stru_l), read_h)
    fd_op5 = min(min(min(list_l, voca_l), stru_m), read_l)
    fd_op6 = min(min(min(list_l, voca_l), stru_a), read_l)
    fd_op7 = min(min(min(list_l, voca_l), stru_h), read_l)
    fd_op8 = min(min(min(list_l, voca_m), stru_l), read_l)
    fd_op9 = min(min(min(list_l, voca_a), stru_l), read_l)
    fd_op10 = min(min(min(list_l, voca_h), stru_l), read_l)
    fd_op11 = min(min(min(list_m, voca_l), stru_l), read_l)
    fd_op12 = min(min(min(list_a, voca_l), stru_l), read_l)
    fd_op13 = min(min(min(list_h, voca_l), stru_l), read_l)
    fd_op = compare(compare(compare(compare(compare(compare(compare(compare(compare(compare(compare(compare(
        fd_op1, fd_op2), fd_op3), fd_op4), fd_op5), fd_op6), fd_op7), fd_op8), fd_op9), fd_op10), fd_op11), fd_op12), fd_op13)

    basic_op1 = min(min(min(list_m, voca_m), stru_m), read_l)
    basic_op2 = min(min(min(list_m, voca_m), stru_m), read_m)
    basic_op3 = min(min(min(list_m, voca_m), stru_m), read_a)
    basic_op4 = min(min(min(list_m, voca_m), stru_m), read_h)
    basic_op5 = min(min(min(list_m, voca_m), stru_a), read_l)
    basic_op6 = min(min(min(list_m, voca_m), stru_h), read_m)
    basic_op7 = min(min(min(list_m, voca_h), stru_m), read_m)
    basic_op8 = min(min(min(list_a, voca_m), stru_m), read_m)
    basic_op9 = min(min(min(list_h, voca_m), stru_m), read_m)
    basic_op10 = min(min(min(list_m, voca_a), stru_m), read_m)
    basic_op11 = min(min(min(list_h, voca_l), stru_l), read_h)
    basic_op = compare(compare(compare(compare(compare(compare(compare(compare(compare(compare(basic_op1, basic_op2),
                       basic_op3), basic_op4), basic_op5), basic_op6), basic_op7), basic_op8), basic_op9), basic_op10), basic_op11)

    elem_op1 = min(min(min(list_a, voca_a), stru_a), read_a)
    elem_op2 = min(min(min(list_a, voca_a), stru_a), read_h)
    elem_op3 = min(min(min(list_a, voca_a), stru_h), read_a)
    elem_op4 = min(min(min(list_a, voca_h), stru_a), read_a)
    elem_op5 = min(min(min(list_h, voca_a), stru_a), read_a)
    elem_op6 = min(min(min(list_l, voca_a), stru_a), read_a)
    elem_op = compare(compare(compare(
        compare(compare(elem_op1, elem_op2), elem_op3), elem_op4), elem_op5), elem_op6)

    inter_op1 = min(min(min(list_h, voca_a), stru_a), read_h)
    inter_op2 = min(min(min(list_a, voca_h), stru_h), read_a)
    inter_op3 = min(min(min(list_a, voca_a), stru_h), read_h)
    inter_op4 = min(min(min(list_h, voca_h), stru_a), read_h)
    inter_op = compare(
        compare(compare(inter_op1, inter_op2), inter_op3), inter_op4)

    advanced_op1 = min(min(min(list_h, voca_h), stru_h), read_a)
    advanced_op2 = min(min(min(list_h, voca_h), stru_h), read_h)
    advanced_op = compare(advanced_op1, advanced_op2)

    return fd_op, basic_op, elem_op, inter_op, advanced_op


fd_op, basic_op, elem_op, inter_op, advanced_op = rule(fuzzy_vars)

# De-fuzzyfication


def area_tr(mu, a, b, c):
    x1 = mu * (b - a) + a
    x2 = c - mu * (c - b)
    d1 = (c - a)
    d2 = x2 - x1
    a_tr = (1 / 2) * mu * (d1 + d2)
    return a_tr  # Returning area


def area_ol(mu, alpha, beta):
    x_ol = beta - mu * (beta - alpha)
    return 1 / 2 * mu * (beta + x_ol), beta / 2


def area_or(mu, alpha, beta):
    x_or = (beta - alpha) * mu + alpha
    a_or = (1 / 2) * mu * ((100 - alpha) + (100 - x_or))
    return a_or, (100 - alpha) / 2 + alpha


def defuzzification(fd_op, basic_op, elem_op, inter_op, advanced_op):
    area_pl = 0
    area_pm = 0
    area_ps = 0
    area_ns = 0
    area_nl = 0
    c_fd = 0
    c_basic = 0
    c_elem = 0
    c_inter = 0
    c_advanced = 0

    if fd_op != 0:
        area_pl, c_fd = area_ol(fd_op, 10, 27)

    if basic_op != 0:
        area_pm = area_tr(basic_op, 27, 39, 50)
        c_basic = 39

    if elem_op != 0:
        area_ps = area_tr(elem_op, 50, 60, 70)
        c_elem = 60

    if inter_op != 0:
        area_ns = area_tr(inter_op, 70, 80, 90)
        c_inter = 80

    if advanced_op != 0:
        area_nl, c_advanced = area_or(advanced_op, 90, 95)

    numerator = area_pl * c_fd + area_pm * c_basic + area_ps * \
        c_elem + area_ns * c_inter + area_nl * c_advanced
    denominator = area_pl + area_pm + area_ps + area_ns + area_nl
    if denominator == 0:
        print("No rules exist to give the result")
        return 0
    else:
        crisp_output = numerator / denominator
        return crisp_output


crisp_output_final = defuzzification(
    fd_op, basic_op, elem_op, inter_op, advanced_op)

if crisp_output_final != 0:
    print("\nThe crisp output value is: ", crisp_output_final)
