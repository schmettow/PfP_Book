# Variables, values and types {#variables}

In chapter 1 Introduction, you took a closer look at the Stroop Task program. While doing so, you encountered components of a computer program called *variables*


```python
col_white = (250, 250, 250)
col_black = (0, 0, 0)
col_gray = (220, 220, 220)
col_red = (250, 0, 0)
col_green = (0, 200, 0)
col_blue = (0, 0, 250)
COLORS   = {"red": col_red,
            "green": col_green,
            "blue": col_blue}
WORDS    = ("red", "green", "blue")
```
You learned that the variable `COLORS` for example collects number combinations for red, green, and blue color in one compound variable, called a *dictionary*.

However, before we can talk about what compound variables such as dictionaries are, you will meet 
the most fundamental component of a computer program: *values*.



```python
print(2 + 2)
```

```
## 4
```

```python
print(20 / 4)
```

```
## 5
```


```python
print("Hello, World!")
```

```
## Hello, World!
```

In the examples above, the *printed* outputs `4`, `5.0` and `Hello, World!` are *values*. Values can thus be numbers, but also words, or even whole sentences. In the interior of a computer program, `4` and `Hello, World` serve the same purpose, they are both building blocks. Values are classified into different *classes*, or *data types*: `4` is a so-called *integer* and `"Hello, World"` is a
*string*, so-called because it is a string of individual letters. The class of a value determines which operations can be performed on a value and how these operations are performed. You can think of operations such as arithmetic addition and subtraction, but also self-defined operations, called *functions*. You will learn about functions later in this book.

If you ever wonder what class a value belongs to, your Python interpreter
can tell you. 


```python
print(type(4))
```

```
## <type 'int'>
```


```python
print(type("Hello, World!"))
```

```
## <type 'str'>
```

You will learn more about basic data types in Section 2.4 [Data types].

You will find the `print` function very useful; it makes some output visible by *printing* to the console of your programming environment whatever is written inside the two brackets `()`. Printing is a way to make values such as the result of the simple calculation `2 + 2` visible. In the example above, if the `print` function were not included, your computer would perform the calculation `2 + 2` internally, but you would not see the result, `4`. Do not blame your computer, as we saw in chapter 1, computers are incredibly dumb. How is your computer supposed to know that in addition to making the calculation, it is also supposed to show you its result on the screen? Computers are unfortunately not gifted with common sense - you need to tell them precisely what to do.

## Variables
Computer programs are usually required to store information in some way for later retrieval or manipulation. In the Stroop Task program we saw in chapter 1, for each trial, we need to store the color and the word that our computer picked and what the reaction time of the subject was. Otherwise, it will be impossible to establish a relation between reaction times and (in)congruence between words and their colors in any subsequent statistical analysis. In other words, the Stroop task program would be useless if it could only manipulate values as we did when we calculated `2 + 2`. You see, when your computer performs a simple value manipulation you get a momentarily answer. Computers are too efficient for their own good sometimes, they quickly forget about the values that pass through their system. The very moment they finish a calculation, the computer program forgets the outcome of this calculation and even that they ever performed the calculation (if you do not remind them that they did). This is where *variables* come in handy. Variables are storage units
in a computer's memory. A variable can store any kind of value. Unlike the result of simple value manipulations, such as `2 + 2`, variables have designated storage addresses in a computer's memory. You need a way to access variables in your computer's memory
and hence, you give them a name. You can think of a variable's name
as a unique identification address in the computer's memory. In fact, during a *value assignment*, a value is stored at a certain position in the computer's memory. You can think of this position as a precisely defined location, much like longitude and latitude coordinates describe a physical location in the Global Positioning System (GPS). The command by which a value is stored in a variable
is called an *assignment statement*. It is common to say "a
value is assigned to a variable".


```python
myNumber = 4
myString = "This is a string"
print(myNumber)
```

```
## 4
```

```python
print(myString)
```

```
## This is a string
```


The order in which the variable and a value are placed
around the equal sign `=` is not arbitrary. Variables always have to be
on the left side, values on the right side. Everything else will
produce an error. As mentioned above, variables can store any kind of value. The right side can be a complex expression, which is not obviously a value at first sight. The single equal sign, as in `a = 4` is exclusivey reserved for assignment statements. If you read a program out loud, practice saying 

> a is assigned the value 4

