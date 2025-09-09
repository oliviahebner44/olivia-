# file: homework1.py 
# --- Variables and Data Types ---

a = 10 
print(a)
print(type(a)) # a is an integer, a whole number with no decimals 

b = 1.5
print(b) 
print(type(b)) # b is a float, a decimal 

c = 3j
print(c)
print(type(c)) # c is a complex, a whole number with a variable 

d = "hello"
print(d)
print(type(d)) # d is a string, a word

e = [1, 2, 3] 
print(e)
print(type(e)) # e is a list, a list of numbers 

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dict (dictionary), stores in pairs 

g = (1,2) 
print(g)
print(type(g)) # g is a tuple, an ordered, unchangable collection that holds different data types 

h = ["apple", "banana", "strawberry"]
print (h)
print(type(h)) # h is a list, a list of words 

i = True 
print(i) 
print(type(i)) # i is a bool, can only have 2 outcomes (true or false) 

j = None 
print(j)
print(type(j)) # j is a Nonetype, represents nothing or no value 

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, has different data types

l = str(14)
print(l)
print(type(l)) # l is a string, enclosed in quotes 

m = 1e4
print(m)
print(type(m)) # m is a float, a number with a decimal point 

# 1. There was 9 different data types 
# 2. integer, float, complex, string, list, dict, tuple, bool, nonetype
# 3. b and m, l and d, k and e and h 
# 4. l is a string because it has str() in it which makes it a string by representing quotations  
# 5. the new data type is a set 

n = {1, 2, 3}
print(n)
print(type(n)) # n is a set, an unordered collection of unique parts 




# --- Booleans ---
print(10 > 9) # True, 10 is greater than 9 
print(10 == 9) # False, 10 does not equal 9 
print(10 <= 9) # False, 
print(bool("abc")) # True 
print(bool(123)) #True 
print(bool(["apple", "cherry", "banana"])) # True 
print(bool(True)) # True 
print(bool(False)) # False 
print(bool(0)) # False 
print(bool("")) # False 
print(bool("  ")) # True 
print(bool(())) # False 
print(bool({})) # False 
print(bool([])) # False 
print(bool(True and False)) # False 
print(bool(True and True)) # True 
print(bool(False and False)) # False 
print(bool(True or False)) # True 
print(bool(True or True)) # True 
print(bool(False or False)) # False 
print(bool(not(False))) # True 
print(bool(not(True))) # False 

# Questions 
# 1. non zero numbers, non empty strings are true. zero, empty strings are false. "and" is true only if both are true. "or" is true if at least 1 is true. not is the opposite 
# 2. ("  ") being true suprised me the most 

print(bool(True or apple))
# 3. True because it is "or" and at least one is true 

print(bool(False and apple))
# 4. False because it is "and" and contains false 



# --- Operators --- 

# --- Arithmetic Operators 
print(10+5) # 15, + performs addition 
print(10 - 5) # 5, - performs subtraction 
print(2*4) # 8, * performs multiplication 
print(6/3) # 2.0, / perfoms division 
print(5%2) # 1, % is the remainder after dividing a by b 
print(3**2) # 9, ** raises to the power 
print(15//2) # 7, divides, and rounds down 

# --- Comparision Operators ---
print(5 ==2) # false, 5 does not equal 2
print(10 !=10) # false, != means not equal to 
print(2<5) # true, 2 is less than 5
print(12>5) # true, 12 is greater than 5 
print(5<=6) # true, 5 is less than or equal to 6 
print(1>=10) # false, 1 is not greater than or equal to 10 

# --- Assignment Operators ---
x = 5 
x -= 4
print(x)
x += 5
print(x)
x *= 3 
print(x)

# --- Logical Operators ---

# 1. 'and' is used to combine two bool experssions. it returns true only if they're both true 
print(True and True)
print(True and False)

# 2. 'or' combines two bool expressions. only true if at least one is true. 
print(True or False)
print(False or False)

#3. 'not' does the referse of the experession 
print((not(False)))
print(not(True))

# --- More Questions --- 
# 1. / is divide by and // is also divide by but round down 
# 2. % is just the remainder and // is just the answer with no remainder 
# 3. use % to find the remainder 
print(6%4)
# 4. assignment operators are shortcuts that combine operators with assignment.


# --- Strings --- 
my_string = "hello"
print(my_string)
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[-1])
print(my_string[1:3])
print(my_string[0:5:2])
print(len(my_string))
print(my_string + "goodbye")
print(7*my_string)

# 1. slicing extracts a part of a string. in line 158 through 165 I sliced parts of the string 
# 2 
name = "Oski"
print("Hello, my name is", name) # Hello, my name is Oski 
# 3
name = "Oski"
print(f"Hello, my name is {name}") # Hello, my name is Oski 
# 4 The results are the same. F string is where things inside {} is nserted directly into the string 

# --- Termial Commands ---
# 1. cd
# changes firectories. Use it to move from one folder to another 
# example: cd Desktop 
# 2. ls 
# list all files and directories in the current folder. 
# ex: ls python_decal_fa25
# 3. ls -a 
# lists the files and directories in current folder, all of them including hidden files (ones that start with .)
# 4. mkdir 
# makes a new folder 
# 5. cat 
# stands for concatenate, it reads and displays the contents of files 
# 6. pwd 
# stands for print working directory, shows the full file path you are on 
# 7. cd .. 
# moves you up one folder from where you are 
# 8. cd . 
# just makes you stay where you are 
# 9. cd ~
# takes you back to the home diretory 
# 10. cp 
# stands for copy and copies files or directories. 
# 11. mv
# stands for move, can relocate or rename a file 
# 12. rm 
# stands for remove, deletes files or directories 
# 13. clear 
# clears the terminal screen, removing previous commands and output 
# 14. grep 
# used to search for text in files or outputs, looking for matches to a pattern or string 

# --- Questions ---
# 1. 
# touch: create an empty file 
# head: display the first few lines of a file 
# tail: display the last few lines of a file.
# 2. They both list files and folders, but the -a shows all hidden files 
# 3. A hidden file is not normally visible when you list directory contents, it starts with a dot and is used to prevent accidental modification on a file that doesn't need to be touched. 
# 4.
# -l (long format): shows detailed info about files like type, size, links, owners
# -t (sort by modification time): sorts files by last modified time, good for finding recently editied files 
# -R (recursive): lists all files in current directpry and all subdirectories









