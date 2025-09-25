# String    - "in quotations"
# Integer   - a whole number ex. 1 4 -10 ect.
# Float     - a decimal number ex. 3.14159265359
# Char      - a single glyph ex.  'c'
# Bool      - True or False

# How to define a variable!!
# <name> = <value>

lowercase = False
UPPERCASE = False
UpperCamelCase = False      #All lowercase, no spaces, capital for new words
lowerCamelCase = False      #All lowercase, no spaces, capital for new words
snake_case = True           #All lowercase, underscores for spaces
SCREAMING_SNAKE_CASE = False

# Other general rules to naming things
# 1. Concise
#   -

the_font_size_for_paragraphs = 10
font_size_para = 10
paragraph_size = 10
para = 10

#Get the number as a string
num = input("What number do you want to square?\n> ")

#Parse (convert) the string to an integer (cast)
num = int(num)

#Do math and print
print(num * num)
