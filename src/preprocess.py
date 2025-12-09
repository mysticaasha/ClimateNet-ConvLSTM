import xarray as xr
import numpy as np
from pathlib import Path
from tqdm import tqdm

RAW_DIR = Path("data/raw")
PROC_DIR = Path("data/processed")
WIN_DIR = Path("data/windows")

PROC_DIR.mkdir(exist_ok=True, parents=True)
WIN_DIR.mkdir(exist_ok=True, parents=True)

def convert_to_netcdf():
    for file in RAW_DIR.glob("*.grib"):
        ds = xr.open_dataset(file, engine="cfgrib")
        out = PROC_DIR / (file.stem + ".nc")
        ds.to_netcdf(out)

def merge_all():
    ncs = list(PROC_DIR.glob("*.nc"))
    ds = xr.open_mfdataset(ncs, combine="by_coords")
    ds.to_netcdf(PROC_DIR / "merged.nc")
    return ds

def resample_daily(ds):
    daily = ds.resample(time="1D").mean()
    daily.to_netcdf(PROC_DIR / "daily.nc")
    return daily

def split_years(ds, train_years, val_years, test_years):
    return (
        ds.sel(time=ds.time.dt.year.isin(train_years)),
        ds.sel(time=ds.time.dt.year.isin(val_years)),
        ds.sel(time=ds.time.dt.year.isin(test_years)),
    )

def make_windows(ds, split_name, input_len=7, horizon=1):
    arr = ds.to_array().transpose("time", "variable", "lat", "lon").values
    X, Y = [], []
    for i in tqdm(range(len(arr) - input_len - horizon)):
        X.append(arr[i:i+input_len])
        Y.append(arr[i+input_len])
    X = np.stack(X)
    Y = np.stack(Y)
    np.save(WIN_DIR / f"{split_name}_X.npy", X)
    np.save(WIN_DIR / f"{split_name}_Y.npy", Y)
