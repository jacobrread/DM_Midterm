import random
import matplotlib.pyplot as plt
import csv


# Graphs the data
def graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Stopping Rule')
    plt.ylabel('Optimal Solutions Found')
    plt.show()


# Populates the lists for testing the stopping rules
def populate_lists(total_candidates):
    solution_found = {}
    optimal_solution_found = {}

    for i in range(total_candidates):
        solution_found[str(i)] = 0
        optimal_solution_found[str(i)] = 0

    return solution_found, optimal_solution_found


# Reads the csv file and returns a list containing its contents
def readCSV(filename):
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(int(row[0]))
    return rows


# Finds the optimal solution using the stopping rule with a 50% chance of accepting the job
def findOptimalSolution50(total_candidates, total_experiments):
    solution_found_count, optimal_solution_found_count = populate_lists(
        total_candidates)

    for experiment in range(total_experiments):
        candidates = random.sample(range(0, 1000), total_candidates)
        optimal_candidate = max(candidates)

        for i in range(1, total_candidates):
            index = i
            # Look at the last 5 candidates
            if index <= 4:
                index = 0
            else:
                index = i - 4

            for candidate in candidates[index:-1]:
                if candidate > max(candidates[0:i]):
                    if bool(random.getrandbits(1)):  # simulates the 50% chance of accepting the job
                        solution_found_count[str(i)] += 1
                        if candidate == optimal_candidate:
                            optimal_solution_found_count[str(i)] += 1
                        break

    return candidates, optimal_solution_found_count


def didAccept(desired, candidates):
    index = candidates.index(desired)

    if index == 0:
        percent = 95 # 95% chance of accepting the job
    elif index == 1:
        percent = 80 # 80% chance of accepting the job
    elif index == 2:
        percent = 65 # 65% chance of accepting the job
    elif index == 3:
        percent = 50 # 50% chance of accepting the job
    elif index == 4:
        percent = 35 # 35% chance of accepting the job
    else:
        percent = 20 # 20% chance of accepting the job

    return random.randrange(100) > percent


# Finds the optimal solution using the stopping rule with a 20% chance of accepting the job
def findOptimalSolution20(total_candidates, total_experiments):
    solution_found_count, optimal_solution_found_count = populate_lists(
        total_candidates)

    for experiment in range(total_experiments):
        # candidates = random.sample(range(0, 1000), total_candidates)
        candidates = []
        for i in range(1, total_candidates):
            candidates.append(random.uniform(1, 1000))

        optimal_candidate = max(candidates)

        for i in range(1, total_candidates):
            index = i
            # Look at the last 5 candidates
            if index <= 4:
                index = 0
            else:
                index = i - 4

            for candidate in candidates[index:-1]:
                if candidate > max(candidates[0:i]):
                    if didAccept(candidate, candidates[index:-1]):
                        solution_found_count[str(i)] += 1
                        if candidate == optimal_candidate:
                            optimal_solution_found_count[str(i)] += 1
                        break

    return candidates, optimal_solution_found_count


# Calculates the optimal threshold
def calcOptimalThreshold(dictionary):
    for key in dictionary:
        if dictionary[key] == max(dictionary.values()):
            return (int(key) / len(dictionary))


# Calculates the stopping point
def calcStoppingPoint(threshold, candidates):
    index = int(threshold * len(candidates))
    return candidates[index]


# Conducts the calculations for problem 1 of the midterm
def run(percent, showGraph):
    total_candidates = 100
    total_experiments = 100000

    if (percent == "20"):
        candidates, optimal_solution_found_count = findOptimalSolution20(
            total_candidates, total_experiments)
    else:
        candidates, optimal_solution_found_count = findOptimalSolution50(
            total_candidates, total_experiments)

    # print("Optimal solutions found count: \n" + str(optimal_solution_found_count))
    optimal_threshold = calcOptimalThreshold(optimal_solution_found_count)
    print("Optimal Search Threshold: " + str(optimal_threshold * 100) + "%")

    optimal_answer = calcStoppingPoint(optimal_threshold, candidates)
    print("Optimal Answer: " + str(optimal_answer))

    if showGraph:
        stopping_rule, optimal_solutions_num = zip(
            *optimal_solution_found_count.items())
        graph(stopping_rule, optimal_solutions_num)



run("20", True)
