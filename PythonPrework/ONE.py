# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name): 

def hello_name(user_name):
    print("hello_", user_name)

hello_name("Anything")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():   
    for x in range(1, 101): 
        if x % 2 == 1:
            print(x)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    result = 0
    for x in a_list:
        if (x > result):
            result = x
    return result
    
print(max_num_in_list([1,2,2,4,5,6,7,7,1231]))

