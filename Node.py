# Import necessary Libraries
import numpy
from enum import Enum
import threading
import random
import time
import math
import socket

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
    
    def __init__(self, ip, portInput, portOutput, number, currentState = State.Susceptible):
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
        self.Identification = "Node " + str(number)        
        self.CurrenState = currentState
        
        #Create socket
        # Send Infection
        self.InfectionSocket  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UPD
        self.InfectionSocket.bind((ip, portOutput))
        
        # receive Infection
        self.ReceiveSocket  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UPD
        self.ReceiveSocket.bind((ip, portInput))
        
        # Initialize Threads 
        # Endogenous infection
        infectEndogenousThread = threading.Thread(target=self.InfectEndogenousThread, args=(1.1,))
        infectEndogenousThread.start()

        # Healing Thread
        healingThread = threading.Thread(target=self.HealingThread, args=(1,))
        healingThread.start()   

        # Exogenoust infection
        infectThread = threading.Thread(target=self.InfectExogenoustTread, args=(0.00001,))
        infectThread.start()     

        # Receive infection from neighbor
        receiveThread = threading.Thread(target=self.ReceiveInfectionFromNeighborTread)
        receiveThread.start()   

        # todo: Create method to finish threads
        # wait thread to be finished
        # infectThread.join()
        # healingThread.join()
        # infectEndogenousThread.join()
        # infectEndogenousThread.join()
        # receiveThread.join()

    # Endogenous infection
    def InfectEndogenousThread(self, rate):
        while True:
            self.wait(rate)            
            # Get any neighbour
            if (self.CurrenState == State.Infected):
                if (len(self.Neighbors) > 0):
                    neighbor = random.choice(self.Neighbors) # Get randomly an neighbor

                    message = str(self.Identification)
                    self.InfectionSocket.sendto(message.encode(), (neighbor.Ip, neighbor.Port))

    def InfectExogenoustTread(self, rate):
        while True:
            self.wait(rate)
            self.CurrenState = State.Infected

    # Healing rate
    def HealingThread(self, rate):
        while True:
            self.wait(rate)
            if (self.CurrenState == State.Infected):
                self.CurrenState = State.Susceptible
                print(self.Identification + " has healed")

    # Listen network to receive infection from network
    def ReceiveInfectionFromNeighborTread(self):
        while True:
            dados_recebidos, endereco_servidor = self.ReceiveSocket.recvfrom(1024)
            print(self.Identification + " has infected by " + dados_recebidos.decode())
            self.CurrenState = State.Infected
    
    def wait(self,param):
        if not isinstance(param, (int, float)):
            raise TypeError('lambda_param deve ser um número')
        # waiting = -math.log(random.random()) / param
        waiting = numpy.random.exponential(1/param) 
        time.sleep(waiting)

    def AddNeighbor(self, ip, port):
        n = Neighbor(ip, port)
        self.Neighbors.append(n)

    def PrintNeighbor(self):
        print ("Node ", str(self.Ip), str(self.PortInput))
        for neighbor in self.Neighbors:
            print(" " + neighbor.Ip, neighbor.Port)

