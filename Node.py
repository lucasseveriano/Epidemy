# Import necessary Libraries
import numpy
from enum import Enum
import threading
import random
import time
import math

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
        # Endogenous infection
        infectEndogenousThread = threading.Thread(target=self.InfectEndogenousThread, args=(1,))
        infectEndogenousThread.start()

        # Healing Thread
        healingThread = threading.Thread(target=self.HealingThread, args=(0.5,))
        healingThread.start()   

        # Exogenoust infection
        infectThread = threading.Thread(target=self.InfectExogenoustTread, args=(1,))
        infectThread.start()     

        # Receive infection from neighbor
        receiveThread = threading.Thread(target=self.ReceiveInfectionFromNeighborTread)
        receiveThread.start()   

        # wait thread to be finished
        infectThread.join()
        healingThread.join()
        infectEndogenousThread.join()
        infectEndogenousThread.join()
        receiveThread.join()

    # Endogenous infection
    def InfectEndogenousThread(self, rate):
        while True:
            self.wait(rate)
            print("Send infection Endogenous", rate)    

    def InfectExogenoustTread(self, rate):
        while True:
            self.wait(rate)
            self.CurrenState = State.Infected 
            print("Get exogenous infected")
        
    # Healing rate
    def HealingThread(self, rate):
        while True:
            self.wait(rate)
            if (self.CurrenState == State.Infected):
                self.CurrenState = State.Susceptible
                print("Healed", rate)
    
        
    
    # Listen network to receive infection from network
    def ReceiveInfectionFromNeighborTread(self):
        while True:
            print("Receive")
    
    def wait(self,param):
        if not isinstance(param, (int, float)):
            raise TypeError('lambda_param deve ser um número')
        waiting = -math.log(random.random()) / param
        time.sleep(waiting)

    
    def AddNeighbor(self, ip, port):
        n = Neighbor(ip, port)
        self.Neighbors.append(n)
   
    def PrintNeighbor(self):
        print ("Node ", str(self.Ip), str(self.PortInput))
        for neighbor in self.Neighbors:
            print(" " + neighbor.Ip, neighbor.Port)

