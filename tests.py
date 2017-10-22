from network import Network

net = Network()

#net.CircularGraph(20, 1)
net.ER_Random(V=20, p=0.1)
#net.Init([[1,0], [2,0], [3,0], [4,0], [5,0], [0,1], [0,2], [0,3], [0,4], [0,5]])
net.ShowNodes()
net.DrawNetwork()
print(net.AvClusteringCoefficient())

print(net.ClosenessCentrality(0))
print(net.HarmonicCentrality(0))
bd1 = net.BetweennessCentrality()
bd2 = net.BetweennessCentrality2()
EC  = net.EigenvectorCentrality()

print("compare algorthms:")
print("\t BC1        BC2        EC")
for key in net.nodes:
    print(key, "{:8f}   {:8f}   {:8f}".format(bd1[key], bd2[key], EC[key]), sep='\t')

#print(net.EigenvectorCentrality())
