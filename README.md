# iffley-wall-app

 An interactive guide to the Iffley bouldering wall.

 To run, first create and activate a virtual environment:

```python
conda env create -f environment.yml
conda activate env-iffley
```

Then run the main script for interactive mode:

```python
python main.py
```

You can also pre-specify the (named) route or holds to highlight:

```python
python main.py --route "The Rocker"
python main.py --holds 7 2 42 43 64
```

Key:

- Orange holds are standing start holds
- Red holds are general holds in the route (if no orange holds then it is a sit start,starting holds should be intuitive)
- Blue hold is final hold in the route
