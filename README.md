# UCS1504: Artificial Intelligence - Coursework

Programs, reports, documentation and screenshots implemented and designed for the laboratory coursework on UCS1504: Artificial Intelligence course.

## Quick References

### Path-finding in Plane with Abstract Polygonal Obstacles ([Exercise 5](/E5-PolygonalObstacles))

- Problem formulation and assumptions
  <img src="/E5-PolygonalObstacles/Documentation/Outputs/StateSpaceFormulation.png" width="750">
  
- Sample problem instance with illustrated result
  <img src="/E5-PolygonalObstacles/Documentation/Outputs/SampleProblem.png" width="750">

### State Space Diagram for The Decantation Problem ([Exercise 2](./E2-StateSpaceSearch(BFS)), [Exercise 4](./E4-StateSpaceSearch(BiDirectional)))
<img src="E2-StateSpaceSearch(BFS)/Documentation/StateSpace.png" width="750">

## Exercises

1. [Performance, Environment, Actuator, Sensor (PEAS) Description Formulation](./E1-PEASDescriptions)
    - For a face-recognition-based smart attendance system
    - For an online autonomous proctoring system
    - For a collaborative robotic system of agents that can contest in soccer contests
    - Draw a house using primitives
    - [Report](./E1-PEASDescriptions/Report.pdf) 
    <br><br>

2. [The Decantation Problem I](./E2-StateSpaceSearch(BFS))
    - State Space Representation Diagram
    - Solved with Breadth-first State Space Search (BFS)
    - [Documentation](./E2-StateSpaceSearch(BFS)/Documentation)
    - [Code on Replit](https://replit.com/@KarthikDesingu/Ex2-StateSpaceSearch-Decantation-Problem)
    <br><br>

3. [The Eight Puzzle Problem](./E3-EightPuzzle)
    - Solved using the traditional Breadth First Search (BFS) approach
    - Solved using the Bidirectional Breadth First Search (Bi-BFS) approach
    - [Documentation](./E3-EightPuzzle/Documentation) 
    <br><br>

4. [The Decantation Problem II](./E4-StateSpaceSearch(BiDirectional))
    - Solved using the Bidirectional Breadth First Search (Bi-BFS) approach
    - Solved using the Iterative Deepening Search approach
    - [Documentation](./E4-StateSpaceSearch(BiDirectional)/Documentation) 
    - [Code on Replit](https://replit.com/@KarthikDesingu/Ex4-DecantationProblem-IterativeDeepening)
    <br><br>
    
5. [The Eight Queens Problem I](./E5-EightQueens)
    - Solved using the Hill Climbing approach to find the first incident solution
    - Utility function defined in terms of the total number of attacks
    - [Documentation](./E5-EightQueens/Documentation) 
    - [Code on Replit](https://replit.com/@KarthikDesingu/Ex5-8QueensProblem-HillClimbing)
    <br><br>
    
6. [Polygonal Path Finding Problem](./E5-PolygonalObstacles)
    - Shortest path between two points in a plane with convex polygonal obstacles
    - Randomized problem instance generator implemented through code
    - Solved using the traditional Breadth First Search (BFS) approach
    - Solved using the Best First Greedy Search approach
    - Solved using the A-star (A*) Search approach
    - Empirical performance analysis through code of each search approach
    - [Documentation](./E5-PolygonalObstacles/Documentation) 
    - [Code on Replit](https://replit.com/@KarthikDesingu/Ex5B-PolygonalPlane-PathFinding)
    <br><br>
    
7. [The Eight Queens Problem II](./Ex6-GeneticAlgorithm)
    - Solved using the Genetic Algorithm approach to find the first incident solution
    - Utility function defined in terms of the total number of attacks
    - [Documentation](./Ex6-GeneticAlgorithm/Documentation) 
    - [Code on Replit](https://replit.com/@KarthikDesingu/Ex6-8QueensProblem-GeneticAlgorithm)
    <br><br>
    
8. [Arithmetic Expression Search](./Ex7-ExpressionSearch)
    - Use the given six integers to arithmetically arrive at a target expression result value
    - Four arithmetic operations are allowed with repitition: addition, subtraction, multiplication and division
    - No fraction may be introduced into the calculation 
    - Each given integer may be used at most once
    - If the exact target cannot be arrived at, find the expression with value closest to the target
    - State-space representation of problem is forulated
    - Solved using the Breadth First Search (BFS) approach
    - [Documentation](./Ex7-ExpressionSearch/Documentation) 
    <br><br>
    
## Other Implementations

- [Cut-Paste Sort Problem (Python and C++, both)](./P1-CutPasteSort)
- [Utility functions for BFS](./Reusables)
    
