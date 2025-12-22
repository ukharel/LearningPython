# Dictionary is the collection of keys and pair
# It is ordered and changable

meaning= {
    "Inclusive": " Something that included in it.",
    "Exclusive":"Somethiing that excluded from it.",
    'Abstract':" Hide core functions",
    'Concrete':" Mostly visible"
}

# print(meaning.get("Inclusive"))
# print(meaning.update({"Features":"Atrribute of something"}))
# print(meaning)
# print(meaning.pop("Abstract"))
# print(meaning)
# print(meaning.popitem())

# print(meaning.keys())
# for key in meaning.keys():
    # print(key)

# print(meaning.values())
# for value in meaning.values():
#     print(value)

# print(meaning.items())
for key,values in meaning.items():
    print(f'{key}:{values}')