import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    categories = r.json()
    titles = list(map(lambda item: item['name'], categories))
    print(titles)
