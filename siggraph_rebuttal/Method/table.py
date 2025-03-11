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
