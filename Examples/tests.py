from network import Network
import network as nt
import time
import numpy as np

nt.np.random.seed(47)
nt.random.seed(47)

net = Network()

net.ModifiedBA_Random22(5000)

net.DegreeDistribution(loglogscale=True)