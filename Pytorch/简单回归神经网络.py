# -*- coding: utf-8 -*-
# Time    : 2020/4/7 12:58
# Author  : zlich
# Filename: 简单的神经网络.py
import torch
import matplotlib.pyplot as plt
import numpy as np
from torchvision import models


# models.inception_v3()

def getdata():
    x = np.linspace(-1, 1, 100)
    y = x * x + 0.2 * np.random.rand(x.shape[0])
    return x, y


class Net(torch.nn.Module):
    def __init__(self, in_num, hidden_num, out_num):
        super(Net, self).__init__()
        self.hidden_1 = torch.nn.Linear(in_features=in_num, out_features=hidden_num)
        self.predict = torch.nn.Linear(in_features=hidden_num, out_features=out_num)

    def forward(self, x):
        x = torch.nn.functional.relu(self.hidden_1(x))  # 激活函数
        x = self.predict(x)  # 输出值
        return x


def train_net():
    data_x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
    # data_x = torch.ones()
    data_y = data_x.pow(2) + 0.2 * torch.rand(data_x.size())
    # data_x = torch.from_numpy(x)
    # # data_x = torch.unsqueeze(data_x, dim=1)
    # data_x = torch.autograd.Variable(data_x)
    # data_y = torch.from_numpy(y)
    # # data_y = torch.unsqueeze(data_y, dim=1)
    # data_y = torch.autograd.Variable(data_y)
    # plt.scatter(data_x.data,data_y.data)
    # plt.show()

    net = Net(in_num=1, hidden_num=5, out_num=1)
    import torchsummary
    torchsummary.summary(net, (1,))
    # print(net)

    optimizer = torch.optim.SGD(net.parameters(), lr=0.2)
    loss_func = torch.nn.MSELoss()
    plt.ion()
    num = []
    loss_num = []
    for i in range(500):
        predict = net(data_x)
        loss = loss_func(predict, data_y)

        optimizer.zero_grad()  # 清空上一步的残余更新参数值
        loss.backward()  # 误差反向传播, 计算参数更新值
        optimizer.step()  # 将参数更新值施加到 net 的 parameters 上
        # if t % 5 == 0:
            # plot and show learning process
        plt.clf()
        plt.suptitle("{}".format(i+1))
        g1 = plt.subplot(211)
        g1.set_title("...")
        plt.scatter(data_x.data.numpy(), data_y.data.numpy())
        plt.plot(data_x.data.numpy(), predict.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
        g2 = plt.subplot(212)
        g2.set_title("...")
        num.append(i)
        loss_num.append(float(loss.data))
        plt.plot(num, loss_num)
        plt.pause(0.01)
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    x, y = getdata()
    train_net()

    # plt.scatter(x,y)
    # plt.show()
