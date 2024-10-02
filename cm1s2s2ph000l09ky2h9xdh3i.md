---
title: "Multithreading in Java and Spring Boot"
seoTitle: "Multithreading in Java and Spring Boot: A Practical Guide"
seoDescription: "Learn how to master multithreading in Java and Spring Boot. Explore essential techniques, from basic thread management in Java to asynchronous programming."
datePublished: Wed Oct 02 2024 16:21:54 GMT+0000 (Coordinated Universal Time)
cuid: cm1s2s2ph000l09ky2h9xdh3i
slug: multithreading-in-java-and-spring-boot
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1727885248978/745b304a-46fb-4dce-a430-31dcefcf51ea.webp
tags: spring, java, performance, springboot, threads

---

## Introduction

In today's world of high-performance applications, responsiveness, and scalability are critical. Whether you're building a web application, processing large datasets, or handling multiple tasks simultaneously, having a solid understanding of [multithreading](https://en.wikipedia.org/wiki/Multithreading_\(computer_architecture\)) can dramatically improve the efficiency and performance of your code.

Multithreading is a key tool in a developer's arsenal, and while Java has long supported multithreading, Spring Boot takes it further by simplifying asynchronous processing. In this guide, we’ll explore how to implement multithreading in Java and dive into Spring Boot's built-in features for managing concurrency, helping you streamline your application development.

## What is Multithreading?

At its core, multithreading allows a program to run multiple parts of its code simultaneously. A [**thread** is the smallest unit of a process](https://en.wikipedia.org/wiki/Thread_\(computing\)), and multithreading involves running multiple threads at the same time, enabling the parallel execution of tasks. This can lead to better performance and responsiveness, especially in resource-intensive applications or those that need to handle many simultaneous operations.

**Benefits of Multithreading:**

* **Improved Performance**: By dividing a task across multiple threads, work can be done faster than running it in a single thread.
    
* **Enhanced Responsiveness**: Applications, especially GUIs or web servers, can remain responsive while handling long-running operations in the background.
    
* **Better Utilization of Resources**: Modern CPUs have multiple cores, and multithreading ensures that they are all used efficiently.
    

However, multithreading is not without its challenges. Threads need to coordinate when accessing shared resources, and improper handling can lead to issues like deadlocks or race conditions. That’s why understanding the underlying mechanisms and using the right tools is essential for successful multithreaded programming.

## Overview of Multithreading in Java

Java has been built with multithreading at its core, and it provides multiple ways to create and manage threads. Whether you're handling simple tasks or complex concurrent operations, Java offers flexibility through various APIs. In this section, we'll cover some of the most common methods for implementing multithreading in Java.

### 1\. Creating Threads in Java

There are two primary ways to create threads in Java: [by extending the `Thread` class](https://www.geeksforgeeks.org/multithreading-in-java/) or by implementing the `Runnable` interface.

**1.1 Extending the** `Thread` Class

One of the simplest ways to create a thread is to extend the `Thread` class and override its `run()` method, which defines the code that the thread will execute.

**Example:**

```java
public class MyThread extends Thread {
    public void run() {
        // Code to be executed in the new thread
        for (int i = 0; i < 5; i++) {
            System.out.println("Thread " + Thread.currentThread().getId() + ": " + i);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread1 = new MyThread();
        MyThread thread2 = new MyThread();
        thread1.start(); // Starts a new thread
        thread2.start(); // Starts another thread
    }
}
```

In this example, two threads (`thread1` and `thread2`) are created, and both execute the code inside the `run()` method concurrently. The `start()` method is used to begin execution in a new thread.

**1.2 Implementing the** `Runnable` Interface

Another more flexible way to create a thread is by implementing the [`Runnable` interface](https://docs.oracle.com/javase/8/docs/api/?java/lang/Runnable.html). This allows your class to extend other classes while still being used in a thread. You pass the `Runnable` object to a `Thread` object, which runs the code in the `run()` method.

**Example:**

```java
public class MyRunnable implements Runnable {
    public void run() {
        // Code to be executed in the new thread
        for (int i = 0; i < 5; i++) {
            System.out.println("Thread " + Thread.currentThread().getId() + ": " + i);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread1 = new Thread(new MyRunnable());
        Thread thread2 = new Thread(new MyRunnable());
        thread1.start(); // Starts a new thread
        thread2.start(); // Starts another thread
    }
}
```

By using `Runnable`, we decouple the thread behavior from the actual thread creation, making the code more modular and flexible.

**1.3 Using Lambda Expressions (Java 8+)**

[With the introduction of Java 8](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html), [you can use lambda expressions](https://stackoverflow.com/questions/66611118/what-is-best-way-of-implementing-multithreading-in-java) to simplify the implementation of the `Runnable` interface. This results in more concise and readable code.

**Example:**

```java
public class Main {
    public static void main(String[] args) {
        Runnable task = () -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Thread " + Thread.currentThread().getId() + ": " + i);
            }
        };

        Thread thread1 = new Thread(task);
        Thread thread2 = new Thread(task);
        thread1.start();
        thread2.start();
    }
}
```

This approach significantly reduces the amount of boilerplate code, making multithreading easier and faster to implement.

### **2\. Managing Threads with ExecutorService**

When working with multiple threads, manually managing thread creation can become cumbersome. Java provides the [`ExecutorService` interface](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/concurrent/ExecutorService.html), which offers a flexible and efficient way to manage thread pools.

[**ExecutorService** manages a pool of threads](https://www.baeldung.com/java-executor-service-tutorial) that can be reused to execute multiple tasks, instead of creating a new thread for each task. This reduces the overhead of thread creation and improves performance.

**Example:**

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExecutorExample {
    public static void main(String[] args) {
        // Create a thread pool with 2 threads
        ExecutorService executor = Executors.newFixedThreadPool(2);

        for (int i = 0; i < 5; i++) {
            executor.submit(() -> {
                System.out.println("Thread " + Thread.currentThread().getId() + " is running");
            });
        }

        // Shutdown the executor service
        executor.shutdown();
    }
}
```

In this example, an `ExecutorService` is created with a fixed pool of 2 threads. The `submit()` method is used to assign tasks to the thread pool, and the executor manages the thread lifecycle for you. Once all tasks are completed, the `shutdown()` method is called to stop the executor.

### **3\. Synchronization and Thread Safety**

Multithreading introduces the need for synchronization when multiple threads access shared resources. Without proper synchronization, data corruption or inconsistent states can occur. Java provides the [`synchronized` keyword](https://stackoverflow.com/questions/1085709/what-does-synchronized-mean) to ensure that only one thread at a time can access critical sections of code.

**Example of Synchronization:**

```java
public class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();

        Thread thread1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        });

        Thread thread2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        });

        thread1.start();
        thread2.start();

        thread1.join(); // Wait for thread1 to finish
        thread2.join(); // Wait for thread2 to finish

        System.out.println("Final count: " + counter.getCount());
    }
}
```

In this example, the `increment()` method is synchronized to ensure that only one thread can modify the `count` variable at a time, preventing race conditions.

## Multithreading in Spring and Spring Boot

Spring Framework provides powerful tools for handling multithreading and asynchronous tasks. By abstracting much of the complexity around thread management, Spring simplifies the process of running tasks concurrently and provides [built-in mechanisms to handle asynchronous](https://spring.io/guides/gs/async-method) operations with minimal boilerplate.

### 1\. Introduction to Spring's Asynchronous Features

Spring allows you to create and manage asynchronous tasks with a variety of abstractions. The most common approach is using the `@Async` annotation, but Spring also provides support for more complex scenarios, such as scheduled tasks, task executors, and even reactive programming for non-blocking I/O.

Spring Boot, in particular, makes it easy to configure and use these features without needing complex setup. Let's dive into how to implement multithreading using Spring Boot.

### 2\. Implementing Asynchronous Methods with `@Async`

Spring's [`@Async` annotation](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/scheduling/annotation/Async.html) is a simple yet powerful way to run methods asynchronously. When applied to a method, it allows the method to execute in a separate thread, freeing up the main thread to continue executing other tasks. This is particularly useful for long-running operations that you don't want to block the main flow of your application.

**Enabling Asynchronous Execution:** To use the `@Async` annotation, you must first [enable async support in your Spring Boot application by adding the `@EnableAsync` annotation to a configuration class](https://www.baeldung.com/spring-async).

**Example:**

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableAsync;

@Configuration
@EnableAsync
public class AsyncConfig {
}
```

