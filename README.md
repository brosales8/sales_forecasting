# Sales Forecasting
### Udacity - Machine Learning NanoDegree

**Author:** Bryan Rosales<br>
**Date:** May 8th, 2021


Overview
---

The goal of the project is to create a Time Series Forecasting model to predict sales quantities for a Wine Distributor company. Even though the company has a catalogue of around 400 products, the projects is focus on 6 best seller items. The problem was approached using a algorithm called Temporal Fusion Transformer developed by Pytorch and included in the package PyTorch Forecasting. Moreover, I use an original Dataset provided by Wine Distributor company with sales of the last 4 years. The dataset was preprocessed to be cleaned, transformed and loaded to modelling.

Please see the following files for more detail:

Files
---
- [1_Data_Preprocessing.ipynb](https://github.com/brosales8/sales_forecasting/blob/main/1_Data_Preprocessing.ipynb) 
Jupyter Notebook providing the source code of all steps performed in the Preprocessing stage
- [2_TemporalFusionTransformer.ipynb](https://github.com/brosales8/sales_forecasting/blob/main/2_TemporalFusionTransformer.ipynb) Notebook with model and prediction stages.
- [Capstone Project Proposal.pdf](https://github.com/brosales8/sales_forecasting/blob/main/Capstone%20Project%20Proposal.pdf) Proposal document explaining the problem.
- [Capstone Project Technical Doc.pdf](https://github.com/brosales8/sales_forecasting/blob/main/Capstone%20Project%20Technical%20Doc.pdf) Document reporting the solution and results.
- [functions.py](https://github.com/brosales8/sales_forecasting/blob/main/functions.py) Module containing some python functions implemented to help with the cleaning process.
- [/datasets](https://github.com/brosales8/sales_forecasting/tree/main/datasets) This folder includes all the csv files used to build the final dataset.
- [/output](https://github.com/brosales8/sales_forecasting/tree/main/output) Include 2 csv files corresponding to final dataset preprocessed (dataset.csv) and errors values (errors.csv) .
<br>

Usage
---
Currently working in deployment interface for users.