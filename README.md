# Replace Word in String

This Python function `replace_word()` allows users to replace a specific word in a given string with another word.

## Usage

1. **Function Description:**

   The `replace_word()` function takes a string, prompts the user to input the word to be replaced (`word_to_replace`), and the word to replace it (`word_replacement`). It then replaces all occurrences of `word_to_replace` in the string with `word_replacement` using the `str.replace()` method.

2. **How to Use:**

   - Run the Python script containing the `replace_word()` function.
   - The function will prompt you to input the word you want to replace (`word_to_replace`) and the word you want to replace it with (`word_replacement`).
   - It will then display the modified string with the replaced words.

3. **Example:**

   ```python
   def replace_word():
       str = "Hi all, my name is Max. I wish you all a good day"
       word_to_replace = input("Which word you wanna replace: ")
       word_replacement = input("With which word you wanna replace it? ")
       print(str.replace(word_to_replace, word_replacement))

   replace_word()
