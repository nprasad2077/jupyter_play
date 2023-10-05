# jupyter_play
Data Science Fun


## Creating the Python (conda) environment

- First, create the conda environment. Specify env name and python version.

```bash
conda create -n myenv python=3.8
```

- To activate environment:

```bash
conda activate myenv
```

- Next, Install Jupyter:

```bash
conda install jupyter
```

- Start Jupyter Notebook: 

```bash
jupyter notebook
```

- Access Jupyter Notebook at http://localhost:8888

---

- Be sure to lock all dependencies and include in repository (execute in shell). This will create a requirements.txt file in your project directory, listing all the libraries in your environment along with their versions.

```bash
pip freeze > requirements.txt
```

