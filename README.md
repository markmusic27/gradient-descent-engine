<img src="https://i.ibb.co/zS1g2ww/header.png" />

<h1 align="center"> <b>Gradient Decent Engine</b>
<img src="https://github.com/alii/use-last-fm/workflows/CI/badge.svg" />
</h1>

## Structure

Gradient descent is an optimization algorithm used to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In machine learning, we use gradient descent to update the parameters of our model. Parameters refer to coefficients in Linear Regression and weights in neural networks.

## Gradient Decent

What makes gradient decent great is the ability that it has to use one fundemental algorithm that can be applied to a number of different regressions and models. These includes linear regression (optimizing the intercept & slope), logistic regression (optimizing squiggle), t-SNE (optimizing clusters), and much more! It works by taking steps that get closer to the optimal value. What makes it so efficient is the way that it does this. The farther away from the optimal value, the larger the steps. When it gets closer, the steps will become smaller.

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

This is no where near complete and is just a fraction of what you can do with Gradient Decent. Feel free to submit issues or pull request! Contributions are welcome.

Made with ❤️ by __[@markmusic2727](https://twitter.com/MarkMusic2727)__



