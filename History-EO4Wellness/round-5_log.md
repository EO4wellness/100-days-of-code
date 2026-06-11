# Current Round Details:
* Log of [T-I-L]((https://github.com/EO4wellness/T-I-L)) and [#100-Days-Of-Code Challenge](https://github.com/EO4wellness/100-days-of-code/)
* Round 5 began:  June 10, 2026
* Round 5 concluded: (ongoing) 

### TOC Courses (Udacity, Coursera, Udemy):	| Completion Rate: 
1. GitHub: From Zero to Pull Request    | 20% 
2. Learning How to Learn: Powerful
Mental Tools to Help you
Master Tough Subjects                   | 26&
3. Google Project Management            
Course 1 of 7
Foundations of Project Management       | 57% 
4. Python Scripting Fundamentals        | 11%
5. Django for WordPress Developers      | 14%

### TEMPLATE:  :new_moon: :walking: :sleeping: :salad: 
##🌱R5D2 2026-06-12
* Project 1: GIT
* Project 2: Learning
* Project 3: PM
* Project 4: Python 
* Project 5: Django for WP Dev 
* Extras N/A
<br>

## :seedling: R5D2 2026-06-11 WO: Legs+Cardio :walking: :sleeping: :salad:
* Project 1: GIT -
Key Terms: Local Git Workflows
Staging

The process of selecting specific file changes to include in the next commit using git add or the VS Code source control plus icon. Staged files move into a holding area so you can build deliberate, well-described commits rather than saving everything at once.
Git Restore

A command that discards uncommitted changes in a working file, reverting it to the last committed version. Safe to use before staging because nothing has been recorded yet, and the equivalent action in VS Code is the discard-changes button in the source control panel.
Git Revert

A safe undo command that creates a new commit which reverses the changes from a previous commit while preserving the original in history. Recommended for undoing work that has already been pushed to GitHub because it keeps the commit history honest and intact.
Git Reset

A command that moves the branch pointer backward, removing commits from history in three modes: soft keeps changes staged, mixed (the default) unstages but preserves file changes, and hard permanently discards both the commits and the file modifications.
Git Log

A command that displays the chain of commits in a repository, showing each commit's hash, author, timestamp, and message. The --oneline flag condenses output to one line per commit for fast scanning, and every commit's full details remain available for deeper inspection.

[Creating a New Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
[Repository Quick Start](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)

```
#Make a new Directory and Test it.  Open command line prompt. 
mkdir mytestrepo

#change into the directory we just made
cd .\mytestrepo\

#open the new directory in vs code
code .

```
Now we are in VSCode we want to initialize the repository.  Go into SOURCE CONTROL  and click initialize repo


* Project 2: Learning - Learned about the research regarding Spaced Repetition Algorithm/AI helps. Struggling to recall strengthens our memory over time. Recommendation: Smarter Humans.AI, Memorise, Anki. Interview with Benny Lewis a.k.a. Benny the Irish Polyglot who authored Fluent in 3 Months-Speak Any Language from Day One. Dr. Terrence Sejnowski neuroscience. Learning by doing. Active engagement-ask questions if you start to get bored to reinvigorate discussion and discovery. Context switching can be difficult unless we practice it frequently, however, some people do better when they've reached the end of what they can absorb on one topic, to context switch to a new topic. A stimulating, rich, intellection environment helps our neurons.  Likewise, exercise helps too. Use your muscles, rather than our brain, to absorb what we've learned in our study, focused, phase.  Be in an intellection, creative, environment to absorb better/more. Not all smart people are successful, instead staying the course, is very important. Learn with fresh, new, eyes to keep learning life-long. Finished module 1, week 1, studies and quiz. 
* Project 3: PM
- Review and Recap of Model 1 & 2. 
- Two approaches:  Waterfall and Agile 
  Life Cycle of a Project 
  Phases of a Task 
  Organize a Project 
- Project Life Cycle - the Structure of the Project 
  Phase 1: :rocket: Initiate the Project 
 	:rocket: - define project goals
 	:rocket: - define deliverables
	:rocket: - understand or source the budget 
	:rocket: - identify needed resources
	:rocket: - identify needed people 
	:rocket: - define the project's value
	:rocket: - discover any potential roadblocks
	:rocket: - receive approval to move forward with it 
  Phase 2: :open_book: Make a Plan - How will you meet the goals of your project? 
        :open_book: exact budget
        :open_book: tasks
        :open_book: communication of team roles and responsibilities 
        :open_book: schedule
        :open_book: resources 
        :open_book: SOP/SLA
  Phase 3: :heavy_check_mark: Execute & Complete Tasks - NOTE: the TEAM has the responsibility to complete the project, 
	   as project manager, your role is to make sure they do and you keep them motivated and watch deadlines
           be flexible  and adapt 
  Phase 4: :trophy: Close the Project - Celebrate what worked, and take note of what didn't to learn for next time. For example, you may build something as your project, and you pass it off to the team to maintain it. 


* Project 4: Python - today's lesson materials reviewed the topic of Data Types. 
Data Types - Python automatically assigns data types based on the kind of information you put into your variables. 

1. String data type is comprised of letters and will not be used for math. 
```
#Python 
varString = "This is a string."
print(varString)
# the output will be :   This is a string.

```
There is a function called type() and the only argument it takes is the thing you want to verify.  Note: you have to print this function to observe it.  Example:
```
#Python
print(type(varString))
```
Escaping the character is where I left off for today. 
* Project 5: Django for WP Dev 
Python VS PHP 
```
# PHP - flexible coding language, shares some of its syntax with C, website friendly. 
# Each line ending has a semicolon; or opening and closing curly braces {}
<?php 

function get_list() {
  return "hello world";
}

# Python - robust, extendable. Yet, it is a lean language. Indentation is super important. 
def get_list()
  return "hello world"

```
CLASS-is a blueprint of something and an object is an instance of a class. 
OBJECT: The thing which a class is based upon
METHOD- a function within a class 
FUNCTION-does something, is not what the class is but what it can do 
ATTRIBUTE- something (often a string, or a whole number or a float) the class is

```
# naming files:  in Python call it name.py and in PHP name.php
# examples cat.py or cat.php 

class Cat(): #this is a class 
  def meow(self): #this a method, it is something it can do, not something that it is 
     print 'meeow' # print is a function 

#variables in Python are just a name and an assigned value.  In PHP it is $name, JavaScript it is var name 
# Python syntax-camel case or underscores, lower case start

tom_the_cat = Cat()

#call a method. in Python we use variable name DOT. method name.  in PHP we use -> to call a method 

tom_the_cat.meow() 

```
To run either of these example files in command line type:
python cat.py

or 

php cat.php

```
<?php

class cat {

  function meow() {
    print('meow');
  } 

}

$tom_the_cat = new (Cat();

$tom_the_cat->meow();

```

INSTRUCTOR: Richard Miles, Web Developer 

This course is an introduction to Django specifically targeted at WordPress or intermediate web developers. In this course we will walk through everything from the basic principles of python to developing a full e-commerce system using the Django framework.

Some of the sections include:

    Discussing the differences and similarities between php and python
    Setting up a functional python workspace
    Creating a basic TODO app in python
    Installing and customising Django
    Creating a blog using Django
    Creating a CMS using Django
    Creating 3 different e-commerce stores using Django

What you’ll learn

    Understand how python works as a programming language
    Create a basic Class and Object in python and php
    Create a TO-DO application using python
    Understand the architecture of the Django framework
    Create a Django server
    Create a basic blog using core python and Django
    Create a CMS using Django's powerful package and extension management system
    Create an eCommerce store using Oscar Commerce
    Create an eCommerce store using Mezzanine and Cartridge
    Create an eCommerce store using Saleor

Are there any course requirements or prerequisites?

    Basic understanding of how web programming works
    Basic knowledge of php/WordPress or python

Who this course is for:

    Anyone who has a basic understanding of web development and would like to broaden their skillset
    Anyone who has a basic understanding of php or python
    NOT for someone who does not want to learn how to code in python


* Extras N/A
   Server maintenance and website maintenance. Read a few articles about AI and advancements with AI. 

<br>


## :seedling: R5D1: 2026-06-10 :walking: Core+Cardio, :sleeping:  :fork_and_knife:
* PROJECT 1: GIT! Just recently, I've been very active in learning, again, so I decided to resume the 100 days of TIL activities, which I used to enjoy. As it's been a while since I used Git-a versioning tool-and GitHub-the platform-, I decided to revisit Coursera's GitHub: From Zero to Pull Request course again. 

Today I studied [Module 1: Git Foundations, Understanding Git](#), Intro to course, Key terms, what is Git and GitHub, installing and using Git, installing git, reflection: understanding Git, and committing this to the repo. Ways to use Git:  Browser Only , Linux development environment, [GitHub Desktop](https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktopgithub) or a local GUI without using terminal or the traditional method: using command line. 

CODE STEPS TO VERIFY GIT INSTALL: 
```
Open Command Prompt 
type: git --version 
which should return something like:  git version 2.x.windows.x

type: git config --list
which should return your set up including user name and email 

if you're email isn't set up, type: git config -global user.email=your git email

if you want to configure the global editor, type: git config --global core.editor 'code --wait' 
```
Course Further Reading: [Code Fork](https://arxiv.org/abs/1004.2889), [Merge](https://arxiv.org/abs/2105.07569), [Starting with Git](https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git) and [Git Setup](https://docs.github.com/en/get-started/git-basics/set-up-git). 

I updated my Git version, GitHub Desktop installation, Notepad++ version, and Visual Studio Code. 

* PROJECT 2: HOW TO STUDY!  I am working on finishing Module 1. One of the "study" tips they include in this coursework is the benefit of rest.  We learned that while we are exercising, showering, resting, we learn. And while we sleep, we recover and some memories are swept away, but others are retained and strengthened. In harmony with keeping the whole person in tip-top shape while learning both sleep and relaxation should be emphasized.  In addition, although the coursework didn't mention it yet--I would add N U T R I T I O N also plays an important role.  Therefore I'm adding to my 100-day coding challenge movement, nutrition, quality sleep priorities. 
* PROJECT 3: GOOGLE PROJECT MANAGEMENT: Today I continued my studies and concluded Module 2 making my progress 50% complete in the Foundations of Project Management coursework.
* PROJECT 4: Python- Earlier this week I studied Module 1: Exploring Programming Concepts. Then, Exploring the Programming Process, and I am now reviewing Basic Syntax: Functions, Variables, Data, Types, Arithmetic Operators, Basic Syntax Assessment. 
- A function is a block of programming code that can be reused.  It typically performs a specific tasks.  It must have a unique name or identifier and a set of open and closing parenthesis. Additionally, function names are lower case. An example of a properly formatted function in python is: 
```
#python
  print()
```
- Arguments are the information, as required, by the function.  If in order to work, the function requires information, the information is then provided inside the function's open and close parenthesis. The information it needs is known as the function's arguments.  If there are multiple arguments, then they are separated by commas.  All text must be enclosed in either a single 'example' or double "example" quotes.  Typing a function with the arguments in a script is called "calling the function".   An example of a properly formatted argument inside a python function is: 
```
#python
  print("Hello World!") 
```
- Good to know: Python has a number of built-in functions. It also has modules that aren't automatically loaded by can easily be added to a Python script. 
Variables are another basic component of successful Python programming. 
What is a program?  A program takes input, processes it, and then it produces output. 
- How do we accept input into Python?  We use the input() function.  This function has the basic syntax of input(prompt) where the prompt is language which helps the user know what to enter for input.  So for example if we wanted to find out someone's Name and Email address we could use two input functions to ingest this information, say for an email list.  But what would the prompt portion look like? It is not the user's input, it is the prompt to inform the user what to input. Here are two examples: 
```
#python
input("Enter your first name")
#or 
input("Enter your email address") 
```
- Variables: when a user responds to our input function's prompt and enters some information, we have to have a way to store their information.  We do this using a variable.  Variables are any value stored in memory and given a name or an identifier. Variables can be set by the script its self, which we write, or from a user who gave us the input. If we fail to capture the user's input into a variable, it will be forever lost.  To assign a value to a variable in Python we follow the syntax of Variable_Name=value. The instructor jokes that variables are tiny "RAM buckets" 

```
variable1 = 10 #script assigned numerical variable 
vairable2 = "Robert" #script assign string variable 
variable3 = input("Please type your first name") #user input 
#Variables can be assigned in one line such as: 
x, y, z = "hello", 'ho are', "you"
#Or you can assign multiple variables to the same value such as: 
x=y=z="test" 

```
- Variable Best Practice:   tyhpe variable names in lower case.  Do not use spaces in variable names. For multiple words, use an underscore or camel case. Conventional practice is to use descriptive words for variables so anyone reading them can understand what they are such as userInput=input("Name")
- Variable Limitations: Variable names must begin with a letter or an underscore.  Variable names can never be a number(digit). Variable names cannot contain spaces.  Variables cannot be the same as Python keywords or as any of your functions.  Variables are case sensitive so that the variable myVariable is NOT the same as myvariable. 

```
#mini list of reserved words in python:
False
None
True
and
as
assert
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is 
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield

```
-Python Output typically uses the print function. The syntax is always a string (letters/characters) and it is print() with is argument always being the string it is going ot print.  
```
#python print() function
print("Hello")
myVariable=input('Name')
print(myVariable)
print("hello ", "how are you?", "I'm fine.")

# Concatenation in Python is super picky it has to be a string
x="hi "
y='how are '
z='you?'
print(x + y + z) 
#Output: hi how are you? 

```
* PROJECT 5: Udemy Coursework. Completed Section 1 study, PHP vs Python  
* Extra: I just finished [Udacity's AI 2026 Challenge](https://www.udacity.com/certificate/e/3d7023f0-2805-11f1-ae96-93aefba44d81) and I'm still thinking about concepts within it, as well as AWS tools. 
<br>


ICONS
Worked Out = :walking:
Quality Sleep = :sleeping:  
Eating Nutritionally = :fork_and_knife: :salad: 
Learning and Growing = :seedling: 
<br>
:calendar:
:first_quarter_moon: 
:full_moon:
:last_quarter_moon:
:new_moon:
<br>
