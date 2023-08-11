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
        for idx in range(30):
            zntrack.examples.ParamsToOuts(params=idx)

    proj.build()

    elapsed_time = time.time() - start_time

    print(f"Elapsed time: {elapsed_time} seconds")

    try:
        df = pd.read_csv("serial.csv", index_col="rev")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["rev", "time"])
        df.set_index("rev", inplace=True)
    df.loc[rev] = [elapsed_time]
    df.to_csv(
        "serial.csv",
    )

    repo = git.Repo()
    repo.git.clean("-xdf")


if __name__ == "__main__":
    app()
