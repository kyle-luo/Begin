def check_sudoku(sudoku):
    n = len(sudoku)
    y = 0
    while y< n:
        checklist = []
        x = 0
        while x < n:
            if sudoku[x][y] not in checklist:
                checklist.append(sudoku[x][y])
                x += 1
            else:
                return False
        y += 1
    for row in sudoku:
        numbers = []
        for number in row:
            if number in range(1,len(row) + 1):
                if number not in numbers:
                    numbers.append(number)
                else:
                    return False
            else:
                return False
    return True