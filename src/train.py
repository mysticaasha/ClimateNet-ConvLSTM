import json
import torch
from torch.utils.data import DataLoader
from model import STModel
from dataset import ClimateDataset
from tqdm import tqdm

CONFIG = json.load(open("config.json"))

train_ds = ClimateDataset("data/windows/train_X.npy", "data/windows/train_Y.npy")
val_ds   = ClimateDataset("data/windows/val_X.npy",   "data/windows/val_Y.npy")

train_loader = DataLoader(train_ds, batch_size=CONFIG["batch_size"], shuffle=True)
val_loader   = DataLoader(val_ds, shuffle=False)

model = STModel(in_ch=train_ds.X.shape[2], hidden_dim=CONFIG["hidden_dim"])
optim = torch.optim.Adam(model.parameters(), lr=CONFIG["learning_rate"])
loss_fn = torch.nn.MSELoss()

best_loss = float("inf")

for epoch in range(CONFIG["epochs"]):
    model.train()
    total = 0
    for X, Y in tqdm(train_loader):
        optim.zero_grad()
        loss = loss_fn(model(X), Y)
        loss.backward()
        optim.step()
        total += loss.item()

    model.eval()
    val_total = 0
    with torch.no_grad():
        for X, Y in val_loader:
            val_total += loss_fn(model(X), Y).item()

    print(f"Epoch {epoch+1} — Train {total:.4f}  |  Val {val_total:.4f}")

    if val_total < best_loss:
        best_loss = val_total
        torch.save(model.state_dict(), "saved_models/best_model.pth")
