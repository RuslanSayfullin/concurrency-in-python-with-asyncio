# подчет частот слов, начинающихся на a
import time

freqs = {}

with open('the_lord_of_the_rings.txt', encoding='utf-8') as f:
    lines = f.readlines()
    start = time.time()
    for line in lines:
        data = line.split('\t')
        word = data[0]
        count = int(data[2])
        if word in freqs:
            freqs[word] + count
        else:
            freqs[word] = count

    end = time.time()
    print(f'{end-start:.4f}')
