# User Guide: Python Exercises for Beginners

Welcome to the Python Exercises app! This application is designed to help you practice your Python skills by working through 42 increasingly challenging exercises. 

This guide will walk you through how to use the app effectively.

## The App Layout

When you open the app, you will see a few distinct areas:

*   **Left Sidebar (Exercises):** This is your navigation pane. You can select unlocked exercises here. It also tracks your progress, lets you switch visual themes (Light/Dark/System), and gives you the option to reset your progress.
*   **Top Bar:** Displays the current exercise title, your completion status for it, and **Previous/Next** navigation buttons.
*   **Left Panel (Description & Validation):**
    *   **Description:** Explains the objective of the current exercise and the rules you must follow.
    *   **Expected Output / Validation:** Explains *how* the app will test your code when you click Submit.
*   **Right Panel (Code & Console):**
    *   **Code Editor:** Where you write your Python code.
    *   **Output Console:** Where the results of your code (and the results of the automated tests) are printed.
    *   **Program Input:** A small box used only for exercises that require `input()` from the user.

---

## Writing and Testing Your Code

When you start a new exercise, you will see a template in the Code Editor that looks like this:

```python
# Exercise #1: Hello, World!
# Prerequisites: print(), strings, string concatenation

# --- SOLUTION CODE ---
# Write your exercise solution below. This is what gets evaluated
# when you click 'Submit'.



# --- TESTING CODE ---
# Write any code you want to manually test below this line.
# This section is run when you click 'Run', but is completely
# ignored by the 'Submit' validation.
```

### The Difference Between Run and Submit

It is very important to understand the two sections in your editor!

#### 1. The `--- SOLUTION CODE ---` Section
This top section is where you should define the actual functions or core logic requested by the exercise description. 

When you click the **Submit** button (the green checkmark), the app takes the code from this top section and runs a battery of automated tests against it to verify your logic is correct.

#### 2. The `--- TESTING CODE ---` Section
As a programmer, you will constantly need to "test" your functions by calling them with various inputs and `print()`-ing the results to see if they work before you actually submit them for grading. This is what the bottom section is for!

When you click the **Run** button (the blue play button), the app executes **everything** in the editor—both your functions at the top, and your manual testing calls at the bottom. 

*Crucially, whatever you put in the `TESTING CODE` section is completely ignored when you click **Submit**.* This prevents your manual `print()` statements from confusing the automated grader. 

### Example Workflow

Let's say an exercise asks you to write an `is_even(number)` function.

**1. Write the logic in the top:**
```python
# --- SOLUTION CODE ---
def is_even(number):
    return number % 2 == 0
```

**2. Test it yourself in the bottom:**
```python
# --- TESTING CODE ---
print("Testing 4 (should be True):", is_even(4))
print("Testing 7 (should be False):", is_even(7))
```

**3. Test it!**
Click **Run**. You will see your test print statements in the console. If they look correct, you are ready to validate.

**4. Validate it!**
Click **Submit**. The app ignores your two `print()` statements, takes your `is_even` function, runs its internal tests, and marks the exercise complete!

---

## Hints and Solutions

If you get stuck on an exercise, don't worry!

*   **Hints:** Click the **💡 Hint** button above the code editor to see the first few lines of the official solution. This is often enough to point you in the right direction without giving away the whole answer.
*   **Solutions:** After you successfully complete an exercise, the **🔑 Solution** button unlocks. Clicking this opens a side-by-side comparison of the code you wrote versus the reference solution written by the book's author, Al Sweigart. Comparing solutions is an excellent way to learn new Python idioms!

---

Happy coding!
