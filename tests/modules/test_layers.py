import torch
import torch.nn as nn

from torch_mimicry.modules import layers


class TestLayers:
    def setup(self):
        self.N, self.C, self.H, self.W = (16, 3, 32, 32)
        self.n_out = 8

    def test_ConditionalBatchNorm2d(self):
        num_classes = 10
        X = torch.ones(self.N, self.C, self.H, self.W)
        y = torch.randint(low=0, high=num_classes, size=(self.N, ))

        # Setup cond. BN --> Note: because we usually do
        # BN-ReLU-Conv, we take num feat as input channels
        conv = nn.Conv2d(self.C, self.n_out, 1, 1, 0)
        bn = layers.ConditionalBatchNorm2d(num_features=self.C,
                                           num_classes=num_classes)

        output = bn(X, y)
        output = conv(output)

        assert output.shape == (16, 8, 32, 32)


if __name__ == "__main__":
    test = TestLayers()
    test.setup()
    test.test_ConditionalBatchNorm2d()
