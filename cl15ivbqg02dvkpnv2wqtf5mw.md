## What are Microservices?

[Microservices](https://en.wikipedia.org/wiki/Microservices) are a type of software engineering architecture. They are the stand-in replacement for the older architecture known as monolithic.

### The problem with monoliths

A monolith is where one codebase contains the entire program. Since the whole program is within one codebase, it often follows one specific stack and accesses only one database.

This architecture can work well for individuals or small teams. However, as the amount of code grows, it can quickly become hard for teams to coordinate development. Deployment and testing are also a challenge. Even small changes require the entire application to be rebuilt and redeployed.

Monolith's drawbacks are fixable by changing architectural strategies and creating microservices.

## Microservices
A microservice is a style of architecture where independently deployable codebases work together to form an application.

### A microservices analogy

Say I want to build a cube. I want my cube to be of a specific size and shape. Making a small cube is probably trivial, but what if I need a 100-meter by 100-meter cube. That large size will be difficult to manufacture or transport. Instead of creating one solid piece, I could take a bunch of smaller cubes and put them together. All these smaller cubes put together would look like a Rubik's cube.

Now let's apply our analogy to programming. It would be trivial to build a simple website, but what if that website is Google? That is an enormously challenging problem. We can simplify the problem by breaking it into smaller pieces.

One of our smaller blocks could handle searching. One block could form the user interface, and one could show advertising, etc. Each of these smaller blocks is called a microservice. While this is a simplified idea of how a complex service like Google operates, the general principle is the same.

### Benefits of microservices
1. Small services are easier to understand and can be owned by a single team. They can also be rewritten quickly if technologies change.
2. Microservices offer more flexibility because you can choose the right tool for each problem and adopt new technologies as required.
3. Deploying is lower risk and faster because microservices don't share codebases making them independently deployable. 
4. Scaling is easier and overall the architecture is more adaptable which benefits agile development.

### Drawbacks of microservices
1. Separately monitoring every microservice is challenging. Additional software is required to centralize logs and monitoring.
2. Setting new developers up to work on the application could be difficult because there are multiple codebases to work on.
3. Deploying and testing will likely require more automation because there are more points of failure.

### More to learn
This article is just an overview of microservices. There is so [much more to learn](https://www.ibm.com/cloud/learn/microservices): hosting options, messaging buses, securing network calls, API gateways, and more are all great topics to look into if you are interested in applying microservices to your next project.