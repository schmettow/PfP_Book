# Lists {#lists}


```python
message = ["Hello,"]
message.append("world")
print(" ".join(message))
```

```
## Hello, world
```

In chapter, 2 Variables, you encountered the four basic data types of the Python programming language: *integers*, *floats*, *Strings* and *Booleans*. You also learned that apart from these four basic data types, Python knows numerous specialized types. In this chapter, you will learn more about one group of these specialized data types: *collections*.

## Lists

One type of collection are *lists*.


```python
a = [10, 5, 15, 25]
b = ["eggs", "bacon", "cheese"]
c = [4, "hello", 7.3, False]
```

The easiest way of creating a list is surrounding some values with cornered brackets `[]` and separating the values of the list with commas `,`. The values that make up a list are called *items* or *elements*.

A special type of list is the so-called *empty list*. An empty list is a list with no elements. Empty lists are denoted with `[]`. Lists can also be *nested* into one another to form *lists of lists*.


```python
a = []
b = [True, 2.0, "hello", [5,6]]
```

In a sense, lists are similar to *Strings*. Strings are basically ordered collections of *characters*. For example, the word `Hello` is an ordered sequence of five characters: `H`,`e`, `l`, `l`, and `o`.
In contrast to Strings, however, the elements of lists can be of *any* type. Ordered collections such as strings and lists are also called *sequences*.

Lists are *ordered* collections of values. However, a list being *ordered* has nothing to do with how humans may be inclinded to order the elements of a list. For example, you may want to order a list `a` with three elements `"A", "B",` and `"C"` according to their alphabetic order: `a = ["A", "B", "C"]`. However, for lists, the value of an element is irrelevant for its position in the list. Lists are not *ordered* because they grasp some underlying semantics about their elements and rank their elements accordingly. In fact, element values are arbitrary for a list. Instead, lists are called *ordered* because they allocate a certain position in memory to each element. Each list element occupies a unique position in memory. Elements of a list are accessed by querying the list at a specified position, a so-called *index*. Accessing a list at a specified index, the value located at that position in memory is returned. The *index operator* `[]` is used to access list elements at specified indices.


```python
a = [3, 17, 8]
print(a[0])
```

```
## 3
```

```python
print(a[1])
```

```
## 17
```

The *expression* inside the brackets of the index operator (in this case the integers `0` and `1`) specifies the *index* of the to-be selected element. Each element inside a list has a unique index, an *integer* describing the element's position in the list. One major cause of errors surrounding lists is that indices start at `0`, not at `1`, as you might expect. This means that the first element of a list is accessed by indexing `0`, not `1`!


```python
a = ["Hello", "World", "!"]
print(a[0])
```

```
## Hello
```

```python
print(a[2])
```

```
## !
```

### Lists are mutable
In contrast to Strings, lists are *mutable* sequences. This means that even after a variable is assigned a list value, specific elements of the list can be changed without reassigning a completely new list! You can use the *index operator* to change specific list items.


```python
shoppinglist = ["appels", "bananas", "tomatoes"]
shoppinglist[2] = "peaches"
print("Updated shopping list: " + ", ".join(shoppinglist))
```

```
## Updated shopping list: appels, bananas, peaches
```


```python
a = [1,2]
a[0] = 10
print(a)
```

```
## [10, 2]
```

But watch out, you **cannot** use the index operator to add new elements to a list. To do so, you would need to access a new index, an index not yet claimed by an existing list element. Trying to access an index outside of the current range of indices will produce an index out of range error.

```{}
a = [1,2]
a[2] = 10
print(a)

IndexError: list assignment index out of range
```

There are several ways of adding elements to a list.


```python
a = []
a.append(1)
print(a)
```

```
## [1]
```

```python
a.append(2)
print(a)
```

```
## [1, 2]
```

The *append* method adds the specified element at the end of the list. You can use the *extend* method to add *multiple* values of another list (or other type of collection) to your list.


```python
a = [1,2]
b = [3,4]
a.extend(b)
print(a)
```

```
## [1, 2, 3, 4]
```

Note that there is a difference between appending a list and extending your list with another list.


```python
a = [1,2]
b = [3,4]
a.append(b)
print(a)
```

```
## [1, 2, [3, 4]]
```

In the above example, **extending** `a` with `b` causes the elements stored in `b` to be appended to `a` sequentially, each of them constituting a new element in `a`. In contrast, the whole list `b` is regarded as an element of `a` when `b` is **appended** to `a`. 
Because lists are mutable, you can sequentially fill them with elements, one by one. This is very handy for storing values you generate throughout your program.

