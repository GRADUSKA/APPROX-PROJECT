import src.parse as parse
import src.bruteForce as bruteForce
import src.first_implem as first_implem

def main():
    path = input("Name of the input:")
    list_perso = parse.create_list(path)
    print("For the brute Force algorithm")
    print(f"Nombre de perso: {bruteForce.bruteForce(list_perso)}")
    print("First implementation of a new algorithm")
    parse.print_perso(first_implem.approx(list_perso))

main()