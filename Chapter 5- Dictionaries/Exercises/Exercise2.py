# Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# * Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
# their meanings as values.
# * Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
# the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
# each word-meaning pair in your output.


Glossary={
    "Variable":" symbolic name given to an unknown quantity that permits the name to be used independent of the information it represents",
    "Function":"a block of code that performs a task.",
    "List":"An ordered collection of items that can be of different data types.",
    "Dictionary":"A key-value data structure used to store and organize information.",
    "String": "A sequence of characters, often used to represent text, enclosed in single or double quotes.",
}
  
for word, defination in Glossary.items():
    print(f"{word}:\n{defination}\n")