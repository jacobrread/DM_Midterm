import matplotlib.pyplot as plt
import numpy as np

from solvers import Solver

def plot_results(solvers, solver_names, figname):
    """
    Plot the results by multi-armed bandit solvers.

    Args:
        solvers (list<Solver>): Solver objects.
        solver_names (list<str): Names of the solvers.
        figname (str): Name of the figure to save.
    """
    assert len(solvers) == len(solver_names)
    assert all(map(lambda s: isinstance(s, Solver), solvers))
    assert all(map(lambda s: len(s.loss) > 0, solvers))

    # # Plot loss in time.
    # plt.figure(figsize=(7, 6))
    
    # for i, s in enumerate(solvers):
    #     plt.plot(range(len(s.loss)), s.loss, label=solver_names[i])

    # plt.xlabel("Step")
    # plt.ylabel("Loss")
    # plt.legend(loc='upper left', shadow=True)
    # plt.show()
    # plt.close()

    b = solvers[0].bandit

    fig = plt.figure(figsize=(16, 8))
    fig.subplots_adjust(bottom=0.3, wspace=0.3)

    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)

    # Sub.fig. 1: loss in time.
    for i, s in enumerate(solvers):
        ax1.plot(range(len(s.loss)), s.loss, label=solver_names[i])

    ax1.set_xlabel('Time step')
    ax1.set_ylabel('Cumulative regret')
    ax1.legend(loc=9, bbox_to_anchor=(1.82, -0.25), ncol=5)
    ax1.grid('k', ls='--', alpha=0.3)

    # Sub.fig. 2: Probabilities estimated by solvers.
    sorted_indices = sorted(range(b.n), key=lambda x: b.probas[x])
    ax2.plot(range(b.n), [b.probas[x] for x in sorted_indices], 'k--', markersize=12)
    for s in solvers:
        ax2.plot(range(b.n), [s.estimated_probas[x] for x in sorted_indices], 'x', markeredgewidth=2)
    ax2.set_xlabel('Actions sorted by ' + r'$\theta$')
    ax2.set_ylabel('Estimated')
    ax2.grid('k', ls='--', alpha=0.3)

    # Sub.fig. 3: Action counts
    for s in solvers:
        ax3.plot(range(b.n), np.array(s.counts) / float(len(solvers[0].loss)), ls='solid', lw=2)
    ax3.set_xlabel('Actions')
    ax3.set_ylabel('Frac. # trials')
    ax3.grid('k', ls='--', alpha=0.3)

    plt.savefig(figname)
