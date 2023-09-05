## What is a unit test?

## Unit Testing Background

**Tl;dr**: a unit test is code that tests other code. 

[Unit tests](https://en.wikipedia.org/wiki/Unit_testing) are the smallest type of software testing. They are meant to verify that a single piece of code is working as intended. Unit testing is typically automated, and developers run tests as part of the development process to make sure everything is working appropriately.

Unit tests are commonly run on every build or change to the codebase.

Unit testing can fall into the category of [TDD or test-driven development](https://blog.seancoughlin.me/what-is-tdd). TDD is a common method in [extreme programming](https://en.wikipedia.org/wiki/Extreme_programming) and [agile](https://en.wikipedia.org/wiki/Agile_software_development) where unit tests are written before the code.

Unit tests can sometimes be difficult to write because code often relies on outside components. In these cases, [stubbing](https://en.wikipedia.org/wiki/Method_stub) or [mocking](https://en.wikipedia.org/wiki/Mock_object) are common techniques to implement unit tests. 

## Unit Testing Frameworks

There are hundreds of testing frameworks in existence because unit testing is so common. Wikipedia maintains a [long list of testing frameworks](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks#C++) for many languages. Some of the most popular frameworks are [Junit](https://en.wikipedia.org/wiki/JUnit) for Java, <a href="https://en.wikipedia.org/wiki/Mocha_(JavaScript_framework)">Mocha</a> for JavaScript, and [PyTest](https://docs.pytest.org/en/7.1.x/) for Python. 

## Advantages

- Unit tests are small and typically quick to run. The speed makes them easier to check and hastens development.
- Unit testing can be helpful documentation because it shows how the code is properly used and can give insight into functionality.
- Developers can use unit tests as a helpful sanity check to make sure their code is working as intended and under many scenarios.

## Disadvantages

- Since unit tests are checking only small chunks of code, they cannot catch large errors that exist on the system level. Other testing methods like [integration tests](https://en.wikipedia.org/wiki/Integration_testing) are required for verifying the system behavior.
- Writing and maintaining unit tests can often be difficult because developers are focused on writing deliverable code for customers.
- Unit tests, like all testing, may not cover every edge case or may be incorrect. Therefore, relying too heavily on unit tests creates a false sense of security that the code is working as intended.

## Further Reading

Unit tests are just the first level of testing. More types of testing can be read about in [my series on software testing and its methods](https://blog.seancoughlin.me/series/software-testing).