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
        labels = list(map(lambda x: x['Country'], data))
        values = list(map(lambda x: x['Population_2019'], data))
        return labels, values
            

if __name__ == '__main__':
    find('./countries_population_data.csv')