---
title: "Learn React Basics: Code Splitting"
datePublished: Fri Nov 24 2023 16:56:05 GMT+0000 (Coordinated Universal Time)
cuid: clpcv6est000308kt9n0o8o32
slug: learn-react-basics-code-splitting
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1700839882500/c6ca2a47-ab15-451e-a37e-33291c0d496e.png
tags: tutorial, web-development, reactjs, typescript, vite

---

## Introduction

For developers working on increasingly complex React applications, performance optimization is key to a smooth user experience. An effective method for enhancing performance in these applications is **code splitting**.

This guide is crafted for those with basic JavaScript and React backgrounds, providing an in-depth understanding of code splitting.

## What is Code Splitting?

Code splitting in React is a technique that divides your application's code into various bundles. These bundles can then be loaded on demand or in parallel, rather than loading the entire application bundle at once.

### The Importance of Code Splitting

* **Enhanced Performance**: It ensures users aren't waiting for unnecessary code to load, leading to faster initial page load times.
    
* **Optimized Resource Use**: This approach minimizes the code transferred over the network, enhancing load times and conserving bandwidth.
    
* **Improved User Experience**: Especially beneficial for users on slower networks or devices, it ensures quicker access to critical application features.
    

## Ideal Scenarios for Code Splitting

1. **Large Components**: Split off components that are large and not required for the initial render.
    
2. **Conditional Components**: Components that appear only in certain scenarios, such as modal windows.
    
3. **Routes**: Implementing code splitting at different pages or routes in your application (this is probably the easiest and most common usage).
    

## Implementing Code Splitting in React

React facilitates code splitting with the `lazy()` function and the `Suspense` component. This functionality is built right into React.

### Understanding lazy and Suspense

`lazy` allows you to define a component that will be dynamically loaded.

```typescript
import { lazy, Suspense } from 'react';

const OtherComponent = lazy(() => import('./OtherComponent'));

function MyComponent() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <OtherComponent />
    </Suspense>
  );
}
```

In this setup, `OtherComponent` is loaded only when `MyComponent` gets rendered.

### The Role of Suspense

The `Suspense` component wraps lazy components and specifies a loading state (using the `fallback` prop) to show until the lazy component is loaded. It's crucial for handling the loading state gracefully.

### Route-based Code Splitting

You can split code based on routes using libraries like `react-router-dom`.

```typescript
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { lazy, Suspense } from 'react';

const Home = lazy(() => import('./routes/Home'));
const About = lazy(() => import('./routes/About'));

function App() {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Switch>
          <Route exact path="/" component={Home}/>
          <Route path="/about" component={About}/>
        </Switch>
      </Suspense>
    </Router>
  );
}
```

Here, `Home` and `About` components are only loaded when the user navigates to the respective routes.

### Practical Example

First, I'll create a very basic app that includes a bunch of routes that all point to the same component.

```typescript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Router>
      <React.Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/1" element={<App />} />
          <Route path="/2" element={<App />} />
          <Route path="/3" element={<App />} />
          <Route path="/4" element={<App />} />
          <Route path="/5" element={<App />} />
          <Route path="/6" element={<App />} />
          <Route path="/7" element={<App />} />
          <Route path="/8" element={<App />} />
          <Route path="/9" element={<App />} />
          <Route path="/10" element={<App />} />
        </Routes>
      </React.Suspense>
    </Router>
  </React.StrictMode>,
)
```

Upon building this application I get an output `dist` file that contains all the minified code bundle required to deploy and run the application. For this example, I have used [Vite](https://blog.seancoughlin.me/maximizing-web-development-efficiency-a-comprehensive-guide-to-vite), but any build tool would work.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1700840258615/18ef760b-1318-4060-ab55-17bd51b2a715.png align="center")

Now we add a lazy function and lazy import the same `App` component. Once again I'll build this application using Vite.

```typescript
import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { lazy } from 'react'

const App = lazy(() => import('./App.tsx'))

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Router>
      <React.Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/1" element={<App />} />
          <Route path="/2" element={<App />} />
          <Route path="/3" element={<App />} />
          <Route path="/4" element={<App />} />
          <Route path="/5" element={<App />} />
          <Route path="/6" element={<App />} />
          <Route path="/7" element={<App />} />
          <Route path="/8" element={<App />} />
          <Route path="/9" element={<App />} />
          <Route path="/10" element={<App />} />
        </Routes>
      </React.Suspense>
    </Router>
  </React.StrictMode>,
)
```

Now notice with this build we see two new files generated. `App-cfVfczdt.css` and `dist/assets/App-_KEqqJC2.js`. These files contain the required code to drive the `App` component. They will only be sent to the client when that component needs to be loaded.

Many routes point to `App`, but the underlying component is the same for all of these routes so only one new code chunk is created.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1700840407473/aa070635-9717-4bd0-92f2-e7bec074ab96.png align="center")

This is a small example, but imagine you have some big page that often isn't viewed by a user. If that page is code split with lazy loading you can save sending it. That will shrink bundle sizes and speed up your client load times.

## Best Practices

* **Performance Testing**: Use tools like Chrome DevTools to evaluate the performance impact.
    
* **Avoid Excessive Splitting**: Too much splitting can lead to many small files, causing performance issues (mostly latency) due to numerous requests.
    
* **Utilize Bundling Tools**: Tools like Webpack or [Parcel](https://parceljs.org/docs/) are essential for effective bundling and splitting strategies.
    

## Conclusion

Code splitting is a potent technique for optimizing React application performance. Proper understanding and implementation can lead to a significantly better user experience.

## Additional Resources

* React Documentation on Code Splitting: [React Docs - Code Splitting](https://reactjs.org/docs/code-splitting.html)
    
* Webpack's Guide on Code Splitting: [Webpack - Code Splitting](https://webpack.js.org/guides/code-splitting/)
    
* Rollup's Guide on Code Splitting: [Tutorial | Rollup - Code Splitting](https://rollupjs.org/tutorial/#code-splitting)
    
* Using Chrome DevTools for Performance Analysis: [Chrome DevTools - Performance](https://developer.chrome.com/docs/devtools/performance/)
    

Implementing code splitting in your React applications can result in a noticeable improvement in performance, especially for large-scale projects. Best of luck!