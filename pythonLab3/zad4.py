
def isWord(word):
    if word != '':
        return True
    return False

f = open("potop.txt", encoding='utf-8')

source_text = f.read().split()

for i in range(len(source_text)):
  
    source_text[i] = source_text[i].strip()
    source_text[i] = source_text[i].strip( ",.!?-:;'\"")

source_text = [word for word in filter(isWord, source_text) ]

grams_counts = dict()
grams_maping = dict()

for i in range(len(source_text)-1):

    digram = [source_text[i], source_text[i+1]]
    digram_rep = digram[0] + "." + digram[1]

    grams_maping[digram_rep] = digram
    
    if digram_rep not in grams_counts:
        grams_counts[digram_rep] = 1

    else:
        grams_counts[digram_rep] += 1
    
    if i < len(source_text) - 2:

        trigram = [source_text[i], source_text[i+1], source_text[i+2]]
        trigram_rep = trigram[0] + "." + trigram[1] + "." + trigram[2]
        grams_maping[trigram_rep] = trigram

        if trigram_rep not in grams_counts:
            grams_counts[trigram_rep] = 1

        else:
            grams_counts[trigram_rep] += 1

gram_count_pairs = []

for gram_rep in grams_counts:
    gram_count_pairs.append((grams_maping[gram_rep], grams_counts[gram_rep]))

sorted_pairs = sorted(gram_count_pairs, key= lambda x: x[1], reverse=True)

for i in range(20):
    print(sorted_pairs[i][0], ":", str(sorted_pairs[i][1]) + ", ", end="")

i = 20
while sorted_pairs[i][1] == sorted_pairs[19][1]:
    print(sorted_pairs[i][0], ":", str(sorted_pairs[i][1]) + ", ", end="")
    i+=1
    
