#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

my_string = "Hello, I am a string"
my_number = 46
my_list = [3,2,1]
my_boolean = False

#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

my_string =  "Hello World"
three_characters = my_string[:3]
print(three_characters)

#Exercise 3: Use an index to grab the first element from your list.

first_list_element = my_list[0]
print(first_list_element)

#Exercise 4: Create a new number variable that adds 10 to your original number.
	
original_number = 46
new_number = original_number + 10
print(new_number)

#Exercise 5: Use an index to get the last element in your list.

last_list_element = my_list[-1]
print(last_list_element)

#Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'

names = 'harry,alex,susie,gail,conner'
names_list = names.split(',')
print(names_list)

#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

my_string = "Hello World"
first_word = my_string.split()[0]
uppercase_first_word = first_word.upper()
new_string = f"{uppercase_first_word}{my_string[len(first_word):]}"
print(new_string)


#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

my_number = 1374821	
print(f"My number is {my_number}.")


#Exercise 9: Print “hello world”.

print("hello world")