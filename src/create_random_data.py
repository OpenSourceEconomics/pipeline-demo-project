import numpy as np
import pandas as pd


def create_random_data():
    np.random.seed(1)

    n_samples = 10_000

    constant = 2
    epsilon = np.random.normal(size=n_samples)
    beta = np.random.uniform(0, 10)

    df = pd.DataFrame({
            "x": np.random.normal(loc=20, scale=3, size=n_samples),
        })

    z = constant + beta * df.x + epsilon
    pr = 1 / (1 + np.exp(-z))

    df["y"] = np.random.binomial(1, pr)

    df.to_csv("{{ produces }}")


if __name__ == '__main__':
    create_random_data()