A double equal expression, as in `a == 4` is used for comparing two values, as in "Does the value of 'a' equal 4?" That is completely different to an assignment and will be covered in Section 2.3 [Data types] and in more detail, in Chapter \@ref(conditionals).


Programmers have much freedom in naming variables, but some strict rules exist, as well as some conventions. Some of them are good practice
and others will throw syntax errors if not adhered to. In the beginning, you may think
of good practice guidelines as superfluous, but you
will learn to value them once you start making more complex programs.

Heeding them pays off!

1. Programmers give meaningful names to variables in order to make their
code more readable for others and themselves. Without meaningful names,
they easily get lost when reading through their code again. Even to them their own code
may appear as nothing more than gargle-bargle.

2. The first character of a variable must be a letter of the alphabet,
either uppercase or lowercase ASCII or Unicode, or an underscore.

3. The rest of a variable name may consist of letters (uppercase or lowercase
ASCII or Unicode characters), underscores, or digits (0-9).

4. Variable names are case-sensitive. This means that the variables `myString`
and `mystring` are not treated as the same variable by your
computer.

5. You may still get sytnax errors despite adhering to all rules named
above. Chances are high that you tried to use one of Python's *keywords*
as a variable name. Python uses a number of keywords to recognize
the structure of a program.`if` and `for` are keywords for example. Your Python interpreter 
can tell you the complete list of keywords known
to your Python version:


```python
import keyword
print(keyword.kwlist)
```

```
## ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
```


## Stroop task variables

Now that you read about how variables are assigned their values, let's have a look at how variables are used in the interactive Stroop program.


```python
# a list for gathering the response times
RT = []
# remember when stimulus was presented
time_when_presented = time()
# remember when the user has reacted
time_when_reacted = time()
# calculate the response time
this_reaction_time = time_when_reacted - time_when_presented
RT.append(this_reaction_time)
```

In the first line of the above code snippets from the Stroop task program, an empty *list* is assigned to the variable `RT`. The purpose of this list is to store reaction times during the Stroop experiment. You will learn more about *lists* in Chapter \@ref(lists). For now it suffices to know that lists are yet another data type, capable of containing values of multiple data types at the same time! You may reckon that they are the ultimate structure for storage. The variables `time_when_presented` and `time_when_reacted` respectively store the point in time (using the *function* `time`) at a certain event. `time_when_presented` records the moment in time when a stimulus is presented and `time_when_reacted` saves the moment in time when the subject reacts to the stimulus. The reaction time of the subject is then calculated by *subtracting* one stored point in time from the other and saved in the variable `this_reaction_time`. Finally, the subject's reaction time is *appended* to `RT`, meaning that `this_reaction_time` is saved in `RT` before the program proceeds to the next trial. Thecode snippets above obviously reduces the mechanics of the Stroop Task program to some highlighted variable assignments, meaning that the code lacks the actual dynamics of the program. But it captures the basic idea of how the program records and manipulates a participant's reaction time with the help of variables.

## How Variables Are Used

More formally, variables are an essential component of any program.
As such, their applications are numerous. This section provides but
a glimpse into the vast and creative application possiblities of variables.
Do not worry, you will soon get a hang of it once you start doing
some programming yourself. One common way of using variables
is storing the output of *functions*:


```python
import random
number = random.randint(0,10)
print(number)
```

```
## 10
```

You will learn in detail about functions in Chapter \@ref(functions). For now it
is good enough to know that the function `random.randint(0,10)` randomly
picks an integer between 0 and 10, and *returns* the chosen
integer. Whatever number is picked by the function is stored in the
variable `number` and can easily be retrieved and used for other
purposes elsewhere. If this piece of information does not satisfy
you, simply type `help(random)` after importing `random`
and your interpreter will give you a more detailed description of
the *class* `random`.

Variables are mutable, meaning that their value can be changed after
an initial assignment. This is very useful for structuring a program:


```python
# determining the maximum number of trials
nTrials = 3
# setting a counting variable to 0
# at the beginning of the program
n = 0
# adding 1 to n as long as n does not exceed nTrials
while(n < nTrials):
    # do something
    n = n + 1
```


This
comes in handy if you want to repeat a part of your program until
a certain condition is fulfilled. For instance, imagine taking measurements
for a fixed number of trials for a psychological experiment.
In the example above, `nTrials` and `n` are used for creating
a counting mechanism until the desired number of repeated measurements
is reached. Note how the old value of `n` is used to mutate
the value of `n` after one execution cycle of the program in `n = n + 1`. In particular, after the first execution of the `while` part of the code snippet,`n` will have the value `1` instead of `0`!
If you are not yet fully getting the hang of it, do not worry. You
will learn more about the use of *conditionals* and the *while loop*
in Chapter \@ref(conditionals) and Chapter \@ref(loops), respectively. The basic idea behind the above code snippet is to show you how the mutability of variables can be used to create a counting mechanism in computer programs.

