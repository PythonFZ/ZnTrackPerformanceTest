import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    nested_df = pd.read_csv("nested.csv")
    serial_df = pd.read_csv("serial.csv")

    fig, ax = plt.subplots(2)
    nested_df.plot(ax=ax[0],  y="time", label="Nested")
    ax[0].set_ylabel("Time t / s")
    serial_df.plot(ax=ax[1],  y="time", label="Serial")
    ax[1].set_ylabel("Time t / s")
    plt.show()