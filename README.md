# Collatz Conjecture Visualizer

A proof of concept visualizer script for the infamous Collatz Conjecture mathematic problem. Written in Python. Uses Matplotlib to plot the lines onto a graph.

## Collatz Conjecture

The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

## How the script works

The script works in three parts.

1. **_Input._** The user is asked to input a starting seed & an ending seed. The script will then create a new list variable with values ranging from the start seed to the end seed.

2. **_The conjecture algorithm._** The script will start a for loop that iterates through every seed in the seedlist. Every seed is used as the starting value for the y-coordinate list. A nested while loop will then iterate (following the Collatz Conjecture rules) until the value < 1, adding the value into the y-coordinate list during every iteration of the while loop. Finally, once the while loop resolves (value < 1) the x-coordinate list will be created by measuring the length of the y-coordinate list.

3. **_Plotting & displaying the graph_** Finally, the script will plot a line corresponding to the x & y lists onto the graph (using matplotlib), before starting a new iteration of the for loop.
