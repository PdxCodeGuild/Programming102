# Unit 2 Practice

## Exercise 3 - Password Generator

Let's create a password generator. This will be just like the **[Password Generator](https://github.com/PdxCodeGuild/Programming101/blob/master/labs/password_generator.md)** from *Programming 101*, except this time we will write some functions to execute some of the repeated logic.

### **3.1**

Define a function called `generate_password()`. 

The function will require one parameter representing the desired length of the password and will `return` a ten-character password. 

The character pool from which the ten characters are selected should contain uppercase letters, lowercase letters, digits (0-9) and some kind of special characters.

**Output**

    Your password: 
    LV!uvg2mu5

### **3.2**

Allow the user to choose the number of characters they want in their password. Require a minimum of 8. 

If the user enters less than 8 for the character count, display a message and tell them they need at least 8 characters.

**Output**

    Enter desired password length: 6

    ** Your password must be at least 8 characters long **

    Enter desired password length: 15

    Your password:
    
### **3.3**

Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using `list()`, `random.shuffle()`, and `''.join()`.

Your function might require an additional parameter in this version.
    
**Output**

    Number of letters: 2
    Number of digits: 2
    Number of special characters: 2

    ** Your password must be at least 8 characters long **

    Number of letters: 6
    Number of digits: 10
    Number of special characters: 5

    Your password:
    68P?Z3036*02@Xl!$b35b

No [**solution**](solutions/exercise_3_solution.md) provided because this is a 101 lab.

---

## [< Exercise 2](exercise_2.md) | [Exercise 4 >](exercise_4.md) 

### [<< Back to Unit 2 Practice](/practice/unit_2/)