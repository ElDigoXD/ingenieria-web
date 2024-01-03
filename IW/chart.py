from enum import Enum


class Type(Enum):
    LINE = 1
    BAR = 2


class Dataset:
    data: str
    y_axis_id: str
    background_color: str
    border_color: str

    def __init__(self,
                 data: str,
                 label="",
                 y_axis_id="y",
                 background_color="rgba(0,0,255,0.5)",
                 border_color="rgba(0,0,255,0.1)"
                 ):
        self.data = data
        self.label = label
        self.y_axis_id = y_axis_id
        self.background_color = background_color
        self.border_color = border_color


class Scale:
    name: str
    position: str

    def __init__(self,
                 name="y",
                 position="left",
                 ticks="ticks: { min: 0 }"
                 ):
        self.name = name
        self.position = position
        self.ticks = ticks


class Chart:
    type: str
    canvas_id: str
    x_labels: str
    datasets: list[Dataset]
    scales: list[Scale]
    name: str

    def __init__(self,
                 canvas_id: str,
                 x_labels: str,
                 datasets: list[Dataset],
                 scales: list[Scale],
                 type=Type.LINE,
                 legend=False,
                 name=""
                 ):
        self.canvas_id = canvas_id
        self.x_labels = x_labels
        self.datasets = datasets
        self.scales = scales
        self.type = "line" if type == Type.LINE else "bar"
        self.legend = legend
        self.name = name

# {{{# chart: type, canvas_id, x_labels, datasets #}}}
# {{{# datasets: [background_color, bordercolor, data, y_axis_id] #}}}
