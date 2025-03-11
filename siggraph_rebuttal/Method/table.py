def toLatexTableStr(data: list) -> str:
    row_num = len(data)
    col_num = len(data[0])

    table_str = ''

    table_str += '\\begin{tabular}{'

    for _ in range(col_num):
        table_str += 'c'

    table_str += '}\n'

    table_str += '\\toprule\n'

    for i in range(row_num):
        for j in range(col_num - 1):
            table_str += str(data[i][j])
            table_str += '&'

        table_str += str(data[i][col_num - 1])
        table_str += '\\\\\n'

    table_str += '\\bottomrule\n'

    table_str += '\\end{tabular}\n'

    return table_str

def toRebuttalTableStr(data: list) -> str:
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

def toTableStr(data: list) -> str:
    return toLatexTableStr(data) + '\n' + toRebuttalTableStr(data)
