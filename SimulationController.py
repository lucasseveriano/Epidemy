# Import necessary Libraries
from Node import *

'''
μ Taxa de descontaminação (limpeza)
η Taxa de infecção em função das taxas exógena (λ) e endógena (γ)
S Estado suscetível
I Estado infectado
N Tamanho da população
λ Taxa de infecção exógena por nó
γ Taxa de infecção endógena
'''

class SimulationController:
    NodeList = [] 
    PortInput = 5000
    PortOutput = 8000
    Ip = "127.0.0.1"
        
    PortListTemp = []
    
    def __init__(self, numberOfNodes, numberOfinfected = 1):
        print(":: Initialize Simulation ::")
        
        # fazer em loop
        for i in range(numberOfNodes):
            if (numberOfinfected > 0):            
                node = Node(self.Ip, self.PortInput, self.PortOutput, i, State.Infected)
                numberOfinfected -= 1
            else:
                node = Node(self.Ip, self.PortInput, self.PortOutput, i)
                
            self.PortListTemp.append(self.PortInput)
            self.PortInput += 1
            self.PortOutput += 1
            self.NodeList.append(node)            
        
        # Initialize list of neighbors of each node in network      
        for nodeItem in self.NodeList:
            for Neighbor in self.NodeList:            
                if (nodeItem != Neighbor):
                    nodeItem.Ip = self.Ip
                    nodeItem.AddNeighbor(Neighbor.Ip, Neighbor.PortInput)                                                 

        print("\n")                    
        for node in self.NodeList:
            node.PrintNeighbor()

