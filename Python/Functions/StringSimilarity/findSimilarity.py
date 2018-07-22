import stringFormatting

def jaccardDistance(text_1, text_2):
    # Jaccard Distance

    data = [text_1, text_2]
    formattedWords = []

    for text in data:
        formattedWords.append(set(stringFormatting.stringFormat(text)))

    set_1, set_2 = formattedWords

    intersection = set_1.intersection(set_2)
    union = set_1.union(set_2)

    j = len(intersection) / len(union)

    return j

def cosineSimilarity(text_1, text_2):
    pass