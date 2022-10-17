<div align="center">

## The Iffley Wall Interactive Guide

![Alt text](img/icon.png?raw=true "Icon")

</div>

 An interactive guide to the Iffley bouldering wall.

 To run, first create and activate a virtual environment:

```python
conda env create -f environment.yml
conda activate env-iffley
```

Clik here to run the program in interactive mode:

 [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iacobo/iffley-wall-app/blob/main/notebook.ipynb)

Alternatively you can run the script natively, specifying the (named) route or holds to highlight:

Command⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  | Output
--------|-------
`python main.py --route "The Rocker"` | ![Alt text](img/rocker.png?raw=true "The Rocker")
`python main.py --holds 1 14 40 62` | ![Alt text](img/holds.png?raw=true "Holds")
`python main.py --all` | ![Alt text](img/all.png?raw=true "Holds")

### Key

- 🟧 <span style="color:orange">Orange</span> holds are standing start holds
- 🟥 <span style="color:red">Red</span> holds are general holds in the route
- 🟦 <span style="color:blue">Blue</span> hold is final hold in the route

If there are no orange holds then it is a sit start. Sit start starting holds *should be* intuitive.
