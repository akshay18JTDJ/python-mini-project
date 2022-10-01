def CompoundInterest(P,r,t):
    CI = P*(1 + r/(100))**t - P
    return round(CI,2)