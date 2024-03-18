# однопоточная модель MapReduce
import functools
from typing import Dict

def map_frequence(text: str) -> Dict[str, int]:
    words = text.split(' ')
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] = frequencies[word] + 1
        else:
            frequencies[word] = 1
    return frequencies

def merge_dictionaries(first: Dict[str, int],
                        second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged

lines = ["I know what I know",
        "I know what I know",
        "I don't know much",
        "They don't know much"]

mapped_results = [map_frequence(line) for line in lines]
for result in mapped_results:
    print(result)

print(functools.reduce(merge_dictionaries, mapped_results))

