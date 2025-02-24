<img src="https://i.ibb.co/zS1g2ww/header.png" />

<h1 align="center"> <b>Gradient Descent Engine</b></h1>

<p align="center">
        <img src="https://github.com/alii/use-last-fm/workflows/CI/badge.svg" />
        <img src="https://img.shields.io/github/issues/markmusic2727/gradient_decent_engine" />
        <img src="https://img.shields.io/github/forks/markmusic2727/gradient_decent_engine" />
        <img src="https://img.shields.io/github/stars/markmusic2727/gradient_decent_engine" />
        <img src="https://img.shields.io/github/license/markmusic2727/gradient_decent_engine" />
        <img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fmarkmusic2727%2Fgradient_decent_engine" />
</p>

## Structure

Gradient descent is an optimization algorithm used to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In machine learning, we use gradient descent to update the parameters of our model. Parameters refer to coefficients in Linear Regression and weights in neural networks.

## Gradient Descent

What makes gradient descent great is the ability that it has to use one fundemental algorithm that can be applied to a number of different regressions and models. These includes linear regression (optimizing the intercept & slope), logistic regression (optimizing squiggle), t-SNE (optimizing clusters), and much more! It works by taking steps that get closer to the optimal value. What makes it so efficient is the way that it does this. The farther away from the optimal value, the larger the steps. When it gets closer, the steps will become smaller.

### __Example:__

<img src="https://i.ibb.co/BgYL2Cr/gradient-example.png" height="300px" />

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

This is no where near complete and is just a fraction of what you can do with Gradient Descent. Feel free to submit issues or pull request! Contributions are welcome.

Made with ❤️ by __[@markmusic2727](https://twitter.com/MarkMusic2727)__



