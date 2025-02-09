# US Health Insurance Dataset

This project involves cleaning and preprocessing the US Health Insurance Dataset, training a machine learning model, and deploying it as an API using FastAPI. The API allows users to make predictions based on input data.

## Table of Contents

- [Dataset Identification](#dataset-identification)
  - [About this File](#about-this-file)
- [Project Overview](#project-overview)
- [Built With](#built-with)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Cloning the Repository](#cloning-the-repository)
  - [Creating a Virtual Environment](#creating-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Running the API Locally](#running-the-api-locally)
- [Running the API with Docker](#running-the-api-with-docker)
  - [Build the Docker Image](#build-the-docker-image)
  - [Run the Docker Container](#run-the-docker-container)
- [API Endpoints](#api-endpoints)
  - [Home Route](#home-route)
  - [Prediction Route](#prediction-route)
- [File Structure](#file-structure)
- [Future Enhancements](#future-enhancements)
- [Contact](#contact)
- [License](#license)

## Dataset Identification

### About this File

This dataset contains 1,338 rows of insured data, where insurance charges are given against the following attributes: Age, Sex, BMI, Number of Children, Smoker, and Region. The attributes consist of both numerical and categorical variables.

**Link to the dataset:** [Kaggle Dataset](https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset)

| Feature Name | Data Type | Description |
|-------------|-----------|-------------|
| Age | Integer | Age of primary beneficiary |
| Sex | String | Gender of the insurance contractor (male/female) |
| BMI | Float | Body mass index, indicating weight category |
| Children | Integer | Number of children covered by health insurance |
| Smoker | String | Whether the individual is a smoker (yes/no) |
| Region | String | Residential area in the U.S. (northeast, southeast, southwest, northwest) |
| Charges | Float | Individual medical costs billed by health insurance |

## Project Overview

- **Data Cleaning & Preprocessing:** Handled in [Data Cleaning & Preprocessing](./Data_Preprocessing.ipynb).
- **Model Training:** The best model is selected and saved as a pickle file ([best model](./best_model_and_preprocessor.pkl)).
- **FastAPI Implementation:** The API is built using FastAPI ([main.py](./main.py)).
- **Schema Definition:** [Schema.py](./Schema.py) defines input data validation using Pydantic.
- **Deployment:** The API is containerized for local deployment using Docker ([Dockerfile](./Dockerfile)).

## Built With

- [Python](https://www.python.org/) – Programming language.
- [NumPy](https://numpy.org/) – Numerical computing.
- [SciPy](https://scipy.org/) – Scientific computing algorithms.
- [Pandas](https://pandas.pydata.org/) – Data manipulation and analysis.
- [scikit-learn](https://scikit-learn.org/) – Machine learning algorithms.
- [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/) – Data visualization.
- [FastAPI](https://fastapi.tiangolo.com/) – Web framework for building APIs in Python.

## Installation

To run the API locally, follow these steps:

### Prerequisites

Ensure you have the following installed:

- Python (>=3.8)
- FastAPI
- Uvicorn
- Pandas, NumPy, Scikit-learn
- Docker (for containerized deployment)

### Cloning the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### Creating a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the API Locally

```bash
uvicorn main:app --reload
```

API available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Running the API with Docker

### Build the Docker Image

```bash
docker build -t ml-api .
```

### Run the Docker Container

```bash
docker run -p 8000:8000 ml-api
```

## API Endpoints

### Home Route

- **URL:** `/`
- **Method:** GET
- **Response:**
  ```json
  {"message": "Welcome to the Machine Learning API"}
  ```

### Prediction Route

- **URL:** `/predict`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "age": 25,
    "bmi": 24.5,
    "children": 2,
    "sex": "male",
    "smoker": "no",
    "region": "southwest"
  }
  ```
- **Response:**
  ```json
  {"prediction": 1234.56}
  ```

## File Structure

```
├── Data_Preprocessing.ipynb  # Data preprocessing steps
├── main.py                   # FastAPI implementation
├── Schema.py                 # Input schema definitions
├── best_model_and_preprocessor.pkl  # Trained model & transformer
├── requirements.txt          # Required dependencies
├── Dockerfile                # Docker setup for containerization
└── README.md                 # Documentation
```

## Future Enhancements

- CI/CD pipeline for automated deployment
- Cloud deployment options (AWS, GCP, DigitalOcean)
- Expanding input validation and error handling

## Contact

For questions or collaborations, please reach out via:

- **Email:** [amogelangmore96@gmail.com](mailto:amogelangmore96@gmail.com)
- **LinkedIn:** [Amogelang More](https://www.linkedin.com/in/amogelang-more)

## License

This project is open-source under the MIT License.

