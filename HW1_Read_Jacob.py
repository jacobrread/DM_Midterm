import random
import matplotlib.pyplot as plt
import sys
import csv

# Graphs the data
def graph(x, y):
  plt.plot(x, y)
  plt.xlabel('Stopping Rule')
  plt.ylabel('Optimal Solutions Found')
  plt.show()


# Populates the lists for testing the stopping rules
# len_candidates: the total number of candidates
def populate_lists(total_candidates):
  solution_found = {}
  optimal_solution_found = {}

  for i in range(total_candidates):
      solution_found[str(i)] = 0
      optimal_solution_found[str(i)] = 0
    
  return solution_found, optimal_solution_found


# Reads the csv file and returns a list containing its contents
# filename: the name of the csv file
def readCSV(filename):
  rows = []
  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(int(row[0]))
  return rows


# Finds the percentage of the array that is equal to the value
# array: the array to search
# value: the value to search for
def findPercentage(array, value):
  for i in range(len(array)):
    if array[i] == value:
      return i / len(array)


# Finds the optimal solution using the stopping rule
# total_candidates: the total number of candidates
# total_experiments: the total number of experiments
def findOptimalSolution(total_candidates, total_experiments):
  solution_found_count, optimal_solution_found_count = populate_lists(total_candidates)

  for experiment in range(total_experiments):
    candidates = random.sample(range(0,1000), total_candidates)
    optimal_candidate = max(candidates)

    for i in range(1, total_candidates):
        for candidate in candidates[i:-1]:
            if candidate > max(candidates[0:i]):
                solution_found_count[str(i)] += 1
                if candidate == optimal_candidate:
                    optimal_solution_found_count[str(i)] += 1
                break
  
  return solution_found_count, optimal_solution_found_count


# Calculates the optimal threshold
# dictionary: the dictionary containing the optimal solutions found
def calcOptimalThreshold(dictionary):
  for key in dictionary:
    if dictionary[key] == max(dictionary.values()):
      return (int(key) / len(dictionary))


# Calculates the stopping point
# threshold: the threshold to use
# filename: the name of the csv file
def calcStoppingPoint(threshold, filename):
  csv = readCSV(filename)
  return csv[int(threshold * len(csv))]


# Conducts the calculations for part 1 of the homework
# filename: the name of the csv file
def part1(filename):
  total_candidates = 100
  total_experiments = 10000

  solution_found_count, optimal_solution_found_count = findOptimalSolution(total_candidates, total_experiments)
  
  print("Optimal solutions found count: \n" + str(optimal_solution_found_count))
  optimal_threshold = calcOptimalThreshold(optimal_solution_found_count)
  print("Optimal Search Threshold: " + str(optimal_threshold * 100) + "%")

  resulting_stopping_position = calcStoppingPoint(optimal_threshold, filename)
  print("Resulting stopping position: " + str(resulting_stopping_position))

  stopping_rule, optimal_solutions_num = zip(*optimal_solution_found_count.items())
  graph(stopping_rule, optimal_solutions_num)


# Generates the data needed for testing and caps the values at 99
# is99: whether or not the data should be generated from a uniform distribution
# total_candidates: the total number of candidates
def getTestCase(is99, total_candidates):
  if is99:
    array = [random.uniform(0,99) for i in range(total_candidates)]
  else:
    array = [random.normalvariate(50, 10) for i in range(total_candidates)]

  for i in range(len(array)):
    if array[i] > 99:
      array[i] = 99

  return array


# Finds the optimal solution using while taking into account the cost of the index
# total_candidates: the total number of candidates
# total_experiments: the total number of experiments
# is99: whether or not the data should be generated from a uniform distribution
def findOptimalWithWeight(total_candidates, total_experiments, is99):
  solution_found, optimal_solution_found = populate_lists(total_candidates)

  for experiment in range(total_experiments):
    candidates = getTestCase(is99, total_candidates)
    optimal_answer = max(candidates)

    # TODO: Take into account the cost of the index (the further into the array you go the more you are pentalized,
    # so potentially a higher value can be a worse pick due if you subtract the penalty from it )
    for stopping_point in range(1, total_candidates):
      comparison_value = max(candidates[0:stopping_point]) - stopping_point
      for i in range(len(candidates[stopping_point:-1])):
        if candidates[i] - stopping_point > comparison_value:
          solution_found[str(stopping_point)] += 1
          if candidates[i] == optimal_answer:
                optimal_solution_found[str(stopping_point)] += 1
          break

  return solution_found, optimal_solution_found, optimal_answer


# Conducts the final calculations for part 2 and displays them
# optimal_answer: the optimal answer
# optimal_solution_found: the optimal solution found
# dictionary: the dictionary containing the optimal solutions found
def finalizeResults(optimal_answer, dictionary, name):
  # print("Optimal Answer:" + str(optimal_answer))
  # print("Optimal Solutions Found:" + str(dictionary))

  threshold = calcOptimalThreshold(dictionary)
  print("Optimal " + name + " Search Threshold: " + str(threshold * 100) + "%")

  resulting_stopping_position = int(threshold * len(dictionary))
  print("Resulting stopping position: " + str(resulting_stopping_position)  + "\n")

  stopping_rule, optimal_solutions_num = zip(*dictionary.items())
  graph(stopping_rule, optimal_solutions_num)


# Conducts the calculations for part 2 of the homework
def part2():
  total_candidates = 100
  total_experiments = 10000

  solution_found_99, optimal_solution_found_99, optimal_answer_99 = findOptimalWithWeight(
    total_candidates, 
    total_experiments, 
    True)
  solution_found_norm, optimal_solution_found_norm, optimal_answer_norm = findOptimalWithWeight(
    total_candidates,
    total_experiments, 
    False)

  finalizeResults(optimal_answer_99, optimal_solution_found_99, "Uniform")
  finalizeResults(optimal_answer_norm, optimal_solution_found_norm, "Normal")


def main():
  help = """
  Invalid command line arguments. 
  Please enter which part of the homework you would like to run (either part1 or part2). 
  If you choose part1, follow that with the name of the csv file that you would like to use. 
  """
  length = len(sys.argv)

  if length == 2:
    if sys.argv[1] == "part2":
      part2()
    else:
      print(help)
      return
  elif length == 3:
    if sys.argv[1] == "part1":
      part1(sys.argv[2])
    else:
      print(help)
      return
  else:
    print(help)
    return

main()