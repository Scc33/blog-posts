## What is Integration Testing?

## Background

[Integration testing](https://en.wikipedia.org/wiki/Integration_testing), also known as integration and testing, is the next step up from [unit testing](https://blog.seancoughlin.me/what-is-a-unit-test). 

In unit testing, individual chunks of software are verified. Whereas, integration testing checks multiple components for correctness.

The goal of integration testing is to confirm software works in a group.

Integration testing makes common use of [stubs and drives](https://www.geeksforgeeks.org/difference-between-stubs-and-drivers/). 

- A stub is a *fake called program*, it allows for the testing of the program calling the stub. 
- A driver is a *fake caller program*, it allows for the testing of the program called by the driver.

## Approaches to Integration Testing

There are [four main approaches to integration testing](https://www.geeksforgeeks.org/software-engineering-integration-testing/).

- Big-bang: all the software modules are created and combined at once.
- [Bottom-up](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design#Programming): low-level components are tested by using drivers before high-level components.
- [Top-down](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design#Programming): first high-level modules are tested by using stubs before low-level components.
- Mix-integration (aka sandwich testing): a combination of the bottom-up and top-down approaches.

## Advantage

- Integration testing is an important way of verifying that larger chunks of code and services work together as intended. 

## Disadvantage

- Integration testing often requires a significant amount of extra code in the form of stubs and drivers to be written.

## Further Reading

Integration tests are just one kind of testing. [My series on software testing and its methods](https://blog.seancoughlin.me/series/software-testing) covers many other testing variations.