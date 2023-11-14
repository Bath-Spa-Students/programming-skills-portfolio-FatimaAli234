#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output

Glossary={
    "Variable":" symbolic name given to an unknown quantity that permits the name to be used independent of the information it represents",
    "Function":"a block of code that performs a task.",
    "List":"An ordered collection of items that can be of different data types.",
    "Dictionary":"A key-value data structure used to store and organixe information.",
    "String": "A sequence of characters, often used to represent text, enclosed in single or double quotes.",
}


Glossary["Tuple"] = "An immutable ordered collection of items, usually enclosed in parentheses."
Glossary["Loop"] = "A control structure which repeatedly executes the block of code."
Glossary["Syntax"] = "A set of rules that dictate the combinations of keywords and symbols used in a programming language."
Glossary["Module"] = "A file containing Python code that can be imported and used in other programs."
Glossary["Algorithm"] = "A step-by-step procedure or set of rules for solving a specific problem or accomplishing a particular task in a finite number of steps."
for word, defination in Glossary.items():
    print(f"{word}:\n{defination}\n")