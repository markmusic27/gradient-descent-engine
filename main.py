import random
import enum
import pandas as pd


class Equation(enum.Enum):
    oyv = 0
    inter = 1
    sl = 2
    x = 3


class GradientDecentEngine:
    equations = []

    def __init__(self, learning_rate, dataset, slope, intercept, x, y):
        self.learning_rate = learning_rate
        self.dataset = dataset
        self.intercept = intercept
        self.slope = slope
        self.x = x
        self.y = y

    def generate(self):
        df = pd.read_csv(self.dataset)
        self.intercept = 0
        pairs = []

        for i in range(len(df[self.x])):
            pairs.append({"x": df[self.x][i], "y": df[self.y][i]})

        for pair in pairs:
            self.equations.append(
                {Equation.oyv: pair["y"], Equation.inter: self.intercept, Equation.sl: self.slope, Equation.x: pair["x"]})

    def train(self):
        eq = self.equations[0]
        sl = 0
        for _ in range(40):
            sl = eq[Equation.sl] * eq[Equation.x]
            sl = self.intercept + sl
            sl = eq[Equation.oyv] - sl
            sl = sl * -2

            ss = sl * self.learning_rate
            self.intercept = self.intercept - ss


eng = GradientDecentEngine(0.1, "example.csv",
                           0.64, 0, "Years Experience", "Previous employers")

eng.generate()

eng.train()