Once you've enabled asynchronous support, you can apply the `@Async` annotation to any method in a Spring-managed bean.

**Example:**

```java
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.concurrent.CompletableFuture;

@Service
public class AsyncService {

    @Async
    public CompletableFuture<String> performAsyncTask() {
        try {
            // Simulate a long-running task
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return CompletableFuture.completedFuture("Task completed");
    }
}
```

In the example above, the `performAsyncTask()` method is marked with `@Async`, meaning that when this method is called, Spring will automatically execute it in a separate thread from the thread pool, allowing the main thread to continue without waiting for the task to complete.

### 3\. Customizing Async Behavior with `ThreadPoolTaskExecutor`

By default, Spring Boot uses a simple thread pool when executing asynchronous tasks. However, in a production environment, you may want to customize the thread pool to suit your application's needs. [Spring Boot provides the `ThreadPoolTaskExecutor`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/scheduling/concurrent/ThreadPoolTaskExecutor.html) for this purpose, which allows you to configure thread pool parameters such as core pool size, max pool size, and queue capacity.

**Example: Custom Thread Pool Configuration**

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.task.TaskExecutor;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.scheduling.annotation.EnableAsync;

@Configuration
@EnableAsync
public class AsyncConfig {

    @Bean(name = "taskExecutor")
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(2);
        executor.setMaxPoolSize(5);
        executor.setQueueCapacity(500);
        executor.setThreadNamePrefix("MyExecutor-");
        executor.initialize();
        return executor;
    }
}
```

In this example, the `ThreadPoolTaskExecutor` is configured with:

* **Core pool size**: Minimum number of threads that will always be available.
    
* **Max pool size**: Maximum number of threads that can be created.
    
* **Queue capacity**: How many tasks can be queued before new threads are created.
    
* **Thread name prefix**: Custom naming pattern for threads in this executor.
    

To use this custom thread pool, the method annotated with `@Async` will automatically utilize the `taskExecutor` defined in the configuration.

Here’s a quick table summarizing good choices for `TaskExecutor` configuration parameters based on different use cases:

| **Use Case** | **Core Pool Size** | **Max Pool Size** | **Queue Capacity** | **Description** |
| --- | --- | --- | --- | --- |
| **Short, Non-blocking Tasks (e.g., logging, simple notifications)** | 2 | 5 | 50 | Small pool size is sufficient since tasks are short-lived and non-blocking. A moderate queue allows efficient task handling without overloading the system. |
| **I/O Bound Tasks (e.g., file reading, database queries)** | 4 | 10 | 100 | For I/O-bound tasks, increase pool size to handle more tasks concurrently. A larger queue ensures tasks can be queued efficiently during I/O waits. |
| **CPU-Intensive Tasks (e.g., complex calculations, image processing)** | \# of CPU cores | \# of CPU cores | 0 or very small (1-10) | Set core pool size and max pool size to the number of CPU cores, ensuring optimal CPU utilization. Avoid large queues to prevent task delays and bottlenecks. |
| **Long-running Blocking Tasks (e.g., external API calls, large data processing)** | 5 | 20 | 200 | Higher pool and queue sizes help handle blocking tasks efficiently, ensuring the system can handle spikes in tasks without being overwhelmed. |
| **High Concurrency (e.g., web applications handling thousands of requests)** | 10 | 50 | 500+ | In high-concurrency environments, a larger pool and queue size ensure that the system can handle many requests concurrently without running out of resources. |

**General Guidelines:**

* **Core Pool Size**: The number of threads that are always available (even if idle). A good default is equal to the number of CPU cores for CPU-bound tasks.
    
* **Max Pool Size**: The maximum number of threads the pool can create. Increase this if tasks are often blocked or waiting on external resources.
    
* **Queue Capacity**: The number of tasks that can be queued before new threads are created. For short tasks, a larger queue is efficient. For long tasks, consider a smaller queue to avoid long delays.
    

### 4\. Scheduling Tasks with `@Scheduled`

Another powerful feature in Spring Boot is the ability to schedule tasks to run at specific intervals or times using the [`@Scheduled` annotation](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/scheduling/annotation/Scheduled.html). This is useful for running background jobs, such as database cleanup, report generation, or sending periodic notifications.

**Enabling Scheduling:** To use the `@Scheduled` annotation, you must enable scheduling by adding `@EnableScheduling` to a configuration class.

**Example:**

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
}
```

