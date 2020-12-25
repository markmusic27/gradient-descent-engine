import random
import enum
import pandas as pd


class Variable(enum.Enum):
    intercept = 0
    slope = 1


class GradientDecentEngine:
    equations = []

    def __init__(self, learning_rate, loops, dataset, variable, slope, intercept, x, y):
        self.learning_rate = learning_rate
        self.loops = loops
        self.dataset = dataset
        self.variable = variable
        self.intercept = intercept
        self.slope = slope
        self.x = x
        self.y = y

    def generateEquations(self):
        # Initializes Dataset / Declares Variables
        df = pd.read_csv(self.dataset)
        self.intercept = random.randint(0, 5)
        pairs = []

        xls = df[self.x]
        yls = df[self.y]

        # Finds X, Y pairs in data

        for i in range(xls.value_counts()):
            pairs.append([{"x": xls[i], "y": yls[i]}])

        # Generates Equation

        for i in pairs:
            print(pairs)

    def loss(self):
        print("hello World")
