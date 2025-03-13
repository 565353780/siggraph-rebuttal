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

def toFormatDataStr(data) -> str:
    format_data_str = ''

    if '\\' in data:
        data_list = data.split('\\')

        data_str = data_list[0]

        outer_tag_num = 0
        for tag in data_list[1:]:
            if tag in ['bf', 'underline']:
                format_data_str += '\\' + tag + '{'
                outer_tag_num += 1
    else:
        data_str = data

    format_data_str += '\\text{'
    format_data_str += str(data_str)

    if '\\' in data:
        for _ in range(outer_tag_num):
            format_data_str += '}'

    format_data_str += '}'

    if '\\' in data:
        for tag in data_list[1:]:
            if tag in ['downarrow', 'uparrow']:
                format_data_str += '\\' + tag
    return format_data_str

def toRebuttalTableStr(data: list) -> str:
    row_num = len(data)
    col_num = len(data[0])

    table_str = ''

    table_str += '$$\\begin{array}{'

    for _ in range(col_num):
        table_str += 'c'

    table_str += '}\\hline\n'

    for i in range(row_num):
        for j in range(col_num - 1):
            table_str += toFormatDataStr(data[i][j])

            table_str += '&'

        table_str += toFormatDataStr(data[i][col_num - 1])

        table_str += '\\\\\\\\\\hline\n'

    table_str += '\\end{array}$$\n'

    return table_str

def toTableStr(data: list) -> str:
    return toLatexTableStr(data) + '\n' + toRebuttalTableStr(data)
