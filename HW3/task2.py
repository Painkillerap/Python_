# def top_10_words(text):
#     words = re.findall(r'\b\w+\b', text.lower())
#     return Counter(words).most_common(10)
# text = "Python 3.9 is the latest version of Python. It's awesome!"
# # text = """Два кота, два друга, шли как-то по тропинке в лесу. Шли два кота, шли, пока не ушли с тропинки и не дошли
# # до деревни. Два кота решили не идти дальше и остаться жить в деревне"""
# print(top_10_words(text))

# def ten_popular(text: str) -> list[str]:
#     delete = ".,!?;:-[]{}()='"
#     for i in delete:
#         text = text.replace(i, "")
#     text = text.lower()
#     return sorted(set(text.split()), key=lambda x: text.count(x))[-10:]
#
# print(ten_popular(text))


# cnt = Counter(x for x in re.findall(r'[A-z\']{1,}', text.lower()))
# print(cnt.most_common(10))


# path = 'eng_t.txt'
# text = ''
# with open(path, 'r') as f:
#     for line in f.readlines():
#         text = line + text
# text = "".join([i for i in text.lower() if i.isalpha() or i == " "])
# print(text)
# myDict = {}
# text = text.split(" ")
# for i in text:
#     myDict[i] = myDict.get(i, 0) + 1
# for key, item in myDict.items():
#     result = sorted(myDict.items(), key = lambda x: (-x[1], x[0]))
# count = 0
# for i, j in result:
#     count += 1
#     print(f' слово {i} встретилось {j} раз')
#     if count == 10 : break

text = "Python 3.9 is the latest version of Python. It's awesome!"


def count_words(text):
    text = text.lower().replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("'", " ")
    words = text.split()
    words_count = {}
    for word in words:
        if not word.isdigit():
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1
    sorted_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:10]


result = count_words(text)
print(result)

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)
