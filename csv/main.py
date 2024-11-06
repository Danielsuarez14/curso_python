from find_col import find as col
from find_country import find as country
from sharts import generate_bar_chart, generate_pie_chart
def run():
    chose = int(input('''What do you want to see:
1. Column
2. Find a country
'''))
    if chose == 1:
        labels, values= col('./countries_population_data.csv')
    elif chose == 2:
        labels, values, countryName= country('./countries_population_data.csv')
    shart = int(input('''What kind of shart do you want :
1. Bar shart
2. Pie shart
'''))
    if shart == 1:
        generate_bar_chart(labels, values, countryName)
    elif shart == 2:
        generate_pie_chart(labels, values, countryName)
run()