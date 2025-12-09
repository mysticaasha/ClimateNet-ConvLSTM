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


## Dataset

This project uses **ERA5-Land** reanalysis data from the Copernicus Climate Data Store (CDS). ERA5-Land provides high-resolution (0.1° x 0.1°) gridded climate variables suitable for land and hydrological applications.  
The dataset used here is **spatiotemporal**: it contains multiple climate variables over time, forming a 4-dimensional tensor structure:
(time, variable, latitude, longitude)

### Data Sources

The raw data is downloaded as **GRIB** files from CDS and then converted to **NetCDF** format for easier processing using Xarray.

The project uses the following ERA5-Land variables (customizable):
- **2m Temperature (t2m)**
- **Total precipitation (tp)**
- **Volumetric soil water layer 1 (swvl1)**
- **Surface net solar radiation (ssr)**  
…and more can be added as needed.

### Temporal Characteristics

ERA5-Land data provides:
- **Hourly temporal resolution**
- A **continuous time series**, typically covering:
  - Date range (example): `2010-01-01` → `2024-01-01`
  - Time increments: **1 hour**
- Each sample is tagged by:
  - `year`
  - `month`
  - `day`
  - `hour`
  - `timestamp index`

This metadata is automatically encoded and stored inside the processed dataset.

### Spatial Characteristics

The data represents a **fixed spatial grid**:
- **Latitude range**: user-selected region (e.g., 48°N → 52°N)
- **Longitude range**: user-selected region (e.g., 22°E → 26°E)
- **Grid resolution**: 0.1° (approx. 9 km)

Each variable is therefore a 2D map per time step:
(variable_count, height, width)

### Data Sources

The raw data is downloaded as **GRIB** files from CDS and then converted to **NetCDF** format for easier processing using Xarray.

The project uses the following ERA5-Land variables (customizable):
- **2m Temperature (t2m)**
- **Total precipitation (tp)**
- **Volumetric soil water layer 1 (swvl1)**
- **Surface net solar radiation (ssr)**  
…and more can be added as needed.

### Temporal Characteristics

ERA5-Land data provides:
- **Hourly temporal resolution**
- A **continuous time series**, typically covering:
  - Date range (example): `2010-01-01` → `2024-01-01`
  - Time increments: **1 hour**
- Each sample is tagged by:
  - `year`
  - `month`
  - `day`
  - `hour`
  - `timestamp index`

This metadata is automatically encoded and stored inside the processed dataset.

### Spatial Characteristics

The data represents a **fixed spatial grid**:
- **Latitude range**: user-selected region (e.g., 48°N → 52°N)
- **Longitude range**: user-selected region (e.g., 22°E → 26°E)
- **Grid resolution**: 0.1° (approx. 9 km)

Each variable is therefore a 2D map per time step:
(variable_count, height, width)
