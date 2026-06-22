# Current Round Details:
* Log of [T-I-L]((https://github.com/EO4wellness/T-I-L)) and [#100-Days-Of-Code Challenge](https://github.com/EO4wellness/100-days-of-code/)
* Round 5 began: R5D1 June 10, 2026  
* Round 5 concluded: R5D100 
* The acronym is ROUND 5 DAY X for each day's entry along with the calendar date it was accomplished.  

### TOC Courses (Udacity, Coursera, Udemy):	| Completion Rate: 
<<<<<<< HEAD
2. Learning How to Learn: Powerful
Mental Tools to Help you
5. Django for WordPress Developers              | 14%

### TEMPLATE:  :walking: :sleeping: :fork_and_knife:
## :seedling: R5D11 2026-06-20  
## :seedling: R5D14 2026-06-23  
* Project 3: PM - Project Initiation: Starting a Successful Project 
* Project 4: Python - 
* Project 5: Django for WP Dev 
* Extras N/A
<br>

=======
3. Google Project Management            
Course 1 of 7
3.1 Foundations of Project Management           | 100% 
3.2 June 15, 2026-Began Course 2 of 7           | 21%
4. Python Scripting Fundamentals                | 21%
=======   
3.2 June 15, 2026-Began Course 2 of 7           | 30%
4. Python Scripting Fundamentals                | 26%
7. PMP Exam Practice                            | 35%

COMPLETED: 
1. GitHub: From Zero to Pull Request            | 100% 
2. Learning How to Learn: Powerful
Mental Tools to Help you
Master Tough Subjects                           | 100%
3. Google Project Management            
Course 1 of 7
3.1 Foundations of Project Management           | 100% 
6. Intro to ClickUp in Project Management       | 100%


:seedling: R5D13 2026-06-22  
* Project 3: PM - Project Initiation: Starting a Successful Project - Looked at [Lean Six Sigma certification](https://www.sixsigmaonline.org/) stats and various [PMI courses](https://www.pmi.org/learning/free-online-courses). 

OKRs are: 
- Aspirational: Is the objective challenging and inspiring?
- Aligned with company goals: Does the objective support company and/or departmental OKRs?-
- Action-oriented: Does the objective motivate the team to take initiative?
- Concrete: Can the project team easily grasp the objective?
- Significant: Will achieving the objective make a meaningful impact or change from where you are currently?


* Project 4: Python - Finished Labs and practice assessment. Scored 100%
* Project 5: Django for WP Dev 
* Project 7: PMP Exam Practice - Continued looking at what is needed to take the exam.  Realized I'll be eligible to take the [Certified Associate in Project Management-CAPM ](https://www.pmi.org/certifications/certified-associate-capm) now and work towards building my recent 8 year experience proof for taking the PMP soon thereafter.  
* Extras N/A -set up computer for Help Desk. 
<br>

:seedling: R5D12 2026-06-21  
* Project 3: PM - Project Initiation: Starting a Successful Project  - worked today on finishing up the OKRs project and setting up ClickUp as a portfolio of my work, as well as initiating a repo for PM templates, best practices, thought guides.  Planned structure and laid out roadmap. 

* Project 4: Python - Took a look at loops. 
## Loops- in Python are any statement which are going to execute more than once. A loop also serves the function of keeping a block of code active until it is no longer needed.

### Types:
1. **While** Loops which execute until some condition is met. 
2. **For** Loops which iterate a specific number of times.  

```
# Use a while loop to test for a valid condition. 

while not (answer == 'y' or answer == 'n'):
     print("I am sorry, thats not a valid answer. Please try again.")
     answer = input("Would you like to play a game? (y/n)")
```
While Loops can also be used as a counter. 

```
# example simple python counter.

answer = input("Please enter a number between 1 and 10")

counter = int(answer)

while counter >0:
     print("tThe value of the counter is ', counter)

counter = counter = 1

```
A for loop is always used with a sequence or collection of items. 

```
a = test 
print(len(a))

``` 

* Project 5: Django for WP Dev 
* Extras N/A
<br>


:seedling: R5D11 2026-06-20  
* Project 3: PM - Project Initiation: Starting a Successful Project working on the OKRs project. 
* Project 4: Python - Today's topic was Identity Operators. 
- Identity Operators-today's topic. 
- Methods
- recall, every object in python has a type. 
- if it is data, it has a data type 
- if it not data, it will have a type related to whatever it is 
- Example if we had a button inside a windows application, the object would be the button type
- When we call a function we have to provide the information in the arguments of the function. 
- If the function affects the object, then we specify the object as one of the arguments. 

```python
# Lets take a look at variables: 

a = "5" 

# now let's check the value: 

print(a)

# the output when we run this Python code is 5 

# now let's check the type: 

print(type(a))

# the output, because we put the quotes around it, is going to return <class 'str'>

```
- Some functions are limited to objects of a certain type or may be functions that are often used with objects of that type. 
- When the programmer creates objects in that language, they specify these functions in advance in the form of methods. 
- A method is a built-in function that can be called by an object.
- when you use (invoke) a method, use this syntax: 'variable.method()' or object.method()
- when you invoke a method, it automatically impacts the object.
- the only arguments you need to supply are any 'missing'  information 
- string objects have an isdigit() method.
- the isdigit method of a string tests to see if the string is actually a number
- if the string contains a number, isdigit() returns a value of True. 
- Python objects = data + abilities 
- this is why bool True and False are capital 
- in Python all objects are standardized to capital letters 

```python
# continuing our previous code above we can test this and illustrate what we have learned

a = '5' 
print(a.isdigit())

# this returns True 
```

- we have two identity operators: 'is' and 'is not' 
- these are not the same as '==' and '!=' 
- because  '==' and '!=' are used to evaluate the values of objects
- whereas identity operators test to see if the two items are or are not the same object 
```
a = 'string'
if type(a) is str:
  # then do something if true
a = 'string' 
if type(a) is not int: 
  # then do something else if not true 

now we can update our little game with a check to make sure it is a number not another character that is not an number 

Order of Operations in Python
1. Exponents 
** 
2. Multiplicative Operators 
* / %
3. Additive Operators 
+ - 
4. Relational/Comparison Operators 
<= <  >  >=
5. Equality Operators 
== != 
6. Identity Operators 
'is'  'is not' 
7. Logical Operators 
'and'  'or'  'not' 



* Project 5: Django for WP Dev 
* Extras N/A
<br>


## :seedling: R5D10 2026-06-19  
* Project 2: Learning - Memory - Finished the assignments in Module 3 and progressed to Module 4-the end is in sight. Completed presentation on self teaching course project. 

* Project 3: PM - Project Initiation: Starting a Successful Project 
While I'm committed to taking, and finishing, the Google PM coursework, I took a moment today to think about and research other options.  I found PMP and the 35 hours of instruction requirement for progressing with certification. I also revisited the exams for Google's Foundations of PM and retook them as a method of recalling the materials.  
OKRs - stretch goals -
Objective
Key Results 

OKR-levels 
- company or organization level (annual updates) 
- department or team level 
- project level 

Office Green Example:   Objective-increase customer retention by adapting to the changing workplace environment

Based on Office Green's over-arching objective, they develop key results such as: 
- 95% of phone, chat, and email customer support tickets are resolved during the first contact. 
- Our top 3 most requested new offering for distributed office environments are in pilot by the end of the second quarter. 
- Our sales and support channels are available 24/7 by the end of the year. 

Any of these could become its own project.   
Any one of these could become further subprojects such as the sales support 24/7 could lead new team OKRs such as Objective: Increase the sales team presence nation wide. to Key Result: New sales offices are open in 10 cities by the end of the year. 

- OKR stands for Objectives and Key Results.  They combine a goal and a metric to determine a measurable outcome. 
- Objectives define what needs to be achieved and describe a desired outcome. 
- Key Results define how you will measure the outcome of your objective. 
- Company-level OKRs are shared across an organization so that everyone can align and focus their efforts to help the company reach its goals. 
- Project-level OKRs help define measurable project goals. They need to align with and support both company and department level OKRs. 

Working on OKR project. 

* Project 4: Python - 
* Project 5: Django for WP Dev 
* Extras N/A
<br>


:seedling: R5D9 2026-06-18  
* Project 1: GIT - COMPLETED dropping from future notes
* Project 2: Learning - Memory 
Logical Operators:  in Python, this also works like SQL.

1. and (both conditionals must be met for the statements to execute 
2. or
3. not

- we always use them in lower case


```python

# this us a python "and" application 

# ask the user if they want to play a game
# a calid answer is "y" or "n"

answer = input('Would you like to play a game? (y/n) ' )

# if statement to verify if the user entered a valid reply or not
# if they don't, then exit.
#  ! Means not equal to 
# The statement only evaluates to true  if the user didn't answer y or n.

if answer != 'y' and answer is 'n':
     print('I see you cannot follow directions.  Goodbye. ')

# elif statement to test if the user enters 'n'
# if they did, exit

elif answer == 'n':
      print('I am sorry you do not want to play. Goodbye.' )

 # else they must gave entered 'y': play the game 

else:
     number = int(input('Please enter a number between 1 and 10: '))

     if number ==0:



```
- If there are multiple conditionals they have to be in parenthesis.  


Next: Identity Operators 

- Methods 
- Every Python object has a type
* data type 
* button type
- When we call a function, we provide info in the arguments of that function.  
- If the function, impacts the object,  then we put the object in as one of the arguments. 



Memory
- we hold on to, and acquire very easily Visual-Spatial memory.  

Anki

Spaced Repetition 
Consolidated
Reconsolidation

Anastrocytes is the most abundant glial cell
- nutritional providers to neurons
-repair 
* Project 3: PM - Identifying project goals: 
For the rest of the course we are following an example: Office Green (a commercial landscaping company)
-service Plant Pals 
-offer high-volume customers small, low-maintenance plants 

-What needs to be done.  Define goals and deliverables before starting. 
CLEAR PICTURE--> how to accomplish it --> 

Project Goal-desired outcome
-  ​Well-defined goals are both specific and measurable. 
-The goal of your Office Green project might be to ​increase revenue by five percent through ​a new service called Plant Pals that offers ​desk plants to top customers by the end of the year.

Project Deliverables-the products or services that area created for the customer, client, or project sponsor. 

Since your deliverables depend on your goals, ​it's in your best interest to get ​those goals as well- defined as possible. 

SMART goals
- specific
- measurable
- attainable
- relevant
- time-bound 

If you set the goals, or not, you need to evaluate them for each project. 

- What do I want to accomplish? ​
- Why is this a goal? ​
- Does it have a specific reason, purpose, or benefit? ​
- Who is involved? 
- Who is the recipient? Employees, customers, the community at large? ​
- Where should the goal be delivered? 
- ​Finally, to what degree? ​In other words, what are ​the requirements and constraints? ​

Metrics-measure your goals.  Some goals are yes or no but most need some type of metric. 

Challenging to encourage growth--but not too extreme that you cannot reach your goal.  Find a balance. 

OKRs
-objectives
-key results


* Project 4: Python - 

Logical Operators:  in Python, this also works like SQL.

1. and (both conditionals must be met for the statements to execute 
2. or
3. not

- we always use them in lower case


```python

# this us a python "and" application 

# ask the user if they want to play a game
# a calid answer is "y" or "n"

answer = input('Would you like to play a game? (y/n) ' )

# if statement to verify if the user entered a valid reply or not
# if they don't, then exit.
#  ! Means not equal to 
# The statement only evaluates to true  if the user didn't answer y or n.

if answer != 'y' and answer is 'n':
     print('I see you cannot follow directions.  Goodbye. ')

# elif statement to test if the user enters 'n'
# if they did, exit

elif answer == 'n':
      print('I am sorry you do not want to play. Goodbye.' )

 # else they must gave entered 'y': play the game 

else:
     number = int(input('Please enter a number between 1 and 10: '))

     if number ==0:



```
- If there are multiple conditionals they have to be in parenthesis.  


Next: Identity Operators 

- Methods 
- Every Python object has a type
* data type 
* button type
- When we call a function, we provide info in the arguments of that function.  
- If the function, impacts the object,  then we put the object in as one of the arguments. 


* Project 5: Django for WP Dev 
* Extras N/A
<br>



:seedling: R5D8 2026-06-17 :new_moon: 
* Project 1: GIT - Completed 
* Project 2: Learning completed Module 2's information about procrastination and best practices. 
Key concepts:  
- Product vs process -research finds focusing on the process helps beat procrastination where focusing on the product does not.  Example: I will study math for 20 minutes (process) vs I will complete my math homework (product). 
- Good habits beat procrastination.  here are 4:  1.  CUE.  It is the thing which triggers us into procrastination mode.  Learn to recognize your own cues and switch your space or context to avoid triggering the cue.  2.  The Routine. The routine is triggered in response to the cue.  Switch the cue, the routine doesn't get triggered.  3.  Reward:  procrastination is an easy habit to develop because of the reward.  4) The belief:  habits are powerful because we believe in them.  
* Project 3: PM completed Fundamental of Project Initiation and Understanding the key components of the project initiation phase. 
There are several KEY COMPLONEST of Initiation Phase. 
-GOALS: This is what you have been asked to do and what you are trying to achieved. 
-SCOPE: This is the process of defining what works needs to happen to complete the project. 
-DELIVERABLES: The products and services that the project creates for the customer, client, or project sponsors. Deliverables can be tangible or intangible.
-SUCESS CRITERIA: The standards by which you measure how successful a project was at reaching its goals. 
-STEAKHOLDERS: The people who are both interested in and affected by the completion and success of the project. 
-RESOURCES: the Budget People and Materials at our disposal to complete the project. 

Use the key components to develop a Project Charter to clearly define the project and its goals and outline what is needed to accomplish them. The charter is used to get organized, set up a framework, and to communicate these details to others. 

Recap: you gather information about your goals, scope, ​deliverables, success criteria, stakeholders, and ​resources, and you document that information in the project charter.

Previously, you learned that a cost-benefit analysis is the process of adding up the expected value of a project—the benefits—and comparing them to the dollar costs. In this reading, we will discuss the benefits of conducting a cost-benefit analysis, guiding questions to help you and your stakeholders conduct one, and how to calculate return on investment (ROI).
The benefits of a cost-benefit analysis

A cost-benefit analysis can minimize risks and maximize gains for projects and organizations. It can help you communicate clearly with stakeholders and executives and keep your project on track. Because this type of analysis uses objective data, it can help reduce biases and keep stakeholder self-interest from influencing decisions. 

Comparing a project’s benefits to its costs can help you make a strong business case to stakeholders and leadership and ensure your organization pursues the most profitable or useful projects. Organizations use cost-benefit analysis to reduce waste and invest their resources responsibly.
Guiding questions for a cost-benefit analysis

When you’re pursuing a project, the benefits should outweigh the costs. It’s important for you and your stakeholders to consider questions like the ones that follow early on, while you prepare the proposal.

To determine the benefits of a project, you might ask:

    What value will this project create? 

    How much money could this project save our organization? 

    How much money will it bring in from existing customers?

    How much time will it save? 

    How will it improve the customer experience?

And to determine the costs of a project, consider questions such as:

    How much time will people have to spend on this project?

    What are the one-time costs?

    Are there any ongoing costs?

    What about long-term costs? 

You might also consider questions about intangible benefits. These are gains that are not quantifiable, such as:

    Customer satisfaction. Will the project increase customer retention, causing them to spend more on the company’s products or services? 

    Employee satisfaction. Is the project likely to improve employee morale, reducing turnover? 

    Employee productivity. Will the project reduce employee’s overtime hours, saving the company money?

    Brand perception. Is the project likely to improve the company’s brand perception and recognition, attracting more customers or providing a competitive advantage?

You can also flip these questions to consider intangible costs. These are costs that are not quantifiable. For example, might the project put customer retention, employee satisfaction, or brand perception at risk?

When assigning values to tangible or intangible costs and benefits, you can reference similar past projects, conduct industry research, or consult with experts.
Calculating costs and benefits

The process of calculating costs and benefits is also called calculating return on investment, or ROI. There are many ways to determine a project’s ROI, but the easiest way is to compare the upfront and ongoing costs to its benefits over time.

One common ROI formula is:

In this formula, G represents the financial gains you expect from the project, and C represents the upfront and ongoing costs of your investment in the project.

For example, imagine your project costs $6,000 up front plus $25 per month for 12 months. Twenty-five dollars for 12 months equals $300 per year, meaning your total cost is $6,300. You estimate that the project will bring in $10,000 in revenue over the course of that year. That leaves you with: 

    G = $10,000

    C = $6,300

Now, using the formula above, you plug in the amounts as follows: 

    ($10,000 - $6,300) ÷ $6,300 = ROI

Then you proceed with the calculation: 

    First, inside the parentheses:  10,000 - 6,300 = $3,700

    Next, $3,700 ÷ $6,300 = 0.5873

    Finally, 0.5873  x 100 = 58.7% 

The ROI comes to 0.587, or 58.7%. Given a strong ROI tends to be anything above 10%, you find 58.7% to be a strong ROI, so you decide to pursue the project.
Key takeaway

Performing a cost-benefit analysis can help you and your stakeholders determine if it makes sense to take on a new project by evaluating if its benefits outweigh its costs. When conducting cost-benefit analyses for your prospective projects, you can use the guiding questions and ROI formula provided in this reading as a reference. 

To learn more about performing a cost-benefit analysis, check out these articles:


* Project 4: Python completed conditional statements
- Conditional Statements in Python are just like conditional statements in SQL.
- if the conditional statement evaluates in python to True, then the code inside the conditional statement will execute. 
- if the condition evaluates to False, the code inside the python statement does not execute. 
- we use the if statement, the else statement and elsif frequently in python. 

```python
# Example of an if statement 
# the syntax for if statements is  if condition: statement
# note it is too easy to forget the : in the IF statement.  when debugging check for : 

if 5>6: print('yah') 

# if we run this statement nothing happens because five is not gre4ater than six so the print statement doesn't execute because it is False

if 5<6: print('yah')

# this statement will print yah 
```

Conclusion is a conditional statement is a simple statement.  It functions in a sense like a light switch.  If something is true, we switch on to execute the associated statement.  If, however, the statement is False, we do nothing--the switch is off.

If we want more than one on/off function we need a else: clause. 

```python
if 5>6: print('yay')
else: print('boo') 

# this returns boo sinc4e five is not greater than six, the statement is false and it runs the else 

```

 In other words, the statements in the else: clause execute when ever the if statement does not evaluate to true. 

We can also use another python conditional technique when we need to check for multiple conditions. 

```
# python syntax looks like 
if condition: 
	statement
elif condition2:
	statement
elif condition 3:
	statement 
else: 
	statement 
```

To see this in action let's make a simple program which uses this structure to look at User input. 

```python

# Ask the user to enter a number 

number = (int(input("Please enter a number between 1 and 10: "))

# Series of if ... elif ... else statements to respond based on the number the user entered. 

if number == 10:
		print("High roller!") 
elif number >- 8: 
		print("You like your numbers high") 
elif number >=4:
		print("You're a middle of the road kind of person, hm?!") 
else: 
		print("Keeping it small.  I like it!") 

# if you save this script with the name conditionalcode1.py
# then visit command line and type python 3 conditionalcode1.py
# you will be able to test the output.  test all of the outputs including if the user doesn't follow the instructions 
```

When testing the script, if we input the number 0, our program doesn't anticipate the person not following instructions.  We can fix this with either a nested statement or another statement before the else.  

```python

# Ask the user to enter a number 

number = (int(input("Please enter a number between 1 and 10: "))

# if statement to test if the user entered 0; if so, exit.

if number == 0 
		print("I can see you do not follow directions. Goodbye!")

# Series of if ... elif ... else statements to respond based on the number the user entered. 

if number == 10:
		print("High roller!") 
elif number >- 8: 
		print("You like your numbers high") 
elif number >=4:
		print("You're a middle of the road kind of person, hm?!") 
elif number >10:
		print("I see you didn't follow the instructions.") 
else: 
		print("Keeping it small.  I like it!") 
```

* Project 5: Django for WP Dev 
* Extras N/A
<br>

:seedling: R5D7 2026-06-16 :new_moon: 
* Project 1: GIT- Completed the next module looking at MCP and copilot automation scope and availability inside Github. 
* Project 2: Learning 
* Project 3: PM - Completed an assessment project where we were given a real-life scenario, and then asked to prove we understood the standard initiation phase of launching a project.  I scoared 100% on the task.
```
  Cost Benefit Analysis Formula:  (g-c) / c = roi 
In this formula, G represents the financial gains you expect from the project, and C represents the upfront and ongoing costs of your investment in the project.
  To determine the benefits of a project, you might ask:

    What value will this project create? 

    How much money could this project save our organization? 

    How much money will it bring in from existing customers?

    How much time will it save? 

    How will it improve the customer experience?

And to determine the costs of a project, consider questions such as:

    How much time will people have to spend on this project?

    What are the one-time costs?

    Are there any ongoing costs?

    What about long-term costs? 
	You might also consider questions about intangible benefits. These are gains that are not quantifiable, such as:

    Customer satisfaction. Will the project increase customer retention, causing them to spend more on the company’s products or services? 

    Employee satisfaction. Is the project likely to improve employee morale, reducing turnover? 

    Employee productivity. Will the project reduce employee’s overtime hours, saving the company money?

    Brand perception. Is the project likely to improve the company’s brand perception and recognition, attracting more customers or providing a competitive advantage?
	```
* Project 4: Python 
* Project 5: Django for WP Dev 
* Extras N/A
<br>

## 🌱 R5D6 2026-06-15 
* Project 3:  Pushing to finish the first course this week. 
Absolutely! Here's a concise outline of the main topics and key definitions from the "Foundations of Project Management" course module that will help you review effectively:

1. **Project Management Basics**
   - Definition of Project Management: The process of initiating, planning, executing, and closing projects to achieve specific goals.
   - What Constitutes a Project: Temporary endeavor with a defined beginning and end, aimed at creating a unique product, service, or result.

2. **Project Manager Roles and Responsibilities**
   - Leading and coordinating teams.
   - Planning and managing resources, timelines, and budgets.
   - Communicating with stakeholders.
   - Managing risks and changes.

3. **Project Life Cycle Phases**
   - Initiating: Defining project goals, scope, and obtaining approval.
   - Planning: Creating timelines, budgets, and task assignments.
   - Executing: Carrying out the project plan and managing the team.
   - Closing: Finalizing deliverables, evaluating outcomes, and celebrating success.

4. **Project Management Methodologies**
   - Waterfall: Sequential, linear phases where each phase must be completed before the next begins.
   - Agile: Iterative and flexible, allowing overlapping tasks and adapting to changes.
   - Lean Six Sigma: Focuses on quality improvement through defined phases (Define, Measure, Analyze, Improve, Control).

5. **Organizational Structure and Culture**
   - How company structure and culture impact project management approaches and communication.

6. **Change Management**
   - Managing changes in project scope, timelines, and resources effectively.

7. **Use of Generative AI in Project Management**
   - Emerging tools and techniques to enhance project planning and execution.

I recommend revisiting the course sections titled "The project management life cycle and methodologies" and "Organizational structure and culture" for detailed explanations.

Does this overview help you focus your review? Would you like to start practicing with some questions now?

   Most common: use IF conditional and the syntax is if condition: statement 
```Python
    # if condition: statement 
if 5>6: print ('yeah!')
   #output of running the above statement is nothing because five is not greater than six. 
if 5<6: print ('yay')
   # the output of running this statement will produce "yay" 
# else statement (branch, clause) 

if 5>6: print('yah!') 
else: print('boo') 
#running this we get the out put of boo because 5 is not greater than six. note the else only runs when the first statement is false. 
```
continuing if we need more outcomes or checks we can use an elif 

```
In addition to IF and Else: you can also use an elif to add criteria.  

The syntax of an if...elif....else statement is: 

if condition:
	statements
elif contition2: 
	statements 
elif conition 3:
	statements (as many as you need) 
else: statements 

```python
# ask the user to enter a number

number = int(input("Please enter a number between 1 and 10: "))

# Series of if ... elif ... else to respond based on the number the user entered 

if number == 10:
		print("High roller!") 
elif number >= 8: 
		print("You like your numbers high!")
elif number >-4:
		print("A middle of the road person, huh?")
elif number == 0: 
		print("I see you cannot follow directions.  Goodbye!") 
else:
		print("Keeping it small, I like it!")
#save this program as conditionalcode1.py
#now switch to command line and type python 3 conditionalcode1.py

# you will see the "Please enter a numb4eer between 1 and 10: " prompt.  You can enter numbers and test output. 
# as a trouble shooting tip be sure they are in the CORRECT order as if you reversed the order--4, then 8, then 10 it wouldn't work 
# BEST PRACTICES always test all possible outcomes to make sure you have things in the right order when using elif statements 
```
Nested If Statements also work for those who don't follow instructions.  Here is an example: 

```Python
# ask the user to enter a number

number = int(input("Please enter a number between 1 and 10: "))

if number == 0:
		print("I see you cannot follow directions.  Goodbye!") 

	elif number == 10:
## :seedling: R5D5 2026-06-14 :walking: leg working, cardio, long walk, and stretching :sleeping: A+ :fork_and_knife: refueling for next week's meal plans
* Project 1: GIT
* Project 2: Learning - Key concepts studied included Transfer, chunks, like ribbons, use of metaphors and LLM to generate useful metaphors for learning outcomes. Neurons=fundamental building blocks of learning. Tent, tent poles as a metaphor which also shows us good fit (where the poles are) and poor fit (where the tent is still flat)  Tip: prompt an LLM for a metaphor for any concept which is difficult to retain. Avoid overlearning. This part of the course is a lot like AI training & concepts. Einstellung = mindset. Interleaving different techniques.  I finished Module 2.  

* Project 3: PM - two parent methodologies: Six Sigma and Lean.  These methods are common in projects where the goal is to improve quality, move through processes quickly, save money.  They focus on team collaboration. Value the team and motivation  and productivity increase. 

1. Positive Work Environment
2. Team Collaboration 
3.  Move quickly through processes
4. Improve quality 
5. Save money. 

Five Phases in the Lean Six Sigma Approach 
1. Define - the project goal and what it will take to meet it. 
2. Measure - how the current process is working.  this focuses on data. map it out. what's going on and find the facts. how will you get the data and how often will you get it  
3. Analyze - being to identify gaps and issues.  data analysis is important to and for PMs 
4. Improve - make improvements after studying the previous steps 
5. Control - implement it.  learn from the work you did to update new processes and keep them in place 

Ideal methodology when you need to improve the current process to fix complex or high risk problems, improving sales, conversions, or eliminating bottleneck(s), 

Lean originated in the manufacturing world.  It focused on removing waste within an operation. Today, the Lean Manufacturing methodology recognizes eight types of waste within an operation: defects, excess processing, overproduction, waiting, inventory, transportation, motion, and non-utilized talent. In the manufacturing industry, these types of waste are often attributed to issues such as: 

*    Lack of proper documentation

*    Lack of process standards

*    Not understanding the customers’ needs

*    Lack of effective communication

*    Lack of process control

*    Inefficient process design

*    Failures of management 

The LEAN methodology has the 5-Ss as a its main tool.  They stand for five pillars or steps: 

1. Sort
2. Set in Order 
3. Shine 
4. Standardize 
5. Sustain. 

KANBAN - scheduling system, visualization tool, optimize work flow, TO DO, in progr4ess, testing, done. 

SIX SIGMA

The seven key principles of Six Sigma are:

*    Always focus on the customer.

*    Identify and understand how the work gets done. Understand how work really happens.

*    Make your processes flow smoothly.

*    Reduce waste and concentrate on value.

*    Stop defects by removing variation.

*    Involve and collaborate with your team.

*    Approach improvement activity in a systematic way.

Use this methodology to find aspects of the product or process that are measurable like time, cost, or quantity. Then inspect that measurable item and reject any products that do not meet the Six Sigma standard. Any process that created unacceptable products has to be improved upon. 

Lean Six Sigma 

After both Lean and Six Sigma were put into practice, it was discovered that the two methodologies could be combined to increase benefits

Waterfall is a traditional methodology in which tasks and phases are completed in a linear, sequential manner, and each stage of the project must be completed before the next begins. The project manager is responsible for prioritizing and assigning tasks to team members. In Waterfall, the criteria used to measure quality is clearly defined at the beginning of the project.

Agile involves short phases of collaborative, iterative work with frequent testing and regularly-implemented improvements. Some phases and tasks happen at the same time as others. In Agile projects, teams share responsibility for managing their own work. Scrum and Kanban are examples of Agile frameworks, which are specific development approaches based on the Agile philosophy.

Scrum is an Agile framework that focuses on developing, delivering, and sustaining complex projects and products through collaboration, accountability, and an iterative process. Work is completed by small, cross-functional teams led by a Scrum Master and is divided into short Sprints with a set list of deliverables.

Kanban is a tool used in both Agile and Lean approaches that provides visual feedback about the status of the work in progress through the use of Kanban boards or charts. With Kanban, project managers use sticky notes or note cards on a physical or digital Kanban board to represent the team’s tasks with categories like “To do,” “In progress,” and “Done.”

Lean uses the 5S quality tool to eliminate eight areas of waste, save money, improve quality, and streamline processes. Lean’s principles state that you can do more with less by addressing dysfunctions that create waste. Lean implements a Kanban scheduling system to manage production.

Six Sigma involves reducing variations by ensuring that quality processes are followed every time. The Six Sigma method follows a process-improvement approach called DMAIC, which stands for define, measure, analyze, improve, and control.

Lean Six Sigma is a combination of Lean and Six Sigma approaches. It is often used in projects that aim to save money, improve quality, and move through processes quickly. Lean Six Sigma is also ideal for solving complex or high-risk problems. The 5S organization framework, the DMAIC process, and the use of Kanban boards are all components of this approach. 


* Project 4: Python 
* Project 5: Django for WP Dev 
* Extras N/A freeCodeCamp Spanish Alphabet Practice 
<br>


:seedling: R5D4 2026-06-13 :walking: :sleeping: :fork_and_knife:
* Project 1: GIT - Reviewed. 
* Project 2: Learning - It is hard to learn when you are not interested.  Neuromodulator encode the importance, not the content.  Why, neurotransmitters:  
1. acetylcholine - particularly important to focused learning.  Synaptic plasticity, creating new long term memory.  form neuromodulatory connections. 
2. dopamine - chemical substance which controls motivation, at the brain stem, reward learning, basal ganglia (unexpected reward), predicting future rewards too, addictive drugs fool this proceeds and highjacks free will. anhedonia-loss of dopamine neurons, Parkinson disease, catatonia. Unconscious brain 
3. serotonin -impacts social life. Linked to risk taking behavior.  Low serotonin equal anti social behaviors, even crime.
Amygdala-almond shaped, at the base of the brain, major center of cognition and emotions are integrated and is a part of the limbic system and with the hippocampus.  Prozac is prescribed to increase serotonin and thereby treat clinic depression.  Diffuse neuromodulatory system. 
Visit brainfacts.org to learn more. 

* Project 3: PM - Working in Module 3:  Understanding the Project Life Cycle, Analyzing the different Project Phases, Comparing Waterfall and Agile approaches to PM as distinct methodologies. 

* Project 4: Python - Today's course materials looked at "Arithmetic Operators".  Python and SQL are the same when it comes to arithmetic operators.  NOTE: it doesn't care about the spaces (x+y) is the same results as (x + y).  I finished the Basic Syntax section of the course and passed the exam scoring 100%. 
```
Addition: 
print(5+4)
Subtraction: 
print(5-4)
Multiplication: 
print(5*4)
Division:
print(20/4) #note this outputs a decimal 5.0 because division is always a float data type
Modulo (returns just the remainder)
print(21%4) (output is just the remainder so it is 1) 

Unlike SQL, Python also has integer division.  It divides the first number evenly by the second, and gets rid of any remainders. 
print(21//4) (this comes back as the integer 5) 

Exponents are a **
print(3**2) (gives us the outcome if 9) 

Order of Operations: 
Python always reads the equation from LEFT to Right for each line.  
it does this order: 
**
* / // % 
+ _ 

Example: 
print(3+4*5) is going to multiple 4x5=20 then add 20+3=23 

Just like in math, we can use parenthesis to override Python's normal order of operations when needed. 

Example:
print((3+4)*5) produces 3+4=7 and 7*5=35

```
Module 1: Completed. To my delight the exam for this module didn't just ask multiple choice questions but actually included typing script!  I scored 10)% on the testing. 

* Project 5: Django for WP Dev - Review 
* Extras N/A  FreeCodeCamp's Spanish constants section. abecedario Server maintenance.  Website updates for WordPress. 
<br>

Next:  A lab to install a virtual box and installing ubuntu so we can create a python script. 

```
# Open Terminal Prompt in a virtual machine 
# type gedit myscript.py and hit enter
# type gedit myscript.py and hit enter to add the shebang
# type  #!/usr/bin/env python3 and hit Enter twice.

#add a statement to welcome the user. 
#!/usr/bin/env python3

print('Welcome to the age calculator.')
answer = input('Would you like to know how old you will be in a particular year?')

year = input('What year were you born?')
future = input('What year did you want to know about?')

age = int(future) - int(year)

print('In the year ', future, 'you will be ', age, ' years old.')
print('Goodbye!') 

# In the command line type python3 myscript.py and hit Enter. 
# Answer the promptes, hitting Enter after each answer.  
```

## :seedling: R5D3 2026-06-12  :walking: Core WO + Cardio :sleeping: Great! :fork_and_knife: nutritious salad today 
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
