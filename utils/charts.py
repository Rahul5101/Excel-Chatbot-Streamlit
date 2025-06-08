import matplotlib.pyplot as plt
import seaborn as sns

def plot_chart(df, chart_info):
    chart_type = chart_info.get("chart_type")
    x = chart_info.get("x")
    y = chart_info.get("y")
    agg = chart_info.get("agg")

    plt.figure(figsize=(10, 6))

    if chart_type == "bar":
        grouped = df.groupby(x)[y].agg(agg).reset_index()
        sns.barplot(x=x, y=y, data=grouped)

    elif chart_type == "hist":
        sns.histplot(data=df, x=x)

    elif chart_type == "line":
        grouped = df.groupby(x)[y].agg(agg).reset_index()
        sns.lineplot(x=x, y=y, data=grouped)

    plt.title(f"{agg.title()} of {y} by {x}")
    plt.xticks(rotation=45)
    return plt.gcf()
