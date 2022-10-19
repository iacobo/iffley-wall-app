<div align="center">

![Alt text](img/icon.png?raw=true "Icon")

## The Iffley Wall Interactive Guide

</div>

A digital guide to the Iffley Bouldering Wall in Oxford. Highlights historic routes from the Iffley Wall Guidebook, and allows users to view custom routes.

### Running locally

First create and activate a virtual environment:

```shell
conda env create -f environment.yml
conda activate env-iffley
```

Then use one of the following commands, specifying the route or holds to highlight:

Command⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀| Output
--------|-------
`python main.py --route "My Name is Neo"` | ![Alt text](img/routes/My%20Name%20is%20Neo.png?raw=true "My Name is Neo")
`python main.py --holds 1 14 40 62` | ![Alt text](img/examples/holds.png?raw=true "Holds")
`python main.py --all` | ![Alt text](img/examples/all.png?raw=true "Holds")

### Interactive mode

Alternatively you can run the interactive notebook. Type in the name of a route or holds and run the appropriate cell to highlight them: [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iacobo/iffley-wall-app/blob/main/notebook.ipynb)

### Key

- 🟨 <span style="color:yellow">Yellow</span>: standing start holds
- 🟩 <span style="color:lime">Green</span>: general holds in the route
- 🟥 <span style="color:red">Red</span>: final hold

### Info

- If there are no yellow holds then it is a sit start.
- Sit starts consist of any hold you can reach while seated (usually with a foot on the first hold).
- You do not need to match hands on the final hold.
