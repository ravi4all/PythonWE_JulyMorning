text_1 = "hello this is python programming and learning python is really easy and python is mostly used for machine learning"
text_2 = "python is a great language for beginners and machine learning is one of the implementation of python"

# Step-1 : Tokenization
list_1 = text_1.split()
list_2 = text_2.split()

# Step-2 : Remove Stopwords - is,am,are,the,a,in,at,for,that
stopwords = {'a','is','am','are','the','and','for','used','of','this'}
set_1 = set(list_1) - stopwords
set_2 = set(list_2) - stopwords

numer = len(set_1.intersection(set_2))
denom = len(set_1.union(set_2))

j = numer / denom * 100

print("Similarity Score is",j,"%")
