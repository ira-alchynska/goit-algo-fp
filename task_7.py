import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):

    sum_counts = {i: 0 for i in range(2, 13)}
    

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1
    

    probabilities = {k: v / num_rolls for k, v in sum_counts.items()}
    
    return probabilities

def plot_probabilities(probabilities):

    theoretical_probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }
    
    sums = list(probabilities.keys())
    sim_probs = [probabilities[sum_] for sum_ in sums]
    theo_probs = [theoretical_probabilities[sum_] for sum_ in sums]
    

    plt.figure(figsize=(10, 6))
    plt.bar(sums, sim_probs, width=0.4, label='Симуляція', align='center')
    plt.bar([x + 0.4 for x in sums], theo_probs, width=0.4, label='Аналітичні', align='center')
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.xticks(sums)
    plt.legend()
    plt.show()

def main():
    num_rolls = 1000000  
    probabilities = simulate_dice_rolls(num_rolls)
    

    print("Ймовірності сум при киданні двох кубиків (симуляція):")
    for sum_, prob in probabilities.items():
        print(f"Сума {sum_}: {prob:.4f}")
    

    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
