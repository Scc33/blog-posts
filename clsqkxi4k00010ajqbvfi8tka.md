---
title: "Crafting a Health Check for Your Website with GitHub Actions"
seoTitle: "Automating Web Health Checks with GitHub Actions: A Step-by-Step Guide"
seoDescription: "Explore automating website health checks with GitHub Actions. This guide covers setup, execution, and benefits for maintaining web app performance."
datePublished: Sat Feb 17 2024 21:17:07 GMT+0000 (Coordinated Universal Time)
cuid: clsqkxi4k00010ajqbvfi8tka
slug: crafting-a-health-check-for-your-website-with-github-actions
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1708203400222/6db7fa84-00e4-4db8-8f75-2fa1f60d784e.webp
tags: github, web-development, testing, github-actions, playwright

---

In the digital age, ensuring your website's reliability and performance is paramount. A health check serves as the heartbeat for your online presence, ensuring everything is running smoothly and efficiently.

This article delves into the essence of health checks and demonstrates how you can implement an automated health check for your website using GitHub Actions and Playwright.

## Understanding Health Checks

A [health check](https://microservices.io/patterns/observability/health-check-api.html) is a procedure that evaluates various aspects of a website or service to ensure it is functioning correctly. It's akin to a routine checkup for your website, identifying potential issues before they escalate into significant problems. The goal is to minimize downtime, enhance user experience, and maintain operational efficiency.

Health checks can cover a range of tests, from simple endpoint pings to verify server response, to more complex transactions that simulate user interactions. The core objectives are to verify availability, responsiveness, and the correct operation of your website or service.

### Aside: Health Checks and Microservices

Health checks are a fundamental component of [microservice architectures](https://en.wikipedia.org/wiki/Microservices), playing a crucial role in ensuring the seamless operation and reliability of distributed systems.

In environments where applications are decomposed into smaller, independently deployable services, health checks provide the necessary mechanism to monitor the status and functionality of each microservice.

They enable automated systems to detect when a service is unhealthy, facilitating quick recovery actions such as restarting the service or rerouting traffic to healthy instances. This not only enhances the overall resilience and fault tolerance of the system but also supports dynamic scaling and load balancing by ensuring that only healthy instances are utilized.

By integrating health checks into microservice architectures, organizations can achieve higher uptime and more robust performance, crucial for maintaining user satisfaction and operational efficiency in complex, distributed environments.

## Why Automate Health Checks with GitHub Actions?

Automating health checks with GitHub Actions brings several advantages. GitHub Actions is a CI/CD platform that allows you to automate your software workflows directly within GitHub. By leveraging GitHub Actions for health checks, you can:

* **Automate Routine Checks**: Schedule health checks to run automatically at predetermined intervals.
    
* **Integrate with Your Development Workflow**: Easily integrate health checks into your existing development and deployment pipelines.
    
* **Respond Quickly to Issues**: Automate notifications and actions based on the outcomes of your health checks.
    

## **Implementing a Health Check with GitHub Actions**

Let's dive into setting up a health check workflow using GitHub Actions.

The provided script exemplifies how to set up an automated health check using GitHub Actions. This will be an example script for testing that a website is up and running. For this tutorial, we will use [Playwright](https://playwright.dev).

The script below outlines the GitHub Action workflow designed to perform health checks on your website:

```yaml
name: healthcheck

on:
  workflow_dispatch:
  workflow_call:
  schedule:
    - cron: "0 0 * * *"

jobs:
  test:
    name: healthcheck
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          ref: screenshots
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
      - name: Install Yarn
        run: npm install -g yarn
      - name: Install dependencies
        run: yarn install --frozen-lockfile
      - name: Install Playwright Browsers
        run: npx playwright install --with-deps
      - name: Run tests
        run: yarn run test:healthcheck
      - name: Commit screenshots
        run: |
          git config --global user.email "youremail@example.com"
          git config --global user.name "Your Name"
          git add -f screenshots
          git commit -m "Add test screenshots"
          git push
```

## The Health Check Script Explained

Let's break down its components and understand how each part contributes to the health check process.

### Workflow Triggers

```yaml
on:
  workflow_dispatch:
  workflow_call:
  schedule:
    - cron: "0 0 * * *"
```

This section defines when the health check workflow is triggered. It's set to run under three conditions:

* `workflow_dispatch`: Allows the workflow to be manually triggered from the GitHub Actions interface.
    
* `workflow_call`: Enables this workflow to be called by other workflows within your GitHub repository.
    
* `schedule`: Automates the workflow to run at a scheduled time, in this case, daily at midnight.
    

### The Health Check Job

```yaml
jobs:
  test:
    name: healthcheck
    runs-on: ubuntu-latest
```

This segment initializes the job, naming it `healthcheck` and specifying it to run on the latest Ubuntu runner provided by GitHub Actions.

### Steps for Setup and Testing

The steps within the job handle the setup and execution of the health check:

1. **Checkout the Project**: Uses `actions/checkout@v4` to checkout the repository, allowing the workflow to access its contents.
    
2. **Set up Node.js**: Utilizes `actions/setup-node@v4` to install Node.js, specifying version 20.
    
3. **Install Yarn**: Installs Yarn using `npm install -g yarn`, as Yarn is the preferred build tool for this project.
    
4. **Install Dependencies**: Runs `yarn install --frozen-lockfile` to install the project dependencies without updating the lock file.
    
5. **Install Playwright Browsers**: Executes `npx playwright install --with-deps` to install browsers needed for Playwright tests.
    
6. **Run Playwright Tests**: Runs `yarn run test:healthcheck` to execute the Playwright tests, which simulate user interactions and check the health of the website.
    

### The Playwright Script

GitHub Actions calls the `test:healthcheck` script which can be pointed to some basic Playwright that verifies a site is up and inter-actable.

```javascript
import { test, expect } from "@playwright/test";

test.describe("Health Check", () => {
  test("should ensure the website is alive", async ({ page }) => {
    await page.goto("/");
    const title = await page.title();
    expect(title).toBe("Sean Coughlin | Software Engineer");
  });

  test("should ensure the website has a header", async ({ page }) => {
    await page.goto("/");

    await expect(
      page.getByRole("heading", { name: "Sean Coughlin", exact: true })
    ).toBeVisible();
  });

  // eslint-disable-next-line playwright/expect-expect
  test("should take a screenshot", async ({ page }) => {
    const date = new Date();
    const photoPath = `./screenshots/healthcheck-${date.toISOString()}.png`;

    await page.goto("/");
    await page.screenshot({ path: photoPath });
  });
});
```

1. **Website Availability Test**: The first test navigates to the homepage and checks if the website's title matches the expected value. This test ensures that the website is up and running, and the main page is accessible.
    
2. **Header Visibility Test**: The second test again navigates to the homepage and verifies the presence of a specific header on the page, ensuring that essential elements of the UI are visible and correctly rendered.
    
3. **Screenshot Capture**: The final test navigates to the homepage and takes a screenshot, saving it with a filename that includes the current date and time. This step is useful for visual verification of the website's state at the time of the test, aiding in debugging and record-keeping.
    

### Committing Test Artifacts

```yaml
- name: Commit screenshots
  run: |
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
    git add -f screenshots
    git commit -m "Add test screenshots"
    git push
```

After running the tests, this step commits any screenshots taken during the tests to the repository. This is useful for visual verification and debugging.

Artifacts from automated processes, such as health checks, can also be stored in dedicated artifact repositories like [JFrog Artifactory](https://jfrog.com/artifactory/), cloud storage services like [AWS S3](https://aws.amazon.com/s3/), or continuous integration tools like [Jenkins](https://www.jenkins.io/doc/), instead of being committed to version control.

## Conclusion

Automating health checks using GitHub Actions is a robust method to ensure the continuous health of your website. It allows for scheduled checks, integrates seamlessly with your development process, and enables quick responses to identified issues.

By following the outlined script and understanding each component's role, you can implement an effective health check workflow tailored to your website's needs, ensuring reliability and performance for your users.

### Where to Learn More

For more in-depth knowledge and resources on leveraging GitHub Actions, consider exploring the following sections:

1. [**GitHub Actions Documentation**](https://docs.github.com/en/actions): This comprehensive guide covers everything from automating workflows to CI/CD, helping you to customize and execute software development workflows within your repository. It's a great starting point to understand the full capabilities of GitHub Actions.
    
2. [**Learn GitHub Actions**](https://docs.github.com/en/actions/learn-github-actions): This section is ideal for both beginners and those looking to deepen their understanding of GitHub Actions. It provides insights into core features, expressions, workflow syntax, and much more, making it a valuable resource for accelerating your application development workflows.
    
3. [**Understanding GitHub Actions**](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions): For a foundational understanding, this article breaks down the basics, including core concepts, essential terminology, and how to create an example workflow. It's perfect for getting acquainted with the components and functionalities of GitHub Actions.
    

These resources offer a wealth of information to get started with GitHub Actions or to expand your existing knowledge, enabling you to automate and optimize your development workflows effectively.

---

I wrote this article based on the health check script I use for my personal website. You can find the source code for that site below:

1. [Package.json](https://github.com/Scc33/Scc33.github.io/blob/master/package.json)
    
2. [Playwright script](https://github.com/Scc33/Scc33.github.io/blob/master/tests/healthcheck.test.js)
    
3. [GitHub Action workflow](https://github.com/Scc33/Scc33.github.io/blob/master/.github/workflows/healthcheck.yml)