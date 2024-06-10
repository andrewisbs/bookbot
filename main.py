
def main():
    path_to_file = "books/frankenstein.txt"


    with open(path_to_file, "r") as f:
        print(f.read())
    return

main()
