import torch
import torch.nn as nn

class qnetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(40, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 12)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

if __name__ == "__main__":
    net = qnetwork()
    fake_camera = torch.randn(1, 40)
    output = net(fake_camera)
    print("output shape:", output.shape)
    print("estimated 12 gear points:", output)