''' This is the 1st chaleenge'''
name = 'Julie'
age = 12
"""print(f'My name is {name} and I am {age} years oold')"""
sentence = f"Hi my name is {name} and I am {age} years old"
print(sentence)

if age > 18:
        print('You are older than 18')
        print('This is another line')

else:
        print('You are younger than 18 years old')

'''Below is the second challenge on the if-else'''
year = 2021

if 2000 < year < 2100:
        print('You are welcome to the 21st century')

else:
        print('You are before or after the 21st cecntury')

'''This is the third challenge on fuctions'''

def hello(name,age):
    print('Hello {}, you are {} years old'.format(name,age))

hello('Alok Rahul',16)

'''If you have to use the return, the code can be used as below'''
def helloreturn(name,age):
    return 'My name is {} and my age is {}'.format(name,age)

sentence = helloreturn('Alok',23)
print(sentence)

'''Challenge 3#Create a funtion named tripleprint that takes a string as a parameter and prints that string 3 times in a row. So if i passed in the string hello , it would print hellohellohello'''

def tripleprint(word):
    print(word*3)

'''List'''

dognames = ['Sally', 'fIDO','udemy', 'pluralsight']
dognames.insert(0,'newDog')
print(dognames)

print(dognames[2])

'''print('delete the third element of the dognames list by del(dognames[2] command')
del(dognames[2])
print(dognames)'''

print('You can find the length of the list by using the len')
print(len(dognames))

'''Udate the existing elemnt of list by below method'''
dognames[4]='Jane'
print(dognames)

print('You can have not just string but anything you want in list')
dognames = ['Sally\n','Fido','Udemy','Jane',23,54,0.342,False,True,]
print(dognames)

'''Challenge 4 # Create a varaible name shooes that is a list of the following items, in order : Spizikes, Air Force1, Curry2, Melo 5'''

shoes = ['Spizikes','Air Force 1','Curry 2', 'Mello 5']
print(shoes)

''' Lets go for the loops'''
print('This is the outcome by using the for loop')
for d in dognames:
    print(d)

print('If you want to run for loop using the range and not list you can do so like this')
for i in range(1,11):
    print(i)

print('Below  is the output from the while loop')

age=0
while age < 7:
    print(age)
    age+=1
'''Chalenge 5 # I have given you a list of ints called numbers, print every nunmber that is greater than 90'''

print('This is output from the challenge 5')
numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 44, 33, 38, 10, 40, 44, 70, 81, 43, 25, 35, 65, 27, 56, 45, 33, 98, 89, 90, 65, 345, 34, 355, 56, 43]
for num in numbers:
        if num > 90:
            print(num)
'''This is the sixth topic , dictioneries'''
print('This is the example of the dictionary, which is the next topic')

dogs =  {"Fido":8,"Sally":7,"Sean":2,"Jane":5}
print(dogs)

print(' Dictionary output is not always in order, dictionary is used to get the values based on key.. which we will see below for Sean ' )

print(dogs["Sean"])

print('If you need to delete wny of the data from dictionaries, you can do so by deleting the key in del.. we have deleted the sally in here')
del(dogs["Sally"])
print(dogs)

print('If you want to add an element to the dictionaries, you can do so by below example of passing its key and value')

dogs["Sarah"] = 9
dogs["Fido"] = False
print(dogs)

print('This is the Dictionaries challenge number 6 : Create a dictionary called cooldictionary where you use words for keys and and definitions for values.')
words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go", "To collect spare changes, either from couches, passerbys on the street or any numerous other ways and means", "When your phone or tablet indicates that you are connected to a wireless network , however you are still not able to load webpages or use any internet services with your device"]

cooldictionary = {}
for i in range(0,3):
    cooldictionary[words[i]] = definitions[i]
print(cooldictionary)

''' We will  now cover the last topic that is the class in refresher '''
print('Generally the class created in python is in the apital letters, you can create methods inside the class')

class Dog:
    dogInfo = 'Hey Dogs , are reallllyy cool'
    def bark(self):
        print('Bark! Bhaw bhaw, Loud Bhaw!!')

'''Once class is created , you can create an object of the class and call in the method of class like shown below'''
mydog = Dog()
mydog.bark()

mydog.name = "Hugo"
mydog.age = 22
print(mydog.name, mydog.age)
print(Dog.dogInfo)
print('Now, the properties dogInfo of class Dog can be changed in runtime by assigning new value to it')
Dog.dogInfo = "Hey there, you dogs are cool"
print(Dog.dogInfo)

print('Lets introduce the init function into the class')

class NewDog:
        def __init__(yey,name='',age=0,furcolor=''):
                yey.name = name
                yey.age = age
                yey.furcolor = furcolor
        
mydog = NewDog("Fado",23,"Green")
print(' This is the name of the dog: ' +mydog.name)
print(mydog.age)

""" Challenge 7 :- Add a method to the Car class called age that returns how old the car is (2020 - year), Be sure to return the age and not print it.
class Car:
        def __init__(self,year, make,model):
                self.year = year
                self.make = make
                self.modedl = model """

print('This is the challenge 7 solution on class ' '\n')

class Car:
        def __init__(self,year, make, model):
                self.year = year
                self.make = make
                self.model = model
        def car_age(self):
                return 2020 - self.year

mycar = Car(1993, "BMW", 123)
print(mycar.make)

'''This is the end of the Python refresher Excercise '''


