import torch
import torch.nn as nn
import sys


class HASH(nn.Module):
    def __init__(self, block_size, output_size):
        super(HASH, self).__init__()
        self.fc1 = nn.Linear(block_size + output_size, output_size)
        self.block_size = block_size
        self.output_size = output_size

    def to_torch(self, bit_str):
        tmp = []
        for i in range(self.block_size):
            if(i < len(bit_str)):
                tmp.append(int(bit_str[i]))
            else:
                tmp.append(0)
        return torch.FloatTensor(tmp)

    def forward(self, msg):
        bit_str = ""
        for c in msg:
            bit_str += bin(ord(c))[2:]
        str_len = len(bit_str)
        iter_num = int(str_len/self.block_size) + 1
        outputs = torch.zeros(1, self.output_size)
        for i in range(iter_num):
            inputs = self.to_torch(
                bit_str[i*self.block_size:(i+1)*self.block_size]).view(1, self.block_size)
            inputs = torch.cat((inputs, outputs), 1)
            outputs = self.fc1(inputs)

        outputs = nn.Sigmoid()(outputs)
        hash_value = ""
        for i in range(outputs.shape[1]):
            tmp = '{:.20f}'.format(outputs[0, i])
            hash_value += hex(int(tmp[8:20]))[2:6]
        return hash_value


unit = int(sys.argv[1])
block = int(sys.argv[2])
NNhash = HASH(block, unit)
torch.save(NNhash.state_dict(), "hash.pth")
