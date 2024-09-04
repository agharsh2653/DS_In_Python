import textwrap

# Define a multi-line string 'sample_text' with text content that includes indentation.
sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''

# Use 'textwrap.dedent' to remove the common leading whitespace (indentation) from 'sample_text'.
text_without_Indentation = textwrap.dedent(sample_text)

# Print an empty line for spacing.
print()

# Print the 'text_without_Indentation', which is the 'sample_text' with indentation removed.
print(textwrap.indent(text_without_Indentation,">>"))

# Print an empty line for spacing.
print()