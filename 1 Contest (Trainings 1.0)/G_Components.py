"""
raw - вес чистого сплава
blank - вес заготовки
piece - масса детали (из каждой заготовки макс количество деталей)

"""


def count_pieces(raw, blank, piece):
    if raw == 0 or blank == 0 or piece == 0:
        return 0
    if piece > blank or blank > raw:
        return 0

    n_blanks = raw // blank
    # print(f"number of blanks: {n_blanks}")

    raw_remainder = raw % blank
    # print(f"raw remainder: {raw_remainder}")

    n_pieces = (blank // piece) * n_blanks
    # print(f"number of pieces: {n_pieces}")

    blank_remainder = (blank % piece) * n_blanks
    # print(f"blank remainder: {blank_remainder}")

    raw_remainder = raw_remainder + blank_remainder

    if raw_remainder >= blank:
        return n_pieces + count_pieces(raw_remainder, blank, piece)
    else:
        return n_pieces


if __name__ == "__main__":
    raw, blank, piece = map(int, input().split())

    # 4
    # raw, blank, piece = 10, 5, 2

    # 3
    # raw, blank, piece = 13, 5, 3

    # 4
    # raw, blank, piece = 14, 5, 3

    print(count_pieces(raw, blank, piece))
