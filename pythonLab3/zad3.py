
def isWord(word):
    if word != '':
        return True
    return False

f = open("potop.txt", encoding='utf-8')

source_text = f.read().split()

for i in range(len(source_text)):

    source_text[i] = source_text[i].strip()
    source_text[i] = source_text[i].strip( ",.!?-:;'\"")

source_text = filter(isWord, source_text)

word_counts = dict()

for word in source_text:

    if word not in word_counts:
        word_counts[word] = 1

    else:
        word_counts[word] += 1

word_count_pairs = []

for word in word_counts:
    word_count_pairs.append((word, word_counts[word]))

sorted_pairs = sorted(word_count_pairs, key=lambda x: x[1], reverse=True)

for pair in sorted_pairs:
    print("\"" + pair[0] + "\":", str(pair[1]) + ", ", end="")

