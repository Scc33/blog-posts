---
title: "Learn React Basics: React Router & Navigating Single Page Applications"
datePublished: Fri Nov 24 2023 18:04:16 GMT+0000 (Coordinated Universal Time)
cuid: clpcxm2vd000409l57w1wgr6g
slug: learn-react-basics-react-router-navigating-single-page-applications
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1700846561962/a8419bad-b259-4f93-b429-9ff39a9fd005.png
tags: web-development, reactjs, frontend-development, single-page-application, reacthooks

---

## Introduction

In the world of React development, understanding how to handle routing in [single-page applications (SPAs)](https://en.wikipedia.org/wiki/Single-page_application) is essential. This blog post will guide you through the fundamentals of [React Router](https://reactrouter.com/en/main), a library that enables dynamic routing in a web application.

This post is designed for developers who are familiar with React and are looking to deepen their understanding of SPAs and routing. Also note routing changed a lot from [v5 to v6](https://reactrouter.com/en/main/upgrading/v5) be wary when following online tutorials :).

## What is React Router?

[React Router](https://www.npmjs.com/package/react-router) is a standard library for routing in React. It allows you to build a single-page web application with navigation without the page refreshing as the user navigates.

React Router uses a component structure to call components, which display the appropriate information.

![React Router NPM page listing](https://cdn.hashnode.com/res/hashnode/image/upload/v1700846699325/2ba772df-9700-4bb5-a567-905ed64ae6db.png align="center")

### Why Use React Router?

* **Seamless Navigation**: It enables the navigation between different components in your application without reloading the page.
    
* **Maintains UI State**: Helps in managing the UI state consistent with the URL.
    
* **Dynamic Routing**: React Router allows dynamic routing, which means routes are defined as your application renders, not in a configuration or convention outside of a running app.
    

## Setting Up React Router

First, you need to install React Router by running `npm install react-router-dom`. This package includes the DOM bindings for the React Router. Once installed, you can start using it in your application.

## Basic Routing with React Router

Here is a simple example of how to use React Router for basic navigation.

### Step 1: Import Required Components from React Router

```typescript
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
```

### Step 2: Define Your Routes

Wrap your application in the `Router` component, then define your routes using the `Route` component. `Routes` is used to group `Route` components.

```typescript
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/about" element={<About />} />
          <Route path="/users" element={<Users />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}
```

### Step 3: Create Components for Your Routes

Define the components that correspond to your routes.

```typescript
function Home() {
  return <h2>Home</h2>;
}

function About() {
  return <h2>About</h2>;
}

function Users() {
  return <h2>Users</h2>;
}
```

And voilà you've created routes!

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1700847318179/055ca449-863e-424a-9ee4-5002fa672950.png align="center")

## Advanced Routing Concepts

* [**Nested Routing**](https://reactrouter.com/en/main/start/overview#nested-routes): This allows you to nest routes within routes, creating a hierarchy of views.
    
* [**Dynamic Routing**](https://reactrouter.com/en/main/route/route#dynamic-segments): React Router can dynamically match parts of the URL and pass them as props to components.
    
* **Protected Routes**: Implementing authentication in your routes to control access to certain parts of your app.
    
* [**Code Splitting**](https://blog.seancoughlin.me/learn-react-basics-code-splitting): Consider code-splitting your routes for best performance.
    

## Best Practices

* Keep your routes structured and predictable.
    
* Utilize [`useParams`](https://reactrouter.com/en/main/hooks/use-params) and other hooks for more dynamic and complex routing scenarios.
    
* Always test your routes and navigation thoroughly. These can be difficult to unit test so acceptance and end-to-end style tests written in a library like [Playwright](https://playwright.dev) can be helpful.
    

## Conclusion

React Router plays a vital role in building SPAs by enabling efficient and smooth navigation.

Understanding how to implement routing effectively can greatly enhance the user experience and the performance of your React application.

## Further Reading and Documentation

* Official React Router Documentation: [React Router - Documentation](https://reactrouter.com/)
    

Routing in React, especially with React Router, opens up a world of possibilities for building dynamic, user-friendly SPAs. With this guide, you are well on your way to mastering this essential aspect of React development.

Happy coding!