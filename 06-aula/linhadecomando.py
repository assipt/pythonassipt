import sys


if __name__ == '__main__':  # É um script!
    print(f"Número de parâmetros: {len(sys.argv)}")
    for n,p in enumerate(sys.argv):
        print(f"Parâmetro {n}: {p}")

    
    
          
