import torch
import torch.nn as nn


class FullyConnected(nn.Module):

    def __init__(self, input_dim=28 * 28, width=50, depth=3, num_classes=10):
        super(FullyConnected, self).__init__()

        self.input_dim = input_dim
        self.width = width
        self.depth = depth
        self.num_classes = num_classes
        # pdb.set_trace()
        layers = self.get_layers()

        self.fc = nn.Sequential(
            nn.Linear(self.input_dim, self.width, bias=False),
            nn.ReLU(inplace=True),
            *layers,
            nn.Linear(self.width, self.num_classes, bias=False),
        )

    def get_layers(self):
        layers = []
        for i in range(self.depth - 2):
            layers.append(nn.Linear(self.width, self.width, bias=False))
            layers.append(nn.ReLU())
        return layers

    def forward(self, x):
        x = x.view(x.size(0), self.input_dim)
        x = self.fc(x)
        return x


def fc(**kwargs):
    return FullyConnected(**kwargs)


if __name__ == '__main__':
    # testing
    x = torch.randn(5, 1, 32, 32)
    net = FullyConnected(input_dim=32 * 32, width=123)
    print(net(x))
