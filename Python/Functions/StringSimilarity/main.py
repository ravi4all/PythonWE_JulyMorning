import findSimilarity

def main():
    # text_1 = 'Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace.'
    # text_2 = 'Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under the GNU General Public License (GPL). This tutorial gives enough understanding on Python programming language.'
    text_1 = input("Enter first string : ")
    text_2 = input("Enter second string : ")

    similarity = findSimilarity.jaccardDistance(text_1, text_2)
    # similarity = findSimilarity.cosineDistance(text_1, text_2)
    print("Similarity is",similarity)

main()