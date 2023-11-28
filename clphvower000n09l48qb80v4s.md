---
title: "Automating NPM Dependency Updates with GitHub Actions"
datePublished: Tue Nov 28 2023 05:09:19 GMT+0000 (Coordinated Universal Time)
cuid: clphvower000n09l48qb80v4s
slug: automating-npm-dependency-updates-with-github-actions
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1701147358758/9abd2408-5740-4306-8661-f7dbe819ad5d.jpeg
tags: github, npm, yarn, cicd-cjy1vtdk2005kjjs17n8couc3, github-actions

---

Maintaining up-to-date dependencies in your software projects is crucial for security, performance, and accessing new features. This task, however, can be tedious and time-consuming.

Fortunately, GitHub Actions offer a powerful and flexible way to automate this process. In this blog post, we'll explore how to set up a GitHub Action to automatically update dependencies in a JavaScript project.

## What are GitHub Actions?

[GitHub Actions](https://docs.github.com/en/actions) is a CI/CD (Continuous Integration and Continuous Deployment) platform that allows you to automate your build, test, and deployment workflows right from your GitHub repository.

You can write individual tasks, called actions, and combine them to create a workflow. Workflows are defined by a YAML file in your repository and can be triggered by various GitHub events (like a push, pull request, or scheduled event).

## Setting Up an Automatic Dependency Update Workflow

Let's dive into how we can use GitHub Actions to automatically update dependencies in a JavaScript project. Here’s a step-by-step guide using the provided example workflow:

### 1\. Understanding the Workflow File

The YAML file for our workflow, which might be named `.github/workflows/update-dependencies.yml`, looks like this:

```yaml
name: Update Dependencies

on:
  workflow_dispatch:
  schedule:
    - cron: '0 0 * * *' # Runs every day at midnight

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      ...
```

This configuration sets up a workflow named “Update Dependencies” that triggers on two occasions: manually (`workflow_dispatch`) and on a schedule (`cron: '0 0 * * *'`, [which means every day at midnight](https://crontab.guru/every-day-at-midnight)).

I like to add the manual configuration (`workflow_dispatch`) because it makes testing easier.

The location of the file is important. [GitHub looks for these actions](https://docs.github.com/en/actions/quickstart) to be located in the `.github/workflow` folder.

### 2\. Configuring the Job

The `update` job runs on the latest Ubuntu runner provided by GitHub and consists of several steps:

* **Checking out the repository**: `actions/checkout@v2` checks out your repository, so your workflow can access it. This action is [provided by GitHub](https://github.com/actions/checkout).
    
* **Setting up Node.js**: `actions/setup-node@v1` sets up the Node.js environment with a specified version (`node-version: '20'`).
    
* **Installing Yarn**: This step installs Yarn, a package manager, using NPM. This step is only required if your application uses Yarn. If your application is based on NPM feel free to skip.
    

### 3\. Updating Dependencies

The core of our workflow is updating the dependencies:

```yaml
- name: Update Dependencies
  run: |
    yarn global add npm-check-updates
    ncu -u
    yarn install
```

This step does the following:

* Installs `npm-check-updates`, a tool for upgrading your `package.json` dependencies to the latest versions.
    
* Runs `ncu -u` (npm-check-updates) which upgrades the `package.json` file.
    
* Runs `yarn install` to install the updated dependencies and generate a new lock file.
    

### 4\. Creating a Pull Request

Finally, the workflow uses the `peter-evans/create-pull-request@v3` action to create a pull request with the updated `package.json` and `yarn.lock` files.

The pull request will include a predefined message, title, and branch name. What you decide to put in the message is entirely up to you.

```yaml
- name: Create Pull Request
  uses: peter-evans/create-pull-request@v3
  with:
      commit-message: Update dependencies
      title: '[DEPENDENCY] Update Dependencies'
      body: |
          Updates dependencies in `package.json`.
      branch: update-dependencies
```

### 5\. Running the Action

The action will run automatically at midnight or whenever you trigger using the manual run workflow trigger (`Actions > Update Dependencies > Run workflow`).

When the action finds dependencies to update, it will automatically create a PR with the required changes that you can merge at your leisure.

[![Example PR created by the update dependencies GitHub action](https://cdn.hashnode.com/res/hashnode/image/upload/v1701146817325/dcf2826b-4a85-4766-830f-cddbc57741fd.png align="center")](https://github.com/Scc33/Scc33.github.io/pull/101)

## Conclusion

By automating the dependency update process using GitHub Actions, you can significantly reduce the manual effort involved in keeping your project dependencies current.

This not only saves time but also helps in maintaining a secure and stable code base. Remember, while the example provided focuses on a JavaScript project, the concept can be adapted to other languages and package managers.

You can find a complete example of this code [here](https://github.com/Scc33/Scc33.github.io/blob/master/.github/workflows/update-dependencies.yml) (I use this to keep my personal site up-to-date).

Happy coding!