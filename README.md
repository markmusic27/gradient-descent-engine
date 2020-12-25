# 🏒 Gradient Decent Engine

## Structure

Gradient descent is an optimization algorithm used to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In machine learning, we use gradient descent to update the parameters of our model. Parameters refer to coefficients in Linear Regression and weights in neural networks.

## Gradient Decent

___

### __Example:__

## Algorithm Snippet

Here's a small snippet of the algorithm that loads the essential values that are then used to train the engine.

```py
def generate(self):
        # Initializes Dataset / Declares Variables
        df = pd.read_csv(self.dataset)
        self.intercept = 0
        pairs = []

        for i in range(len(df[self.x])):
            pairs.append({"x": df[self.x][i], "y": df[self.y][i]})

        for pair in pairs:
            self.equations.append(
                {Equation.oyv: pair["y"], Equation.inter: self.intercept, Equation.sl: self.slope, Equation.x: pair["x"]})
```

This is no where near complete and is just a fraction and small piece of what you can do with Gradient Decent. Feel free to submit issues or pull request! Contributions are welcome.

Made with ❤️ by __[@markmusic2727](https://twitter.com/MarkMusic2727)__



