# Debugging and good programming practices

## Debugging

Debugging is one of the most intellectually challenging aspects of programming. It is often also perceived as the most frustrating aspect. To a large extent, the problems that people face while debugging are not so much technical as they are psychological. Debugging starts with the realization that a computer does nothing wrong. In fact, it does exactly what you tell it to do. The fault lies thus in how the programmer conceived or implemented a solution. You should always remember that even though debugging can be a difficult and frustrating endeavour, it can be done. At times, it will require all the creativity and skill at your disposal, but you will succeed if you act systematically and do not give up on the task.

There is no recipe-like cookbook approach to debugging, but adhering to some general principles will probably help.

1. **The print statement is an aspiring programmer's best friend**. In debugging you take on the role of a detective. As such, you focus on what the errorneous program is doing, rather than why it is not doing what you wanted it to do. You work from the facts. Variables and the flow of your program are the key to finding the crucial pieces of information that will lead you to the clue to what is going wrong.

The `print` statement is a commonly used tool for debugging. Even if you have no clue as to what is going wrong, you often have a hunch where the culprit might be. If you do not have any idea where to start, simply start from the beginning of your program. It also helps to realize that the bug is not moving around in your code, trying to trick or to evade you (even though it might feel as if it has a will of its own at times). It is sitting in the same place, doing the wrong thing in the same way every time. You start from your hunch and take a closer look at your variables and whether the program is doing what it is supposed to do in this place. Here, `print` statements come in handy. You can use `print` statements to make the current values assigned to your variables visible. By following the control flow of the program in your mind (that is calculating the expected values of your variables as you go through the program), you should verify whether your variables were assigned their expected values. If yes, continue to search for the error further downward in the flow of the program. If not, look further upward for the bug. Also take a close look at the values themselves. Do they belong to the expected *data type*? Are their values in any way remarkable (too high, too low, etc.)? This will give some indication of what is going wrong.

2. **Frequent unit-testing**. Rome was not built in a day and the same is very true about computer programs. Programming, as any other task, can and should be split into subtasks. These subtasks can be chunks of code like *functions* that generalize operations you frequently need in your program, or the division between graphical and state transition dynamics of your program. Individual components should frequently and extensively be tested for bugs *before* merging them into the rest of your code. One simple bug in a small component of your program can become untracable in your main code and cause the weirdest errors. It is generally a good idea to pull out code from your main program and put it into functions to keep the main flow of your program readable and to prevent yourself from writing out the same lines of code over and over again. Just make sure that you frequently test these units of code before putting them into the main flow of your program and of course, that the main flow of your program is still working nicely. Inserting `print` statements before and after calling a function to check whether the involved variables were mutated in the intended way is one way to make sure that the different chunks of your program interact with each other nicely.