## Data types

Earlier in this chapter, you learned that
each value belongs to a certain *class* or *data type*.
This section will introduce the *basic data types*: *integers*,
*floats*, *strings*, and *booleans*. Apart from the basic data types, Python knows numerous
specialized types. Earlier in this chapter, you already encountered two such specialized data types: *dictionaries* and *lists*. Literally any computer program contains values of at least the basic types and thus, it seems to be reasonable to say a word or two about them. 

### Numbers

There are two main types of numbers in Python, *integers*
and *floating point numbers*, or *floats* for short.
Integers are whole numbers, such as `6` and `1234`, while
floats are numbers including a decimal point, such as `2.4`
and `45.768`. But wait, what happens if we add a float to a
variable of type integer? Let's try!


```python
number = 7
print(type(number))
```

```
## <type 'int'>
```

```python
number = number + 3.5
print(type(number))
```

```
## <type 'float'>
```


The variable changed from type *int* to *float*! This
is an example of implicit *typecasting*. Typecasting means
changing the type of a variable, and it can be done explicitly and
implicitly. At times you will want to change the type of a variable
to suit your needs. For this, you use explicit typecasting: 


```python
number = 10.5
int(number)
10
```

And here you discover one tricky thing about typecasting *floats*
to *integers*. Python does not round off the value of floats
when typecasting them into integers, it simply cuts off whatever there
is after the decimal point. This can become especially tricky when
typecasting implicitly and should be monitored with caution.

### Strings

If numbers are *integers* or *floats*, what about
values such as `"17"` and `"13.65"`? They look like numbers,
but they are wrapped in quotation marks like *strings*. 


```python
print(type("17"))
print(type("13.65"))
```

They are strings! In Python, strings can be enclosed in either single
quotes (`'`), or double quotes (`"`), or three of each
(`'''` or `"""`). But what if your string includes a quote and you want to indicate this by using quotation marks *within* your string? Using the same quotation marks as used for defining the string will prematurely end the string.

```{}
quote = "Freud: "The mind is like an iceberg, it floats with one-seventh of its bulk above water.""

SyntaxError: invalid syntax
```

Instead, when using single quotes, you can use double quotes or triple quotes inside them:


```python
quote = 'Carl Rogers: "In my early professional years I was asking the question: How can I treat, or cure, or change this person? Now I would phrase the question in this way: How can I provide a relationship which this person may use for his own personal growth?"'
```

Double quoted strings can have single quotes and triple quotes inside
them: 


```python
quote = "Ivan Pavlov's best known findings relate to the phenomenon of conditioning."
```

Triple quoted strings can include either single or double quotes.
Strings are basically a sequence of single characters tied together
and unlike variable names, strings may include spaces! They are usually
used to display text or to export information out of the
program. The latter you probably want after a participant has completed all trials of an experiement to save the recorded measurements.

### Booleans
A *boolean expression* is an expression that is either `True` or `False`.

```python
print(5 == (3+2))
```

```
## True
```

```python
print(5 == 6)
```

```
## False
```


```python
j = "hel"
print("hello" == j + "lo")
```

```
## True
```

`True` and `False` are special values of type boolean; they are no strings! 


```python
print(type(True))
```

```
## <type 'bool'>
```


```python
print(type(False))
```

```
## <type 'bool'>
```

A *boolean expression* consists of two operands, located left and right of a *relational* or *comparative* operator. There are six comparison operators in Python:

+ `x == y # x equals y`
+ `x != y # x is not equal to y`
+ `x > y  # x is greater than y`
+ `x < y  # x is smaller than y`
+ `x >= y # x is greater or equal to y`
+ `x <= y # x is smaller or equal to y`

These operators are probably familiar to you, but their usage in Python differs from the mathematical symbols you know from highschool. One very common confusion surrounds the `equals` (`==`) operator. Remember that `=` is reserved as assignment operator and `==` is used for comparisons. There is no such thing as `=>` or `=<`.  
Apart from that, boolean values can be handled exactly as any other value, that is, they can be assigned to variables, printed and so on.


