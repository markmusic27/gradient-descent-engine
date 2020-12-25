import random
import enum
import pandas as pd


class Variable(enum.Enum):
    intercept = 0
    slope = 1


class Equation(enum.Enum):
    oyv = 0
    inter = 1
    sl = 2
    x = 3


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

    def generate(self):
        # Initializes Dataset / Declares Variables
        df = pd.read_csv(self.dataset)
        self.intercept = random.randint(0, 100)
        pairs = []

        # Finds X, Y pairs in data

        for i in range(len(df[self.x])):
            pairs.append({"x": df[self.x][i], "y": df[self.y][i]})

        # Generates Equation

        for pair in pairs:
            self.equations.append(
                {Equation.oyv: pair["y"], Equation.inter: self.intercept, Equation.sl: self.slope, Equation.x: pair["x"]})

    def train(self):
        eq = self.equations[0]
        sl = 0
        for _ in range(self.loops):
            sl = eq[Equation.sl] * eq[Equation.x]
            sl = self.intercept + sl
            sl = eq[Equation.oyv] - sl
            sl = sl * 2

        print(sl)


eng = GradientDecentEngine(0.1, 1000, "example.csv", Variable.intercept,
                           0.64, 0, "Years Experience", "Previous employers")

eng.generate()

eng.train()
