# MuJoCo Modelling Study

## Introduction

This repository is meant to contain knowledge i obtained while creating
simulations for Google DeepMind's [MuJoCo simulator](https://mujoco.org).
As of today (17/04/2025) the documentation of MuJoCo is not very beginner
friendly, even though it is extense and contains many tutorials. The path is
not straightfoward on how to create simulations containing complex models,
terrains and custom robots and that is problematic considering that MuJoCo is
the most utilized simulator in reinforcement learning research [1].

We have 3 objectives in this repository:
- Create an uneven terrain for a quadruped robot control RL task for a [Spot](https://bostondynamics.com/products/spot/) robot;
- Create a functional MJCF file for a [DENSO VS-050](https://www.denso-wave.com/en/robot/product/five-six/vs050-060.html) robot and a scene for a pick
  and place RL task;
- Create a functional MJCF file for a [ROSbotXL](https://husarion.com/manuals/rosbot-xl/overview/) and a scene for a imitation learning task;
- Present tutorials for modelling more complex scenes for MuJoCo using real
  robots models

The choice for these robots, except for Spot, is justified by the fact that currently i am a
scholarship holder at [Softex's Robotics and AI](https://residenciarobotica.cin.ufpe.br) laboratory at the Federal University
of Pernambuco and these are the equipment we possess to pursue our research.

### Project Files

```
mujoco-study
│   denso_test.xml--┰-> MJCF scene files. Includes models, terrains, skyboxes, etc. 
│   spot_test.xml---┤
│   sandbox.xml-----┘
└───assets--> Folder containing folders with the assets (.obj, .stl, etc) of each model being used
│   │   denso
│   │   spot
│   │   chair
│   |   terrain
└───models--> MJCF files for each different model
    │   chair.xml
    │   denso_vs050.xml
    |   spot.xml
    |   spot_arm.xml
    |   my_mj_terrain.xml
run_simulation.py--> Python file that receives the path to a scene file as argument.
squares_png_test.py
```

### Useful Tutorials Links
[MuJoCo official documentation](https://mujoco.readthedocs.io/en/stable/overview.html)

[Simulating YOUR robot in MuJoCo, Yasunori Toshimitsu](https://yasunori.jp/en/2024/07/13/mujoco-model-yourself.html)


### References
[1] [A Review of Nine Physics Engines for Reinforcement Learning Research](https://arxiv.org/pdf/2407.08590)