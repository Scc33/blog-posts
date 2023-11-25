---
title: "Learn React Basics: Redux"
datePublished: Sat Nov 25 2023 19:33:48 GMT+0000 (Coordinated Universal Time)
cuid: clpeg936n000b09jjc54jd08g
slug: learn-react-basics-redux
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1700939969352/32abfc19-16eb-41af-9afe-bf202c8a8825.jpeg
tags: javascript, web-development, reactjs, redux, frontend-development

---

Redux has emerged as a significant player in the realm of state management for modern web applications, particularly those built with React.

Powerfully, its utility extends beyond React, making it a versatile choice for developers. However, it is a complex library with a high learning curve and a lot of boilerplate.

In this blog post, we'll dive into what Redux is, its use cases, and how it integrates with React, along with alternatives and an introduction to Redux Toolkit.

[![Redux NPM page](https://cdn.hashnode.com/res/hashnode/image/upload/v1700940248490/2b24f3c4-42d3-4ddb-9e54-81772e75c77e.png align="center")](https://www.npmjs.com/package/redux)

## What is Redux?

Redux is both a pattern and a library for managing and updating application state, using events called "actions". One mental shortcut for thinking about Redux is that it's a client-side database.

It's based on the [Flux architecture](https://www.geeksforgeeks.org/redux-and-the-flux-architecture/), but with simpler and more predictable behavior, thanks in part to its use of a single central store. This design makes state mutations predictable in large-scale applications.

This type of architecture is sometimes called a [unidirectional data flow](https://en.wikipedia.org/wiki/Unidirectional_Data_Flow_(computer_science)). It is a powerful concept, but not typically how I think of using data in an application.

Redux was [built by Facebook and released in 2015](https://en.wikipedia.org/wiki/Redux_(JavaScript_library)). Redux operates with a few key patterns that define the structure of the library and how it functions.

* [Redux Documentation](https://redux.js.org/)
    

### Redux as a Pattern

As a pattern, Redux establishes strict guidelines for how state should be updated and accessed. This pattern involves three main principles:

1. **Single Source of Truth**: The state of your entire application is stored in an object tree within a single store.
    
2. **State is Read-Only**: The only way to change the state is to emit an action, an object describing what happened.
    
3. **Changes are Made with Pure Functions**: To specify how the state tree is transformed by actions, you write pure reducers.
    

* [Redux's Three Principles](https://redux.js.org/understanding/thinking-in-redux/three-principles)
    

### Redux as a Library

As a library, Redux provides a [lightweight and flexible API](https://redux.js.org/api/api-reference) to implement this pattern. It offers functions like [`createStore`](https://redux.js.org/api/createstore), [`combineReducers`](https://redux.js.org/tutorials/fundamentals/part-3-state-actions-reducers#combinereducers), and [`applyMiddleware`](https://redux.js.org/api/applymiddleware) to help manage the state and integrate middleware.

Be warned. While the API might seem small, warm, and fuzzy, it is chocked full of boilerplate and confusing pitfalls. This is just a high-level overview and I would recommend watching and reading more tutorials before diving into implementation.

## When to Use Redux

Redux shines in scenarios where:

* You have large-scale, complex applications with significant amounts of application state.
    
* Multiple parts of the application need to access and modify the same state.
    
* The state structure is complex or involves deep nesting.
    
* You need a predictable state with a powerful debugging toolset.
    

## Integrating Redux with React

Here's how to quickly install Redux:

```bash
yarn add -D redux
```

And here's a simple example of using Redux in a React application:

```javascript
import { createStore } from 'redux';

// Reducer function
function counter(state = 0, action) {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    case 'DECREMENT':
      return state - 1;
    default:
      return state;
  }
}

// Create Redux store
const store = createStore(counter);

// React Component
function Counter () {
    return (
      <div>
        <button onClick={() => store.dispatch({ type: 'DECREMENT' })}>-</button>
        <span>{store.getState()}</span>
        <button onClick={() => store.dispatch({ type: 'INCREMENT' })}>+</button>
      </div>
    );
}

export default Counter;
```

* [React-Redux Documentation Quick Start](https://react-redux.js.org/tutorials/quick-start)
    

### Redux DevTools

Redux DevTools is a powerful debugging tool that enhances the development experience with Redux.

It provides a live-editing and time-traveling environment, allowing developers to inspect every state and action payload, track state changes over time, and even "travel back in time" by reverting to previous states. This makes it easier to understand how and why your application's state changes, facilitating debugging and development.

The DevTools can be used as a browser extension, offering features like action replay and state snapshots. This tool is invaluable for developers working with Redux, as it provides deep insights into the state and behavior of their applications, greatly simplifying the debugging process.

![Redux dev tools chrome extension](https://lh3.googleusercontent.com/ji5MEDLJ4bCt4FqacHWhcAAvC2aMXs537utkDQdTaFs4T3RgyZIwJRiXX9i9_SBcmJY219PE-lsCr0OmqJ29uC7Xbw=s1280-w1280-h800 align="left")

* [Redux DevTools](https://github.com/zalmoxisus/redux-devtools-extension)
    
* [Redux DevTools Chrome Extension](https://chromewebstore.google.com/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd?pli=1)
    

## Alternatives to Redux

While Redux is popular, it's not the only option for state management in React applications. Alternatives include:

* [**Context API**:](https://legacy.reactjs.org/docs/context.html) A React feature for passing data through the component tree without having to pass props down manually.
    
* [**MobX**](https://mobx.js.org/README.html): A library that makes state management simple and scalable by transparently applying functional reactive programming.
    
* [**Recoil**](https://recoiljs.org): A state management library for React that provides several capabilities to efficiently manage state with minimal boilerplate.
    

## Redux Beyond React

Redux is not exclusively tied to React. It can be used with any UI layer or framework, including Angular, Vue, and even vanilla JavaScript. This universality is part of what makes Redux a versatile tool in a developer's arsenal.

* [Redux in Angular](https://blog.angular-university.io/angular-2-redux-ngrx-rxjs/)
    

## Redux Toolkit

Redux Toolkit is the "[official, opinionated, batteries-included toolset for efficient Redux development](https://redux.js.org/redux-toolkit/overview#what-is-redux-toolkit)." It simplifies store setup, reduces boilerplate, and even includes utilities to define reducers and perform asynchronous logic.

By incorporating best practices and simplifying common Redux patterns, RTK makes Redux development more straightforward and maintainable. It's an essential toolkit for any developer working with Redux, streamlining state management tasks and enhancing productivity.

In my professional experience, production environments are not using plain Redux anymore. They use Redux Toolkit because it greatly improves the developer experience.

* [Redux Toolkit Documentation](https://redux-toolkit.js.org)
    

[![Redux toolkit NPM page](https://cdn.hashnode.com/res/hashnode/image/upload/v1700940764188/4c9cbfda-637b-483b-846e-1c5a137a3918.png align="center")](https://www.npmjs.com/package/@reduxjs/toolkit)

---

## Further Learning

To deepen your understanding of Redux and its ecosystem, here are some resources:

* [Redux Essentials](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
    
* [Redux Advanced Tutorial](https://redux.js.org/tutorials/fundamentals/part-1-overview)
    
* [React-Redux Documentation](https://react-redux.js.org/)
    
* [Redux Toolkit Tutorial](https://redux-toolkit.js.org/tutorials/overview)
    

By embracing Redux and its alternatives, developers can choose the most suitable state management strategy for their React applications, enhancing scalability, maintainability, and developer experience.

As usual, no one explains it better than [Fireship](https://www.youtube.com/@Fireship). These 100-second videos are wicked good and I would always highly recommend them.

%[https://youtu.be/_shA5Xwe8_4?si=97XQY9fzlVFvDOB1] 

One last note. Don't forget that Redux and state management tools might be overkill! If you're building a small app or just learning, you might be able to forgo any complex libraries.

Cheers! Best of luck coding!