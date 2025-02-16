An academic project divided into two blocks: irap_management contains the code in its most extensive version, while db_integration is a lite version focused on integrating with a database (DBB) using Flask.

# How to use IRAP-Calculator

## Part 1: irap_management

The **irap_management** folder contains the main program for managing the calculation of IRAP for businesses.

To fully understand how the program works and learn how to use it, please refer to the associated **Readme** file.

### Running the program

Follow these steps to run the program:

1. **Navigate to the project folder:**
$ cd irap_management

2. **Create a virtual environment:**

Use the **venv** module to create an isolated virtual environment for the project.
$ python3 -m venv .venv

3. **Activate the virtual environment:**

    -Linux/MacOS:
    ```
    $ source .venv/bin/activate
    ```
    -Windows:
    ```
    $ .venv\Scripts\activate
    ```
    If the command doesn't work, you may need to run the following command first:
    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    Then, run the command again to activate the virtual environment:
    ```
    $ .venv\Scripts\activate
    ```

### **NB: Make sure the virtual environment has been activated correctly, otherwise proceed with manual selection**

4. **Install dependencies:**

Use **pip** to install the necessary dependencies listed in the **requirements.txt** file.
$ pip3 install -r requirements.txt

### **NB: Make sure you are inside the irap_management directory so that the code correctly reads the imprese.txt file**

## Part 2: db_integration

The **db_integration** folder contains a lite version of the program for data integration with the database.

To fully understand how the program works and learn how to use it, please refer to the associated **Readme** file.

### Running the program

Follow these steps to run the program:

1. **Navigate to the project folder:**
$ cd db_integration

2. **Create the virtual environment and install the dependencies as explained above**
