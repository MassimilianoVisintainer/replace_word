def replace_word():
    str = "Hi all, my name is Max. I wish you all a good day"
    word_to_replace = input("Which word you wanna replace:")
    word_replacement = input(" With which word you wanna replace it?")
    print(str.replace(word_to_replace,word_replacement))

replace_word()