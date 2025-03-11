from siggraph_rebuttal.Method.table import toTableStrFromFile

if __name__ == '__main__':
    metric_file_path = '../ma-sh/output/metrics/Thingi10K_ours.npy'

    table_str = toTableStrFromFile(metric_file_path)

    print('Table:')
    print(table_str)
