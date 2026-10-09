def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.split(',')
                cat = {
                    'id': str(cat_id),
                    'name': name.strip(),
                    'age': str(age)
                }
            cats.append(cat)
    except FileNotFoundError:
        return []
    return cats