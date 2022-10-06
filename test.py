list = ["aa", "ba", "ca", "pas", "zeub"]
print(list)
to_del = []
for mot in list:
    print(mot)
    if len(mot) >= 3:
        to_del.append(mot)
print(to_del)
for mot in to_del:
    list.remove(mot)
print(list)


if "a" not in "bark":
    print('oue')