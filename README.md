# US-Insurance-Data

This end-to-end machine learning project leverages US insurance data to train a model for predicting insurance premiums. It includes an API, containerized for deployment, and a user-friendly interface. This repository showcases a complete data science workflow, from model development to deployment.

## Table of Contents

1. [About The Project](#about-the-project)
     
    1.1 [Features](#features)
2. [Built With](#built-with)
3. [Getting Started](#getting-started)
     
    3.1 [Prerequisites](#prerequisites)
   
    3.2 [Installation](#installation)
   
4. [Usage](#usage)
   
    4.1 [Training](#training)
   
    4.2 [Evaluation](#evaluation)
   
    4.3 [Inference](#inference)
   
8. [Dataset](#dataset)
9. [Model Architecture](#model-architecture)
10. [Experiments](#experiments)
11. [Results](#results)
12. [Contributing](#contributing)
13. [License](#license)
14. [Contact](#contact)
15. [Acknowledgments](#acknowledgments)

## **About The Project**

This project predicts US insurance premiums using features like age, sex, BMI, children, smoking status, and region. Designed for modularity and scalability, it enables seamless experimentation with different algorithms.

### Features

- **Data Preprocessing:** Automated scripts to clean and transform raw data.
- **Model Training:** Well-documented training pipelines with customizable hyperparameters.
- **Evaluation Metrics:** Comprehensive evaluation of model performance.
- **Inference Pipeline:** Ready-to-use scripts for running predictions on new data.

## Built With

- [Python](https://www.python.org/) – Programming language.
- [NumPy](https://numpy.org/) – Numerical computing.
- [Scipy](https://scipy.org/) - Fundamental algorithms for scientific computing in Python
- [Pandas](https://pandas.pydata.org/) – Data manipulation and analysis.
- [scikit-learn](https://scikit-learn.org/) – Machine learning algorithms.
- [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/) – Data visualization.
- [FastAPI](https://fastapi.tiangolo.com/) – Web framework for building APIs with Python.

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Just-Aymz/US-Insurance-Data.git
   
2. **Navigate to the project directory:**
    ```bash
    cd US-Insurance-Data

3. **Create and activate a virtual environment:**
      ```bash
      python -m venv env
      # On Unix or MacOS:
      source env/bin/activate
      # On Windows:
      env\Scripts\activate

4. **Install the required packages:**
    ```bash
     pip install -r requirements.txt

## Usage

### Training
      ```bash
      python train.py --config config.yaml


