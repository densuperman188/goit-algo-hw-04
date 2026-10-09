def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                    name, salary = line.split(',')
                    salary = float(salary)
                    total += salary
                    count += 1
        average = total / count
        return total, average
    except FileNotFoundError:
        return 0, 0