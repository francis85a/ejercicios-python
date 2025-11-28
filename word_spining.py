def spin_words(words):
    result = ""
    
    for word in words.split():
        if len(word) >= 5:
            result += word[::-1] + " "
        else:
            result += word + " "
    return result.strip()
