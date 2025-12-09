import torch
from torch.utils.data import Dataset

class ClimateDataset(Dataset):
    def __init__(self, x_path, y_path):
        self.X = torch.tensor(np.load(x_path), dtype=torch.float32)
        self.Y = torch.tensor(np.load(y_path), dtype=torch.float32)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.Y[idx]
