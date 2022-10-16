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
python main.py -route "The Great Escape"
python main.py -holds 7 2 42 43 64
```