Using the index operator, you can access (and change!) several elements at a time in a list using so-called *list slices*:


```python
a = [1, "a", 2, "b", 3, "c"]
print(a[1:4])
```

```
## ['a', 2, 'b']
```

```python
print(a[0:2])
```

```
## [1, 'a']
```

```python
a[0:2] = "d"
print(a)
```

```
## ['d', 2, 'b', 3, 'c']
```

The indices around the `:` colon indicate the starting and ending index of the selected list slice. Note that a list slice will always include the element located at the starting index, but exclude the element located at the ending index. To include `2` in the second list slice you would thus need to access `a[0:3]`, or simplified `a[:3]`. The latter meaning "every element up until, but excluding index 3".

Note that the statement `a[0:2] = d` mutates both elements, `1` *and* `"a"` into a single new item `"d"`. This means that the statement did not only change some elements of `a`, but also `a`'s total number of elements!

When no starting or ending index is specified, the `:` expression selects all elements of a list and can be used for *cloning* lists.


```python
a = [1, "a", 2, "b", 3, "c"]
aCopy = a[:]
print(aCopy)
```

```
## [1, 'a', 2, 'b', 3, 'c']
```

###A word about class specific functions
By now, you have seen a few examples of class-specific *functions*, such as `append()` for lists or `join()` for strings. Even though a detailed explanation of *functions* (also called *methods*) is postponed to Chapter \@ref(functions), a quick introduction to objects, classes, and class-specific functions will help you make the most of your lists and their built-in functions. For now, you can see functions as pieces of reusable code.

When you create a variable `a` and assign a value to it, say `[4,5]`, you can think of it as creating an *object* (i.e. an instance) of the Python *class* *list*. The *list* class has been programmed by the developers of the Python language, same as any other built-in Python class, such as integers and strings. Classes are blueprints, a specification of how to build certain objects. Engineers use blueprints to build cars, buildings, bridges and more. Chefs use recipes to put together meals. Python classes are the same in that they specify how objects of a certain type are programmed when you initiate them. A class has built-in *methods* that can be used by *any* object that has been create using the class' blueprint. This is very useful, because you can use a wide range of useful functions specifically designed for instances of the class. Your lists can use a range of built-in functionalities simply because they inherit these functionalities from their initial blueprint. An example is the `append()` method for the `list` class.


```python
a = [4,5]
a.append(6)
print(a)
```

```
## [4, 5, 6]
```

The `append()` method adds the value specified between the brackets to the end of the list. Typing `help(list)` in your console will give you a complete list of built-in functions of the class `list` and what their functionalities are.

What is the take-home message of this excursion to object-orientation? Make use of built-in class functions as much as you can! They provide a tremendous amount of functionality which you are likely going to need and want, written in neat code which makes them very efficient to use.

