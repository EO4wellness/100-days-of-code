# Current Round Details:
* Log of [T-I-L]((https://github.com/EO4wellness/T-I-L)) and [#100-Days-Of-Code Challenge](https://github.com/EO4wellness/100-days-of-code/)
* Round 5 began: R5D1 June 10, 2026  
* Round 5 concluded: R5D100 
* The acronym is ROUND 5 DAY X for each day's entry along with the calendar date it was accomplished.  

### TOC Courses (Udacity, Coursera, Udemy):	| Completion Rate: 
1. GitHub: From Zero to Pull Request            | 37% 
2. Learning How to Learn: Powerful
Mental Tools to Help you
Master Tough Subjects                           | 33%
3. Google Project Management            
Course 1 of 7
Foundations of Project Management               | 57% 
4. Python Scripting Fundamentals                | 12%
5. Django for WordPress Developers              | 14%

### TEMPLATE:  :new_moon: :walking: :sleeping: :fork_and_knife:
## :seedling: R5D4 2026-06-13
* Project 1: GIT
* Project 2: Learning
* Project 3: PM
* Project 4: Python 
* Project 5: Django for WP Dev 
* Extras N/A
<br>



## :seedling: R5D3 2026-06-12  :walking: :sleeping: :fork_and_knife:
* Project 1: GIT  UNDO in GIT is super important!    
 1. Right click-source control in VS Code and select "Discard Changes". 
 2. In terminal type git restore
 3. Staged file-click the minus icon in VS Code
 4. git restore --stage (file name) 
 5. undoing committed changes- git revert (safe option, creates a new commit that undoes the changes and the original commit stays in the history so you are not erasing anything) 
 6. git revert head undoes the most recent commit 

A note about Git Reset.  It is powerful but more dangerous soft, mix, and hard 

* [Predicting Merge Conflicts in Collaborative Software Development](https://arxiv.org/abs/1907.06274)
* [Detecting Semantic Conflicts using Static Analysis](https://arxiv.org/abs/2310.04269)
* [Reverting a commit in GitHub Desktop](https://docs.github.com/en/desktop/managing-commits/reverting-a-commit-in-github-desktop)
* [Resetting to a commit in GitHub Desktop](https://docs.github.com/en/desktop/managing-commits/resetting-to-a-commit-in-github-desktop)

Key Terms: GitHub Integration
Origin

The conventional name for the primary remote repository when you connect a local Git repository to GitHub using git remote add origin <url>. Once set, the -u flag on the first push links local and remote branches so future pushes require only git push.
Git Push

A command that sends all local commits to the remote repository on GitHub, making your snapshots visible to collaborators. After the initial git push -u origin main, every subsequent push synchronizes your local history with the cloud copy.
Git Pull

A command that fetches the latest commits from GitHub and updates the local repository to match, essential when changes have been made on the remote (such as edits through the GitHub web interface) that do not yet exist on your machine.
Git Clone

A command that downloads a complete repository from GitHub, including all files and the full commit history, onto your local machine. Used when joining a project for the first time or setting up on a new computer, after which git pull keeps the copy current.
Secure Shell (SSH)

One of several authentication protocols available when cloning or pushing to GitHub, alongside Hypertext Transfer Protocol Secure (HTTPS) and the GitHub Command-Line Interface (CLI). Each method secures the connection between your local machine and the remote repository.
Citations

arXiv: An Insight into the Pull Requests of GitHub (Rahman & Roy, 2018) — https://arxiv.org/abs/1807.01853

arXiv: On the impact of pull request decisions on future contributions (2018) — https://arxiv.org/abs/1812.06269

GitHub Docs: Managing remote repositories — https://docs.github.com/en/get-started/git-basics/managing-remote-repositories

GitHub is a professional profile 

git Remote followed by URL tells us where our local repo it is
origin
* PUSH: sends from the local copy to github
* PULL: updates local copy.  in terminal git pull 
* CLONE: copies a complete copy of a repo, when joining a new project for the first time, or setting up a new machine for the first time 

Journal Prompts

1. Creating a GitHub account transforms a local Git workflow into a publicly visible portfolio. How does the decision to make a repository public versus private affect your approach to commit hygiene, repository organization, and the quality of documentation you include? What specific steps would you take when setting up a new GitHub repository to ensure that a potential employer or collaborator can understand your project within the first 30 seconds of visiting it?

2. The commands git push, git pull, and git clone form the bridge between local development and remote collaboration on GitHub. If you cloned a teammate's repository, made local changes, and discovered that the remote had been updated by someone else in the meantime, what sequence of Git operations would you follow to synchronize your work without losing either set of changes? How does the concept of an origin remote simplify this workflow, and what pitfalls might arise if you skip the initial git pull before pushing?

arXiv: How Do Developers Usehttps://docs.github.com/en/get-started Code Suggestions in Pull Request Reviews? (Bouraffa, Pham, & Maalej, 2025) — https://arxiv.org/abs/2502.04835

arXiv: Fork Entropy: Assessing the Diversity of Open Source Software Projects' Forks (2022) — https://arxiv.org/abs/2205.09931

GitHub Docs: About repositories — https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories

GitHub Docs: Get started with GitHub documentation — https://docs.github.com/en/get-started



* Project 2: Learning - Finished the Module 1 assignment and peer review, then studied Module 2: The Essentials Chunking materials. Highlighting and underlying is often an illusion of learning.  While learning, close the study material, and attempt to recall (mental retrieval of key ideas) the material, regular do self testing, pay attention to correcting wrong thinking. Be sure to recall the materials OUTSIDE of the locations/places you normally study. 
* Project 3: PM - Today I reviewed PM concepts as I spent more time than usual on the assignment for project 2. 
* Project 4: Python 
   ### Data Types - Python assigns data type automatically to variables based on the data you assign to them. 
   1. String - Generally string data is comprised of characters that will not later be used for mathematics. Note, digits can also be strings.  Why?  Some times we have numbers we don't want to use in mathematic equations, so we use a string for those. An example of this would be a zip code.  While it is entirely comprised of numeric digits, it is not something we enter in to math equations or calculate. It works well as a string value. 
   2. Integer - this data type contains whole numbers. 
   3. Floats - this contains numbers which are not integers. 
   4. Boolean - This data type contains only two possible values:  True or False (NOTE: capital T and capital F) 

   ### Coding Examples: 
```
#Python example of creating a string variable. 
varString = 'This is a string data type in a variable named varString.'

#If we use the print(varString) command and run it, the output of the above code will be:  This is a string data type in a variable named varString.

#There is a TYPE function in Python which we can use to check a variable's type. Remember it needs to be printed to see the result. 

print(type(varString)) # Output would be <class 'str'> telling us it is a string. 

#If you need your string to contain a character which already has meaning in Python code, then you need to tell Python not to assign the character its normal meaning. For example, a single quote in Python means this is a string.  But if we need a single quote as an apostrophe then we need to use an escape (or black slash in front of the character) to tell Python its not a string. 

varEscape = 'I\'m in love with Python.'
print(varEscape)

#output would be:  I'm in love with python. 
# The other method is to use double quotes. 

varInteger = 3 
print(varInteger) 
# Output when run is 3
# Check the data type: 
print(type(varInteger))
# This statement returns <class 'int'>

# Create a float variable, print it and view its type. 
varFloat = 3.25 
print(varFloat)
print(type(varFloat))
#the results are it will first return 3.25 on one line, then the next line it will return <class 'float'>

#Create a Boolean variable, print it, and view its data type. 
varBoolean = True 
print(varBoolean)
print(type(carBoolean))

# running this returns True on the first line then <class 'bool'> on the second line. 
#Note this is Case sensitive thus if we create varBoolA = true when run this python code will return an error message. 

Traceback (most recent call last):
  File...
    varBoola = true 
NameError: name "true" is not defined. Did you mean: 'True'? 

```

Data types are important.  You should also be aware of what type of data is stored in a variable. If you don't, your program is likely to crash or not function as expected.  

RULE: The data stored in a variable as the output of the input() function is always a string.

```
#Python 
varInputA= input('Name? ')
Name? Shad 
print(varInputA)
# output is Shad 
print(type(varInputA))
# output is <clas 'str'>

varInputB= input('Age? ')
Age? 50
print(varInputB)
# output is 50
print(type(varInputB))
# output is <clas 'str'>

#If we do not understand this and try to do math with it, we get an error message.  Example: 
print(varInputB / 10) 

Output is: Traceback (most recent call last): 
  File...
     print(varInputB /10) 
TypeError: Unsupported operand types(s) for /: "str" and "int" 

```

When ever the INPUT() function is used, we have to change the datatype of the variable before we do math with it. 
To do this we use the INT() function.  

```
print(int(varInputB) / 10) 
#output is 5.0

# The int() function changes the data type of the argument to the integer data type.  We can check this by testing the type of the variable that comes out of the int() function by using a nested function like this: 

print(type(varInputB))

# Output is ,class 'str'>

print(type(int(varInputB) / 10))
#output is: <class 'float'>  NOTE it is a FLOAT even if the value stored is a whole number!  

```
### Convert any data type using these functions: 
1.   float()
2.   int() 
3.   str()
4.   bool() 

The boolean is interesting because if there is something assigned to the variable, if it has a stored value, the boolean function will return TRUE but if it is empty it will return FALSE. 

```
# Write a simple Python script which passes in someone's age and calculates what age they will be in five years

varAge = input('Age? ')
# Inputting at the prompt: Age? 50 
print(age5 = int(varAge) + 5)

print (age5)
# Running this returns 55

 Also we can do this before hand (order) 

varLastYear = int(input('Age last year? '))
Age last year? 49 
print(type(varLastYear))
<blas 'int'>


```

Recall: if you separate arguments in the print() function with commas, print will convert the variable to a string. 

* Project 5: Django for WP Dev 
* Extras: Want to prioritize finishing GIT and the LEARNING coursework, while progressing with the Project Management daily, even if it is reviewing concepts due to occasional time constraints. I discovered FreeCodeCamp has Spanish certification now.  I'm going for it.  I completed the intro & vowels today. 
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
```
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
```

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
CLASS-is a blueprint of something and an object is an instance of a class. |

OBJECT: The thing which a class is based upon |

METHOD- a function within a class |

FUNCTION-does something, is not what the class is but what it can do |

ATTRIBUTE- something (often a string, or a whole number or a float) the class is |


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


* Extras 
   1. Server maintenance and wordpress updates. 
   2. Read a few articles about AI and advancements with AI.
   3. Completed a Health and Wellness course on Coursera about Metabolism and recent science regarding it.  

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


##ICONS:
1. Worked Out = :walking:
2. Quality Sleep = :sleeping:  
3. Eating Nutritionally = :fork_and_knife: 
4. Learning and Growing = :seedling: 
<br>
:calendar:
:first_quarter_moon: 
:full_moon:
:last_quarter_moon:
:new_moon:
<br>
