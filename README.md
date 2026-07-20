<div align="center">

# 🐍 Python, DSA & Generative AI — Learning Notebooks

> A structured collection of Jupyter Notebooks covering **Python fundamentals**, **Data Structures & Algorithms**, and **Generative AI / NLP** from scratch.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

</div>

---

## 📖 About

This repository is a self-paced study journal for mastering **Python programming**, **Data Structures & Algorithms (DSA)**, and **Generative AI / NLP fundamentals**. Each topic is covered in its own interactive Jupyter Notebook (or polished Markdown study note), with code examples, explanations, and practice problems.

Whether you're a beginner starting with Python or someone brushing up on data science and GenAI concepts, this repo has something for you.

---

## 📂 Repository Structure

The repo is organized into three top-level tracks:

```
DSA-In-Python-GenAI/
├── PythonTutorial/     # Core Python language fundamentals + a small OOP project
├── DataScience/        # NumPy, Pandas, and hands-on practice notebooks
└── GenerativeAI/       # NLP preprocessing, text representation & GenAI study notes
```

### 🐍 PythonTutorial/

| # | Notebook | Topics Covered |
|---|----------|----------------|
| 01 | [`01IntroPython.ipynb`](./PythonTutorial/01IntroPython.ipynb) | Python intro, installing & importing packages (NumPy, Pandas, Matplotlib, Seaborn) |
| 02 | [`02Variables.ipynb`](./PythonTutorial/02Variables.ipynb) | Variables, data types, type casting |
| 03 | [`03String.ipynb`](./PythonTutorial/03String.ipynb) | Strings, slicing, methods, formatting |
| 04 | [`04Condition.ipynb`](./PythonTutorial/04Condition.ipynb) | `if`, `elif`, `else` — conditional statements |
| 05 | [`05Operators.ipynb`](./PythonTutorial/05Operators.ipynb) | Arithmetic, logical, bitwise & comparison operators |
| 06 | [`06TimeAndSpace.ipynb`](./PythonTutorial/06TimeAndSpace.ipynb) | Big-O notation, time & space complexity, asymptotic analysis |
| 07 | [`07Loops.ipynb`](./PythonTutorial/07Loops.ipynb) | `for`, `while`, nested loops, `break` & `continue` |
| 08 | [`08Function.ipynb`](./PythonTutorial/08Function.ipynb) | Functions, arguments, return values, scope |
| 09 | [`09List.ipynb`](./PythonTutorial/09List.ipynb) | Lists, list operations, comprehensions |
| 10 | [`10Tupple.ipynb`](./PythonTutorial/10Tupple.ipynb) | Tuples, immutability, use cases |
| 11 | [`11Dictionary.ipynb`](./PythonTutorial/11Dictionary.ipynb) | Dictionaries, key-value pairs, methods |
| 12 | [`12Set.ipynb`](./PythonTutorial/12Set.ipynb) | Sets, set operations (union, intersection, difference) |
| 12 | [`12Lambda.ipynb`](./PythonTutorial/12Lambda.ipynb) | Lambda functions, `map()`, `filter()`, `reduce()` |
| 13 | [`13Oops_part1.ipynb`](./PythonTutorial/13Oops_part1.ipynb) | Classes, objects, abstraction, encapsulation, `del` |
| 13 | [`13oops_part2.ipynb`](./PythonTutorial/13oops_part2.ipynb) | More OOP practice (ATM machine, Fraction class, etc.) |
| — | [`oops/book_reservation/`](./PythonTutorial/oops/book_reservation) | A small multi-file OOP project (`movie.py`, `customer.py`, `booking.py`, `main.py`) applying encapsulation with a driver script |

### 📊 DataScience/

| Notebook | Topics Covered |
|----------|-----------------|
| [`01_Introduction_numpy.ipynb`](./DataScience/01_Introduction_numpy.ipynb) | NumPy arrays, creation, attributes, indexing/slicing, reshaping, stacking/splitting |
| [`02_numpy_advanced.ipynb`](./DataScience/02_numpy_advanced.ipynb) | Vectorization speed/memory, advanced indexing, broadcasting, ML loss functions (MSE, BCE, CCE), meshgrids |
| [`03_numpy_tricks.ipynb`](./DataScience/03_numpy_tricks.ipynb) | Cheat-sheet of frequently used NumPy functions (`sort`, `where`, `argmax`, `clip`, set functions, etc.) |
| [`04_pandas_series.ipynb`](./DataScience/04_pandas_series.ipynb) | Pandas `Series` — creation, attributes, indexing, editing, boolean filtering |
| [`05_pandas_dataframes.ipynb`](./DataScience/05_pandas_dataframes.ipynb) | Pandas `DataFrame` — creation, selection (`loc`/`iloc`), filtering, adding columns, dtype tuning |
| [`content/`](./DataScience/content) | Sample datasets used by the notebooks above (movies, IPL matches, subscriber counts, etc.) |
| `Task_01_NumPy_intro.ipynb` → `Task_06_Pandas_DataFrame_2.ipynb` | Standalone practice problem sets for NumPy and Pandas |

