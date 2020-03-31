"""Module contains code to run all sample projects."""
import os
from pathlib import Path

import click
from click.testing import CliRunner
from pipeline.cli import cli


def main():
    """Loop over projects and execute them."""
    cwd = Path.cwd()
    runner = CliRunner()

    example_folders = [
        path for path in cwd.glob("*") if path.is_dir() and path.name != ".git"
    ]

    for example_folder in example_folders:
        click.echo(f"### Build {example_folder.name}")

        os.chdir(example_folder)
        runner.invoke(cli, ["clean"])
        runner.invoke(cli, ["build"])

        click.echo("### Finished")


if __name__ == "__main__":
    main()
