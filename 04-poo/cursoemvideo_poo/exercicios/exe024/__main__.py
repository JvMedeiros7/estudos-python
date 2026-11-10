from classes024 import Cachorro, Gato, Pato, Galinha, Pitbull, Spitz

def main():

    a = Cachorro("Rex")
    b = Gato("Mingau")
    c = Pato("Donald")
    d = Galinha("Pepita")
    e = Spitz("Fifi")
    f = Pitbull("Max")
    a.emitir_som()
    b.emitir_som()
    c.emitir_som()
    d.emitir_som()
    e.emitir_som()
    f.emitir_som()

if __name__ == "__main__":
    main()