```python
number_of_EC_required_for_BSA = 45
passed_BSA = number_of_EC_required_for_BSA <= 50
print(passed_BSA)
```

```
## True
```

## Common errors

1. Confusing the *assignment operator* (`=`) with the comparative *equals* operator (`==`). The first is solely used for assigning values to variables as in 


```python
myString = "This is an assignment statement"
```

the latter for comparing two values


```python
17+3 == 21
```

Usually, when you confuse the assignment operator with the equals operator, you will get a syntax error.

```{}
17+3 = 21

SyntaxError: can't assign to operator
```

2. Forgetting to typecast other data types when incorporating them into strings

```{}
myGrade = 8
print("I got an " + myGrade + " on the last exam!")

TypeError: cannot concatenate 'str' and 'int' objects

```

Often, you will want to export some arithmetic result (such as a participant's reaction time in the Stroop Task program) or other non-string data out of the program, or you simply want to print them to the screen. This is usually done by first converting the data into type string and then writing to some external file (such as good old plain text files) or using the *print command* to write to the console. Quite often people forget that *explicit typecasting* is required when incorporating non-string values into a sequence of strings.


```python
myGrade = 8
print("I got an " + str(myGrade) + " on the last exam!")
```

```
## I got an 8 on the last exam!
```

3. Unintentionally cutting off decimals when typecasting to *integers*.


```python
import numpy
RT = [3.749,2.998,3.0147]
mean_RT = numpy.mean(RT)
print("The subject had a mean reaction time of " + str(int(mean_RT)) + " seconds.")
```

```
## The subject had a mean reaction time of 3 seconds.
```
Obviously, a mean reaction time of exactly `3` is unrealistic with `3.749`, `2.998`, and `3.0147` as individual trial reaction times. You may feel inclined to typecast anyway to shorten the numerical string expression, but remember that typecasting from *float* to *integer* results in the loss of any information after the decimal point. Besides, usually there are better ways for rounding off floating points; consider the `round` method for instance.


```python
import numpy
RT = [3.749,2.998,3.0147]
mean_RT = numpy.mean(RT)
print("The subject had a mean reaction time of " + str(round(mean_RT, 3)) + " seconds.")
```

```
## The subject had a mean reaction time of 3.254 seconds.
```

4. Forgetting to reassign the mutated value of a variable

```python
count = 1
count + 1
print(count)
```

```
## 1
```
Remember to assign the new value of a mutated variable to either a new variable or the original variable name; your computer will otherwise ignore the variable mutation and keep the variable's old value in memory.


```python
count = 1
count = count + 1
print(count)
```

```
## 2
```

## Debugging

Despite all efforts and skill, programmers encounter programming errors on a daily (if not hourly) basis. In this, programming beginners and experts are no different. In fact, debugging is a very challenging and instructive task in itself.

Apart from some general good debugging practices introduced in chapter 9 [Debugging], there are some tricks that are especially useful in tracing errors that originate from the variables in your program.

1. Checking all of your equals `==` and assignment `=` operators is a good start when tracking down bugs suspected to originate from variables. For this you can either scan your code from top to bottom manually or use the search function of your programming environment. Use `Cltr` + `F` to search for an expression in your code (in this case either `=` or `==`, or the name of the variable you expect to be the culprit). Then, for each instance of the equals `==` or `=` assignment operator, or the variable itself, ask yourself whether you used the right operator for the intended job. Confusing the equals and assignment operator usually results in a syntax error, but a syntax error does not necessarily need to originate from confusing operators. In fact, syntax errors are undoubtly the most generic errors in programming.

2. Once you are positive that the bug is not caused by confusing the equals with the assignment operator, you should take a closer look at the operations you perform on your variables (such as comparing variables or performing arithmetic calculations). Operations are another potential source of bugs.


```python
a = 1
b = "1"
print(a + b)
```

In the example above, it is evident what goes wrong. `Strings` and `integers` cannot be added as two numbers are summed. A `type error` is thrown. However, in more complex programs it is often less evident where the bug originates from. Therefore, it is useful to check the data type of your variables at multiple locations in your program. Who knows, you may have unknowingly converted a variable to another type somewhere in your code and at a later moment, this causes your program to throw an error. Use the functions `type()` and `print()` to display the data type of your variables at different places in your code and hit `run`!


```python
a = 1
b = "1"
print(type(a))
```

```
## <type 'int'>
```

```python
print(type(b))
```

```
## <type 'str'>
```
3. Performing operations on variables may still have unexpected results, even when no type errors are involved. Arithmetic (`+`, `-`, `*`, `/`) and *Boolean* operators follow rules of precedence. Arithmetic operators follow the same rules of precedence as you learned about in highschool mathematics. All arithmetic operators also precede any Boolean operator, meaning that in the code snippet below `1 + 1` is evaluated before being compared to `2`.


```python
print(1 + 1 == 2)
```

```
## True
```

As a debugging strategy, it is useful to change the precedence of operators with the help of brackets `()`. The bug may originate in a false assumption about operator precedences. Using brackets, you can make sure that operations are executed in the exact order you intended.

4. When you neither confused the equals with the assignment operator, nor made a type error, nor had false assumptions about operator precedences, the last resort is to mentally follow the flow of your program and to check whether your variables are assigned the expected value at all times. For instance, in the code snippet below, you may expect the result to be `1` since you added `2` to the initial value of `a` and `2 / 2` is `1`.


```python
a = 0
b = 2
a + 2
print(a / b)
```

```
## 0
```

However, `a` was never assigned the new value of `2` and `0 / 2` is obviously `0`. It is easy to overlook such a mistake when scanning through your code. Therefore, checking which values are assigned to your variables as you read through your program is very helpful. You could for instance adjust the code above if you are puzzled why the result is not `2`, like so


```python
a = 0
b = 2
a + 2
print(a, b, a / b)
```

```
## (0, 2, 0)
```

which prints first the value of `a`, then `b` and then the result of `a / b` to the console.

## Exercises

### Exercise A. Operators

What is the output of the following code snippets?


```python
x = 2
y = 1.0
print(x + y)
```


```python
x = 4.0
y = x + 1
print(x + y)
```


```python
x = 1
y = "1.0"
print(x + y)
```

```python
x = 4
y = 4.0
print(x == y)
```

```python
x = 12
y = x / 2
print(y >= 5)
```

### Exercise B. Values

Which statements about values are true?

* Values are storage units in a computer's memory and thus, they are persistent throughout a computer program
* Each value exclusively belongs to one data type
* There are four basic data types that occur in virtually any computer program: strings, integers, floats and dictionaries
* Variables can be assigned any type of value
* Any operation (e.g. subtraction) can be performed on any two pairs of values  

### Exercise C. Mini programs

What is the output of the following mini programs?


```python
x = "1.0"
y = "1"
print(x + y)
```


```python
x = 5
y = 2
print((x / y) == 2.5)
```


```python
x = 1
x = x + 1
x = x - 2
print(x)
```

### Exercise D. Debugging

What goes wrong in the following code snippets?

```{}
x = 1
2x = 2
print(x + 2x)
```

* The letter `x` may not repeat in multiple assignment statements
* Variable declarations must be ordered in descending order, so the value `2` should be assigned before `1`
* An illegal variable name is used

```{}
x = 3
y = "3"
print(x = y)
```

* A wrong arithmetic equation is printed, `3` does not equal `"3"`
* Strings and integers are not comparable using boolean operators
* The assignment operator is used instead of a comparative operator

```{}
name = "Colin"
print(This is + name)

```

* Variables cannot be called in `print` statements
* The `name` variable needs to be typecasted into a String
* The content of the `print` statement lacks quotation marks

### Exercise 1. String concatenation

Consider the three blocks of code below.

1. What is the output of the respective *print statement* at the end of each block?
2. Describe in your own words what *string concatenation* is.
3. There is an error hidden in the code. Explain what is going wrong and adjust the code so that it runs without throwing any errors.


```python
myString = "The statement 'Veni, vidi, vici.'"
s1 = " was coined by Gaius Julius Caesar."
myString = myString + s1
print(myString)
myString = "The statement 'Veni, vidi, vici.'"
s1 = " was coined by Gaius Julius Caesar."
s2 = ", 'I came, I saw, I conquered.',"
myString = myString + s2 + s1
print(myString)
myString = "The statement 'Veni, vidi, vici.'"
s1 = " was coined by Gaius Julius Caesar,"
s2 = " supposedly around "
year = 47
s3 = " BC."
myString = myString + s1 + s2 + year + s3
print(myString)
```

Want to know more about *string concatenation*? The following website
provides a gentle introduction to the topic: [Python for Beginners: String concatenation and formatting in Python](http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python)

### Exercise 2. Variable names

For the following variable names indicate whether the name is legal
or not. For illegal variable names, point out what makes the name violate rules and/or conventions.
```{}
Reg       = "What have the Romans ever given us?"
man1      = "The aqueduct?"
2ndMan    = "The sanitation"
m@n3      = "And the roads"
man_4     = "Irrigation"
man 5     = "Medicine"
SixthMan  = "Education"
man_no._7 = "And the wine!"
8thMan    = "Public votes"
no9atReg  = "Public order; it's finally safe to walk in the streets at night."
reg       = """All right. But apart from sanitation,
            medicine, education, wine, public order,
            irrigation, roads, a fresh water system,
            and public health;
            what have the Romans ever done for us?"""
```


### Exercise 3. Stroop task welcome message

In this exercise you will add a welcome message to the starting screen
of the Stroop Task program.

1. Open the file `stroop_modifiedCh1Ex3.py`. Run it.
2. Make two new variables, `msgColor` and `msgText`. Choose any color and welcome message you want.
3. Read and try to understand the code written in lines 134-137. Try to formulate in your own words what each line of the code does.
4. Uncomment lines 134-137. *Hint*: In Python, a commented line starts with a `#`. Commented lines will not be executed.
5. Hit `Run file` again and see your first modification of the Stroop task algorithm in action.


### Exercise 4. Printing

The following code prints part of a Methods section. Copy it and run it.


```python
participants = 52.0
trials = "200"
experimental_sessions = 3
trials_pp = trials * experimental_sessions
conditions = 4
"""
to be implemented by you
condition1 = 
condition2 = 
condition3 = 
condition4 =
"""
print("In total,", participants, "participants participated in the study.")
print("A 2x2 factorial between-subjects design was employed.")
print("The study examined the interaction of two independent variables: ")
print("task difficulty (easy, difficult) and time (limited, unlimited).")
print(conditions, "conditions were devised, plus a control condition.")
print("The conditions were:",condition1,condition2,condition3,condition4)
print("Participants were tested in", experimental_sessions, "experimental sessions.")
print("Each session consisted of",trials,"trials.")
print("In total, each partcipant thus completed", trials_pp, "trials.")
```

1. The first time you run the script, you get an error. Initialize the variables `condition1, condition2, condition3, condition4` to solve the error. Fill in semantically and syntactically correct values for the four condition variables. For example, in the context of the given Method excerpt, it would not make sense to say that one of the four conditions was `easy-locationA-limited`, right?
2. Once you have filled in the blank variable declarations, you get a a curious output for the number of trials per person. Adjust
the code so that the correct number of trails per person is printed. Explain what happened in your own words.
3. `52.0` participants looks a bit ugly when printed as part of the text. Adjust the code in such a way that only full integers are printed to the console.

### Exercise 5. Using Python as a calculator

Make a python script `Ch1Ex5.py` and implement the following pseudo code:

* assign the value 37 to the variable `n1`
* assign the value 456 to `n2`
* calculate 1027 modulo n1 and assign the result to `n3`
* divide `n2` by `n3`
* add 4 to `n2`
* calculate `n2` modulo 5 and assign the result to `n4`
* subtract 17 from `n4`
* calculate 65 modulo `n4` and divide the result by 2

What is the resulting value of `n4`?

### Exercise 6. A Boolean puzzle

Fill in the blank spots (indicated by a question mark `?`) in the following code in such a way that `True` Boolean values are returned. You can use your Python interpreter for calculations.
```{}
n1 = 238
n2 = 17

print(n1 ? n2)
print(n1 / ? == 14)
print(n1 * ? == n2)
print(n1 + ? == n2 - ? and n1 + ? == 972%243 and n2 - ? == 0)
print(n2 * ? == n1*47)
print(n1 / ? == n2 / ? * ?)
```

## Think Further

For more information and exercise on Variables and Data Types you
may want to consult some of the following resources:


* [Downey, A. (2012). Think Python. O'Reilly Media, Inc.. Chapter 2. Variables,
expressions and statements](http://www.greenteapress.com/thinkpython/thinkpython.pdf)
* [Official Python Tutorial, parts 3.1.1 Numbers and 3.1.2 Strings](https://docs.python.org/2/tutorial/introduction.html)
* [Learnpython ``Variables and Types'' interactive tutorial](http://www.learnpython.org/en/Variables_and_Types)
* [Swaroop, C. H. (2003). A Byte of Python. Chapter 6 ``Basics''](https://python.swaroopch.com/basics.html)