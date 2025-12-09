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

## Problem Definition

Earth system processes are inherently **spatiotemporal**: climate variables evolve over space and time in ways that are nonlinear, multiscale, and highly dependent on past conditions. Traditional statistical models often fail to capture these dynamics, especially when dealing with high-resolution gridded datasets.

The goal of this project is to build a model that can:

**Given a sequence of past climate fields (e.g., the last 24 hours), predict the next climate field (t + 1 hour).**

This is framed as a **supervised spatiotemporal forecasting problem**, commonly applied to:
- climate and weather nowcasting  
- hydrology  
- renewable energy forecasting  
- soil conditions and agriculture  

By training on historical ERA5-Land data, the model learns how climate variables evolve, allowing it to generate accurate short-term predictions.

---

## Model Description

The model used in this project is a **ConvLSTM** (Convolutional Long Short-Term Memory) neural network. ConvLSTMs are specifically designed for **spatiotemporal sequence modeling**, making them ideal for climate data.

### Why ConvLSTM?

Classic LSTMs flatten spatial grids and therefore lose important spatial relationships.  
ConvLSTM fixes this by replacing the linear operations in LSTM with **2D convolutions**, enabling the cell to:

- track local spatial patterns  
- preserve grid structure  
- learn motion and evolution over time  
- model both short-term and long-term dependencies  

### Model Architecture (Simplified)
Input Sequence → ConvLSTM Layer(s) → 3D Hidden State → 1×1 Convolution → Output Grid
The implemented model consists of:

1. **ConvLSTM Layer**
   - Input shape:
     ```
     (batch_size, seq_len, num_variables, H, W)
     ```
   - Hidden state retains spatial dimensions.
   - Learns temporal transitions of local spatial patterns.

2. **Final 1×1 Convolution**
   - Converts hidden channels back to the original variable count.
   - Produces:
     ```
     (num_variables, H, W)
     ```

3. **Loss Function**
   - Mean Squared Error (MSE), suitable for continuous-valued fields.

4. **Optimization**
   - Adam optimizer with learning rate scheduling.

### Strengths of This Model

- Maintains spatial resolution at all steps  
- Captures spatiotemporal dependencies efficiently  
- Handles multiple climate variables simultaneously  
- Performs well even on moderate hardware  

### Limitations

- Computationally heavier than simple LSTMs  
- Forecasts only one step ahead (extendable)  
- Performance depends on careful normalization and preprocessing  


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
