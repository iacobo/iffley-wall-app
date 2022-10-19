<div align="center">

![Alt text](img/icon.png?raw=true "Icon")

## The Iffley Wall Interactive Guide

</div>

### Running locally

First create and activate a virtual environment:

```shell
conda env create -f environment.yml
conda activate env-iffley
```

Then use one of the following commands, specifying the route or holds to highlight:

Command⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀| Output
--------|-------
`python main.py --route "The Rocker"` | ![Alt text](img/routes/The%20Rocker.png?raw=true "The Rocker")
`python main.py --holds 1 14 40 62` | ![Alt text](img/holds.png?raw=true "Holds")
`python main.py --all` | ![Alt text](img/all.png?raw=true "Holds")

### Interactive mode

Alternatively you can run the interactive notebook. Type in the name of a route or holds and run the appropriate cell to highlight them: [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iacobo/iffley-wall-app/blob/main/notebook.ipynb)

### Key

- 🟨 <span style="color:yellow">Yellow</span>: standing start holds
- 🟩 <span style="color:lime">Green</span>: general holds in the route
- 🟥 <span style="color:red">Red</span>: final hold

### Info

- If there are no orange holds then it is a sit start.
- Sit starts consist of any hold you can reach while seated (usually with a foot on the first hold).
- You do not need to match hands on the final hold.
