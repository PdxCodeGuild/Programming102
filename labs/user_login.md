# <a id="top"></a>Lab 5 - User Login

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)

Create a REPL which allows a user to 'login'. 

### **5.1**

- Create a dictionary called `user_profile`

    The `user_profile` should contain **key : value** pairs for:

    - `username`
    - `password`


- Define a function called `login()` which will have parameters for:
  -  `username`
  -  `password`

    The `login()` function will `return True` if the values passed to the function for `username` and `password` match the values for `username` and `password` found in the `profile`. 
    
    If the credentials don't match those in the `profile`, the `login()` function will `return False`

- Create variables for a `username` and `password` which will emulate a user's login attempt. 

- Pass the `username` and `password` to `login()` and tell the user whether their login attempt was successful.

Output:
    
    profile:
        username: gandalfTheGrey
        password: noneShallPass!


    # successful login
    username: gandalfTheGrey
    password: noneShallPass!

    Welcome, gandalfTheGrey!

    # unsuccessful login
    username: gandalfTheGrey
    password: myPrecious?

    Error! Your username or password was incorrect!

### **5.2**

Create a REPL that asks the user for their `username` and `password` and attempts to log them in. 

If their login is **successful**, print a welcome message and end the program.

If their login is **unsuccessful**, ask if they'd like to try again.

### **5.3**

Allow the user three attempts to login. If they exceed three attempts without a successful login, tell the user and end the program

Output:

    username: gandalfTheGrey
    password: myPrecious?

    Error! Your username or password was incorrect!

    Enter 'y' to try again, 'n' to quit: y

    You have 2 login attempts remaining...

    username: gandalfTheGrey
    password: foolOfATook!

    Error! Your username or password was incorrect!

    Enter 'y' to try again, 'n' to quit: y

    You have 1 login attempts remaining...

    username: gandalfTheGrey
    password: bilboBaggins!

    Error! Your username or password was incorrect!

    Your login has been unsuccessful three times! Try again later. Goodbye!


### **5.4 - Advanced**

Add support for **multiple** users.

A few things will need to change:

- Instead of one `profile`, you will need a ***list*** of `profiles`, which will be a **list** of `profile` **dictionaries**. Each dictionary will represent a `profile` and will contain **key : value** pairs for `username` and `password`.
  
- The `login()` function will need a parameter called `profile` to receive each `profile` as we loop through `profiles`.

- Define a function called `user_exists()` which will:
  - loop through each `profile` in the `profiles` list
  - check to see if the `username` the user entered already exists within one of the `profile` dictionaries.
  - if the user already exists, `return True` otherwise, `return False`

- Define a function called `create_user()` which:
  -  prompts the user for a `username` and `password`. 
  -  checks to see if the `username` already exists in the `profiles` list using the  `user_exists()` function
  -  If the `username` is unique and doesn't appear in the `profiles` list, `.append()` it to the `profiles` list. 

- The `login()` function will now:
  -  take in the list of `profiles` instead of just one `profile`.
  
  - need to loop through each `profile` in the `profiles` list and check the `username` and `password` against the `username` and `password` for each `profile` until one matches.
  
  - If no `profile` is found whose `username` and `password` match those provided by the user, the login is unsucessful, `return False`. Otherwise, `return True`

- Integrate the `create_user()` function into your REPL to allow the user to create a new username. 

---

Profiles list:
    
    username: gandalfTheGrey
    password: noneShallPass!

    username: bilboBaggins
    password: theShire123

    username: iAmSmeagol
    password: myPrecious!

    
Output:

    Welcome! 
    
    Please select from the following options:

        1. Create user
        2. Login

    Enter the number of your choice: 1

    Create User
    -----------
        Enter your new username: gandalfTheGrey

        That username already exists!

        Enter your new username:
        mrSamwise

        Enter your password: 
        frodoIsMyFriend

    Thanks for signing up, mrSamwise!

    Please select from the following options:

    1. Create user
    2. Login

    Enter the number of your choice: 2

    Login:
    ------

        username: smaugTheDragon
        password: gimmeYerGold!

        Error! Your username or password was incorrect!

    Enter 'y' to try again, 'n' to quit: y

    You have 2 login attempts remaining...

        username: iAmSmeagol
        password: myPrecious!

    Welcome, iAmSmeagol!

---

[Back to Syllabus](https://github.com/PdxCodeGuild/Programming102#top)