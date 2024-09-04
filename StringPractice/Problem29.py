import textwrap

# Write a Python program to set the indentation of the first line.
sample_text ='''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

# Use 'textwrap.dedent' to remove common leading whitespace and 'strip' to remove any trailing whitespace.
text1 = textwrap.dedent(sample_text).strip()

# Use 'textwrap.fill' to format and wrap the 'text1' string to a line width of 80 characters.
# The 'initial_indent' and 'subsequent_indent' parameters control the indentation, which is adjusted here.
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))

print() 
