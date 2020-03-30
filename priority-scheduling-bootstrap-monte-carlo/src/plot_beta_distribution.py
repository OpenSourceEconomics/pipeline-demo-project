import joblib
import matplotlib.pyplot as plt
import seaborn as sns


def load_betas():
    betas = []
    for path in {{depends_on}}:
        model = joblib.load(path)
        betas.append(model.params["x"])

    return betas


def plot_histogram(betas):
    fig, ax = plt.subplots(figsize=(12, 8))

    sns.distplot(betas, ax=ax)

    plt.savefig("{{ produces }}")


if __name__ == "__main__":
    betas = load_betas()

    plot_histogram(betas)
