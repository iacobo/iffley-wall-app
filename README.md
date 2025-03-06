<div align="center">

<img src=".assets/img/icon.svg" width="100">

# Digital Iffley Wall Guide

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) ![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)

</div>

A digital guide to the [Iffley Bouldering Wall](https://users.ox.ac.uk/~climbing/ACTIVITIES/indoor.shtml) in Oxford. Provides topos for routes from the [Iffley Bouldering Guide](https://www.oxfordalpineclub.uk/shop.php#!/Iffley-10-The-Iffley-Bouldering-Guide/p/59136024/category=10367386) ([pdf](.assets/Iffley%20Bouldering%20Guidebook.pdf?raw=true)), and allows users to create and view custom routes. You can browse routes along with topos here:

<div align="center">

### 🪨 [All routes](static/topos.md)

### 🪨 [Tick Lists](static/ticklists.md)

### 🪨 [Circuits](static/circuits.md)

</div>

---

## Custom routes

You can run the script used to create this guide yourself and display your own custom routes. First create and activate a virtual environment:

```shell
conda env create -f environment.yml
conda activate env-iffley
```

Then use one of the following commands, specifying the holds (or route) to highlight:

```shell
>>> python main.py --holds 2 14 42 44 96
```

> ![Alt text](.assets/img/examples/holds.png?raw=true "Holds")

```shell
>>> python main.py --route "This is a Low"
```

> ![Alt text](.assets/img/routes/thisisalow.png?raw=true "This is a Low")
