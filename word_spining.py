def spin_words(words):

    return " ".join(word[::-1] if len(word) >= 5 else word for word in words.split())


if __name__ == "__main__":

    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert spin_words("This is another test") == "This is rehtona test"
    assert spin_words("Welcome") == "emocleW"
    assert spin_words("to") == "to"
    assert spin_words("CodeWars") == "sraWedoC"
    print("Pasa los casos test")