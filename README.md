# Errors-and-exceptions
# Python Errors & Exceptions — Practice

This repository contains my practical exercises and experiments while learning **Errors and Exceptions in Python**.

The goal of this practice is to understand how Python handles errors and how to write programs that can deal with unexpected situations safely and clearly.

## Topics Covered

* `try`
* `except`
* `else`
* `finally`
* Handling specific exceptions
* `ZeroDivisionError`
* `TypeError`
* `ValueError`
* Raising exceptions with `raise`
* Writing functions with error handling
* Testing different error scenarios
* Understanding the difference between errors and exceptions

## Practice Approach

I am solving these exercises step by step while learning Python.

Some exercises are completed independently, while others are discussed and reviewed to improve my understanding of **why the code works**, not just how to make it work.

The focus is on:

* Understanding the cause of an exception
* Choosing the appropriate exception to handle
* Writing clean and readable error-handling code
* Testing functions with valid and invalid inputs
* Learning from mistakes and debugging problems

## Example

One of the exercises is a safe division function:

```python
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid Type"
    return result
```

The function is tested with different inputs to understand how Python handles successful operations and exceptions.

## Purpose

This repository is part of my ongoing journey to become a stronger **Python developer** through consistent practice, problem solving, and building projects.

> Learn → Practice → Make mistakes → Debug → Understand → Improve

## Technologies

* Python 3
* Git
* GitHub

---

**Learning in progress 🚀**