The interested reader can find more information on Python classes [here](https://docs.python.org/2/tutorial/classes.html).

## Tuples

Much like lists, *tuples* are an ordered collection of values, but with less exentensive functionality and  their unique characteristic being that they are *immutable*. Once you created a *tuple* in memory, you cannot change its content.

```{}
thorndike = ("Edward", "Lee", "Thorndike", 1874, "Law of effect", "Law of exercise")
thorndike[4] = "Law of recency"

TypeError: 'tuple' object does not support item assignment
```

Tuples are usually used when you assume that a collection of values will not change in the course of your program. They are *records* of related information, chunked together so that we can use it as a single entity.

However, if you really need to change the contents of an already existing tuple, you can always assign a new value to the variable which holds the value of the tuple you want to change.


```python
thorndike = ("Edward", "Lee", "Thorndike", 1874, "Law of effect", "Law of exercise")
thorndike = thorndike[:] + ("Law of recency",)
print(thorndike)
```

```
## ('Edward', 'Lee', 'Thorndike', 1874, 'Law of effect', 'Law of exercise', 'Law of recency')
```

Note the `,` in the second assignment statement `("Law of recency,")`. Without the comma at the end of the parentheses, Python ignores the parentheses and treats the content of one-element tuples such as `("Law of recency",)` as the data type of the element (in this case a `str`). As a result, a *type error* is thrown when you try to concatenate the `thorndike` tuple and `("Law of recency")`.

Python has a very powerful *tuple assignment* feature that allows a tuple of variable names on the left of the assignment operator `=` to be assigned values from a tuple on the right of the assignment operator. Thereby you can easily perform several variable assignments in just one line!


```python
thorndike = ("Edward", "Lee", "Thorndike", 1874)
name, middle_name, surname, born = thorndike
print(name)
```

```
## Edward
```

```python
a, b = ("Hello", "World")
print(b)
```

```
## World
```


## Dictionnaries

*Dictonnaries* share similarities with real-life address books where you can find a person's contact details by looking up his or her name.


```python
address_book = {"studyadviser-PSY": "studyadviser-psy@utwente.nl ",
                "studentservices" : "studentservices@utwente.nl",
                "ICT-helpdesk"   : "servicedesk-ict@utwente.nl"
                }
print(address_book["studyadviser-PSY"])
```

```
## studyadviser-psy@utwente.nl
```


Dictionaries associate *keys* (e.g. a name) with *values* (e.g. contact details). The `key:value` pairs of a dictionnary are separated by commas. Each pair contains a *key* and a *value* separated by a colon `:`. `key:value` pairs are always one-to-one mappings. You can, of course, map a *key* to a *list* of multiple values. *Keys* are required to be immutable and unique within a dictionnary. This means that you cannot have two `"studyadviser-PSY"` keys in the `address_book`. Unlike sequence types, such as lists and tuples, the elements of a dictionnary are unorderded in the sense that they do not have indices that mark their position. Values contained in a dictionnary can solely be accessed through their *keys*.

Dictionnaries are mutable. You can modify the values of a dictionnary by accessing its associated key:


```python
address_book = {"studyadviser-PSY": "studyadviser-psy@utwente.nl ",
                "studentservices" : "studentservices@utwente.nl",
                "ICT-helpdesk"   : "servicedesk-ict@utwente.nl"
                }
                
address_book["studentservices"] = ("studentservices@utwente.nl", "0534892124")
print("The telephone number of the student services is", str(address_book["studentservices"][1]))
```

```
## ('The telephone number of the student services is', '0534892124')
```

You can add entries and remove whole entries of a dictionnary using the `del` statement.


```python
address_book = {"studyadviser-PSY": "studyadviser-psy@utwente.nl ",
                "studentservices" : "studentservices@utwente.nl",
                "ICT-helpdesk"   : "servicedesk-ict@utwente.nl"
                }
                
address_book["studentUnion"] = "studentunion@union.utwente.nl"
print(address_book)
                
```

```
## {'studentservices': 'studentservices@utwente.nl', 'studyadviser-PSY': 'studyadviser-psy@utwente.nl ', 'studentUnion': 'studentunion@union.utwente.nl', 'ICT-helpdesk': 'servicedesk-ict@utwente.nl'}
```

```python
del address_book["ICT-helpdesk"]
print(address_book)
```

```
## {'studentservices': 'studentservices@utwente.nl', 'studyadviser-PSY': 'studyadviser-psy@utwente.nl ', 'studentUnion': 'studentunion@union.utwente.nl'}
```


## Putting data structures to use

Lists, tuples and dictionnaries are used readily in programming interactive software, such as the Stroop experiment, to structure user data or structuring elements of the program in a computer's memory. Structuring user input makes later retrieval of information easier, for instance for the purpose of statistical analysis.


```python
KEYS     = {"red": K_b,
            "green": K_n,
            "blue": K_m}
RT = []
STATE = "wait_for_response"
if STATE == "wait_for_response":
    if event.type == KEYDOWN and event.key in KEYS.values():
        time_when_reacted = time()
        this_reaction_time = time_when_reacted - time_when_presented
        RT.append(this_reaction_time)
```


## Common errors

* `index out of range` errors are among the most common programming errors made, even by experienced programmers.They typically occur if you try to access an element that does not exist in a sequence.

```{}
shoppinglist = ["milk", "eggs", "bread", "appels"]
print shoppinglist[4]

IndexError: list index out of range
```

Most of the time, this error will occur because you confused the starting index `0` with `1`. Remember that, for instance, in a list of four elements the last element is stored at index `3`, instead of at index `4`.

```python
shoppinglist = ["milk", "eggs", "bread", "appels"]
print(shoppinglist[3])
```

```
## appels
```

* Trying to change the content of a *tuple*. Tuples are immutable, meaning that you cannot change their content after their initialization. You can, however, re-assign the variable name of an existing tuple to a new tuple containing different information.

```{}
myTuple = (1,2,4)
myTuple[2] = 3

TypeError: 'tuple' object does not support item assignment
```


```python
myTuple = (1,2,4)
print(myTuple)
```

```
## (1, 2, 4)
```

```python
myTuple = (1,2,3)
print(myTuple)
```

```
## (1, 2, 3)
```

## Debugging

## Exercises

### Exercise 1. Shopping list

```python
shoppinglist = ["bread","cheese","jam","milk","oatmeal","blueberries","oranges","apples"]
shoppinglist[0] = "buns"
shoppinglist = shoppinglist + ["chocolate"]
del shoppinglist[2]
shoppinglist_mum = ["eggs","yoghurt","potatoes","salmon"]
shoppinglist += shoppinglist_mum
del shoppinglist[10]
ingredients_muffins = ["icing sugar","whipping cream","lemons","flower","vanilla sugar","eggs","mandarines","baking powder","sugar","margarine"]
shoppinglist.append(ingredients_muffins)
del shoppinglist[11][6]
shoppinglist[8:11] = [shoppinglist[8:11]]
del ingredients_muffins[7]
```

The above shopping list has been subject to several changes since it has been written. Standing in the supermarket, you want to know the contents of the final shopping list. Which groceries do you have to buy?

You can check your answer afterwards by running the code.

### Exercise 2. Dictionnaries


```python
famous_psychologists = {"Freud":("Sigmund", "Freud", (1856,1939), "Psychoanalysis"),
                        "Piaget":("Jean", "Piaget", (1896,1980), "Theory of Cognitive Development"),
                        "Skinner":(("Burrhus", "Frederic"), "Skinner", (1904,1990), "Operant Conditioning"),
                        }
                      
erikson = ("Erik", "Erikson", (1902,1994), "Theory of Psychological Development")
famous_psychologists["Erikson"] = erikson
more_on_Skinner = {"Schedules of Reinforcement":("positive reinforcement", "negative reinforcement", "extinction"),
                   "Skinner Box":("pigeon","lever","food"),
                  }
famous_psychologists["Skinner"] = famous_psychologists["Skinner"][:3] + ("Behaviorism",) +         (famous_psychologists["Skinner"][3],) + (more_on_Skinner,)
```

Using the given dictionnary on famous psychologists and the above changes made to the dictionnary:

* Try to understand the changes made to the original dictionnary by writing down the content of the following print statements


```python
print(famous_psychologists["Erikson"][:3])
print(famous_psychologists["Piaget"][3:])
print(famous_psychologists["Freud"][2][0])
print(famous_psychologists["Skinner"][0][1])
print(famous_psychologists["Skinner"][5].keys()[1])
word = famous_psychologists["Skinner"][5].keys()[0]
print(famous_psychologists["Skinner"][5][word][0])
```

* Afterwards, you may check your answers by running the code. Pay attention that your own answers match exactly.

### Exercise 3. Element selection

For the following data structures, give the code by which you can access the specified element.


```python
dinner = ["minced beef", "tomatoes", "pasta", "onions", "pasta sauce", "courgette"]
shoppingList = [dinner, "bread", "milk", "cornflakes", "cheese"]
```


```python
grades = {"p1": ("Judith",21,"female","B-PSY",(5.6,7.7,7.3)),
          "p2": ("Menno",19,"male","B-CREATE",(8.6,6.9,7.4)),
          "p3": ("Jan",19,"male","B-CREATE",(3.9,4.5,8.9)),
          "p4": ("Eva",20,"female","B-MATH",(8.0,7.0,9.1)),
          "p5": ("Sophia",22,"female","M-PSY",(4.9,6.7,7.6)),
          "p6": ("Jeroen",25,"male","M-BME",(8.5,8.5,8.5)),
          "p7": ("Max",18,"male","B-IBA",(7.9,2.0,6.5))
         }
```


1. `milk` in `shoppingList`
2. `minced beef` in `shoppingList`
3. The study of `Jan` in `grades`
4. The age of `Sophia` in `grades`
5. The name of participant 6 in `grades`
6. Judith's grade on the third partial exam in `grades`
7. The grade of participant 5 on the first partial exam in `grades`
8. The maximum grade achieved on the second partial exam


### Exercise 4. Adjust a dictionnary data set

The data set below originates from a (fictive) language course given at the University of Twente. During the course, the following information was stored about the participants: age, gender, nationality, study programme, for each lesson, whether the participant was present or not (`True` indicates presence during the lesson and `False` absence), and the paricipant's score on the final exam.


```python
dataset = {'p1':[21,"Female","Dutch","B-Psychology",[True,False,True,False,False],5.2],
           'p2':[20,"Female","Dutch","B-Psychology",[True,True,True,False,True],8.4],
           'p3':[21,"Female","Dutch","B-Applied_Mathematics",[False,True,True,False,True],7.8],
           'p4':[23,"Male", "German","B-Communication_Science",[True,True,"n/a","n/a",True],8.8],
           'p5':["n/a","n/a","Dutch","M-Business_Administration",[False,False,True,True,True],7.6],
           'p6':[19,"Male","Swedish","B-Computer_Science",[True,False,False,True,False],7.5],
           'p7':[19,"Male","German","B-Communication_Science",[True,True,False,True,True],5.4]
           }
```
The lecturer has to perform some last minute changes to the data set before handing it in for statistical examination. Perform the following changes to the data set by accessing the relevant elements.

1. After taking a resit, participant 1 and participant 7 did pass the course. Participant 1 scored a 6.1 on the resit and participant 7 a 7.4.
2. Participant 5 forgot to put her age and gender on the registration form. Participant 5 is female and 23 years old.
3. The docent forgot to sign the presence of participant 4 during two lessons. Participant 4 was present during all lessons.
4. During the course, participant 2 changed her study programme from B-Psychology to B-Health Sciences.
5. After the final examination, it was revealed that participant 4 cheated during the exam. The examination board decided to void the student's achievements on the exam. In such a case, the additional note `expelled` is added to the student's record, indicating the student's misbehaviour.

### Exercise 5. A dictionnary data set

Fill in the participant information given in the table below in a Python dictionnary with the following structure:


```python
participants = {participant_no:(gender, age, nationality, profession)}
```

Participant No.|Gender|Age|Nationality|Profession
-|-|-----|-------|------|----------
1|Male|19|Dutch|Student
2|Male|47|Dutch|Pharmacist
3|Male|31|Italian|PhD Student
4|Female|22|German|Student
5|Female|46|Dutch|Florist
6|Male|27|Dutch|Student
7|Female|22|Dutch|Police trainee
8|Female|26|Indian|Architect
9|Male|18|American|Student
10|Male|20|Chinese|Student

Using Python and by accessing the relevant elements in the dataset

1. Calculate the *average age* of the participants
2. Calculate the *standard deviation* of the age variable
3. Calculate the *maximum* and *minimum* of the age variable

*Hint*: Libraries provide built-in methods beyond the repertoire of the standard Python language. For instance, `NumPy` provides all kinds of methods for statistical operations in Python. You can import a library by typing `import (library name)` and make use of library-specific methods like this `(library name).(method)`. Take a look at the documentation of the `NumPy` library.

### Exercise 6. Stroop extension

In this exercise you will implement a conditional execution of the interactive Stroop program. Imagine that you want to examine whether the number of colors influences the reaction time of participants in the Stroop experiment. In particular, you have gathered ten participants whom you randomly assigned to either a three or a five word version of the Stroop task. The table below summarizes which participant is assigned to which condition.

Participant No.|Condition
-|-|
1|Stroop 3
2|Stroop 3
3|Stroop 5
4|Stroop 3
5|Stroop 5
6|Stroop 5
7|Stroop 5
8|Stroop 3
9|Stroop 5
10|Stroop 3

For this exercise, a modified version of the Stroop task is given. In `ch4ex6Stroop.py`, a rudimentary implementation of user console input is provided. In two additional `STATES`, the user enters his participant number and the entered number is stored for the rest of the program run. The modified script has a function `pickColor5()`, which implements the random selection of words and colors for the five-color version.

In order to implement the comparative Stroop version program (three vs. five colors) program, consider the following steps:

* Open `ch4ex6Stroop.py` and scan the changes to the original code. Try to understand the changes performed to the code.
* Incorporate the information contained in the table above on the condition assignment of the ten participants. Which data structure will you use for storing this information?
* Prepare the code for both Stroop task versions, a version with three words, three colors, and three buttons and the same for the five-word version. Choose any two additional colors.
* Think about which places in the program need to be adapted and which of them need adaptation depending on the condition.

## Think further

* For more detailed information on *lists* beyond the scope of this chapter, you are advised to take a look at [Wentworth, P., Elkner, J., Downey, A. B., & Meyer, C. (2015). How to think like a computer scientist: Learning with Python 3. Chapter 11. Lists](http://openbookproject.net/thinkcs/python/english3e/lists.html)
* For more information on *dictionnaries*, including explanation on useful built-in functions of the dictionnary class, you are invited to take a look at [Wentworth, P., Elkner, J., Downey, A. B., & Meyer, C. (2015). How to think like a computer scientist: Learning with Python 3. Chapter 20. Dictionnaries](http://openbookproject.net/thinkcs/python/english3e/dictionaries.html)
* More information on *tuples* can be found in [Wentworth, P., Elkner, J., Downey, A. B., & Meyer, C. (2015). How to think like a computer scientist: Learning with Python 3. Chapter 9. Tuples](http://openbookproject.net/thinkcs/python/english3e/tuples.html)

