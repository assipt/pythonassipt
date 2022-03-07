
def entrada(msg, converter=int, xmin=None, xmax=None, ntentativas=5, x=None):
            
    for i in range(ntentativas):
        try:
            val = converter(input(msg))
            if xmin is not None and  val < xmin:
                raise ValueError("Valor mínimo deve ser {xmin}")
            if xmax is not None and val > xmax:
                raise ValueError("Valor máximo deve ser {xmax}")
            return val
        except ValueError as e:
            print(f"Valor ilegal - {e}! Tente novamente!")
                
    if x is None:
        raise ValueError("Nenhum valor fornecido")
    else:
        return x
    
def entrada_int(msg, xmin=None, xmax=None, ntentativas=5, x=None):
    return entrada(msg, int, xmin, xmax, ntentativas, x)

def entrada_float(msg, xmin=None, xmax=None, ntentativas=5, x=None):
    return entrada(msg, float, xmin, xmax, ntentativas, x)

def converter_sn(s):
    s = s.lower()
    if s == 's':
        return True
    elif s == 'n':
        return False
    else:
        raise ValueError(f"{s} deve ser S/s/N/n")
                         
    
def sim_ou_não(msg, ntentativas=3, x="s"):
    if x.lower() == 's':
        x = True
    else:
        x = False
        
    msg = f"{msg} (s/n): "
    return entrada(msg, converter_sn, xmin=None, xmax=None, x=x)
    