3. **The copy-paste syndrome**. Copying code is generally a bad idea. Extensive copying of code takes one of two forms. Some programmers over-copy their own code, others copy other people's code. Little is more frustrating than realizing that you are debugging the same bug multiple times. Whenever you copy undebugged chunks of code, you also copy the bugs within them. You forget which chunks of code you copied where and voilà; chances are high that you encounter the same bug in different places. Putting chunks of code that your program repeatedly uses into functions is a good way to counteract over-copying one's own code. There is no point in re-inventing the wheel, so there is nothing wrong about trying out another person's debugging approach to one's own code. However, over-copying other people's code is not only bound to cause more errors in the long run, it will also leave you with a great deal of unanswered questions about *why* another's solution fixes the bug and *why* your own attempts do not. In the worst case, you do no longer understand your own code! Copying code works against understanding code. Instead, try to program something similar, adjust small parts and see what happens. That way, you work towards understanding (another's) code.

4. **Standing on the shoulders of giants**. That being said, chances are high that, whatever you try to accomplish in programming, somebody else has already tried it (and may have run into the same errors and bugs). Looking on the internet for a solution can prove to be useful and point your debugging efforts into the right direction. Truth be told, you will rarely find the perfect solution to your individual problem in the context of your personal, specific code. Still, you can figure out on the internet whether you are dealing with a known bug or read up on more specific information in the Python documentation. To do so, you should search for keywords relevant to your problem, such as *operator precedence* or *float division*. Just be aware that you will always need to transfer whatever you read about to your individual situation which can be a difficult task as a programming beginner. Taking on the role of detective and figuring out yourself what is going wrong is usually the way to go. Reading up on the internet is merely a tool.

## How to develop your programming skills quickly

When you start programming, it is easy to become intimidated by the amount of information you find in programming books and the multitude of error messages you encounter. Initially, you may also have difficulty adjusting to how a programmer thinks. Really, to some extent programming is but another way to approach the problem at hand. Programming means seeing a problem from another perspective. To cheer you up, even the most experienced programmers make mistakes, beginner's mistakes included. They encounter the same error messages as you do. I dare to say that, in total, they spend about as much time on debugging code than any beginner. That is the reality of programming. As your programming skills improve and you become acquainted with thinking with the mind of a programmer, you will be enabled to tackle more advanced problems and solve easier problems in more efficient ways. Luckily, there are some good practices that will speed up the development of your programming skills. In truth, without these good practices, your journey as an aspiring programmer will be much harder. Therefore, it is best to internalize the following practices from the beginning.

### Going with the flow

Whenever you read code, try to mentally follow the flow of the program step by step.


```python
x = 1
x = 2
print(x)
```

```
## 2
```

In the code snippet above, the *variable* `x` is assigned the *value* `1` in line one. You would thus think for yourself "variable x is assigned the value of 1" when reading the first line of code. Chapter 3 [Variables, values and types] explains in detail what *variables* are and how they are assigned a *value*. For now, we focus on how to approach such a code snippet. Back to the code snippet, you read line two. In line two, `x` is assigned another value, namely `2`. You will learn in Chapter 2 that variables can only be assigned one value at a time and that assigning a new value to a variable erases any earlier value assignment. Variable `x` has thus a new value once the program executes line two, namely `2`. In the last line of the program, the value of the variable `x` is printed to the console. When it is executed, `2` thus appears in the console.

Why do neither `1` nor `3` not appear in the console output? The console output is not `1` because the `print` statement comes after the second value assignment. `x` is assigned the value `2` already. The output is neither `3` because any value assignment after an initial assignment simply overwrites a variable's earlier value.

Following the flow of a program will help you understand the algorithm in front of you. You can decipher even complex algorithms by just following the flow of code.
Comprehending the flow of a computer program is a crucial step in understanding what the program does and how it achieves its purpose. The best thing is, approaching
code by following its flow develops your own programming skills much like reading a book in a foreign language improves your language skills.
By reading a book your vocabulary expands. You learn new words, how a word is used in a sentence and in which context a word is used. Often, when you encounter an unfamiliar word, you understand its meaning based on context alone. Reading code and following its flow is to your programming skills what reading a book in a foreign langauge is to your capability to understand and produce that language. At first, you encounter numerous unfamiliar constructs, but following the flow of the program will help you understand these. *Printing* to the console is a useful tool for making the flow of a program visible. Do not hesitate to insert `print` statements in any code in front of you. `print` statements can show you the value of a variable at any time or whether the program reaches a certain part of the program before it is terminated (possibly prematurely due an error).

### Just do it!

When you read about something new, be it in this book, on the internet or in class, try it yourself and see what happens! This is an essential learning attitude when learning how to program. Definitely, you cannot learn how to program by just reading books. It is above all a "learning by doing" skill. Chapter 2 [Variables, values and data types] introduces *float division*. Float division is a peculiarity of all Python 2 versions. When an integer division does not result in another integer, the result is truncated instead of represented as a floating point. Your first reaction when reading about float division should be to open your Python interpreter and try out what happens when you divide two integers which do not share a common multiple.


```python
x = 7
y = 3
print(x / y)
```

```
## 2
```

After having executed the above code snippet in your Python interpreter, does it not become more apparent what I meant by *truncated*? Being a psychologist you know that writing (by hand) facilitates structuring your thoughts and subsequently, memorizing. Trying out code snippets is no different in this respect.