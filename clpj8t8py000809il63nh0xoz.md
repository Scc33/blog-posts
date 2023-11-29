---
title: "Streamlining Your JavaScript Development with GitHub Actions for Continuous Integration"
datePublished: Wed Nov 29 2023 04:04:23 GMT+0000 (Coordinated Universal Time)
cuid: clpj8t8py000809il63nh0xoz
slug: streamlining-your-javascript-development-with-github-actions-for-continuous-integration
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1701229772998/4ddd7ce4-c6be-448a-ac03-f274635cb987.jpeg
tags: github, javascript, automation, github-actions, ci-cd

---

## Introduction

[Continuous Integration (CI)](https://en.wikipedia.org/wiki/Continuous_integration) has revolutionized web development. CI methodologies automate the integration of code changes, ensuring smooth collaboration and quality in software projects. They are common across production environments and open-source software.

### Common CI checks

In a typical Continuous Integration (CI) pipeline, several key tasks are routinely performed to ensure the quality and viability of the codebase.

These often include pulling the latest code changes, running automated tests to detect bugs or inconsistencies, and executing linting processes to maintain coding standards and style guidelines.

Additionally, CI pipelines usually involve building the application to verify that it compiles correctly and performing static code analysis to catch potential issues.

Advanced CI pipelines may also run security checks, code coverage analysis to assess test effectiveness, and automated performance testing to ensure the application runs efficiently.

By automating these tasks, CI pipelines play a crucial role in maintaining the health and stability of software projects, streamlining the development process, and allowing teams to deliver high-quality software efficiently.

### Why Continuous Integration?

The advantages of CI in web development include:

1. **Automated Testing:** Automatically runs tests on every commit.
    
2. **Immediate Feedback:** Quickly identifies issues for early resolution.
    
3. **Streamlined Workflow:** Automates build and deployment processes.
    
4. **Consistency:** Maintains coding standards across teams.
    
5. **Quality:** Keeps code commit quality high.
    

### What are GitHub Actions?

[GitHub Actions is a CI/CD](https://en.wikipedia.org/wiki/GitHub#Services) platform that automates your workflows directly within your GitHub repository. It enables you to automate your build, test, and deployment pipeline. You can create custom workflows using configurations stored in YAML files within your GitHub repositories.

## The CI Configuration File

For this configuration, I'm using my [personal site](https://github.com/Scc33/Scc33.github.io) as an example. It is a [Svelte application](https://svelte.dev), so some of these configurations are specific to Svelte.

The layout of my CI file is intended to cover only the basics of a Svelte application. You can customize these actions to your heart's desire.

1. **Workflow Triggers:**
    
    ```yaml
    name: CI
    
    on:
      workflow_dispatch:
      push:
        branches: [master]
      pull_request:
        branches: [master]
    ```
    
    * `workflow_dispatch`: Allows manual workflow execution. This is not strictly necessary, but I think it helps with debugging.
        
    * `push` and `pull_request`: Triggers the workflow on pushes and pull requests to the master branch. This can be configured to any branch name.
        
2. **Build Job:**
    
    ```yaml
    jobs:
      build:
        name: build-and-test
        runs-on: ubuntu-latest
    ```
    
    * Runs on `ubuntu-latest` which is simply the latest version of Ubuntu provided by GitHub.
        
    * The action is named `build-and-test`. Once again you can name the action whatever you please. However, the name will be important when creating [GitHub rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) if you choose to do so.
        
3. **Workflow Steps:**
    
    * **Checkout:**
        
        ```yaml
        - name: Checkout
          uses: actions/checkout@v2
        ```
        
        Checks out your project code. Uses the [checkout tool provided by GitHub](https://github.com/actions/checkout).
        
    * **Set up Node.js:**
        
        ```yaml
        - name: Set up Node.js
          uses: actions/setup-node@v1
          with:
            node-version: '20'
        ```
        
        Installs Node.js version 20 using the [Node tool provided by GitHub](https://github.com/actions/setup-node).
        
    * **Install Yarn:**
        
        ```yaml
        - name: Install Yarn
          run: npm install -g yarn
        ```
        
        Installs Yarn for package management. Yarn is my personal preference for package managers. You can use whatever package manager fits your fancy.
        
    * **Install Dependencies:**
        
        ```yaml
        - name: Install dependencies
          run: yarn install --frozen-lockfile
        ```
        
        Installs project dependencies based on a lockfile. Using the lockfile ensures consistency in the project dependencies.
        
    * **Build Application:**
        
        ```yaml
        - name: Build application
          run: yarn run build
        ```
        
        Builds the application. In my case, this is a pipeline for a Svelte application, so it would build the Svelte code into an output directory. I like to run the build step to ensure the project can be built successfully. A more advanced pipeline might take that build output, containerize it, and place it in an artifact manager. However, are staying simple with this tutorial.
        
    * **Run Tests:**
        
        ```yaml
        - name: Run tests
          run: yarn run test
        ```
        
        Executes automated tests. These can be whatever tests you have defined for the repository.
        
    * **Run Lints:**
        
        ```yaml
        - name: Run lints
          run: yarn run lint
        ```
        
        Ensures code quality and style with ESLint. Very standard for a JavaScript application.
        
    * **Run Pretty Checks:**
        
        ```yaml
        - name: Run pretty checks
          run: yarn run pretty-check
        ```
        
        Verifies code formatting with prettier (pretty-check is a [script defined in the package.json)](https://github.com/Scc33/Scc33.github.io/blob/c2cb019a4d9367efa1d69cc63b1cf802600972f1/package.json#L17). Once again this is standard for a JavaScript application.
        
    * **Run Svelte-Check:**
        
        ```yaml
        - name: Run svelte-check
          run: yarn run svelte-check
        ```
        
        Finally, I perform Svelte-specific checks. This step is only because I'm working with a Svelte application.
        

### The Complete CI File

```yaml
name: CI

on:
  # Can run on command
  workflow_dispatch:
  # Runs on pushes to main
  push:
    branches: [master]
  # Runs on pull requests
  pull_request:
    branches: [master]

jobs:
  build:
    name: build-and-test
    # Running on ubuntu-latest, nothing special
    runs-on: ubuntu-latest
    steps:
      # As usual, we simply checkout the project
      - name: Checkout
        uses: actions/checkout@v2
      # Install the latest version of node
      - name: Set up Node.js
        uses: actions/setup-node@v1
        with:
          node-version: '20'
      # Install yarn (prefered build tool)
      - name: Install Yarn
        run: npm install -g yarn
      # Install project dependencies
      - name: Install dependencies
        run: yarn install --frozen-lockfile
      # Make sure the application can build
      - name: Build application
        run: yarn run build
      # Now we run our tests
      - name: Run tests
        run: yarn run test
      # Now we run our lints
      - name: Run lints
        run: yarn run lint
      # Now we run our pretty checks for code formatting
      - name: Run pretty checks
        run: yarn run pretty-check
      # Finally we run svelte-check for some last minute svelte sanity
      - name: Run svelte-check
        run: yarn run svelte-check
```

### Implementing the CI Pipeline

To implement this CI pipeline, create a `.github/workflows` directory in your project and add a file (e.g., `ci.yml`) with the above configuration. This setup activates GitHub Actions to run your workflow based on the defined triggers.

You can find the [code that drives this action in my repository](https://github.com/Scc33/Scc33.github.io/blob/master/.github/workflows/ci.yml).

## Conclusion

Integrating CI into your development process, particularly with JavaScript frameworks, enhances code quality and streamlines development.

GitHub Actions offers a flexible, powerful tool for implementing CI in modern web development.

### Additional Resources

* [GitHub Actions Documentation](https://docs.github.com/en/actions)
    
* [Svelte Official Documentation](https://svelte.dev/docs)
    
* [Yarn Package Manager](https://yarnpkg.com/)
    
* [ESLint Documentation](https://eslint.org)
    
* [Automating NPM Dependency Updates with GitHub Actions](https://blog.seancoughlin.me/automating-npm-dependency-updates-with-github-actions)