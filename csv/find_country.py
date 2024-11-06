import csv 
def find(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        countryName = input('Insert the country to find: ')

        i = 0
        for i in range(len(data)):
            value = data[i]['Country']
            if countryName == str(value):
                country_dict = data[i]
                population = {
                2019: int(country_dict['Population_2019']),
                2020: int(country_dict['Population_2020']),
                2021: int(country_dict['Population_2021']),
                2022: int(country_dict['Population_2022']),
                2023: int(country_dict['Population_2023'])
            }
                labels = list(population.keys())
                values = list(population.values())
    return labels, values, countryName
            

if __name__ == '__main__':
    find('./countries_population_data.csv')