# Import necessary Libraries
import numpy
from enum import Enum

# States that indicates that node is infected or susceptible
class State(Enum):
    Infected = 1
    Susceptible = 2    

class Neighbor:
    Ip = ""
    Port = 0
    
    def __init__(self, ip, port):
        self.Ip = ip
        self.Port = port

class Node:
    CurrenState = State.Susceptible 
    PortInput = 0
    PortOutput = 0
    Ip = 0
    Neighbors = []

    def __init__(self, ip, portInput, portOutput):
        print("Initialize node")          
        print("IP: " + str(ip))          
        print("Input Port: " + str(portInput)) 
        print("Output Port: " + str(portOutput))
        print("------------------------ ")      
                 
        self.Ip = ip
        self.PortInput = portInput
        self.PortOutput = portOutput        
        self.Neighbors = []  
        self.CurrenState = State.Susceptible
        
        #Create socket
        
        # Initialize Threads            
        
                  
    def AddNeighbor(self, ip, port):        
        n = Neighbor(ip, port)
        self.Neighbors.append(n)
   
    def PrintNeighbor(self):    
        print ("Node ", str(self.Ip), str(self.PortInput))
        for neighbor in self.Neighbors:
            print(" " + neighbor.Ip, neighbor.Port)
        
   

   


