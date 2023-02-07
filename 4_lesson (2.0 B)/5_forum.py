n = int(input())
themes = {}
themes_messages = [0] * (n + 1)
themes_count = 0
for i in range(1, n + 1):
    number = int(input())
    if number == 0:
        theme_name = input()
        input()
        themes[theme_name] = [themes_count, 0]
        themes_count += 1
        themes_messages[i] = theme_name
    else:
        input()
        themes_messages[i] = themes_messages[number]

for i in range(1, n + 1):
    theme_name = themes_messages[i]
    themes[theme_name][1] += 1

most_popular_theme = ""
max_messages = 0

for theme_name, theme_data in sorted(themes.items(), key=lambda x: x[1][0]):
    if theme_data[1] > max_messages:
        max_messages = theme_data[1]
        most_popular_theme = theme_name

print(most_popular_theme)
