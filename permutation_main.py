import graph_data
import permutation


def displayHamiltonian(graphIndex):
    smallGraphHamiltonianCycles = permutation.checkHamiltonian(graph_data.graph_data[graphIndex])
    print("Valid Hamiltonian Cycles for Graph " + str(graphIndex) + ": ")
    print(smallGraphHamiltonianCycles)
    
displayHamiltonian(3)