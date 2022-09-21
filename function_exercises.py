#!/usr/bin/env python
# coding: utf-8

# ## Q1

# In[10]:


# is_two defines one parameter, n that is an int, and returns a boolean value
def is_two(n):
    
    #we check to see if the argument is equal to 2 and return the boolean value
    return n == 2
#is_two(2)


# ## Q2

# In[30]:


# is_vowel defines one parameter, n that is a string, and returns a boolean value
def is_vowel(n):
    
    # check to see if the argument is equal any vowel characters and return boolean value
    return n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u'
#is_vowel('a')


# ## Q3

# In[23]:


# is_consonant defines one parameter, n that is a string, and returns a boolean value
def is_consonant(n):
    
    # check to see if the argument is NOT equal to ALL vowel characters and return a boolean value
     return n != 'a' and n != 'e' and n != 'i' and n != 'o' and n != 'u'
#is_consonant('c')


# ## Q4

# In[93]:


# cap_start_con takes in user input, n as a string, and returns users input capitalized so long as it begins with a consonant
def cap_start_con():
    
    # user input string as n
    n = input('Enter a word: ')
    
    # initialize string vowel used to compare first position of user input n
    vowel = 'aeiouAEIOU'
    
    # check to see if first position in user input n is within string vowel
    if n[0] in vowel:
        
        # prints error message, ends function
        print('No consonant in first position')
        
    # continues function
    else:
        # runs python function to capitalize string on user input n
        n = n.capitalize()

    return n
#cap_start_con()


# ## Q5

# In[94]:


# calculate_tip takes in two user inputs as arguments, n and m which are casted as a float from string
# returns a single float
def calculate_tip():
    
    # user input percentage as n to multiply total bill by to get tip
    n = float(input('Enter tip %: '))
    
    # user input total bill as m to multiply percentage by to get tip
    m = float(input('Enter total bill: $'))
    
    # calculated tip by multiplying n and m
    tip = (.01*n)*m
    
    # we round the result of the calculations to the nearest second decimal point
    tip = round(tip, 2)
    
    # return string with rounded tip amount
    return print(f'Tip calculated: ${tip}')

#calculate_tip()


# ## Q6

# In[54]:


# apply_discount takes in two user inputs as arguments, n and m as floats, and returns a float
def apply_discount():
    
    # user input price n
    n = float(input('Enter price: $'))
    
    # user input discount m
    m = float(input('Enter discount %: '))
    
    # equation to find discounted price using n and m as discountprice
    discountprice = (1-(.01*m))*n
    
    # rounding result of discountprice
    discountprice = round(discountprice, 2)
    
    # return string with discountprice
    return print(f'Discounted Price: ${discountprice}')


#apply_discount()


# ## Q7

# In[ ]:


# handle_commas takes in user input, n as a string, and returned an int
def handle_commas():
    
    # takes in user input as a string n
    n = input('Enter a number with commas: ')
    
    # removes commas and replaces character with nothing
    n = n.replace(',','')
    
    # returns n casted as an int, returns error if user input is not a number
    return int(n)
#handle_commas()


# ## Q8

# In[4]:


# get_letter_grade takes in user input, n as a string, and returns a string
def get_letter_grade():
    
    # user input as a string which gets casted to an int
    n = int(input('Enter a number: '))
    
    
    # n is checked against multiple ranges to determine what string will be returned
    if n in range(90,101):
        return 'Grade A'
    elif n in range(80,90):
        return 'Grade B'
    elif n in range(70,80):
        return 'Grade C'
    elif n in range(60,70):
        return 'Grade D'
    elif n in range(0,60):
        return 'Grade F'
#get_letter_grade()


# ## Q9

# In[67]:


# remove_vowels takes in user input, n as a string, and returns a string
def remove_vowels():
    
    #initialize local variable string to compare
    vowels = 'aeiouAEIOU'
    
    #initialize local variable empty string to build new string to return
    result = ''
    
    # user input string to compare
    n = input('Enter a word with vowels: ')
    
    # loop to iterate through characters in user input string n
    for letter in n:
        
        # compares letter to vowels and checks if letter is not a vowel
        if letter not in vowels:
            
            # adds passing letter to result string
            result += letter
            
     #return newly built string result       
    return result
#remove_vowels()


# ## Q10

# In[84]:


import re #Regular expression operations
def normalize_name(n):
    
    # user input as a string n
    #n = input('Enter a string with valid python identifiers: ')
    
    # replaces spacese with underscores
    n = n.replace(' ','_')
    
    # casts string as all lower case characters
    n = n.lower()
    
    # removes white space before and after string
    n = n.strip()
    
    #removes non-alphanumeric character from string
    n = re.sub(r'\W+', '', n) #used import instead of a more intensive workaround
    return n
#normalize_name()


# ## Q11

# In[91]:


# cumulate_sum function takes in one argument, nlist as a list, and returns a list
def cumulate_sum(nlist):
    
    # local variable to mark the position and its cumulative sum
    position = 0
    
    # local variable empty list to be built with cumulative sums
    cum_list =[]
    
    # iterate through numbers in nlist
    for i in nlist:
        
        # sum value of position and i
        position=position+i
        
        #updates empty list with results of summation
        cum_list.append(position)
        
    # returns new list   
    return cum_list
    
#cumulate_sum([1,2,3,4,5]) # or just import numpy and use numpy.cumsum()

