---
title: "Testing a React App Built with Vite Using Jest and Babel"
datePublished: Thu Jan 18 2024 18:27:42 GMT+0000 (Coordinated Universal Time)
cuid: clrjjo2gw000009gneten7pef
slug: testing-a-react-app-built-with-vite-using-jest-and-babel
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1705600649141/47783664-e52b-4c9b-a55b-beb409a67055.jpeg
tags: web-development, reactjs, jest, vite, testing-library

---

In the world of modern web development, React has become a go-to library for building dynamic user interfaces. Vite, a build tool that significantly improves the developer experience, complements React by offering a fast and efficient development workflow.

However, setting up testing for a React application built with Vite, especially when using Jest and Babel, requires some configuration. This blog post walks you through the process step by step.

## Setting Up the Environment

First, ensure you have a React application created with Vite. Vite offers a template for React which can be used to set up a new project:

```bash
npm create vite@latest my-react-app --template react
cd my-react-app
npm install
```

This command scaffolds a React application. Once your project is set up, you can begin configuring Jest and Babel for testing.

## Installing Jest and Babel

Jest is a delightful JavaScript Testing Framework with a focus on simplicity, and Babel is a JavaScript compiler that lets you use next generation JavaScript, today. To get started, install Jest, Babel, and their necessary plugins:

```bash
npm install --save-dev jest jest-environment-jsdom jest-transform-stub @testing-library/jest-dom
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/preset-react
```

## Configuring Babel

Create a Babel configuration file at the root of your project (`babel.config.cjs`) and configure it to transpile JSX and ES6+ syntax:

```javascript
module.exports = {
    presets: [
        '@babel/preset-env', [
            '@babel/preset-react',
            {
                runtime: "automatic"
            }
        ]
    ]
};
```

This configuration tells Babel to use the necessary presets to transform JSX and modern JavaScript into a format Jest can understand.

## Configuring Jest

Jest requires some configuration to work seamlessly with Vite and React. Create a `jest.config.cjs` file in your project root:

```javascript
module.exports = {
  transform: {
    '^.+\\.[t|j]sx?$': 'babel-jest',
  },
  moduleNameMapper: {
    '^.+\\.(jpg|jpeg|png|gif|webp|svg|css)$': 'jest-transform-stub'
  }
  testEnvironment: 'jsdom',
  testPathIgnorePatterns: ["<rootDir>/node_modules/"]
};
```

This configuration tells Jest to use `babel-jest` for transforming your test files.

`jest-transform-stub` is a useful tool when dealing with non-JavaScript assets in Jest tests. It allows Jest to ignore asset imports (like CSS, images, etc.), which it cannot natively handle, by transforming them into a stub.

`jsdom` is a pure-JavaScript implementation of many web standards, primarily the WHATWG DOM and HTML Standards, for use with Node.js, allowing the simulation of a browser environment for testing JavaScript code outside of a browser.

## The Necessity of Babel in Jest Testing with Vite and React

Incorporating Babel into our Jest setup plays a crucial role, especially in the context of a React application built with Vite. Vite, by design, leverages native [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript) modules (ESM) for a faster development experience, and it inherently supports modern JavaScript features and JSX out of the box. However, Jest does not natively understand ESM or JSX syntax. This is where Babel becomes essential.

Babel acts as a bridge between the modern JavaScript and JSX code that we write (and that Vite comfortably handles) and the more traditional JavaScript environment that Jest operates in. When we run our tests, Jest invokes Babel to transpile the code. This transpilation step converts JSX into regular JavaScript function calls and transforms ES6+ syntax into a format that Jest can process.

Under the hood, Babel uses the specified presets - `@babel/preset-env` and `@babel/preset-react`. The `@babel/preset-env` preset allows Babel to transpile ES6+ syntax (like arrow functions, template literals, etc.) down to ES5, ensuring compatibility with Jest's execution environment. The `@babel/preset-react`, on the other hand, specifically deals with JSX, transforming it into `React.createElement` calls, which is standard JavaScript understood by Jest.

Without Babel, Jest would encounter syntax it doesn’t understand (like import statements or JSX), leading to syntax errors and failed tests. Therefore, Babel is not just a convenience; it's a necessity for bridging the gap between the modern development experience provided by Vite and the testing capabilities of Jest. By integrating Babel, we ensure that our modern, efficient React codebase remains testable and robust, adhering to best practices in software development.

## Writing Your First Test

Create a new file for your tests. For example, if you're testing a component `App.jsx`, create a file `App.test.jsx`. Here’s a simple test case:

```javascript
import { render } from '@testing-library/react';
import App from './App';
import '@testing-library/jest-dom';

test('renders learn vite link', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/Click/i);
  expect(linkElement).toBeInTheDocument();
});
```

This test uses React Testing Library to render the component and then asserts that specific text is present. It uses the `jest-dom` library for the `toBeInTheDocument` matcher.

## Running Tests

Add a script in your `package.json` to run Jest:

```json
"scripts": {
  "test": "jest"
}
```

You can now run your tests using:

```bash
npm test
```

## Conclusion

Setting up Jest with a React application created using Vite ensures that your application is not only fast and efficient but also reliable and bug-free. Remember, testing is a crucial part of the development process, helping you catch bugs early and maintain code quality.

For more information and advanced configurations, refer to the official documentation:

* [Jest Documentation](https://jestjs.io/docs/getting-started)
    
* [Babel Documentation](https://babeljs.io/docs/en/)
    
* [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    

For an example application you can check out the repo I used for writing this post:

* [**vite-jest-ex**](https://github.com/Scc33/vite-jest-ex)
    

Happy testing!