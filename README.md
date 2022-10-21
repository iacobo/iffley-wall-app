<div align="center">

![Alt text](img/icon.png?raw=true "Icon")

## Digital Iffley Wall Guide

</div>

A digital guide to the Iffley Bouldering Wall in Oxford. Provides topos for routes from the [Iffley Bouldering Guide](https://www.oxfordalpineclub.uk/shop.php#!/Iffley-10-The-Iffley-Bouldering-Guide/p/59136024/category=10367386), and allows users to create and view custom routes.

- You can browse route topos [here](img/routes/)
- The original guide is available as a pdf [here](img/Iffley%20Bouldering%20Guide.pdf?raw=true)

### Running locally

First create and activate a virtual environment:

```shell
conda env create -f environment.yml
conda activate env-iffley
```

Then use one of the following commands, specifying the route or holds to highlight:

⠀⠀⠀⠀⠀Command⠀⠀⠀⠀⠀| Output
:--------:|:-------:
`python main.py --holds 2 14 42 44 96` | ![Alt text](img/examples/holds.png?raw=true "Holds")
`python main.py --route "This is a Low"` | ![Alt text](img/routes/thisisalow.png?raw=true "This is a Low")

### Interactive mode

Alternatively you can run the interactive notebook. Type in the name of a route or holds and run the appropriate cell to highlight them: [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iacobo/iffley-wall-app/blob/main/notebook.ipynb)

---

### Key

- 🟨 <span style="color:yellow">Yellow</span>: standing start holds
- 🟩 <span style="color:lime">Green</span>: general holds in the route
- 🟥 <span style="color:red">Red</span>: final hold

### Info

- If there are no yellow holds then it is a sit start.
- Sit starts consist of any hold you can reach while seated (usually with a foot on the first hold).
- You do not need to match hands on the final hold.
