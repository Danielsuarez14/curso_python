import matplotlib.pyplot as plt
from find_col import find
def generate_bar_chart(labels, values, countryName='bar'):
    print(values)
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{countryName}.png')
    plt.close()
    
def generate_pie_chart(labels, values, countryName='pie'):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'./imgs/{countryName}.png')
    plt.close()


if __name__== '__main__':
    labels, values = find('./countries_population_data.csv')
    generate_bar_chart(labels, values)