Now, you can create methods that are scheduled to run at fixed intervals, using cron expressions, or after a specific delay.

**Example:**

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class ScheduledTask {

    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("Task executed every 5 seconds");
    }

    @Scheduled(cron = "0 0 12 * * ?")
    public void performTaskAtNoon() {
        System.out.println("Task executed at 12 PM every day");
    }
}
```

In this example, the `performTask()` method runs every 5 seconds, while `performTaskAtNoon()` runs every day at 12 PM. Spring handles the scheduling internally, ensuring that the tasks are executed on time without blocking the main application thread.

### 5\. TaskExecutor for Higher-Level Abstraction

[Spring provides the `TaskExecutor` interface as a higher-level abstraction for managing asynchronous tasks](https://docs.spring.io/spring-framework/reference/integration/scheduling.html). This allows you to execute `Runnable` tasks without dealing with the lower-level details of thread management.

**Example:**

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.task.TaskExecutor;
import org.springframework.stereotype.Service;

@Service
public class TaskExecutorService {

    @Autowired
    private TaskExecutor taskExecutor;

    public void executeAsyncTask() {
        taskExecutor.execute(() -> {
            System.out.println("Task executed asynchronously using TaskExecutor");
        });
    }
}
```

Here, the `TaskExecutor` interface is injected, and the `executeAsyncTask()` method uses it to execute a task asynchronously. This provides a simple and clean way to run background tasks without needing to create new threads manually.

### 6\. Reactive Programming with WebFlux

