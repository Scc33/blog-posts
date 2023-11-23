---
title: "Learn React Basics: Components and Props"
datePublished: Thu Nov 23 2023 19:34:09 GMT+0000 (Coordinated Universal Time)
cuid: clpbldtnx000009jy9cl81b8g
slug: learn-react-basics-components-and-props
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1700760094346/17da68a4-445e-4794-9c0c-20f47fb9a29d.png
tags: tutorial, javascript, web-development, reactjs, frontend-development

---

[React](https://react.dev), a popular JavaScript library for building user interfaces is known for its [component-based architecture](https://en.wikipedia.org/wiki/Component-based_software_engineering). This architecture not only makes React powerful but also easy to learn, especially when you start with the basics of React Components and Props. In this blog post, we'll delve into these concepts, providing code examples and linking to additional resources for an enriched learning experience.

## What are React Components?

[React components](https://react.dev/reference/react/components) are the core building blocks of a React application. They are independent, reusable pieces of UI that can be nested within each other. Components let you split the UI into separate sections, like header, footer, and body, each of which operates independently.

### Types of Components

#### 1\. Class Components (Legacy)

[Class components](https://react.dev/reference/react/Component) are a legacy method for creating components. They are defined using [ES6 classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) and extend from `React.Component`. They can hold and manage local state and lifecycle methods.

**Example:**

```typescript
import { Component } from 'react';

class Welcome extends Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}

export default Welcome;
```

Here, `Welcome` is a class component that renders a simple greeting. It accesses props using [`this.props.name`](http://this.props.name).

For more on class components, check the [React documentation on Components and Props](https://react.dev/reference/react/Component). Note this is an older way of creating components. The new (and better method is functional components)

#### 2\. Functional Components

Functional components are simpler and defined using plain [JavaScript functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions). They can manage state [using hooks](https://blog.seancoughlin.me/learn-react-hooks), which was exclusive to class components in the past (before React 16.8).

**Example:**

```typescript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

export default Welcome;
```

This functional component does the same thing as the class component above but with less boilerplate.

Refer to [React’s Functional Components](https://reactjs.org/docs/components-and-props.html#function-and-class-components) for more insights.

## Understanding Props in React

Props (short for properties) are how you pass data from a parent component to a child component in React. They are read-only, which means a child component cannot modify the props it receives.

### Example of Using Props

```typescript
import Welcome from './Welcome'; // some other predefined component

function App() {
  return (
    <div>
      <Welcome name="Alice" />
      <Welcome name="Bob" />
    </div>
  );
}

export default App;
```

In this example, `App` is the parent component that renders the `Welcome` component twice, each time passing a different `name` as a prop.

For a comprehensive guide on props, visit [React’s official documentation](https://reactjs.org/docs/components-and-props.html#rendering-a-component).

## Conclusion

Understanding React components and props is fundamental for any beginner in React development. These concepts form the backbone of React applications, enabling developers to create complex, efficient, and maintainable UIs.

As you progress, you’ll discover more advanced features and patterns, but mastering components and props will give you a solid foundation to build upon.

Remember, the best way to learn React is by practice. Experiment with different types of components and props, and refer to the React documentation for deeper insights and best practices. Happy coding!

---

For further exploration, the [React documentation](https://reactjs.org/docs/getting-started.html) is an invaluable resource, providing in-depth tutorials and guides on various aspects of React.