---
title: "Mastering Snapshot Testing with Vite, Vitest, or Jest in TypeScript"
seoTitle: "Master Snapshot Testing with Vite, Vitest, and Jest in TypeScript"
seoDescription: "Master snapshot testing in TypeScript with Vite, Vitest, and Jest. This guide covers setup, configuration, and best practices for maintaining UI consistency"
datePublished: Wed Jul 10 2024 22:26:21 GMT+0000 (Coordinated Universal Time)
cuid: clyget7oz000309jq8aq11gsd
slug: mastering-snapshot-testing-with-vite-vitest-or-jest-in-typescript
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1720650255517/a29d7413-b973-4c1e-9fc6-ae05e07bbdca.webp
tags: web-development, frontend-development, jest, snapshot-testing, vite

---

Snapshot testing is a powerful and efficient way to ensure the UI of your application remains consistent over time. By capturing the rendered output of a component and comparing it to a previously stored snapshot, any unintended changes can be quickly identified.

This article will guide you through the process of setting up snapshot testing in a TypeScript project using Vite as the build tool, with both Vitest and Jest as the testing frameworks.

## What are Snapshot Tests?

Snapshot tests are a type of automated test that helps you verify the UI of your application. They work by rendering a component, taking a snapshot of its output, and comparing it to a previously stored snapshot. If the output has changed, the test will fail, alerting you to a potential unintended change in your UI.

Snapshot tests are particularly useful for large components and complex UIs, as they allow you to quickly identify when something has changed, ensuring your UI remains consistent.

### Why are Snapshot Tests Important?

1. **Consistency**: They ensure that your UI remains consistent over time, catching any unexpected changes.
    
2. **Efficiency**: They automate the process of checking the UI, saving time compared to manual testing.
    
3. **Confidence**: They give you confidence that your changes have not unintentionally affected the UI.
    

---

## Introduction to Vite

Vite is a fast and modern build tool for JavaScript projects. It provides a smooth development experience with features like hot module replacement (HMR), lightning-fast cold starts, and a highly optimized build process. Using Vite, you can create and develop your applications efficiently, making it a popular choice for modern web development.

## Setting Up a New Vite Application

To get started, create a new Vite application with [the following command](https://www.npmjs.com/package/create-vite):

```bash
npm create vite@latest
```

Follow the prompts to set up your project. Once the setup is complete, navigate to your project directory.

## Installing Vitest and Required Packages

Next, install Vitest along with the necessary packages for testing:

```bash
npm install vitest@latest --save-dev
npm install --save-dev @testing-library/react @testing-library/dom jsdom
```

## Configuring Vite for Testing

To configure Vite for testing with Vitest, modify your `vite.config.ts` file as follows:

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    include: ['**/*.test.tsx'],
  }
});
```

This configuration sets up the testing environment to use `jsdom` and includes all files with a `.test.tsx` extension.

## Writing a Snapshot Test with Vitest

Create a test file named `App.test.tsx` and add the following code:

```typescript
import { render } from "@testing-library/react";
import { expect, it } from "vitest";
import App from "./App";

it("toUpperCase", () => {
  const { asFragment } = render(<App />);
  expect(asFragment()).toMatchSnapshot();
});
```

This test renders the `App` component and captures a snapshot of its output. When you run the test for the first time, [Vitest will generate a snapshot file](https://vitest.dev/guide/snapshot) containing the rendered output.

To run your tests, use the following command:

```bash
npx vitest run
```

## Vitest Snapshot Output

The output of the snapshot test will look something like this:

```xml
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`toUpperCase 1`] = `
<DocumentFragment>
  <div>
    <a
      href="https://vitejs.dev"
      target="_blank"
    >
      <img
        alt="Vite logo"
        class="logo"
        src="/vite.svg"
      />
    </a>
    <a
      href="https://react.dev"
      target="_blank"
    >
      <img
        alt="React logo"
        class="logo react"
        src="/src/assets/react.svg"
      />
    </a>
  </div>
  <h1>
    Vite + React
  </h1>
  <div
    class="card"
  >
    <button>
      count is 0
    </button>
    <p>
      Edit 
      <code>
        src/App.tsx
      </code>
       and save to test HMR
    </p>
  </div>
  <p
    class="read-the-docs"
  >
    Click on the Vite and React logos to learn more
  </p>
</DocumentFragment>
`;
```

---

## Setting Up Jest for Snapshot Testing

Jest is another popular testing framework that was originally built with CommonJS modules in mind. Setting up Jest in a Vite project involves a bit more configuration.

First, install the required packages:

```bash
npm install --save-dev jest ts-jest @types/jest
npm install --save-dev jest-environment-jsdom jest-transform-stub
```

Initialize the Jest configuration:

```bash
npx ts-jest config:init
```

Modify the generated `jest.config.js` file to include the following settings:

```javascript
/** @type {import('ts-jest').JestConfigWithTsJest} **/
export default {
  testEnvironment: "jsdom",
  transform: {
    "^.+.tsx?$": ["ts-jest", { tsconfig: "tsconfig.app.json" }],
  },
  testMatch: ["**/*.spec.tsx"],
  moduleNameMapper: { "\\.(css|less|scss|sass|svg)$": "jest-transform-stub" },
};
```

## Writing a Snapshot Test with Jest

Create a test file named `App.spec.tsx` and add the following code:

```typescript
import { render } from "@testing-library/react";
import App from "./App";

