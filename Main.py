import numpy as np
from scipy.stats import norm

S = float(input("S: "))
K = float(input("K: "))
r = float(input("r, ratio not percent, ex) 30% -> 0.3: "))
sig = float(input("Sigma, ratio not percent, ex) 30% -> 0.3: "))
Time = float(input("Time: "))

def N(x):
    return norm.cdf(x, 0, 1)
def PV(K,r,Time):
    return K*np.exp(-r*Time)
    
def BS(S,K,r,sig,Time):
    d1 = np.log(S/K)+(r+(sig**2)/2)/(sig*np.sqrt(Time))
    d2 = d1 - sig*np.sqrt(Time)
    C = S*N(d1)-PV(K,r,Time)*N(d2)
    P = PV(K,r,Time)*N(-d2)-S*N(-d1)
    print("d1: "+str(d1),"d2: "+str(d2))
    print("Call: "+str(C),"Put: "+str(P))

BS(S,K,r,sig,Time)

