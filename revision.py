#Write a Python function that takes two arguments (a and b) and returns their sum.
def add(a,b):
    return a+b
a=5
b=4
print(add(a,b))
#Write a Python function that takes a string as input and returns the string reverse
def reversed_string(name):
    return name[::-1]
name="yvonne"
print(reversed_string(name))
#Write a Python function that takes a list of integers as input and returns the sum of all the integers in the lis
def list_of_intergers(nums):
    sum=0
    for num in nums:
        sum+=num
        return sum
    print(list_of_intergers(3,5,2,7,9))


#Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
def removed_evenNumbers(number):
    newArray[]
    for num in number:
        if num%2!=0:
            newArr.append(num)
    return newArr

list=[2,5,4,6,7,1,9] 
print(remove_even_numbers(list))       

#Write a Python function that takes a list of integers as input and returns the highest value in the list.
def get_height_value(numbers):
    



#Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.
def capitalize_strings(games):
    return[string.capitalize()for string in games]
games=["netball","football","hockey"]
print(capitalize_string(games))