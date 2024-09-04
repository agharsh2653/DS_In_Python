#27. Write a Python program to remove existing indentation from all of the lines in a given text.

import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''

print()
remove_existing_indentation = textwrap.dedent(sample_text)
print(remove_existing_indentation)