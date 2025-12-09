import torch
import torch.nn as nn

class ConvLSTMBlock(nn.Module):
    def __init__(self, in_ch, hid_ch):
        super().__init__()
        self.lstm = nn.LSTM(input_size=in_ch, hidden_size=hid_ch, batch_first=True)

    def forward(self, x):
        out, _ = self.lstm(x)
        return out[:, -1]    # last timestep

class STModel(nn.Module):
    def __init__(self, in_ch, hidden_dim=32):
        super().__init__()
        self.temporal = ConvLSTMBlock(in_ch=in_ch, hid_ch=hidden_dim)

        self.spatial = nn.Sequential(
            nn.Conv2d(hidden_dim, 32, 3, padding=1), nn.ReLU(),
            nn.Conv2d(32, in_ch, 1)
        )

    def forward(self, x):
        B, T, C, H, W = x.shape
        xt = x.reshape(B, T, C*H*W)
        h = self.temporal(xt)
        h = h.reshape(B, -1, H, W)
        out = self.spatial(h)
        return out
