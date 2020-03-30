"""Module for data generation."""
import numpy as np
import pandas as pd


def create_random_data():
    """Create a random data set."""
    np.random.seed(1)

    n_samples = 10_000

    constant = 0.1
    epsilon = np.random.normal(size=n_samples)
    beta = np.random.uniform(-1, 1)

    df = pd.DataFrame({"x": np.random.normal(loc=0, scale=1, size=n_samples)})

    z = constant + beta * df.x + epsilon
    pr = 1 / (1 + np.exp(-z))

    df["y"] = np.random.binomial(1, pr)

    df.to_csv("{{ produces }}")


if __name__ == "__main__":
    create_random_data()
