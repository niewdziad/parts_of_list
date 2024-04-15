# parts_of_list

def partlist(list_): - Definiuje funkcję partlist, która przyjmuje listę list_ jako argument.

result = [] - Inicjuje pustą listę result, która będzie przechowywać wszystkie pary podziałów listy.

for i in range(1, len(list_)): - Rozpoczyna pętlę for, która będzie iterować przez indeksy od 1 do len(list_) - 1 (z wyłączeniem ostatniego indeksu).

part1 = ' '.join(list_[:i]) - Tworzy pierwszą część podziału, łącząc elementy listy od początku do bieżącego indeksu i za pomocą spacji.

part2 = ' '.join(list_[i:]) - Tworzy drugą część podziału, łącząc elementy listy od bieżącego indeksu i do końca listy za pomocą spacji.

result.append((part1, part2)) - Dodaje krotkę zawierającą obie części podziału do listy wynikowej result.

return result - Zwraca listę wynikową zawierającą wszystkie możliwe podziały listy na dwie części.

test_data = ["az", "toto", "picaro", "zone", "kiwi"] - Definiuje listę testową test_data, która zawiera dane wejściowe dla funkcji partlist.

print(partlist(test_data)) - Wywołuje funkcję partlist na danych testowych test_data i drukuje wynik.
