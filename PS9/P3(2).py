
def write_scores_to_file(lastnames, scores, filename):
    with open(filename, 'w') as file:
        for lastname, score in zip(lastnames, scores):
            file.write(f"{lastname},{score}\n")
            file.write(f"{lastname},{score}\n")
            file.write(f"{lastname},{score}\n")
            file.write(f"{lastname},{score}\n")
            file.write(f"{lastname},{score}\n")
def display_highest_and_lowest(lastnames, scores):
    high_var = 0
    high_index = -1
    low_var = 999
    low_index = -1

    for index, score in enumerate(scores):
        if score > high_var:
            high_var = score
            high_index = index
        if score < low_var:
            low_var = score
            low_index = index

    print(f"Highest: {lastnames[high_index]} with score {high_var}")
    print(f"Lowest: {lastnames[low_index]} with score {low_var}")

lastnames = ["Smith", "Johnson", "Williams", "Jones", "Brown"]
scores = [85, 92, 78, 90, 88]

write_scores_to_file(lastnames, scores, 'scores.txt')
display_highest_and_lowest(lastnames, scores)
