
import os
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

class Environment:

    def __init__(self, probs):
        self.probs = probs  # success probabilities for each arm

    def step(self, action):
        # Pull arm and get stochastic reward (1 for success, 0 for failure)
        return self.probs[action]

class Agent:

    def __init__(self, nActions, eps):
        self.nActions = nActions
        self.eps = eps
        self.n = np.zeros(nActions) # action counts n(a)
        self.Q = np.zeros(nActions) # value Q(a)

    def update_Q(self, action, reward):
        # Update Q action-value given (action, reward)
        self.n[action] += 1
        self.Q[action] += (1.0/self.n[action]) * (reward - self.Q[action])

    def get_action(self):
        # Epsilon-greedy policy
        if np.random.random() < self.eps: # explore
            return np.random.randint(self.nActions)
        else: # exploit
            return np.random.choice(np.flatnonzero(self.Q == self.Q.max()))


def get_probabilities(withArea0):
    probs = [
        np.random.beta(7, 3) + 2,
        np.random.uniform(0, 4),
        np.random.beta(3, 7) + 2,
        np.random.normal(2, 1.4),
        np.random.normal(1.3, 7),
    ]

    # Now assume that you have a baseline sensor: area0 = normal(1.5, 3)
    if withArea0:
        probs = [
            np.random.normal(1.5, 3),
            np.random.beta(7, 3) + 2,
            np.random.uniform(0, 4),
            np.random.beta(3, 7) + 2,
            np.random.normal(2, 1.4),
            np.random.normal(1.3, 7),
        ]
        # Negative values set to zero
        if probs[0] < 0:
            probs[0] = 0

    return probs


def get_area(num, withArea0):
    if withArea0:
        if num == 0:
            return "area0"
        elif num == 1:
            return "area1"
        elif num == 2:
            return "area2"
        elif num == 3:
            return "area3"
        elif num == 4:
            return "area4"
        elif num == 5:
            return "area5"
    else:
        if num == 0:
            return "area1"
        elif num == 1:
            return "area2"
        elif num == 2:
            return "area3"
        elif num == 3:
            return "area4"
        elif num == 4:
            return "area5"
        

# Start multi-armed bandit simulation
def experiment(probs, N_episodes):
    env = Environment(probs) # initialize arm probabilities
    agent = Agent(len(env.probs), eps)  # initialize agent
    actions, rewards = [], []
    for episode in range(N_episodes):
        action = agent.get_action() # sample policy
        reward = env.step(action) # take step + get reward
        agent.update_Q(action, reward) # update Q
        actions.append(action)
        rewards.append(reward)
    return np.array(actions), np.array(rewards)


# Plot reward results
def plot_reward(output_dir):
    R_avg =  R / float(N_steps)
    plt.plot(R_avg, ".")
    plt.xlabel("Step")
    plt.ylabel("Average Reward")
    plt.grid()
    ax = plt.gca()
    plt.xlim([1, N_steps])
    if save_fig:
        if not os.path.exists(output_dir): os.mkdir(output_dir)
        plt.savefig(os.path.join(output_dir, "rewards.png"), bbox_inches="tight")
    else:
        plt.show()
    plt.close()


# Plot action results
def plot_action(probs, actions, output_dir):
    for i in range(len(probs)):
        steps = list(np.array(range(len(actions)))+1)
        plt.plot(steps, actions, ".",
                linewidth=5,
                label="Arm {}".format(i+1))
    plt.xlabel("Step")
    plt.ylabel("Selection over Time")
    plt.xlim([1, N_steps])
    plt.ylim([-2, 6])
    if save_fig:
        if not os.path.exists(output_dir): os.mkdir(output_dir)
        plt.savefig(os.path.join(output_dir, "actions.png"), bbox_inches="tight")
    else:
        plt.show()
    plt.close()


def run(withArea0, output_dir, R):
    for i in range(N_steps):
        probs = get_probabilities(withArea0)
        actions, rewards = experiment(probs, N_steps)  # perform experiment
        R += rewards
        for j, a in enumerate(actions):
            A[j][a] += 1

    print("Chosen Area: {}".format(get_area(np.argmax(np.bincount(actions)), withArea0)))
    plot_reward(output_dir)
    plot_action(probs, actions, output_dir)


N_steps = 500 # number of steps (episodes)
eps = 0.1 # probability of random exploration (fraction)
save_fig = True # save file in same directory
output_dir1 = os.path.join(os.getcwd(), "output1")
output_dir2 = os.path.join(os.getcwd(), "output2")
R = np.zeros((N_steps)) # reward history sum
A = np.zeros((N_steps, 21)) # action history sum

# Without area0
run(False, output_dir1, R)
# With area0
run(True, output_dir2, R)