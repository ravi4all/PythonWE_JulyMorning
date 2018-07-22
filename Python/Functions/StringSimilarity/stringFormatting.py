def stringFormat(text):
    # Tokenization
    tokens = text.split()
    # Convert words to lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    # Removing . and ,
    for i in range(len(tokens)):
        if tokens[i].endswith("."):
            tokens[i] = tokens[i].replace(".","")
        elif tokens[i].endswith(","):
            tokens[i] = tokens[i].replace(",","")

    # Removing Stopwords
    stopwords = ['is','am','and','the','that','by','as',
                 'are','was','it','this','a','on','in',
                 'for', 'has', 'also'
                 ]

    wordsList = []
    for word in tokens:
        if word not in stopwords:
            wordsList.append(word)

    return wordsList
