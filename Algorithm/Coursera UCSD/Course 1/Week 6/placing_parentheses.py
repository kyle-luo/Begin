# Uses python3
import re

def get_maximum_value(dataset):
    num = re.split(r'[+\-*/]', dataset)
    op = re.split(r'[0-9]', dataset)
    op = op[1:-1]

    dps = [[None for _ in range(len(num))] for _ in range(len(num))]
    dpl = [[None for _ in range(len(num))] for _ in range(len(num))]

    for i in range(len(num)):
        dps[i][i] = num[i]
        dpl[i][i] = num[i]

    def values(a, b):
        vals = []
        for i in range(a, b):
            vals.append(eval(dps[a][i] + op[i] + dps[i + 1][b]))
            vals.append(eval(dpl[a][i] + op[i] + dpl[i + 1][b]))
            vals.append(eval(dps[a][i] + op[i] + dpl[i + 1][b]))
            vals.append(eval(dpl[a][i] + op[i] + dps[i + 1][b]))
        return str(min(vals)), str(max(vals))

    for i in range(1, len(num)):
        for j in range(len(num) - i):
            dps[j][j + i], dpl[j][j + i] = values(j, j + i)

    return int(dpl[0][len(num) - 1])


if __name__ == "__main__":
    print(get_maximum_value(input()))
