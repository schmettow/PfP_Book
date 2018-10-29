# Loops {#loops}


```python
for i in range(2):
    print "Hello, World!"
```

```
## Hello, World!
## Hello, World!
```

Computers are good at executing repetitive tasks without making errors, unlike people. The repeated execution of a set of statements is called *iteration*. Because making computers do boring, repetitive tasks is so common in programming, Python has a number of language features that make iteration easier.

## The `for` loop


```python
for letter in "Hello!":
    print letter
```

```
## H
## e
## l
## l
## o
## !
```

```python
print "The for loop is over"
```

```
## The for loop is over
```

The `for` loop statement *iterates* over a sequence of objects. This means that it goes through all items of a sequence. The statement begins with the `for` keyword, followed by a *loop variable* (`letter` in the example above), which can really be any valid variable name. Then the `in` keyword follows and after that, a *sequence* (such as a `list` or a `string`) or a *range object* (returned by `range()`) follows. Finally a `:` demarcates the end of the statement. On each iteration of the loop, the loop variable takes on the value of the next item in the sequence. The *loop body* specifies the statements that are to be executed during each iteration. The borders of the loop body are demarcated by *indentation*. Once the value of the last item in the sequence has been assigned to the loop variable and the body of the loop has been executed, the loop terminates and program execution is continued on the first line after the loop body.

## The `while` loop


```python
sum = 0
value = 1
while value < 5:
    sum += value
    value += value
    print "current sum is:", sum, "current value is:", value
```

```
## current sum is: 1 current value is: 2
## current sum is: 3 current value is: 4
## current sum is: 7 current value is: 8
```

```python
print "The loop is over, the sum is:", sum
    
```

```
## The loop is over, the sum is: 7
```

A `while` loop allows you to repeatedly execute a number of statements as long as the condition in the `while` statement remains `True`. Note that the body of a while loop is never executed if the loop condition is `False` at its first execution.

The body of a `while` loop should change one or more (loop) variables so that the loop condition eventually becomes `False`. Otherwise, the loop will continue forever and we speak of an *infinte loop*. If unintended, infinite loops can manoeuver your program into a dead end.

At times it may be confusing whether either a `for` or a `while` loop will suit your needs best, ask yourself the following questions:

* Do I know in advance how many times I need the loop body to be executed? Any problems like "search a list of words" or "execute until the desired number of trials is reached" suggest that a `for` loop will suit your needs best.
* Do I require the computations to stop when some condition is met, but I cannot calculate in advance when (of if) this will happen? Chances are high that a `while` loop will fit your needs best in this case.

## The `break` statement


```python
myNumber = 17
while True:
    guess = input("Enter a number:")
    if guess > 17:
        print "My number is smaller than", guess
    elif guess < 17:
        print "My number is larger than", guess
    else:
        break
print "Ding! Ding! You guessed correctly, my number is", myNumber
```

The `break` statement allows you to immediately exit any loop. The next statement that is executed is the first after the loop body. Interactive programs that process user input often require to exit their loops prematurely. Depending on the input given, the program may need to transition to the next state or terminate altogether.

## Control flow

By now you will have noticed that by default, Python faithfully executes any program in a top-down order. But what if you want to change the order in which specific parts of your program are being executed, possibly depending on external conditions such as the time of the day, or user input?

Yes, you may have guessed it already, this is achieved by using *control flow statements*. Python knows three control flow statements: : `ìf`,`for`, and `while`statements. We already encountered `if` statements in Chapter 3 [Conditionals]. Control flow statements are readily used in interactive software such as the Stroop experiment


```python
STATE = "welcome"
while True:
    # Changing states by user input
    for event in pygame.event.get():
        if STATE == "welcome":
            if event.type == KEYDOWN and event.key == K_SPACE:
                STATE = "prepare_next_trial"
                print(STATE)
        
        if event.type == QUIT:
                STATE = "quit"
```

