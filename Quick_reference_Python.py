"""
This document is created using the reference of official python tutorial
(https://docs.python.org/3/tutorial/).This material is not a complete reference
of python programming language. Here you can find quick reference of python
syntaxs and some of it's basic concepts.
"""

""" Using  Interpreter """

# To start interpreter
python or python3 # in terminal(linux)
python # in command prompt (Windows) or you can directly open IDLE

# To check the version

python --version or python3 --version

# To stop the interpreter
 control + D to stop # in linux
 ctrl + Z to stop # in Windows


# give the commands in double quotes

# Example : python -c "print(6 + 7)"
 python -c command [args] # give the commands in double quotes
# Example : python -m pip install numpy (Here pip is the module)
 python -m module [args]


# Source code encoding

"""
Note : By default pyhton uses UTF-8 encoding method. To read any python file
editor must recognize UTF-8
"""
# To declare encoding other than the default encoding method.
# The following line should be added in first line of your python code
"# -*- coding: encoding_type(UTF-8 or cp1252 etc)" #(with out quotes) for windows

# For unix you have to add the line in second line

# An Introduction

# This is the single line comment (Begin with Hashtag symbol)
"""
This is muliple line comment (enclosed with triple double Quotes)
"""

# Pyhton as calculator

# Interpreter act as a simple calculator
# Numbers
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6

"""
Note: There is a difference between / and //. / is a classical division and
// is a floor division
"""

>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
>>> width = 20 # Equal operator is used to assign the value. Here width is assigned to 20
>>> height = 5 * 9
>>> width * height
900

"""
Note : If the variable is not assigned with any value. Then the interpreter
will give you an error.
"""

>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined

"""
Note : There is a high priority for floating point operator. If you mixed the
floating point value in any operation then the result will be in floating point value.
"""

>>> 4 * 3.75 - 1
14.0

# In python there is a built-ion function for the complex number
>>> 2 + 5j # by indicating j at the end you are telling the interpreter as this
           # number is a complex number

# Strings
