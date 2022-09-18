# Identity exercise Q1:

# Identify the data type of the following values.
print(type(99.9))
# 99.9 == float
print(type("False"))
# "False" == string
print(type(False))
# False == boolean
print(type('0'))
# '0' == string
print(type(0))
# 0 == int
print(type(True))
# True == boolean
print(type('True'))
# 'True' == string
print(type([{}]))
# [{}] == list
print(type({'a':[]}))
# {'a':[]} == dictionary

#Q2
#What data type would best represent:

#A term or phrase typed into a search box?
#string
#If a user is logged in?
#boolean
#A discount amount to apply to a user's shopping cart?
#float
#Whether or not a coupon code is valid?
#boolean
#An email address typed into a registration form?
#string
#The price of a product?
#float
#A Matrix?
#list
#The email addresses collected from a registration form?
#string
#Information about applicants to Codeup's data science program?
#dictionary

#Q3 real world example variables
#Rent example
price = 3;
days_rented = 0;
like_it = True;
dont_like = False;

#contractor example
google_pay = 400;
amazon_pay = 380;
fb_pay = 350;
hours_worked = 0;

#student example
class_not_full = True;
class_full = False;
schedule_clear = True;
schedule_conflict = False;

#product offer example
items_purchased = 0;
items_purchased > 2;
offer_available = True;
premium = True;
items_purchased_prem = 0;
items_purchased_prem = 0;

#username and password
username = 'codeup'
password = 'notastrongpassword'
password_len = 0;
password_len > 5 and password_len < 20
username != password