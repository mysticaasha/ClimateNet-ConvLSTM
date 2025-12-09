# ClimateNet-ConvLSTM
Deep Spatio-Temporal Climate Forecasting using ConvLSTM + CNN on ERA5 Reanalysis Data
This project builds a basic deep learning pipeline for climate-variable forecasting using ERA5 and a ConvLSTM-based neural network.
It handles data extraction → preprocessing → modeling → evaluation.

🌍 Project Overview

Climate change analysis requires models that understand both space and time.
This project predicts climate variables (e.g., temperature, precipitation) from gridded spatio-temporal data.

We use:
	•	ERA5 Reanalysis (ECMWF)
	•	GRIB → NetCDF processing
	•	Spatial+temporal deep learning architecture (ConvLSTM + CNN)
	•	Sliding-window forecasting
	•	PyTorch training pipeline

🚀 Features

✔ Fully automated preprocessing
	•	Unzip GRIB
	•	Extract variables
	•	Convert GRIB → NetCDF
	•	Merge different variables
	•	Unit conversions
	•	Daily resampling
	•	Train/Val/Test split
	•	Sliding window creation

✔ ConvLSTM deep learning model
	•	Learns temporal sequences
	•	Captures spatial climate structure
	•	Predicts future maps from past frames

✔ Training with:
	•	MSE loss
	•	Learning rate scheduler
	•	Automatic checkpointing
	•	Best-model saving
	•	GPU/CPU compatible

✔ Evaluation tools
	•	RMSE, MAE, MAPE, R²
	•	Visualization of predictions vs ground truth
🔧 Dataset

We use variables from the ERA5 Reanalysis dataset such as:
	•	2m temperature
	•	Total precipitation
	•	Short-wave radiation
	•	Volumetric soil water (layers 1–4)
	•	Wind speed components (u10, v10)

Dataset is downloaded via the CDS API (Copernicus).
