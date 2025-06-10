dictionary = {
     "кіт": "cat",
    "собака": "dog",
    "дім": "house",
    "понімать": "understand",
    "їсти": "eat",
    "камінь": "stone",
    "самотність": "alone",
    "дерево": "tree",
    "яблуко": "apple",
    "вода": "water"
}
known_words = set(dictionary)

print("=== Перекладач ===")


word = input("Слово для перекладу: ")
translation = dictionary.get(word)
if translation:
    print("Переклад:", translation)
else:
    print("Слово не знайдено.")


ukr = input("Додати слово (укр): ")
eng = input("Переклад (eng): ")
dictionary[ukr] = eng
known_words.add(ukr)
print(f"Додано слово '{ukr}'.")


to_remove = input("Слово для видалення: ")
removed = dictionary.pop(to_remove, None)
if removed:
    if to_remove in known_words:
        known_words.remove(to_remove)
    else:
        known_words.discard(to_remove)
    print(f"Слово '{to_remove}' видалено.")
else:
    print("Слова не було у словнику.")
