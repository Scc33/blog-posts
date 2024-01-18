---
title: "Testing React Applications Built with Vite Using Vitest"
datePublished: Thu Jan 18 2024 18:59:41 GMT+0000 (Coordinated Universal Time)
cuid: clrjkt7nf000708jo2w1c44mf
slug: testing-react-applications-built-with-vite-using-vitest
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1705603557977/9a437fcb-7889-4e74-bd36-1e314ec45b75.jpeg
tags: web-development, jsdom, vite, testing-library, vitest

---

In the ever-evolving world of JavaScript development, React remains a popular choice for building user interfaces. When paired with Vite, a next-generation frontend tooling, it accelerates development with its out-of-the-box features like fast hot module replacement (HMR).

However, an often overlooked aspect of this powerful duo is efficient testing. This article delves into using Vitest, a Vite-native test framework, to test React applications written in plain JavaScript.

## Why Vitest?

Vitest stands out due to its compatibility with Vite's ecosystem, enabling features like native ES modules support, fast cold-start, and fine-grained watch mode. It's a Jest-compatible framework, meaning those familiar with Jest will find it easy to adapt.

## **Setting Up the Environment**

First, ensure you have a React application created with Vite. Vite offers a template for React which can be used to set up a new project:

```bash
npm create vite@latest my-react-app --template react
cd my-react-app
npm install
```

This command scaffolds a React application. Once your project is set up, you can begin configuring Vite for testing.

## Setting Up the Testing Environment

### Installing Vitest

To integrate Vitest, install it along with the necessary testing libraries:

```bash
npm install vitest @testing-library/react @testing-library/jest-dom jsdom --save-dev
```

### Configuring Vite and Vitest

Vitest benefits from sharing Vite's configuration. Create a `vite.config.js` file at the root of your project with the following:

```javascript
// <reference types="vite/client" />
// <reference types="vitest" />

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  test: {
    // Vitest configurations
    globals: true,
    environment: 'jsdom',
  },
});
```

This configuration enables React support and sets up basic Vitest configurations.

* `globals` automatically imports the [utility functions](https://vitest.dev/api/vi) to each test file
    
* `environment` is the package used to mimic a DOM (i.e. [jsdom vs happy-dom](https://blog.seancoughlin.me/jsdom-vs-happy-dom-navigating-the-nuances-of-javascript-testing))
    

## Writing Tests

With the environment set up, let’s write a simple test. Assume you have a component `MyComponent.js`:

```javascript
export function MyComponent() {
  return <div>Hello, world!</div>;
}
```

Create a test file `MyComponent.test.js`:

```javascript
import { render, screen } from '@testing-library/react';
import { MyComponent } from './MyComponent';

test('displays the correct text', () => {
  render(<MyComponent />);
  expect(screen.getByText('Hello, world!')).toBeInTheDocument();
});
```

This test renders `MyComponent` and asserts that the text "Hello, world!" is present in the document.

## Running Tests

To run tests, modify your `package.json` to include a test script:

```json
{
  // ...
  "scripts": {
    "test": "vitest"
  }
  // ...
}
```

Run the tests using:

```bash
npm run test
```

Vitest will execute the tests and provide output in the console.

![Vitest console output](https://cdn.hashnode.com/res/hashnode/image/upload/v1705603947556/d076d805-2466-484a-9173-b7be6efd2d14.png align="center")

## Watching for Changes

Vitest can watch for file changes and re-run tests. This is particularly useful during development. Run Vitest in watch mode:

```bash
npm run test watch
```

## Conclusion

Testing React applications with Vitest offers a seamless experience, especially for projects using Vite. It leverages Vite’s configuration and provides a fast, efficient testing environment.

By following this guide, you've set up a basic testing framework for your React application, enabling you to write and run tests with ease.

For further reading and advanced configurations, refer to the following official documentation:

* [Vitest documentation](https://vitest.dev/)
    
* [Vite documentation](https://vitejs.dev/)
    

For an example application, you can check out the repo I used for writing this post:

* [vite-vitest-ex](https://github.com/Scc33/vite-vitest-ex)
    

Remember, testing is not just about finding bugs but ensuring your application behaves as expected, making it a crucial part of the development process.

Happy testing!