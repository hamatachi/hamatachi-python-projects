
# Initial list of scores
scores = [61, 84, 26, 77, 34, 88, 90, 56, 67, 97]

# Sorting the scores using insertion sort
n = len(scores)
for x in range(1, n):
    current = scores[x]
    y = x
    while y > 0 and scores[y - 1] > current:
        scores[y] = scores[y - 1]
        y = y - 1
    scores[y] = current 

# Function to calculate mean
def mean():
    total_sum = sum(scores)
    return round(total_sum / len(scores), 2)  # Return the average rounded to 2 decimal places

# Function to calculate mode
def mode():
    count = {}
    for score in scores:
        count[score] = count.get(score, 0) + 1
    max_count = 0
    mode_value = None
    for score, y in count.items():
        if y > max_count:
            max_count = y
            mode_value = score
    return mode_value  

# Function to display results
def display():
    print("Sorted scores:", scores)
    print("Mean:", mean_value)
    print("Mode:", mode_value)

# Function to add a new score
def add_score():
    new_score = int(input("Enter the new student's score: "))  
    scores.append(new_score)  
    # Recalculate mean and mode after adding the new score
    global mean_value, mode_value
    mean_value = mean()
    mode_value = mode()

# Calculate initial mean and mode
mean_value = mean()
mode_value = mode()

# Continuous loop for updating scores and displaying results
while True:
    display()
    add_score()


