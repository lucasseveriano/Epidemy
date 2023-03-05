from SimulationController import SimulationController

'''
μ Taxa de descontaminação (limpeza)
η Taxa de infecção em função das taxas exógena (λ) e endógena (γ)
S Estado suscetível
I Estado infectado
N Tamanho da população
λ Taxa de infecção exógena por nó
γ Taxa de infecção endógena
'''

# Executar o programa principal
if __name__ == '__main__':
    
    # Código principal
    sc = SimulationController(2)
    