from src.Main import Main
import argparse

# Argumenty do uruchamiania programu
parser = argparse.ArgumentParser(description='Opis programu')

typ = parser.add_argument_group('Uruchomienie')
typ_required = typ.add_mutually_exclusive_group(required=True)
typ_required.add_argument('-A', action='store_true', help='Oba rodzaje algorytmów')
typ_required.add_argument('-P', action='store_true', help='Algorytmy procesora')
typ_required.add_argument('-M', action='store_true', help='Algorytmy pamięci')

akcja = parser.add_argument_group('Akcja')
akcja_required = akcja.add_mutually_exclusive_group(required=False)
akcja_required.add_argument('-S', action='store_true', help='Symulacja algorytmów')
akcja_required.add_argument('-g', action='store_true', help='Rysowanie wykresów')
akcja_required.add_argument('-s', action='store_true', help='Generowanie podsumowania')
akcja_required.add_argument('-r', action='store_true', help='Generowanie pliku README')

verbose = parser.add_argument_group('Verbose')
verbose.add_argument('-v', action='store_true', help='Verbose')

args = parser.parse_args()

if __name__ == '__main__':
    # Inicjalizacja głównej klasy programu
    f = Main(verbose=args.v)

    # Jeżeli nie podano żadnej dodatkowej opcji - wykonaj wszystkie
    optionalOptions = [args.S, args.g, args.s, args.r]
    optionalOptionNotExists = optionalOptions.count(False) == len(optionalOptions)

    # Uruchamianie programu
    if args.A:
        if args.S or optionalOptionNotExists: f.runAllSimulations()
        if args.g or optionalOptionNotExists: f.makeAllGraphs()
        if args.s or optionalOptionNotExists: f.generateAllSummary()
        if args.r or optionalOptionNotExists: f.generateAllReadme()
    elif args.P:
        if args.S or optionalOptionNotExists: f.runProcessorSimulations()
        if args.g or optionalOptionNotExists: f.makeProcessorGraphs()
        if args.s or optionalOptionNotExists: f.testManager.generateProcessorSummary()
        if args.r or optionalOptionNotExists: f.generateProcessorReadme()
    elif args.M:
        if args.S or optionalOptionNotExists: f.runRamSimulations()
        if args.g or optionalOptionNotExists: f.makeRamGraphs()
        if args.s or optionalOptionNotExists: f.testManager.generateRamSummary()
        if args.r or optionalOptionNotExists: f.generateMemoryReadme()
    else:
        print("Nieznana kombinacja argumentów!")

    f.save()