For more advanced use cases, Spring Boot also supports [**reactive programming** with **Spring WebFlux**](https://docs.spring.io/spring-framework/reference/web/webflux.html). This is particularly useful for non-blocking, event-driven applications that need to handle a large number of concurrent requests without consuming excessive system resources.

**Example:**

```java
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import java.time.Duration;

@RestController
public class ReactiveController {

    @GetMapping("/reactive")
    public Flux<String> getReactiveStream() {
        return Flux.just("Message 1", "Message 2", "Message 3")
                   .delayElements(Duration.ofSeconds(1));
    }
}
```

In this example, a `Flux` (a reactive stream) is returned, which emits a series of messages with a delay of 1 second between each. This non-blocking model ensures that the server can handle other requests while the stream is being processed.

## Thread Safety in Spring Boot

When dealing with multithreading in Spring Boot, thread safety is a critical consideration, especially since Spring beans are typically singleton by default. This means that multiple threads could access the same instance of a bean simultaneously, potentially leading to data corruption or inconsistent states if shared resources are not handled correctly.

#### **Common Thread Safety Issues:**

1. [**Race Conditions**](https://en.wikipedia.org/wiki/Race_condition): Occurs when two or more threads access shared data and try to change it at the same time.
    
2. [**Deadlocks**](https://en.wikipedia.org/wiki/Deadlock_\(computer_science\)): Happen when two or more threads are blocked forever, waiting for each other to release resources.
    
3. **Memory Consistency Errors**: Result when multiple threads access shared variables without proper synchronization.
    

#### **Handling Thread Safety in Spring Boot:**

1. **Use of** `synchronized` Keyword: You can synchronize methods or code blocks to ensure that only one thread can execute them at a time, preventing race conditions.
    
    **Example:**
    
    ```java
    @Service
    public class CounterService {
        private int count = 0;
    
        public synchronized void increment() {
            count++;
        }
    
        public synchronized int getCount() {
            return count;
        }
    }
    ```
    
    In this example, both `increment()` and `getCount()` are synchronized to ensure that the counter is safely updated and retrieved, preventing multiple threads from corrupting the shared variable.
    
2. **Atomic Variables**: For lightweight thread-safe operations, you can use Java's `Atomic` classes (e.g., `AtomicInteger`, `AtomicBoolean`), which [provide methods for thread-safe manipulation of variables without the overhead of synchronization](https://stackoverflow.com/questions/16729364/atomic-operations-and-multithreading).
    
    **Example:**
    
    ```java
    import java.util.concurrent.atomic.AtomicInteger;
    
    @Service
    public class AtomicCounterService {
        private AtomicInteger count = new AtomicInteger(0);
    
        public void increment() {
            count.incrementAndGet();
        }
    
        public int getCount() {
            return count.get();
        }
    }
    ```
    
3. **ThreadLocal Variables**: [`ThreadLocal` variables](https://www.baeldung.com/java-threadlocal) allow you to store data that is specific to the current thread, ensuring that each thread has its own copy of the variable. This is useful for managing thread-specific data like request contexts.
    
    **Example:**
    
    ```java
    public class UserContext {
        private static final ThreadLocal<String> userContext = new ThreadLocal<>();
    
        public static void setUser(String user) {
            userContext.set(user);
        }
    
        public static String getUser() {
            return userContext.get();
        }
    
        public static void clear() {
            userContext.remove();
        }
    }
    ```
    

By carefully managing shared resources and considering thread safety in your Spring Boot applications, you can avoid common pitfalls like race conditions and data inconsistency.

## Conclusion

Multithreading is an essential tool for building high-performance, responsive applications, both in Java and Spring Boot. Starting with core Java concepts like extending `Thread`, implementing `Runnable`, and using `ExecutorService`, you can efficiently handle concurrent tasks. Spring Boot makes multithreading even easier by abstracting much of the complexity, offering tools like the `@Async` annotation, custom thread pools via `ThreadPoolTaskExecutor`, and scheduling tasks with `@Scheduled`.

Whether you're managing simple asynchronous tasks or building large, scalable systems that need to handle thousands of concurrent requests, the right use of multithreading can significantly improve your application's performance and scalability. Understanding thread safety and using the appropriate tools (such as synchronization, atomic variables, or `ThreadLocal`) ensures that your application functions reliably under concurrent loads.

With the knowledge gained from this guide, you're well-equipped to implement multithreading in your Java and Spring Boot applications efficiently and safely.

### Further Reading

* [Java Concurrency](https://docs.oracle.com/javase/tutorial/essential/concurrency/index.html)
    
* [Java Memory Model](https://en.wikipedia.org/wiki/Java_memory_model)
    
* [Understanding Concurrency vs. Parallelization](https://blog.seancoughlin.me/understanding-concurrency-vs-parallelization)