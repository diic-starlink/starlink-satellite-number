import json
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np


def load_starlink_data():
    raw_data = json.load(open("./data.json"))
    df = pd.DataFrame(data=raw_data)

    return df


satcat_df = load_starlink_data()
satcat_df.head()

satellite_numbers = {}
START_YEAR = 2019
START_MONTH = 5

STOP_YEAR = datetime.now().year
STOP_MONTH = datetime.now().month


def accumulate_monthly_satellites():
    for current_year in range(START_YEAR, STOP_YEAR + 1):
        active_satellites = 0

        if current_year == START_YEAR:
            start_loop_month = START_MONTH
        else:
            start_loop_month = 1

        if current_year == STOP_YEAR:
            stop_loop_month = STOP_MONTH
        else:
            stop_loop_month = 13

        for current_month in range(start_loop_month, stop_loop_month):
            label = f"{current_year}-{current_month}"
            current_date = datetime.strptime(
                f"{current_year}-{current_month}-01", "%Y-%m-%d"
            )

            for i in range(0, len(satcat_df)):
                launch_date = datetime.strptime(
                    satcat_df["LAUNCH"][i], "%Y-%m-%d")

                if satcat_df["DECAY"][i]:
                    decay_date = datetime.strptime(
                        satcat_df["DECAY"][i], "%Y-%m-%d")
                else:
                    decay_date = current_date + timedelta(days=1)

                if launch_date < current_date and decay_date > current_date:
                    active_satellites += 1

            satellite_numbers[label] = active_satellites
            active_satellites = 0

    with open("satellite-development.csv", "w") as f:
        content = "MONTH,NUMBER\n"
        for key, value in satellite_numbers.items():
            content += f"{key},{value}\n"

        f.write(content)


def plot_satellite_development(data):
    # Convert to DataFrame for easier handling
    df = pd.DataFrame(list(data.items()), columns=["date", "value"])
    # Convert date strings to datetime objects
    df["datetime"] = pd.to_datetime(df["date"], format="%Y-%m")
    # Sort by date
    df = df.sort_values("datetime")
    # Main line plot
    plt.plot(
        df["datetime"],
        df["value"],
        linewidth=2.5,
        color="#2563eb",
        marker="o",
        markersize=4,
    )

    # Customize the plot
    plt.ylabel("Number of Satellites", fontsize=12)

    # Format y-axis to show thousands with commas
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, p: f"{x:,.0f}"))
    plt.grid(True, alpha=0.3, linestyle="--")

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Add some key annotations
    start_value = df.iloc[0]["value"]
    end_value = df.iloc[-1]["value"]
    max_value = df["value"].max()
    max_date = df.loc[df["value"].idxmax(), "datetime"]

    # Annotate start point
    plt.annotate(
        f"May 2019",
        xy=(df.iloc[0]["datetime"], start_value),
        xytext=(0, 20),
        textcoords="offset points",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
    )

    end_date = df.iloc[-1]["datetime"].strftime("%B %Y")
    # Annotate end point
    plt.annotate(
        f"{end_date}: {end_value:,}",
        xy=(df.iloc[-1]["datetime"], end_value),
        xytext=(-120, -10),
        textcoords="offset points",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
    )

    # Tight layout to prevent label cutoff
    plt.tight_layout()
    plt.savefig("starlink-satellite-development.pdf")


accumulate_monthly_satellites()
plot_satellite_development(satellite_numbers)
