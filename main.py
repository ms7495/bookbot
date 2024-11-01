import string
path = "./books/frankenstein.txt"

with open(path) as f:
    cont = f.read()
    word = cont.split()
    count = len(word)


def fun(knjiga, slovo):
    slovo.lower()
    knjiga.lower()
    stevec = 0
    for k in knjiga:
        if(k == slovo):
            stevec+=1
    return stevec

mala_slova = string.ascii_lowercase

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count} words found in the document \n")

for slovo in mala_slova:
    opa = fun(cont, slovo)
    if(opa>0):
        print(f"The '{slovo}' character was found {opa} times")

print("--- End report ---")