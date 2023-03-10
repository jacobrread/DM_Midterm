import matplotlib.pyplot as plt
import numpy as np
import math


class Call_Payoff:

    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price > self.strike:
            return stock_price - self.strike
        else:
            return 0


class GeometricBrownianMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            if change_volatility and self.T < 0.5 and not self.volatilityHasChanged:
                self.volatility = 0.19
                self.volatilityHasChanged = True
                print("changed volatility to 0.19")

            dWt = np.random.normal(0, math.sqrt(self.dt))  # Brownian motion
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Account for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.volatilityHasChanged = False
        self.simulate_paths()


# Plot the generated path
def graph(price_path):
    plt.plot(price_path)    
    plt.ticklabel_format(style='plain')
    plt.xlabel('Months')
    plt.ylabel('Price')
    plt.title("Franchise Value")
    plt.show()   


def run():
    # Generate a path
    price_path = GeometricBrownianMotion(initial_price, drift, volatility, dt, T).prices

    # Round the prices to the nearest cent
    for i in range(len(price_path)):
        price_path[i] = round(price_path[i], 2)

    ec = Call_Payoff(initial_price)
    risk_free_rate = .01

    call_payoff = (ec.get_payoff(price_path[-1])/(1 + risk_free_rate))  # We get the last stock price in the series generated by beta motion to determine the payoff and discount it by one year
    final_price = (price_path[-1])

    print(f"Value of franchise after {int(1 / dt) * T} days: $", round(final_price, 2))
    print("European value of Franchise with payoff: $", round(call_payoff, 2))

    if max(price_path) > desired_price:
        print("The American option reached at time {}".format(price_path.index(max(price_path)) * dt))

    print("The American option value is {}".format(max(price_path)))

    graph(price_path)


# Model Parameters
initial_price = 385000
desired_price = 535000
drift = 0.04 / 12
volatility = .03
dt = 1/120
T = 1
change_volatility = True

run()
