# Automated web page testing with Python and Selenium

This repository contains python 3.x code for an automated test of a 
website. Following UI automation best practices, 
Page Object Model and Page Factory design patterns were used in writing the tests.
This ensure a higher code readability, maintainability and it becomes easier
to extend or add more tests. 

## Code Structure

3 test suites were used to logically organize the code
 * Login Test Suite 
 * Booking Page Elements Suite
 * Booking Page Elements Validation Suite
 
*Login Test Suite* contains login-related positive and negative tests.
*Booking Page Elements Suite* checks that all the required elements
are displayed on the webpage and have correct labels. *Booking Page Elements Validation Suite* 
checks the validation error messages on the booking page.
Each test method starts with a word **test_** and corresponds to 
a test case in detailed set of test cases [in this Google Sheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vRZ5UyBDdKybkiYYee5QzL0lKlVrBpx6cYemh3yJZ9zfEuO__Qks4voNqGP8rq9tJR58lOV4_r0cTEi/pubhtml).

Using Page Objects the webpages are modeled as classes which allows
code reusability. A Page Object for each of the test suites 
are created. Another best practice used in the code is that there
are no *magic* values. All string constants like URL, mobile number 
and so on are stored in a separate file for an easier reference.

All tests were run locally with 100% 
<span style="color:green">*passed*</span> rate.