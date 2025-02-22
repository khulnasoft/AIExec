import matplotlib.pyplot as plt
import numpy as np

from khulnasoft_charts import chart_figure_to_chart
from khulnasoft_charts.charts import ScatterChart


def _prep_chart_figure():
    # Create data
    N = 5
    x1 = np.random.rand(N)
    y1 = np.random.rand(N)
    x2 = np.random.rand(2 * N)
    y2 = np.random.rand(2 * N)

    plt.figure(figsize=(10, 6))

    plt.xlabel("A")
    plt.ylabel("B")

    plt.scatter(x1, y1, c="blue", label="Dataset 1")
    plt.scatter(x2, y2, c="red", label="Dataset 2")

    return plt.gcf()


def test_scatter_chart():
    figure = _prep_chart_figure()
    chart = chart_figure_to_chart(figure)
    assert chart

    assert isinstance(chart, ScatterChart)

    assert chart.title is None
    assert chart.x_label == "A"
    assert chart.y_label == "B"

    assert chart.x_scale == "linear"
    assert chart.y_scale == "linear"

    assert all(isinstance(x, float) for x in chart.x_ticks)
    assert all(isinstance(y, float) for y in chart.y_ticks)

    assert all(isinstance(x, str) for x in chart.y_tick_labels)
    assert all(isinstance(y, str) for y in chart.y_tick_labels)

    assert len(chart.elements) == 2

    first_data = chart.elements[0]
    assert first_data.label == "Dataset 1"
    assert len(first_data.points) == 5
    print(first_data.points)
    assert all(isinstance(x, tuple) for x in first_data.points)

    second_data = chart.elements[1]
    assert second_data.label == "Dataset 2"
    assert len(second_data.points) == 10
    assert all(isinstance(x, tuple) for x in second_data.points)
