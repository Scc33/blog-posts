## What is TDD?

Test-driven development, or TDD, is a programming style. TDD focuses on improving code by focusing on writing tests first. This is the opposite of typical software development. In most cases, the software is developed first, and test cases are created later.

## The Rules of TDD

The general principle follows just three steps:
1. Write one unit test describing an aspect of the program. The test should fail upon running because the program lacks the needed feature.
2. Write the minimal amount of code possible that will solve the test. The goal should be to keep things simple. We only need to make the test pass.
3. Refactor if necessary to reduce duplicate code or improve quality. Then continue on to repeat the process.

## Benefits of Test-Driven Development

- Test coverage is extremely high because code is written to make test cases pass. This ensures good code quality and keeps defects to a minimum.
- Writing only the very basics to make a test pass keeps code simple and the design cleaner.
- Defects are caught earlier because the test cases are already written.

## Cons of TDD

- TDD is a design pattern, so teams can implement TDD differently. Even within teams developers can have various levels of adherence to the principles.
- TDD can lead to an over-focus on small code chunks and less focus on wider functionality tests.
- Testing becomes part of the project and maintenance can be high if tests are written too rigidly.

## Further Reading

TDD is closely related to [ATDD](https://en.wikipedia.org/wiki/Acceptance_test–driven_development) or acceptance test-driven development and [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) or behavior-driven development.