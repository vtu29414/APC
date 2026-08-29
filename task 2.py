import random
def objective_function(x):
    return -x**2 + 10 
def get_neighbor(x):
    return x + random.choice([-1, 1])  
def hill_climbing(start, max_iterations=100):
    current = start
    current_value = objective_function(current)
    for _ in range(max_iterations):
        neighbor = get_neighbor(current)
        neighbor_value = objective_function(neighbor)
        if neighbor_value > current_value:
            current = neighbor
            current_value = neighbor_value

    return current, current_value
start = random.randint(-10, 10)
best_x, best_value = hill_climbing(start)

print("Start:", start)
print("Best Solution:", best_x)
print("Best Value:", best_value)