### 🤖 GenerativeAI/

| Folder | Contents |
|--------|----------|
| [`01_Data_Preprocessing/`](./GenerativeAI/01_Data_Preprocessing) | Text preprocessing notebook + study note — cleaning, tokenization, IMDB sentiment dataset |
| [`02_Data_Representation/`](./GenerativeAI/02_Data_Representation) | Word embeddings, text representation & ML-based text classification notebooks + study note |
| [`03_Generating_AI/`](./GenerativeAI/03_Generating_AI) | Polished Markdown study notes: intro to GenAI/LLMs, data representation & vectorization, text classification & preprocessing, large language models, and transformers in depth |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/) (Python 3.8 or higher recommended)
- [Git](https://git-scm.com/downloads) (for cloning the repository)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/pratham1659/DSA-In-Python-GenAI.git
   cd DSA-In-Python-GenAI
   ```

2. **Create a virtual environment** (strongly recommended)
   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

   > **Note**: You should see `(venv)` in your terminal prompt when the virtual environment is active.

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

   Or launch JupyterLab for a more modern interface:
   ```bash
   jupyter lab
   ```

5. **Open any `.ipynb` file and start learning!** 🎉

### Virtual Environment Management

**Activating the environment** (do this every time you work on the project):
```bash
# Navigate to project directory
cd path/to/DSA-In-Python-GenAI

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

**Deactivating the environment** (when you're done working):
```bash
deactivate
```

**Verifying your setup**:
```bash
# Check if you're in the virtual environment
which python  # Should show path to venv/bin/python

# Check installed packages
pip list

# Test key imports
python -c "import numpy, pandas, matplotlib, seaborn, sklearn, jupyter; print('All packages imported successfully!')"
```

### Troubleshooting

**Common Issues:**

1. **Virtual environment not activating**: Make sure you're in the correct directory and the `venv` folder exists.

2. **Package installation fails**: Try upgrading pip first:
   ```bash
   pip install --upgrade pip
   ```

3. **Jupyter not found**: Make sure you've activated the virtual environment before running jupyter commands.

4. **Import errors in notebooks**: Ensure your Jupyter kernel is using the virtual environment:
   ```bash
   python -m ipykernel install --user --name=venv --display-name="Python (DSA-GenAI)"
   ```

---

## 🧠 Concepts Covered

### 🐍 Python Fundamentals
- Variables & Data Types
- Strings & String Manipulation
- Conditional Statements & Operators
- Loops (for, while)
- Functions & Scope
- Lists, Tuples, Dictionaries & Sets
- Lambda & Higher-Order Functions
- Object-Oriented Programming (classes, abstraction, encapsulation, mini OOP project)

### ⏱️ Data Structures & Algorithms (DSA)
- Time Complexity (Big-O Notation)
- Space Complexity
- Asymptotic Analysis (Best, Average, Worst Case)

### 📊 Data Science
- NumPy arrays, indexing, broadcasting, and vectorized math
- Common ML loss functions (MSE, Binary & Categorical Cross-Entropy)
- Pandas `Series` and `DataFrame` fundamentals
- Practice problem sets applying NumPy & Pandas to real datasets

### 🤖 Generative AI / NLP
- Text preprocessing & tokenization
- Text representation and word embeddings
- Text classification with classical ML
- Large Language Models (LLMs) and Transformers, explained from first principles

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| `Python 3.x` | Core programming language |
| `Jupyter Notebook` | Interactive coding environment |
| `NumPy` | Numerical computing |
| `Pandas` | Data manipulation |
| `Matplotlib` | Data visualization |
| `Seaborn` | Statistical data visualization |
| `scikit-learn` | Classical machine learning |
| `Plotly` | Interactive visualization |
| `ipywidgets` | Interactive notebook widgets |

See [`requirements.txt`](./requirements.txt) for exact pinned versions.

---

## 📈 Roadmap

- [x] Python Basics (Variables, Strings, Conditions, Loops)
- [x] Functions & Data Structures (Lists, Tuples, Dicts, Sets)
- [x] Time & Space Complexity
- [x] Object-Oriented Programming (classes, abstraction, encapsulation)
- [x] NumPy & Pandas fundamentals + practice notebooks
- [x] GenAI/NLP fundamentals (preprocessing, embeddings, LLMs, Transformers)
- [ ] Arrays & Searching Algorithms
- [ ] Sorting Algorithms (Bubble, Merge, Quick Sort)
- [ ] Recursion & Backtracking
- [ ] Linked Lists
- [ ] Stacks & Queues
- [ ] Trees & Graphs
- [ ] Dynamic Programming

---

## 👤 Author

**Pratham Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-pratham1659-black?logo=github)](https://github.com/pratham1659)

---

## 📄 License

No license has been chosen for this project yet — all rights reserved by default. If you'd like to reuse this material, please reach out first.

---

<div align="center">

⭐ **If you found this helpful, please give it a star!** ⭐

*Happy Learning & Keep Coding!* 🚀

</div>
