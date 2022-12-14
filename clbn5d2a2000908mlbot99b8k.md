# UIUC MCS - CS 435 Review - Cloud Computer Networking

## Overview

*   **TLDR:** 435 is a high workload, high reward class with a dedicated professor and practical assignments that provide a solid basis for understanding computer networking.
    
*   **Difficulty:** Hard
    
*   **Opinion:** Enjoyed
    
*   **Weekly workload:** 12 hours
    
*   **Semester taken:** Fall 2022
    

## Class Content

### Lecture Content

The class was roughly split into two components. The first half of the semester focused on routing and how the internet works. These lectures were very high quality and instructive. They cover the networking layer model, routing algorithms like BGP, transport layer TCP/UDP, and application layer functionality like DNS.

The second half of the semester focused on data center networking including, Clos topologies, virtualization, SDN, CDN, and more. There were many attached research papers explaining the academic underpinnings of these applications. This portion of the class was outdated and felt like it did not cover any innovations past the mid-2010s.

### MPs

The course had three machine problems. MP 1 was a good warmup exercise in client and server interaction. It required implementing HTTP GET requests using C socket programming.

The second MP was monstrous. Going into the class, I had seen a lot of posts online about the rigor of this assignment which I brushed off. I felt confident in my C skills and had the expectation that most embellish workloads. I was terribly wrong.

MP 2 requires building an entire router from the ground up. You must implement in C/C++ either link-state or distance-vector routing, the data and control plane, and a protocol for message exchange. My solution was almost two thousand lines of dense, multithreaded, low-level code. I would recommend brushing up on C and clearing a few weekends in preparation for this assignment.

The last MP was the easiest and shortest. The assignment simulates a data center running a streaming application, and you provide routing instructions using software-defined networking instructions. Based on the routing instructions you give the simulated data center, you see the quality of the streaming application change.

*   MP 1 - HTTP Client (5-10 hours of work and 15% of the final grade)
    
*   MP 2 - Routing (50+ hours of work and 30% of the final grade)
    
*   MP 3/4 - Software Defined Networking (5 hours of work and 15% of the final grade)
    

### Final

The final was thirty percent of the final grade and two hours long. The exam was comprehensive and open-note. It was a mixture of multiple choice, select multiple, and math calculations. The difficulty was manageable, but the assignment was unfortunately hosted on ProctorU.

## My takeaways

CS 435 was a great class. The lecture quality was solid, the assignments were a good use of time, and the professor cared a lot. The course used Campuswire as the forum, and the professor and TAs were very responsive to questions.

The one bad mark on the class was the cloud portion felt outdated and not as rigorous. The course has *cloud* in the title which offers a certain appealing buzz. I wouldn't say that it was bad content. You definitely will learn about cloud networks, but this section could use a refactor.

The class workload was highly varied. Some weeks I put zero to five hours of work in. In October, I was easily putting in 20-30 hours a week to keep up with the second MP. I would recommend staying as far ahead on lectures as possible which gives more wiggle room for when MP 2 time comes.

Overall, I would recommend this class. I learned a lot about networking, and I found the material engaging.

### Banner Credit

The banner was generated using the [UIUC LinkedIn Banner Generator](https://d7.cs.illinois.edu/projects/linkedin-banner-image/). Should you need an Illinois-themed banner for anything, it is an awesome tool.

### More Reviews

Check out [uiucmcs.org](https://uiucmcs.org/courses/CS-435-Cloud-Networking) for more reviews of MCS courses. I don't know who maintains this site, but it's a good collection of reviews from many semesters.

I have also written up a [CS 427 review](https://blog.seancoughlin.me/uiuc-mcs-cs-427-review-software-engineering#write-comment).