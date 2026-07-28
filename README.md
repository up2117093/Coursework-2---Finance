# Coursework 2 - Financial Time Series Modelling

This repository contains my work for Coursework 2, where I build and evaluate several models for financial time‑series forecasting. The project is organised into three main notebooks:

- Q1_folder/Q1.ipynb: Baseline Linear Regression using lag features

- Q2_folder/Q2.ipynb: Simple Multi‑Layer Perceptron (MLP) neural network

- Q3_folder/Q3.ipynb: Advanced model: Random Forest

All notebooks use shared helper functions stored in py/functions.py.

The dataset used throughout the coursework is located in the project root as finance_economics_dataset.csv.

## Summary of Work

### Q1 — Baseline Model
- Cleaned dataset
- Created lag features
- Trained Linear Regression
- Evaluated using MAE and RMSE
- Plotted actual vs predicted values
- Wrote beginner‑friendly explanations

### Q2 — MLP Neural Network
- Built a simple feed‑forward neural network
- Trained on lag features
- Compared performance with Q1
- Explained results clearly

### Q3 — Advanced Model
- Builds a more complex model
- Evaluates improvements
- Final comparison across all models

## Project Structure
Coursework-2---Finance/
- py/
  - functions.py
  - __init__.py

- Q1_folder/
  - Q1.ipynb

- Q2_folder/
  - Q2.ipynb

- Q3_folder/
  - Q3.ipynb
│
- dependencies.txt
- finance_economics_dataset.csv
- README.md


## How to Run

Install dependencies:
pip install -r dependencies.txt

Because each notebook lives inside its own folder, the first cell includes a small path adjustment so Python can find the shared py/functions.py module:
import sys, os
project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(project_root)

Then open any notebook:
jupyter notebook
