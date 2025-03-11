import numpy as np


def toTableStr(data: list) -> str:
    row_num = len(data)
    col_num = len(data[0])

    table_str = ''

    table_str += '$$\\begin{array}{'

    for _ in range(col_num - 1):
        table_str += 'c|'

    table_str += 'c'

    table_str += '}\\hline\n'

    for i in range(row_num):
        for j in range(col_num - 1):
            table_str += '\\text{'
            table_str += str(data[i][j])
            table_str += '}&'

        table_str += '\\text{'
        table_str += str(data[i][col_num - 1])
        table_str += '}'

        table_str += '\\\\\\\\\\hline\n'

    table_str += '\\end{array}$$\n'

    return table_str

def toMeanMetric(metric_dict: dict, metric_name: str) -> float:
    metric_list = []
    for value in metric_dict.values():
        if metric_name not in value.keys():
            continue
        metric_list.append(value[metric_name])

    if len(metric_list) == 0:
        return np.nan

    return np.mean(metric_list)

def toTableStrFromFile(metric_file_path: str) -> str:
    metric_dict = np.load(metric_file_path, allow_pickle=True).item()

    title = ['Method', 'Ours']

    chamfer = ['chamfer', toMeanMetric(metric_dict, 'chamfer')]
    fscore = ['fscore', toMeanMetric(metric_dict, 'fscore')]
    nic = ['nic', toMeanMetric(metric_dict, 'nic')]

    data = [title, chamfer, fscore, nic]

    return toTableStr(data)
