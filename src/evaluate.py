import torch
import numpy as np
from model import STModel
from dataset import ClimateDataset
from torch.utils.data import DataLoader

test_ds = ClimateDataset("data/windows/test_X.npy", "data/windows/test_Y.npy")
test_loader = DataLoader(test_ds, shuffle=False)

model = STModel(in_ch=test_ds.X.shape[2])
model.load_state_dict(torch.load("saved_models/best_model.pth"))
model.eval()

loss_fn = torch.nn.MSELoss()
total = 0
with torch.no_grad():
    for X, Y in test_loader:
        total += loss_fn(model(X), Y).item()

print("Test MSE:", total)
