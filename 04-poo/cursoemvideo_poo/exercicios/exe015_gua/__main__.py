from avaliacao import Avaliacao
from rich import inspect, print 
from rich.panel import Panel
from rich.traceback import install

install()



def main():
    av1 = Avaliacao("João", "Matemática", 8.5)
    inspect(av1)
    print(dict(av1.__dict__))
    print(vars(av1))



if __name__ == "__main__":
    main()