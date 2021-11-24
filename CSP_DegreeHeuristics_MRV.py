territory = {'WA': ['SA', 'NT'],
             'Q': ['SA', 'NT', 'NSW'],
             'T': [],
             'V': ['SA', 'NSW'],
             'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
             'NT': ['Q', 'WA', 'SA'],
             'NSW': ['Q', 'V', 'SA']
             }

sorted_territory = []
for k in sorted(territory, key=lambda i: len(territory[i]), reverse=True):
    sorted_territory.append(k)

territory_colors = {'WA': ['red', 'green', 'blue'],
                    'Q': ['red', 'green', 'blue'],
                    'T': ['red', 'green', 'blue'],
                    'V': ['red', 'green', 'blue'],
                    'SA': ['red', 'green', 'blue'],
                    'NT': ['red', 'green', 'blue'],
                    'NSW': ['red', 'green', 'blue']
                    }

final_colors = {}

territory_colors[sorted_territory[0]] = ['red']
for i in territory[sorted_territory[0]]:
    territory_colors[i].remove(territory_colors[sorted_territory[0]][0])
final_colors[sorted_territory[0]] = territory_colors[sorted_territory[0]]
for i in territory[sorted_territory[0]]:
    territory[i].remove(sorted_territory[0])
territory.pop(sorted_territory[0])
territory_colors.pop(sorted_territory[0])


while territory_colors:
    next_territory = sorted(territory_colors, key=lambda i: len(territory_colors[i]))[0]
    temp = territory_colors[next_territory][:]
    territory_colors[next_territory].clear()
    territory_colors[next_territory].append(temp[0])
    final_colors[next_territory] = territory_colors[next_territory]
    for i in territory[next_territory]:
        territory_colors[i].remove(territory_colors[next_territory][0])
    for i in territory[next_territory]:
        territory[i].remove(next_territory)
    territory.pop(next_territory)
    territory_colors.pop(next_territory)

print(final_colors)

