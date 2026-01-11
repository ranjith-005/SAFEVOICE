import torch
import torch.nn as nn

class LanguageIDModel(nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()

        self.cnn = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.lstm = nn.LSTM(
            input_size=32 * 40,
            hidden_size=128,
            num_layers=2,
            batch_first=True,
            bidirectional=True
        )

        self.fc = nn.Linear(256, num_classes)

    def forward(self, x):
        x = self.cnn(x)
        b, c, f, t = x.size()
        x = x.view(b, t, c * f)
        x, _ = self.lstm(x)
        x = self.fc(x[:, -1, :])
        return x
