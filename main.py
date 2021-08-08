### Author: Atte Tarkiainen ###
### Build Date: 08/08/2021 ###
### Dependencies: Matplotlib ###

import matplotlib.pyplot as plt

start = int(input("Please enter the first seed to start iterating from: "))
stop = int(input("Please enter the last seed to stop iterating on: "))

seedlist = list(range(start, stop + 1))

for seed in seedlist:
    value = seed
    y = []
    x = []
    y.append(value)
    # Collatz Conjecture Algorithm
    while (value > 1):
        if (value % 2 == 0):
            value = value / 2
            y.append(value)
        else:
            value = (value * 3) + 1
            y.append(value)

    # Plotting the line onto the graph
    x = list(range(1, len(y) + 1))
    plt.plot(x, y, color="red", marker="o",
             markerfacecolor="black", markersize="2")

plt.title('Collatz Conjecture Visualizer!')
plt.show()
