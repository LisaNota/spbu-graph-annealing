# Shortest Path Search Using Simulated Annealing

This project entails the implementation of an algorithm to find the shortest path in a graph using simulated annealing method. The project comprises two main parts: the algorithm implementation and a graphical user interface for visualization and interaction with the results.

## Project Structure

1. **Algorithm Implementation**:
    - The `annealing.py` file contains the implementation of the simulated annealing algorithm for finding the shortest path.
    - The `Annealing` class embodies the core functionality of the algorithm, including initialization, initial solution creation, distance calculation, and the annealing process itself.

2. **Graphical User Interface**:
    - The `graph_gui.py` file contains the `GraphGUI` class, which constructs a graphical interface for user interaction with the algorithm.
    - This interface enables users to create graphs by specifying the number of vertices and edges, as well as to initiate the shortest path search algorithm.

3. **Helper Functions**:
    - The `main.py` file contains the main function `main()`, which launches the user interface.
    - The `creating()` and `annealing_solution()` functions are utilized for graph creation and finding the shortest path, respectively.

## How to Use the Project

1. Run the program by executing the `main.py` file.
2. Enter the number of vertices in the graph and input the weighted edges in the format `(vertex_1, vertex_2, weight); (vertex_1, vertex_2, weight); ...`, where vertices are numbers from 0 to (number of vertices - 1).
3. Click the "Create Graph" button to build the graph based on the input data.
4. Set the algorithm parameters: initial temperature, cooling coefficient, and number of iterations.
5. Click the "Compute Optimal Path" button to initiate the algorithm and obtain the shortest path.
6. The resulting path and its length will be displayed on the screen.

## Dependencies

1. Python 3.x
2. Libraries:
    - `tkinter`
    - `matplotlib`
    - `networkx`

## Notes

- It's crucial to input weighted edges in the correct format and ensure that the graph is connected for the algorithm to work correctly.
- Make sure that the algorithm parameters provided are within reasonable limits for the task to achieve acceptable execution time.
