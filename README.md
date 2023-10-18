Important libraries to run this test suite
    1. pytest [for creating pytest framework]
    2. pytes-xdist [To run test on multiple workers]
    3. selenium [To import Webdriver and automating webpages]
    4. pytest-html [To generate HTML reports]
    5. allure-pytest [To generate allure libraries]

Packages used in this framework for code re-usability and for better communition between test files and test supporting file
    1. TestCase [To store conftest file and test cases]
    2. PageObjects [To create separate Class for each page]
    3. Utilities [To store test case supporting files]

Folders used in this Framework
    1. Configuration [To Config.ini file to use common data across all test case ]
    2. Logs [To store log file]
    3. Reports [To store test reports]
    4. ScreenShots [To take screen shots for failed and passed test Cases]

Explanation
In TestCase package I have written all test cases for each functionality for which methods are already define in page objects class.Because whenever we want to make any changees our test cases will be untouched and changes will be implemented in page object classes  and wont disturb our test cases
 
In PageObjects package I have designed unique module and unique class for each page e.g. Login, Search by filter, Search by name and i have define methods for each action happens on that page . Implemented explicit wait code optimization and web elements to be located.
Designed a status checking method return a Boolean valu so i can use that for assertion in our test case to get the final result whether it gets pass or fail.
Also implemented error handling by using try and except block.

In Utilities package i have implemented all test case supporting files and assigned unique class for each so i can use each method for enhance my test cases.

Remark:
    I am pushing these files on github and sending you link so u can access it.