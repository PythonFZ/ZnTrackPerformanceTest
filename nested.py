import time

import git
import pandas as pd
import typer
import zntrack.examples

app = typer.Typer()


@app.command()
def run(rev: str):
    start_time = time.time()
    with zntrack.Project(automatic_node_names=True) as proj:
        for idx in range(10):
            zntrack.examples.AddNodes(
                a=zntrack.examples.AddNumbers(a=idx, b=idx),
                b=zntrack.examples.AddNumbers(a=idx, b=idx),
            )

    proj.build()

    elapsed_time = time.time() - start_time

    print(f"Elapsed time: {elapsed_time} seconds")

    try:
        df = pd.read_csv("nested.csv", index_col="rev")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["rev", "time"])
        df.set_index("rev", inplace=True)
    df.loc[rev] = [elapsed_time]
    df.to_csv(
        "nested.csv",
    )

    repo = git.Repo()
    repo.git.clean("-xdf")


if __name__ == "__main__":
    app()
