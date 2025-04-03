---
title: "Building an Interactive SQL Learning Platform with React, Next.js, and SQL.js"
datePublished: Thu Apr 03 2025 21:30:10 GMT+0000 (Coordinated Universal Time)
cuid: cm91vde2c000d09juaqm9e6hd
slug: building-an-interactive-sql-learning-platform-with-react-nextjs-and-sqljs
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1743715757003/582c3d3d-0d57-48a8-bf1e-21aa0171a851.png
tags: web-development, webassembly, sql, education, nextjs

---

Have you ever tried teaching someone [SQL](https://en.wikipedia.org/wiki/SQL) only to spend the first hour fighting with database installations? Or maybe you've been that frustrated beginner, wondering why you need to configure a server just to learn a query language. This exact pain point inspired me to build [SQL Playground](https://buddysql.seancoughlin.me) - a side project that lets anyone learn SQL directly in their browser, no setup required.

> **Note:** While researching after development, I discovered there was once a PHP-based tool called "[SQL Buddy](https://en.wikipedia.org/wiki/SQLBuddy)" (last updated in 2011), which was a database administration tool for MySQL and SQLite. My project, despite the similar educational focus on SQL, is entirely unrelated and takes a completely different approach as a modern, client-side learning platform rather than a database administration tool. Coincidentally, I deployed my project to [buddysql.seancoughlin.me](http://buddysql.seancoughlin.me) before learning about the old SQL Buddy tool - the URL similarity is purely accidental!

## The Vision: SQL Without the Setup Ceremony

Anyone who's taught SQL knows the first obstacle isn't the language itself—it's getting everyone to successfully install and configure a database system. This "setup tax" creates a significant barrier to entry, especially for beginners. My side project, **SQL Playground**, eliminates this friction entirely.

By leveraging SQL.js (SQLite compiled to WebAssembly) and the modern capabilities of client-side web applications, I've created an environment where learners can:

* Write SQL queries directly in their browser
    
* See results immediately with proper feedback
    
* Progress through structured lessons that build upon each other
    
* Practice on a realistic sample database
    
* Save their progress locally without requiring accounts
    

## The Technology Stack: Modern, Typed, and Component-Driven

My implementation rests on a carefully selected technology foundation that prioritizes developer experience, maintainability, and performance:

### Core Stack

* **Next.js 15** - For its robust React framework capabilities and excellent developer experience
    
* **React 19** - Providing the component-based UI architecture
    
* **TypeScript** - Adding type safety throughout the codebase
    
* **Tailwind CSS** - For utility-first styling that scales elegantly
    
* [**SQL.js**](https://sql.js.org/#/) - The magic ingredient that brings SQLite to the browser via WebAssembly
    

### Key Implementation Details

The architecture follows a clean separation of concerns:

1. **Data Layer**:
    
    * SQL.js provides a complete SQLite database engine in the browser
        
    * Custom hooks manage database initialization and query execution
        
    * Local storage persists user progress between sessions
        
2. **UI Layer**:
    
    * React components for lesson content, SQL editor, and results display
        
    * Tailwind CSS for responsive, maintainable styling
        
    * Split-view interface that keeps lessons and code editor visible simultaneously
        
3. **Learning Content**:
    
    * Structured curriculum from SQL basics to joins and aggregations
        
    * Interactive challenges with intelligent feedback
        
    * Pre-populated e-commerce database with realistic relationships
        

## The Development Journey: From Concept to Implementation

My development process followed an iterative approach, starting with the core functionality of executing SQL in the browser and gradually building up the educational framework around it.

### Step 1: Setting Up the SQL.js Environment

The first technical challenge was properly integrating SQL.js. This required:

```javascript
// Initializing SQL.js with WebAssembly
async function initializeSql() {
  const SQL = await initSqlJs({
    locateFile: file => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/${file}`
  });
  const db = new SQL.Database();
  return { SQL, db };
}
```

The SQL.js initialization was straightforward once I understood the right approach to load it as a client-side module:

### Step 2: Creating the Interactive SQL Editor

The SQL editor component became the heart of the application. It needed to:

* Allow users to write and edit SQL
    
* Execute queries against the in-memory database
    
* Display results in a readable format
    
* Provide helpful feedback on errors
    

The editor implementation uses React state to track the current query and results:

```jsx
const [query, setQuery] = useState(initialQuery || "");
const [queryResult, setQueryResult] = useState({
  results: null,
  error: null
});

