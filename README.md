# CSC-333-OR-Linear-Programming-Solutions

This repository contains solutions to various Linear Programming (LP) problems from CSC 333 - Computational Science and Numerical Methods. The solutions are provided in two formats:

    Hand-solved solutions (scanned images or PDFs).
    Python graphical solutions using libraries like matplotlib, numpy, and pulp.

Problem Description

The assignment consists of solving multiple LP problems, each with its unique objective (maximizing profit, minimizing cost, etc.) and constraints. The problems involve finding optimal solutions for scenarios like factory production, resource allocation, advertising budget optimization, and more. Below is a summary of the problems:

    Maximizing Profit for a Factory:
        A factory produces two products with constraints on machine time and raw materials. The objective is to maximize profit.
    Minimizing Cost for a Manufacturer:
        A company manufactures two products with constraints on labor and materials. The objective is to minimize production cost.
    Maximizing Production with Multiple Resources:
        A factory produces two products using labor, materials, and machine time. The goal is to maximize profit.
    Maximizing Revenue from Sales:
        A company sells two products under constraints of advertising budget and production capacity to maximize revenue.
    Resource Allocation for Two Projects:
        Allocating labor hours and capital to maximize profits for two projects.
    Production Planning for a Bakery:
        A bakery must allocate resources between chocolate and vanilla cakes to maximize profit.
    Minimizing Cost for a Transport Company:
        Optimizing trips for two types of vehicles with constraints on fuel and driver time.
    Maximizing Revenue from Two Products:
        A company optimizes labor, materials, and machine time for two products to maximize revenue.
    Advertising Campaign Budget Allocation:
        Allocating a budget across advertising campaigns to maximize audience reach.
    Meal Planning for a School Cafeteria:
        Allocating resources for two types of meals to maximize revenue.

Steps for Solving the LP Problems

Each LP problem is solved using two approaches:
Hand-Solved Graphical Method:

    Identify Constraints:
        Convert the problem statements into mathematical inequalities.
    Graph Constraints:
        Plot each constraint line by finding intercepts.
        Shade the feasible region where all constraints overlap.
    Find Corner Points:
        Solve equations at the intersections of constraint lines to find the vertices of the feasible region.
    Evaluate Objective Function:
        Substitute each vertex into the objective function to find the optimal solution.

Python Graphical Solution:

    Setup Environment:
        Install necessary libraries using pip install matplotlib numpy pulp.
    Define the Problem:
        Represent constraints as inequalities.
        Define the objective function.
    Plot Constraints and Feasible Region:
        Use matplotlib to graph constraints and shade the feasible region.
    Optimize Using Linear Programming:
        Use pulp or scipy.optimize.linprog to calculate the optimal solution programmatically.

How to Run the Python Code
Requirements:

    Python 3.x
    Libraries: matplotlib, numpy, pulp

Steps:

    Clone this repository to your local machine:

git clone https://github.com/<your-username>/CSC-333-OR-Linear-Programming-Solutions.git

Navigate to the project directory:

cd CSC-333-OR-Linear-Programming-Solutions

Open the Python file for the specific problem you want to solve (e.g., lp_graphical_solution.py) in your IDE or terminal.
Run the Python script:

    python lp_graphical_solution.py

    View the output:
        The script will display a graph showing constraints, the feasible region, and the optimal solution.
        The console will print the optimal values of variables and the objective function.

Repository Contents

    Hand-Solved-Solutions/: Contains scanned or photographed hand-drawn solutions.

    Python-Solutions/: Python scripts for solving each LP problem graphically.

    README.md: This guide.

Example Output
Problem 1: Maximizing Profit for a Factory

    Optimal Solution:
    X=4X=4, Y=2Y=2, Z=20Z=20 (maximum profit).

    Graph: Displays constraints, feasible region, and optimal solution.
