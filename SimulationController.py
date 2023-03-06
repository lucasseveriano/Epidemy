# Import necessary Libraries
from Node import *
import matplotlib.pyplot as plt

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
            self.counter = 1
            
            self.Infected = []
            self.susceptible = []
            self.timer = []
        
        # Initialize list of neighbors of each node in network      
        for nodeItem in self.NodeList:
            for Neighbor in self.NodeList:            
                if (nodeItem != Neighbor):
                    nodeItem.Ip = self.Ip
                    nodeItem.AddNeighbor(Neighbor.Ip, Neighbor.PortInput)                                                 

        print("\n")                    
        for node in self.NodeList:
            node.PrintNeighbor()
            
        while True:
            self.UpdateNetworkState(self.counter)            
            time.sleep(1)
            if (self.counter == 10):
                break
        
        #finishThread
        self.FinishThreads()
        self.PlotChart()
        
    def PlotChart(self):
        # Plotagem
        plt.plot(self.timer, self.Infected, label='I')
        plt.plot(self.timer, self.susceptible, label='S')

        # Configurações de eixo
        plt.xlabel('Time')
        plt.ylabel('Population')

        # Título do gráfico
        plt.title('Gráfico com duas séries')

        # Legenda
        plt.legend()

        # Exibição do gráfico
        plt.show()        
            
    def UpdateNetworkState(self, counter):     
        i = sum(map(lambda x : x.CurrenState == State.Infected, self.NodeList))  
        s = sum(map(lambda x : x.CurrenState == State.Susceptible, self.NodeList))        
        
        self.susceptible.append(s)
        self.Infected.append(i)   
        self.timer.append(self.counter)
        
        self.counter += 1
        
    def FinishThreads(self):
         for node in self.NodeList:
            node.IsRunning = False

