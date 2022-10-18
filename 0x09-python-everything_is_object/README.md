0x09. Python - Everything is object
===================================

-   By Guillaume
-   Weight: 1
-   Project over - took place from 12-14-2021 to 12-15-2021 - you're done with 10% of tasks.
-   QA review fully automated.

#### In a nutshell...

-   **Auto QA review:** 0.0/94 mandatory & 0.0/59 optional
-   **Altogether:**  **0.0%**
    -   Mandatory: 0.0%
    -   Optional: 0.0%
    -   Calculation:  0.0% + (0.0% * 0.0%)  == **0.0%**

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)

Background Context
------------------

Now that we understand that everything is an object and have a little bit of knowledge, let's pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>

```

OK. But what about this?

```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>

```

![](https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif)

This project is a little bit different than the usual projects. The first part is only questions about Python's specificity like "What would be the result of...". You should **read all documentation first (as usual :))**, then take the time to **think and brainstorm with your peers** about what you think and why. **Try to do this without coding anything for a few hours**.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. **Don't go this route**. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It's important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types. The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.

Note that during interviews for Python positions, **you will most likely have to answer to these type of questions**.

All your answers should be only one line in a file. No space before or after the answer.

Resources
---------

**Read or watch**:

-   [9.10. Objects and values](https://alx-intranet.hbtn.io/rltoken/MrtBogRzYETxnSKG97E7Sg "9.10. Objects and values")
-   [9.11. Aliasing](https://alx-intranet.hbtn.io/rltoken/Ro-7kVXtmWyAeOXEw7RhSg "9.11. Aliasing")
-   [Immutable vs mutable types](https://alx-intranet.hbtn.io/rltoken/X1lEmkwQRWI3fP4W7bq_qw "Immutable vs mutable types")
-   [Mutation](https://alx-intranet.hbtn.io/rltoken/HpKOdgDg6GIoBoG0UPOgPA "Mutation") (*Only this chapter*)
-   [9.12. Cloning lists](https://alx-intranet.hbtn.io/rltoken/-Gi4PX4srBYFKpZ5Er6sqA "9.12. Cloning lists")
-   [Python tuples: immutable but potentially changing](https://alx-intranet.hbtn.io/rltoken/NZIom4L-tS0HjpY_uEVr9A "Python tuples: immutable but potentially changing")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/J02m-YVaLqu3rtRDGfg5NQ "explain to anyone"), **without the help of Google**:

### General

-   Why Python programming is awesome
-   What is an object
-   What is the difference between a class and an object or instance
-   What is the difference between immutable object and mutable object
-   What is a reference
-   What is an assignment
-   What is an alias
-   How to know if two variables are identical
-   How to know if two variables are linked to the same object
-   How to display the variable identifier (which is the memory address in the CPython implementation)
-   What is mutable and immutable
-   What are the built-in mutable types
-   What are the built-in immutable types
-   How does Python pass variables to functions

Requirements
------------

### Python Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version 2.7.*)*
-   All your files must be executable
-   The length of your files will be tested using `wc`

### `.txt` Answer Files

-   Only one line
-   No Shebang
-   All your files should end with a new line

More Info
---------

### Manual QA Review

**It is your responsibility to request a review for your blog from a peer before the project's deadline. If no peers have been reviewed, you should request a review from a TA or staff member.**

**Author:**
** Abdallah Mahmoud** [Abdallah](https://github.com/abdamah)