const executeQuery = () => {
  try {
    const result = onExecuteQuery(query);
    setQueryResult(result);
    // ... additional processing for grading/feedback
  } catch (err) {
    console.error("Error executing query:", err);
  }
};
```

### Step 3: Building the Learning Framework

With the technical foundation in place, we focused on crafting an effective learning experience. This meant:

1. **Designing a curriculum** that progresses logically from basic SELECT statements to complex joins
    
2. **Creating a sample database** with realistic relationships between customers, products, orders, etc.
    
3. **Implementing a grading system** that can evaluate SQL queries beyond simple string matching:
    

```typescript
// Grading logic excerpt
export function gradeQuery(
  userQuery: string,
  queryResults: SqlResult[] | null,
  hasError: boolean,
  options: GradeOptions
): GradeResult {
  // Various checks for correctness...
  if (options.mustContain && options.mustContain.length > 0) {
    const normalizedUserQuery = normalizeQuery(userQuery, options.caseSensitive);
    const missingTerms = options.mustContain.filter((term) => {
      const normalizedTerm = options.caseSensitive ? term : term.toLowerCase();
      return !normalizedUserQuery.includes(normalizedTerm);
    });

    if (missingTerms.length > 0) {
      return {
        isCorrect: false,
        score: 40,
        feedback: `Your query is missing some important elements.`,
        hints: [`Make sure your query includes: ${missingTerms.join(", ")}`],
        type: "warning",
      };
    }
  }
  // Additional validation logic...
}
```

4. **Storing progress** using browser local storage:
    

```typescript
export function useLocalStorage<T>(
  key: string,
  initialValue: T
): [T, (value: T | ((val: T) => T)) => void, () => void] {
  const [storedValue, setStoredValue] = useState<T>(initialValue);

  useEffect(() => {
    try {
      const item = window.localStorage.getItem(key);
      setStoredValue(item ? JSON.parse(item) : initialValue);
    } catch (error) {
      console.error(error);
      setStoredValue(initialValue);
    }
  }, [key, initialValue]);

  // ... setter and removal functions
  
  return [storedValue, setValue, removeValue];
}
```

## Technical Challenges and Solutions

No project is without its hurdles. Here are some of the more interesting challenges I encountered:

### Challenge 1: SQL.js WebAssembly Loading

**Problem**: SQL.js requires WebAssembly, which has specific loading requirements in modern browsers.

**Solution**: I implemented a custom `useSqlJs` hook that handles script loading, WebAssembly initialization, and database setup. After exploring different approaches, I found it much simpler to load SQL.js from a CDN rather than trying to manually compile it into the application. This approach simplified dependency management and ensured the WebAssembly files were properly served:

### Challenge 2: Query Evaluation

**Problem**: Determining if a user's SQL query is "correct" is not straightforward - there are often multiple valid approaches to the same problem.

**Solution**: We developed a flexible grading system that can:

* Check for required SQL elements (SELECT, FROM, specific table names)
    
* Validate result structure (column names, row counts)
    
* Provide specific feedback based on different types of errors
    

### Challenge 3: React Hydration

**Problem**: Next.js server-side rendering doesn't play well with browser-only libraries like SQL.js.

**Solution**: We made specific components "client-only" using the "use client" directive, ensuring that SQL.js initialization only happens in the browser environment.

```typescript
"use client";

import { useState, useEffect, useRef } from "react";
// SQL.js related code...
```

## The Database Architecture: An E-commerce Playground

To provide a realistic learning environment, I created a sample e-commerce database with four key tables:

1. **Customers**: customer\_id, first\_name, last\_name, email, join\_date
    
2. **Products**: product\_id, name, description, price, category
    
3. **Orders**: order\_id, customer\_id, order\_date, total\_amount
    
4. **Order\_Items**: item\_id, order\_id, product\_id, quantity, price\_each
    

This schema allows for meaningful queries that demonstrate real-world SQL concepts:

* Basic SELECTs for product or customer information
    
* Filtering with WHERE to find products in specific categories
    
* Aggregations to calculate total sales or average prices
    
* JOINs to connect orders with customer information
    

## Lessons Learned and Future Directions

Building SQL Playground taught me several valuable lessons:

1. **WebAssembly is powerful but quirky** - The ability to run SQLite in the browser is remarkable, but WASM has its own set of challenges around loading and memory management.
    
2. **Client-side state management requires careful thinking** - Without a backend, all progress tracking had to be managed through local storage with appropriate fallbacks.
    
3. **Feedback is crucial for learning** - Simply executing queries isn't enough; meaningful feedback dramatically improves the learning experience.
    

For future enhancements, I'm considering:

* **More advanced SQL lessons** - Covering subqueries, window functions, and common table expressions
    
* **Custom database import** - Allowing users to upload their own schemas
    
* **Query visualization** - Displaying query execution plans visually
    
* **Performance optimizations** for larger datasets
    

## Conclusion: The Browser as a Learning Environment

[SQL Playground](https://buddysql.seancoughlin.me) demonstrates how modern web technologies can assist technical education. By eliminating setup friction and providing immediate feedback, I've created an environment where learning SQL becomes about the language itself, not the surrounding infrastructure.

This project showcases the power of WebAssembly to bring traditionally server-side technologies to the client, opening new possibilities for interactive learning experiences. Whether you're a SQL novice or looking to sharpen your skills, I hope this tool makes your journey more enjoyable and effective.

The code is open-source and [available on GitHub](https://github.com/Scc33/BuddySQL), and I welcome contributions from the community to enhance this learning resource further.

---

*This side project was built with React, Next.js, TypeScript, Tailwind CSS, and SQL.js, demonstrating how modern web technologies can create powerful, serverless applications for technical education.*