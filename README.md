# The Challenge

This is a programme to compute, given n number of iterations, how many widgets can be produced on a production line. See the end for a full description.


# Running the code, tests and working on the code

## Before doing anything:

* Clone this repository

* Set up and activate virtualenv with `virtualenv VENV` and `source VENV/bin/activate`

* Install requirements with `pip install -r requirements.txt`

## Running the tests

``pytest``

## Running the application

`python main.py n` where n is the number of iterations. This will print the number of widgets produced in the number of iterations.

## Assumptions

A widget is only counted if it reaches the end of the conveyor belt

The second member of a pair will only perform an action if the first member cannot act on that tick

If a worker can perform an action, they will. This means that the first pair will always be the busiest pair, and subsequent pairs will only be used when the first pair cannot perform an action.

# Structure and approach

In completing this challenge, I stuck to principles of :

* TDD
* OOD

The programme is tested with pytest, test files are prefixes with 'test_'

The programme is split into three classes, with roughly single responsibilities:

* **Worker** - stores components and produces widgets when sufficient components
* **Assembly line** - manages the components  and widgets on the conveyor belt, and tracks the number of widgets which have made it to the end of the conveyor
* **Task manager** - the bulk of the logic. Instructs workers to take components, or place widgets on the conveyor. Updates time at each iteration.

In addition, there is a **'main'** file which runs the programme overall (see below for running instructions).


## Appendix - Description of the challenge

The production line is centered around a conveyor length (with a default length of 3), and a number of worker pairs equal to the length of the conveyor.

At each 'tick' of time, the belt moves forward by one. New elements ('A' and 'B') are randomly generated. A worker can take a component, but only one worker of each pair can touch the conveyor belt in any one tick.
Once a worker has both components, they assemble a widget in four ticks and can place the widget on the conveyor belt at the next empty slot.
