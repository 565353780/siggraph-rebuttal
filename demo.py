from siggraph_rebuttal.Method.table import toTableStr

if __name__ == '__main__':
    data = [
        ['Method', 'Ours',],
        ['mAP', 1.0,],
    ]

    table_str = toTableStr(data)

    print('Table:')
    print(table_str)
