# ClimateNet-ConvLSTM
**Deep Spatio-Temporal Climate Forecasting using ConvLSTM + CNN on ERA5 Reanalysis Data**

This project implements a complete deep-learning pipeline for forecasting climate variables from gridded spatio-temporal data.  
It includes data extraction, preprocessing, model training, evaluation, and visualization.

---

## 🌍 Project Overview

Climate forecasting requires models that capture both **spatial patterns** and **temporal evolution**.  
This project uses:

- **ERA5 Reanalysis data (ECMWF)**
- **GRIB → NetCDF conversion**
- **Sliding-window forecasting**
- **A hybrid ConvLSTM + CNN architecture**

The goal is to predict future climate-variable maps using a sequence of past maps.

---

## 🚀 Features

### ✔ Fully automated preprocessing pipeline
- Unzipping downloaded ERA5 files  
- GRIB extraction  
- GRIB → NetCDF conversion  
- Merging multiple variables  
- Unit conversions  
- Daily aggregation  
- Train/Validation/Test splitting  
- Sliding window generation  

### ✔ Deep Learning Architecture
- ConvLSTM layers for sequence modeling  
- CNN decoder for spatial prediction  
- PyTorch implementation  
- Best-model checkpointing  

### ✔ Evaluation Tools
- RMSE, MAE, MAPE, R²  
- Spatial error heatmaps  
- Prediction vs Ground Truth plots  

---


🔧 Dataset

We use variables from the ERA5 Reanalysis dataset such as:
	•	2m temperature
	•	Total precipitation
	•	Short-wave radiation
	•	Volumetric soil water (layers 1–4)
	•	Wind speed components (u10, v10)

Dataset is downloaded via the CDS API (Copernicus).
