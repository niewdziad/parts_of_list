def partlist(list_):
    result = []
    for i in range(1, len(list_)):
        part1 = ' '.join(list_[:i])
        part2 = ' '.join(list_[i:])
        result.append((part1, part2))
    return result

test_data = ["az", "toto", "picaro", "zone", "kiwi"]
print(partlist(test_data))
