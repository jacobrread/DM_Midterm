import sys
import time
import graphing

from bandits import BernoulliBandit
from solvers import EpsilonGreedy, ThompsonSampling
from probabilities import get_probs

# Setup
steps = 10000
 

def calcFastestEpsilon(calc_times, test_solvers, names, num_machines, num_steps):
    """
    Calculate the fastest epsilon
    
    Args:
        calc_times (dict): Dictionary of calculation times
        test_solvers (list<Solver>): Solver objects.
        solver_names (list<str): Names of the solvers.
        num_machines (int): number of slot machines.
        numb_steps (int): number of time steps to try.
    """
    seconds = 10000
    print("\nCalculation times")
    for key, value in calc_times.items():
        if value < seconds:
            if key == "Thompson Sampling":
                continue
            seconds = value
            fastest = key
        print("\t{0}: {1:.4f} seconds".format(key, value))

    print("\nThe optimal {0} has a time of {1:.4f} seconds".format(fastest, seconds))
    graphing.plot_results(test_solvers, names, "results_{}_{}.png".format(num_machines, num_steps))


def runCalculation(num_steps, test_solvers, solver_names, use_drift):
    """
    Run the calculations
    
    Args:
        num_steps (int): number of time steps to try.
        test_solvers (list<Solver>): Solver objects.
        solver_names (list<str): Names of the solvers
    """
    calc_times = {}
    counter = 0
    for s in test_solvers:
        start = time.time()
        s.run(num_steps, use_drift)
        calc_times[solver_names[counter]] = time.time() - start
        counter += 1
        
    return calc_times


def experiment(use_drift):
    """
    Run a small experiment on solving a Bernoulli bandit with K slot machines,
    each with a randomly initialized reward probability.

    Args:
        num_machines (int): number of slot machines.
        numb_steps (int): number of time steps to try.
    """
    probs = get_probs(0, False)
    num_machines = len(probs)
    b = BernoulliBandit(num_machines, probs)
    print("Randomly generated Bernoulli bandit has reward probabilities:\n", b.probas)
    print("The best machine has index: {} and proba: {}".format(
        max(range(num_machines), key=lambda i: b.probas[i]), max(b.probas)))

    test_solvers = [
        EpsilonGreedy(b, 0.4),
        EpsilonGreedy(b, 0.1),
        EpsilonGreedy(b, 0.05),
        EpsilonGreedy(b, 0.01),
        ThompsonSampling(b)
    ]
    names = [
        'Epsilon 0.4',
        'Epsilon 0.1',
        'Epsilon 0.05',
        'Epsilon 0.01',
        "Thompson Sampling"
    ]

    calc_times = runCalculation(steps, test_solvers, names, use_drift)
    calcFastestEpsilon(calc_times, test_solvers, names, num_machines, steps)


def main():
    help = """
    Invalid command line arguments. 
    Please enter which part of the homework you would like to run (either '1' for part 1 or '2' for part 2). 
    """
    length = len(sys.argv)

    if length == 2:
        if sys.argv[1] == "1":
            experiment(False)
        elif sys.argv[1] == "2":
            experiment(True)
        else:
            print(help)
    else:
        print(help)

main()