In principle, the above code can run infinitely, unless the user triggers the `QUIT` `event.type`. Note that in the original Stroop experiment, there is another condition that prevents the program from running infinitely, namely a maximum number of trials.

Within the main `while` loop, a `for`loop manages the changing of program states as a consequence of user input. To this end, the loop variable `event` iterates over *event objects* stored in an *event queue*, which is essentially a special sequence devised by the `Pygame library`. The `pygame.event` *module* knowns a number of event types, among which the `KEYDOWN` event, referring to the event that the user presses a key on the keyboard.

In the example above, several conditions have to be fulfilled so that the program state changes to `"prepare next trial"`: The current program state has to be `"welcome"`, the event has to be a `KEYDOWN`and the key pressed has to be `SPACE`. Note that in the program above, program termination can be achieved at any time through the `"quit"` state.

## Common errors

* Trying to make a `for` loop iterate over an *integer* instead of a *sequence*. Very often, you will want your program to modify all elements of a given sequence according to a set of statements. Logically, you will need as many iterations as elements in the sequence. This often leads to `for`statement definitions such as:

```python
myList = [1,2,3,4,5]
for i in len(myList):
    myList[i] += 1
```

    TypeError: 'int' object is not iterable

Probably, your intention was to make the loop repeat as many times as there are elements in `myList`. However, `len(myList)` returns an *integer*, not a *sequence* object. Instead, you will have to convert the *length* of `myList` into a *sequence*, for instance by using `range()`.


```python
myList = [1,2,3,4,5]
for i in range(len(myList)):
    myList[i] += 1
  
print myList
```

```
## [2, 3, 4, 5, 6]
```

* `index out of range` errors tend to slip in when working with loops


```python
myList = [range(10),[1,2,3]]
for i in range(len(myList[0])):
     myList[0][i] = 0
     myList[1][i] = 0
```

 
    IndexError: list assignment index out of range

Always make sure that sequences you intend to modify in a `for` loop body actually have as many elements as the sequence over which you are iterating in the `for` statement.

## Exercises

### Exercise 1. Following the control flow

Read the script below carefully. Indicate the values of the following expressions after the script has finished executing:


```python
dataset.keys()
dataset[dataset.keys()[0]]
condA[0]
condA[0][0]
len(condA)
len(condB)
meanA
meanB
```

You can check your answers afterwards by running the script.



```python
import numpy as np
dataset = {'p1':(21,"Female","Dutch","B-Psychology"),
           'p2':(20,"Female","Dutch","B-Psychology"),
           'p3':(21,"Female","Dutch","B-Applied_Mathematics"),
           'p4':(23,"Male", "German","B-Communication_Science"),
           'p5':(20,"n/a","Dutch","M-Business_Administration"),
           'p6':(19,"Male","Swedish","B-Computer_Science"),
           'p7':(19,"Male","German","B-Communication_Science"),
           'p8':(24,"Female","Italian","M-Psychology"),
           'p9':(23,"Female","Italian","M-Communication_Science"),
           'p10':(18,"Male","Dutch","B-Computer_Science")
           }
condA = []
condB = []
ageA = []
ageB = []
for participant in dataset.keys():
    if dataset[participant][1] == "Female":
        condA.append(dataset[participant])
    elif dataset[participant][1] == "Male":
        condB.append(dataset[participant])
for participant in condA:
    ageA.append(participant[0])
count = 0
while count < len(condB):
    ageB.append(condB[count][0])
    count += 1
    
meanA = np.mean(ageA)
meanB = np.mean(ageB)
```


### Exercise 2. Debugging

The script below calculates some descriptives from `data`. The code is still somewhat buggy. Debug the script and indicate the values of `fastest`, `slowest`, and `all_mean`.


