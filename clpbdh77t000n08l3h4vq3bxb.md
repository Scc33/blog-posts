---
title: "Learn React Basics: React Hooks"
datePublished: Thu Nov 23 2023 15:52:49 GMT+0000 (Coordinated Universal Time)
cuid: clpbdh77t000n08l3h4vq3bxb
slug: learn-react-hooks
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1700754380336/4b3d029e-6f05-4f6b-a960-25c897e99cf0.png
tags: tutorial, web-development, reactjs, frontend-development, react-hooks

---

Here we go another React Hooks tutorial :). I definitely created the first one of these on the internet (cough cough sarcasm).

React Hooks, [introduced in React 16.8](https://legacy.reactjs.org/docs/hooks-intro.html), drastically changed the way we write React components. They allow you to use state and other React features in functional components, which was previously only possible in [class components](https://legacy.reactjs.org/docs/react-component.html). This makes code more readable and easier to maintain.

Today, we'll explore two key hooks: `useState` and `useEffect`, with examples and documentation links. These are by far the most common hooks out there. By no means do they mark the complete universe of hooks, but you can get pretty far in the React universe with just these two.

## Understanding useState

The [`useState` hook](https://react.dev/reference/react/useState) is the cornerstone for managing state in functional components. It's a simpler and more elegant way to introduce state in your components without converting them into classes (which for all intents and purposes are dead in React at this point).

### Example: A Simple Counter

Here's a basic example that demonstrates the `useState` hook:

```typescript
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}

export default Counter;
```

In this example, `useState(0)` initializes the `count` state variable to 0. `setCount` is a function that updates `count`. When you click the button, `setCount` is called with the new count value, triggering a re-render with the updated state.

Note the automatic re-render where React will re-render the page to show the updated state. There is some performance overhead with this operation.

For more details on `useState`, check the [official documentation](https://react.dev/reference/react/useState).

## Exploring useEffect

The [`useEffect` hook](https://react.dev/reference/react/useEffect) is used for performing side effects in function components. It's similar to lifecycle methods like `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` in class components.

### Example: Updating Document Title

Let's look at an example where `useEffect` is used to update the document title:

```typescript
import { useState, useEffect } from 'react';

function TitleUpdater() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    // Update the document title using the browser API
    document.title = `You clicked ${count} times`;
  });

  return (
    <div>
      <p>Click count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increase count
      </button>
    </div>
  );
}

export default TitleUpdater;
```

In this example, `useEffect` is used to update the document's title every time the component renders. The hook runs after every render by default, including the first render.

For an in-depth understanding of `useEffect`, refer to the [React documentation](https://react.dev/reference/react/useEffect).

## Conclusion

React Hooks offer a more intuitive and functional approach to building components. By understanding and utilizing hooks like `useState` and `useEffect`, you can write more concise and maintainable React applications. They not only simplify your component logic but also pave the way for better state management and side-effect handling in functional components.

For further reading and advanced hook patterns, the [React documentation](https://react.dev) provides comprehensive guides and examples. Happy coding!