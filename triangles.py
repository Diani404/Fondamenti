#Si definisca la funzione ex1(triangles) che prende in input una lista
#di triple di numeri positivi ed elimina dalla lista tutte le triple
#che non possono essere i lati di un triangolo rettangolo. Ogni numero della
#tripla puo' essere o cateto o ipotenusa e non vi è alcun ordine
#prestabilito.  La funzione deve ritornare il numero di triple
#eliminate dalla lista triangles. La lista triangles deve risultare
#modificata in-place alla fine dell'esecuzione di ex1. Per valutare se un
#triangolo è rettangolo si può usare il teorema di Pitagora, per cui la
#somma dei quadrati costruiti sui cateti deve essere uguale al quadrato
#costruito sull'ipotenusa.
#Per i confronti, si usi la funzione di arrotondamento round(x,3).

#Esempio: se triangles = [(3, 4, 5), (12, 36.05551, 34),
#                         (1,1,3), (8,8,8), (2, 3, 4)],
#         la funzione ex1(triangles) resituisce il valore 3 e modifica la lista
#         in modo che
#            triangles = [(3, 4, 5), (12, 36.05551, 34)].

#Infatti, considerando il risultato atteso triangles = [(3, 4, 5), (12, 36.05551, 34)]
#vale:

#| tripla             | check is True                                  |
#| (3, 4, 5)          | round( 3² + 4² ), 3) == round( 5² ,3)          |
#| (12, 36.05551, 34) | round( 12² + 34² ), 3) == round( 36.05551² ,3) |

#NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
#semplici.##

triangles = [(3, 4, 5), (12, 36.05551, 34),(1,1,3), (8,8,8), (2, 3, 4)]

def ordine(triangles):
    lista_ordinata=[]
    for i in triangles:
        element=i
        lista_ordinata.append(sorted(element))
    return lista_ordinata

triangles=ordine(triangles)

print("Queste sono le triple ordinate")
print(triangles)

def check_triangolo(triangles):
    for i in triangles[::-1]:
        element=i
        if round((element[2]**2),3)==round((element[1]**2+element[0]**2),3):
            pass
        else:
            triangles.remove(element)
    print("Queste sono le triple triangolari")
    print(triangles)

check_triangolo(triangles)