items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):

    items_sorted = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, data in items_sorted:
        if total_cost + data['cost'] <= budget:
            chosen_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']

    return chosen_items, total_cost, total_calories


budget = 100
chosen_items, total_cost, total_calories = greedy_algorithm(items, budget)
print(f"Вибрані страви (жадібний алгоритм): {chosen_items}")
print(f"Загальна вартість: {total_cost}, Загальна калорійність: {total_calories}")


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, data = item_list[i - 1]
        cost = data['cost']
        calories = data['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    total_cost = 0
    chosen_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, data = item_list[i - 1]
            chosen_items.append(item_name)
            w -= data['cost']
            total_cost += data['cost']

    chosen_items.reverse()
    return chosen_items, total_cost, total_calories


budget = 100
chosen_items, total_cost, total_calories = dynamic_programming(items, budget)
print(f"Вибрані страви (динамічне програмування): {chosen_items}")
print(f"Загальна вартість: {total_cost}, Загальна калорійність: {total_calories}")