it("toUpperCase", () => {
  const { asFragment } = render(<App />);
  expect(asFragment()).toMatchSnapshot();
});
```

Notice that the test syntax is nearly identical to that of Vitest, as Vitest implements the Jest API.

To run your Jest tests, use the following command:

```bash
npx jest
```

---

## Conclusion

Snapshot testing is a valuable technique for maintaining UI consistency in your applications. In this article, we explored how to set up snapshot testing in a TypeScript project using Vite as the build tool, with both Vitest and Jest as the testing frameworks.

While Vitest offers a more streamlined setup with Vite, Jest remains a powerful option with extensive community support and plugins. By following these steps, you can ensure your UI remains consistent and catch any unintended changes early in the development process.

## FAQ

### What is snapshot testing?

Snapshot testing is an automated testing technique that captures the rendered output of a component and compares it to a previously stored snapshot to identify any changes.

### Why use Vite for building applications?

Vite offers a fast and modern development experience with features like hot module replacement and optimized builds, making it a popular choice for modern web development.

### How does Vitest compare to Jest?

Vitest implements the Jest API, making it a more streamlined choice for Vite projects. However, Jest offers extensive community support and plugins, making it a versatile option for many projects.

### Can I use snapshot testing with TypeScript?

Yes, both Vitest and Jest support TypeScript, allowing you to use snapshot testing in your TypeScript projects.

### How do I update a snapshot?

To update a snapshot, you can run the tests with the `-u` flag (e.g., `npx vitest run -u` or `npx jest -u`), which will update the stored snapshots with the current output.

By implementing snapshot testing in your Vite projects using Vitest or Jest, you can enhance the reliability and consistency of your UI, ensuring a smoother and more efficient development process.

## GitHub Example

To see the complete code in action, visit the following GitHub repository.

* [**snapshot-example**](https://github.com/Scc33/snapshot-example)
    

## Related Articles

I have a passion for frontend development and testing! Be sure to check out my other articles on the subject for more insights and tips.

* "[jsdom vs happy-dom: Navigating the Nuances of JavaScript Testing](https://blog.seancoughlin.me/jsdom-vs-happy-dom-navigating-the-nuances-of-javascript-testing)"
    
* "[Maximizing Web Development Efficiency: A Comprehensive Guide to Vite](https://blog.seancoughlin.me/maximizing-web-development-efficiency-a-comprehensive-guide-to-vite)"
    
* "[Vitest vs. Jest: The New JavaScript Testing Framework](https://blog.seancoughlin.me/vitest-vs-jest-the-new-javascript-testing-framework)"
    
* "[Testing React Applications Built with Vite Using Vitest](https://blog.seancoughlin.me/testing-react-applications-built-with-vite-using-vitest)"
    
* "[Testing a React App Built with Vite Using Jest and Babel](https://blog.seancoughlin.me/testing-a-react-app-built-with-vite-using-jest-and-babel)"
    

## Documentation

Nothing is complete without documentation, visit the following resources for more information.

* [Vite documentation](https://vitejs.dev)
    
* [Vitest documentation](https://vitest.dev)
    
* [Jest documentation](https://jestjs.io/docs/getting-started)
    
* [ts-jest documentation](https://kulshekhar.github.io/ts-jest/docs/)
    
* [Jest snapshot testing](https://jestjs.io/docs/snapshot-testing)
    
* [jsdom GitHub](https://github.com/jsdom/jsdom)