```python
data = {'p1':(21,"Female","Condition B",[0.675,0.777,0.778,0.62,0.869]),
        'p2':(20,"Female","Condition A",[0.599,0.674,0.698,0.569,0.7]),
        'p3':(21,"Female","Condition A",[0.655,0.645,0.633,0.788,0.866]),
        'p4':(23,"Male", "Condition A",[0.721,0.701,0.743,0.682,0.654]),
        'p5':(20,"Male","Condition B",[0.721,0.701,0.743,0.682,0.654]),
        'p6':(19,"Male","Condition B",[0.711,0.534,0.637,0.702,0.633]),
        'p7':(19,"Male","Condition B",[0.687,0.657,0.766,0.788,0.621]),
        'p8':(24,"Female","Condition A",[0.666,0.591,0.607,0.704,0.59]),
        'p9':(23,"Female","Condition B",[0.728,0.544,0.671,0.689,0.644]),
        'p10':(18,"Male","Condition A",[0.788,0.599,0.621,0.599,0.623])
        }
fastest = ("initialization",100)
for participant in data:
    RTsum = 0
    for i in len(data[participant][3]):
        RTsum += data[participant][3][i]
    RTmean = RTsum/len(data[participant][3])
    if RTmean < fastest[1]:
        fastest = (participant,RTmean)
        
slowest = ("initialization",0)
for participant in data:
    RTsum = 0
    for RT in participant[3]:
        RTsum += RT
    RTmean = RTsum/len(data[participant][3])
    if RTmean > slowest[1]:
        slowest = (participant,RTmean)
        
all_mean = 0
all_sum = 0
number_of_trials = 0
for participant in data:
    counter = 0
    while counter < len(data[participant][3]):
        all_sum += data[participant][3][counter]
all_mean = all_sum/number_of_trials*len(data)
```



### Exercise 3. Nested loops

Nested data often requires *nested loops* for answering certain questions about the data. Let's have a look at the `list` data set below. each participant has a participant number paired with a list of additional experiment information.


```python
participants = [
    ("p1", ["Condition 1","Location A","withdrew","no audio"]),
    ("p2", ["Condition 1","Location A","no audio","no video"]),
    ("p3", ["Condition 2","Location B"]),
    ("p4", ["Condition 1","Location A","withdrew"]),
    ("p5", ["Condition 2","Location A"]),
    ("p6", ["Condition 2","Location B","withdrew"]),
    ("p7", ["Condition 1","Location A","no video"]),
    ("p8", ["Condition 1","Location B"]),
    ("p9", ["Condition 2","Location B","withdrew"]),
    ("p10",["Condition 2","Location A","withdrew"])]
```

If we want to know how many participants withdrew their participation we need a counter, and for each participant we need a second loop that tests each of the experiment information in turn on the `"withdrew"` keyword:


```python
counter = 0
for (participant,expInfo) in participants:
  pass
        # to be implemented by you
        
print "The number of participants who withdrew their participation is", counter
```

Implement the second `for` loop that iterates over the experiment information and count the number of participants who withdrew their participation.

### Exercise 4. Data transformation using loops

* Write a script that transforms the data set `participants` from Exercise 3 into a dictonary data set.
* Extend the script with a `counter` mechanism that counts the number of participants who were tested at location A and location B respectively.

### Exercise 5. Calculating a mean

For the sequence `seq` calculate the arithmetic mean using a `while` loop. Check your implementation using the `mean()` method of the `NumPy` library.


```python
import numpy as np
seq = range(1000)
```


### Exercise 6. A guessing game

Make a Python script `guessing.py` that implements the following behaviour:

* At the beginning of the script, a random number between 0 and 1000 is generated.
* The program continuously asks for user input prompting the user with the request to enter a number.
* If the user guesses the number correctly, the program gives feedback that the number was guessed correctly. The program also shows the number of guesses needed. Finally, the program terminates.
* If the guessed number is too large, the program gives feedback that the number is smaller.
* If the guessed number is too small, the program gives feedback that the number is larger.
* If no input is given, the program should terminate. In this case, the program should terminate if the given input is *empty*. *Hint:* Use the internet to figure out how to handle empty input.

*Hint*: Prompting and feedback via the console is sufficient.
