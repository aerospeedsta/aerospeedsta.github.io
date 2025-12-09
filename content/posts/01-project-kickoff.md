---
title: "Project Launch: GPU-Accelerated Safety for High-Dimensional Dynamics"
date: 2025-10-27
project_id: "fno-reachability"
summary: "Why standard Hamilton-Jacobi reachability fails in high dimensions and how Neural Operators could fix it."
tags: ["control-theory", "deep-learning", "research"]
---

## The Problem: The Curse of Dimensionality

Safety-critical control often relies on Hamilton-Jacobi (HJ) reachability analysis to guarantee that a system (like a drone or satellite) will never enter an unsafe state. The core challenge is that the computational cost of solving the HJ partial differential equation scales exponentially with the number of state dimensions.

For a 3-DOF Dubins car, it takes seconds. For a 12-DOF quadrotor, it is mathematically impossible on standard grids.

## The Solution: Neural Surrogates

This project explores using **Fourier Neural Operators (FNOs)** to approximate the solution operator of the HJ PDE. Instead of solving the grid point-by-point, we train an operator to map system conditions directly to the Value Function $V(x)$.

### Initial Benchmark: 3-DOF Dubins Car

To establish a ground truth baseline, I have implemented a PyTorch-based Godunov scheme solver. Below is the computed Backward Reachable Set (BRS) for a standard Dubins car avoiding a target at the origin.

{{< plotly json="/data/dubins_reachset.json" id="fig1" height="600px" >}}

*Figure 1: The computed Backward Reachable Set (BRS). Any state inside this tube will inevitably hit the target set within T=1.0s.*

## Next Steps
1.  Train an FNO to reproduce this surface from sparse data.
2.  Compare inference time (GPU) vs. the Grid Solver (CPU).
