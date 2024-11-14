lista1 = ["3", "5"]
def aggiunta_elementi():
    elemento = input(f"Inserisci l'elemento")
    lista1.append(elemento)
    
def visualizzare():
    for i in range(len(lista1)):
        print(f"{i + 1}. {lista1[i]}")
n=0
def eliminare():
    n=int(input("inserisci il numero dell elemento da eliminare"))
    lista1.pop(n)

def contare():
    print(len(lista1))

def pulisci_lista():
    lista1.clear()

while True:
    print("premi 0 per uscire,\npremi 1 per aggiungerre un elemento,\npremi 2 per visualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare gli elementi della lista,\n premi 5 per eliminare un elemento")
    x=int(input(""))
    if x == 0:
        break
    elif x == 1:
        aggiunta_elementi()
        
    elif x == 2:
        visualizzare()
        
    elif x == 3:
        eliminare()

    elif x == 4:
        contare()

    elif x == 5:
        pulisci_lista()