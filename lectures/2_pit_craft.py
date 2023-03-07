"""
Игра PitCraft происходит в двумерном мире, который состоит из блоков
размером 1 на 1 метр.

Остров игрока представляет собой набор столбцов различной высоты, состоящих из
блоков камня и окруженный морем.

Над островом прошёл сильный дождь, который заполнил водой все низины, а не
поместившаяся в них вода стекла в море, не увеличив его уровень. По ландшафту
острова определите, сколько блоков воды осталось после дождя в низинах на
острове.
"""

h = [3, 1, 4, 3, 5, 1, 1, 3, 1]


def pit_craft(h):
    max_pos = 0
    for i in range(1, len(h)):  # поиск максимума
        if h[i] > h[max_pos]:
            max_pos = i

    result = 0

    current_max = 0
    for i in range(1, max_pos):  # слева направо
        if h[i] > h[current_max]:
            current_max = i
        else:
            result += h[current_max] - h[i]

    current_max = len(h) - 1
    for i in range(len(h) - 1, max_pos, -1):  # справа налево
        if h[i] > h[current_max]:
            current_max = i
        else:
            result += h[current_max] - h[i]

    return result


print(pit_craft(h))  # 7
