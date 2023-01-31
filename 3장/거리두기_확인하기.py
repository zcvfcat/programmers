def check(place):
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            if cell != 'P':
                continue

            isNotEndRow = idx_row != 4
            isNotEndCol = idx_col != 4
            isNotFirstCol = idx_col != 0
            isBeforeThirdRow = idx_row < 3
            isBeforeThirdCol = idx_col < 3

            # 잠시 스탑...


def solution(places):
    return [check(place) for place in places]
