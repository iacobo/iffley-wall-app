<div align="center">

![Alt text](img/icon.png?raw=true "Icon")

## The Iffley Wall Interactive Guide

</div>

 An interactive guide to the Iffley bouldering wall. Click here to run the program in interactive mode:

 <div align="center">

 [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iacobo/iffley-wall-app/blob/main/notebook.ipynb)

 </div>

### Running locally

Alternatively you can run the script natively. First create and activate a virtual environment:

```python
conda env create -f environment.yml
conda activate env-iffley
```

Then use one of the following commands, specifying the route or holds to highlight:

Command⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  | Output
--------|-------
`python main.py --route "The Rocker"` | ![Alt text](img/rocker.png?raw=true "The Rocker")
`python main.py --holds 1 14 40 62` | ![Alt text](img/holds.png?raw=true "Holds")
`python main.py --all` | ![Alt text](img/all.png?raw=true "Holds")

### Key

- 🟧 <span style="color:orange">Orange</span>: standing start holds
- 🟥 <span style="color:red">Red</span>: general holds in the route
- 🟦 <span style="color:blue">Blue</span>: final hold

If there are no orange holds then it is a sit start. Sit start starting holds *should be* intuitive.
