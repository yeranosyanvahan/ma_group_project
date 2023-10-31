# Table of Contents

1. [Milestone 1](#milestone-1--2oct-13oct)
2. [Milestone 2](#milestone-2--16oct-27oct)
3. [Milestone 3](#milestone-3--30oct-10nov)
<!-- 3. [Subsection 1.1](#subsection-1-1)
4. [Section 2](#section-2)
5. [Conclusion](#conclusion) -->

# Feedback | Group 5

## Milestone 1 | 2Oct-13Oct

1. **Define the problem: ** <span style='color:green'>done</span>
    - Well defined!
2. **Finalizing roles:** <span style='color:green'>done</span>
3. **Create a product roadmap and prioritize functionality (items)** <span style='color:orange'>partially done</span>
    - In the roadmap, I found the term dashboard a couple of times. Are you going to build a dashboard?
    - We have an API developer Db developer, while you have mentioned Back-End and Front-End
    - there is a need to fix this (I have posted tasks for Milestone 2 you can use them as well)
4. **Creating the GitHub repository included readme.md and .gitignore (for Python) files:** <span style='color:green'>done</span>
5. Create a virtual environment in the above repo and generate requirements.txt (venv must be ignored in git) <span style='color:green'>done</span>
6. Push *point 1, point 3, point 5 (requirements.txt).<span style='color:green'>done</span>
7. Complete the first chapter of  Developing Python Packages <span style='color:green'>completed by everyone</span>
9. Create a private Slack channel in our Workspace and name it Group-{number} <span style='color:green'>done</span>
10. Schedule a call with me and Garo or come during office hours. <span style='color:green'>done</span>


Continue, according to the roadmap and also add the tasks for milestone 2 required by me,

**Grade:** 8/10 
Good job!


# Milestone 2 | 16Oct-27Oct

## Fixes From the Milestone 1

Fixes were note required!

## Milestone 2

**Overall you did an excellent job!**

Inside of the  package you cannot have `ipynb` (data_generator.ipynb) files

1. **DB developer:**
    - Design the database using Star schema (provide ERD): <span style='color:green'>done</span>
    - Insert Sample to data <span style='color:green'>done</span>
3. **Data Scientist:**
    - Complete data generation/acquisition/research: <span style='color:green'>done</span>
    - Select data from DB: <span style='color:green'>done</span>
    - Insert data to DB: <span style='color:green'>done</span>
4. **API developer:**
    - Select data from DB <span style='color:green'>done</span>
    - Insert data to DB <span style='color:green'>done</span>
    - Update data in DB <span style='color:green'>done</span>
    - <span style='color:orange'>I would recommend  using `SQLHandler()` for crud, in order to avoid redundant functions.</span>
5. Finish the second chapter of Datacamp course <span style='color:green'>done by everyone</span>
6. Finalize file/folder structure: relative imports must work properly <span style='color:green'>done, just remove notebook file</span>
    - docs folder: putting all the documents there <span style='color:red'>done</span>
    - models folder: putting modeling-related classes, functions <span style='color:red'>done</span>
    - api folder: api related stuff <span style='color:red'>done</span>
    - db folder: db related stuff <span style='color:red'>done</span>
    - initialize `__init__.py` files accordingly (see Datacamp assignment chapter 1 and chapter 2) <span style='color:red'>done</span>
    - logger folder: I will provide this module <span style='color:green'>done, try to use them in your py files</span>
    - <span style='color:red'>`basic_clv.py, convert.ipynb,model.py` must be out of the package, in your case out of CLV folder </span>



*I can see multiple contributors!*  

**Grade:** 20/20 


# Milestone 3 | 30Oct-10Nov



1. Finish the **third** chapter of Datacamp course (please complete only the 3rd one)
2. **API Developer:** 
    - Create a `run.py` file for an API (find the minimum workable example [here](https://github.com/hovhannisyan91/fastapi)). <span style='color:green'>You have already done this</span>
    - Test it on swagger <span style='color:green'>You have already done this</span>
    - following request types must be available to test (GET, POST, PUT), will provide more details on Friday. <span style='color:green'>You have already done this</span>
3. **DB developer:** <span style='color:green'>You have already done this, complete all the methods</span>
    - complete/fix the methods from `SQLHandler()` class 
    - finalize the documentation for `schema.py` by using `pyment` package
    - finalize the documentation for `SQLHandler()` by using `pyment` package
4. **Data Scientist:** start working on modeling part, by selecting the date from SQL DB
    - we just need to run sample model and store the output to sql
5. **Product Manager**
    - since you have partially done 1-3 points, concentrate on the application scenario 





