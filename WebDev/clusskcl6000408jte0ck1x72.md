---
title: "Accelerating Frontend Development with Bun and Vite"
seoTitle: "Boost Frontend Speed: Bun & Vite"
seoDescription: "Discover how to supercharge your frontend development using Bun for runtime, Vite as your build tool, and Vitest as your test runner."
datePublished: Tue Apr 09 2024 19:45:47 GMT+0000 (Coordinated Universal Time)
cuid: clusskcl6000408jte0ck1x72
slug: accelerating-frontend-development-with-bun-and-vite
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1712690735632/626dfa33-f10d-4295-b416-de02399370b4.webp
tags: web-development, frontend-development, vite, bun, vitest

---

## Rolling with Bun

In the vibrant world of web development, the quest for more efficient tools and workflows is unending. Enter [Bun](https://bun.sh), a modern JavaScript runtime that’s piquing the interest of developers for its all-in-one approach. But what exactly makes Bun a game-changer, especially for frontend development?

At its core, Bun is designed to speed up JavaScript and TypeScript application development by [integrating several tools into one cohesive unit](https://blog.seancoughlin.me/bun-the-comprehensive-toolkit-for-javascript-and-typescript): a runtime, a package manager, a bundler, and a test runner. This consolidation aims to streamline development processes, reduce setup times, and, most importantly, enhance performance.

## Do you need Vite if you have Bun?

[Bun's integrated bundler](https://bun.sh/docs/bundler), while powerful, hasn’t been fully optimized for frontend tooling. Specifically, [it lacks features](https://x.com/youyuxi/status/1701039789741629721) like control over chunk splitting, which is crucial for optimizing load times of client-side applications. It also lacks a dev server which makes local development really difficult.

This limitation might suggest a gap in Bun’s utility for frontend projects; however, this is where the synergy with [Vite](https://vitejs.dev) comes into play. Vite, [a build tool renowned for its fast unbundled development and flexible production bundling](https://blog.seancoughlin.me/maximizing-web-development-efficiency-a-comprehensive-guide-to-vite?source=more_series_bottom_blogs), complements Bun’s capabilities by addressing its frontend tooling limitations.

Using Vite atop Bun, instead of the traditional [Node.js runtime](https://nodejs.org/en), can significantly boost performance. Vite leverages Bun’s fast execution environment for running its build processes, which can speed up tasks like dependency installation and development server startup.

This combination ensures that developers can enjoy Vite's rapid development feedback loop and optimized bundling for production, all while running on Bun’s high-performance runtime.

Check out this great article if you want to learn more about Vite vs. Bun: "[Why use Vite when Bun is also a bundler? - Vite vs. Bun](https://dev.to/this-is-learning/why-use-vite-when-bun-is-also-a-bundler-vite-vs-bun-2723)."

## Baking an App with Bun and Vite

Bun allows you to scaffold an app with their [baked in templating commands](https://bun.sh/docs/cli/init). This is a really easy place to start for launching an app.

```bash
$ bun create vite my-app
✔ Select a framework: › React (or your choice of Svelte, Vue, etc.)
✔ Select a variant: › TypeScript
Scaffolding project in /path/to/my-app...
```

![Terminal output for starting up an app with Bun and templates](https://cdn.hashnode.com/res/hashnode/image/upload/v1712690150114/693fb22a-ca56-495f-9f23-bcbb61300f57.png align="center")

After scaffolding your project, installing dependencies with Bun showcases the first taste of speed improvement:

```bash
cd my-app
bun install
```

![Terminal output for downloading dependencies with Bun](https://cdn.hashnode.com/res/hashnode/image/upload/v1712689618997/ce7a2c07-a7bf-4402-b61e-64d2218e719d.png align="center")

To harness Bun for running Vite, modify the `"dev"` script in your `package.json`:

```json
"scripts": {
  "dev": "bunx --bun vite --open",
  "build": "vite build",
  "serve": "vite preview"
},
```

![Terminal output for starting an app with Bun](https://cdn.hashnode.com/res/hashnode/image/upload/v1712689700290/94f2d4e4-11a2-47db-9a0b-c4d19e1c9702.png align="center")

This setup not only simplifies command execution but also aligns Vite’s development environment with Bun’s runtime, marrying Vite's frontend prowess with Bun's backend efficiency.

Since Bun's philosophy is being the best all-in-one tool. You can run all your scripts using Bun. Run `bun build` to build your application or `bun dev` to start the dev server.

## Bun and Running Tests

Bun includes its test runner, but for frontend projects, [especially ones utilizing Vite](https://blog.seancoughlin.me/vitest-vs-jest-the-new-javascript-testing-framework), [Vitest](https://vitest.dev) running on Bun provides a more robust solution. Although Bun’s test runner shows promise, its current state lacks the full suite of features that frontend tests often require. By leveraging Vitest, developers can utilize a familiar Jest-like API with the added speed benefits of Bun’s runtime, ensuring tests are both fast and comprehensive.

Looking forward, there’s potential for Bun to evolve into a more integrated solution for frontend testing. However, until then, utilizing Vitest for testing strikes a balance between speed and functionality, offering a pragmatic approach to modern web development testing needs.

You can follow the progress of `bun test` with [Bun's open GitHub issue](https://github.com/oven-sh/bun/issues/1825).

## My Experience Using Bun, Vite, and Vitest

Embarking on the journey to enhance [my personal website](https://seancoughlin.me), I decided to make a pivotal transition from using Node/Yarn to embracing Bun for the entire development lifecycle. This shift, documented in my latest [Pull Request (PR)](https://github.com/Scc33/Scc33.github.io/pull/207), encapsulates a broad overhaul—from the build process and [continuous integration (CI) setup](https://github.com/Scc33/Scc33.github.io/pull/209) to tooling— all now reliant on Bun. This decision stemmed from a curiosity to deepen my understanding of package managers and JavaScript runtimes, alongside Bun's reputation for speed and innovation.

My initial impressions of Bun have been overwhelmingly positive. The allure of Bun is not just its comprehensive toolkit, which seamlessly amalgamates the roles of a runtime, package manager, and more into a singular, cohesive entity. What truly sets it apart is the remarkable speed enhancement it offers, particularly in download times—a difference that's palpable.

Vite operates marvelously with Bun, replacing Node in our stack, and notably speeds up the execution of installations and development workflows. Although Bun harbors its own test runner, I opted for Vitest running on Bun’s runtime for a more robust testing solution. This choice reflects a cautious optimism about Bun’s future as a comprehensive test runner, acknowledging its current nascent stage in this domain.

Please note that I'm just a solo developer working on a small hobby project with simple requirements. My experience has been positive, but it's anecdotal and I don't have enough evidence right now to say how larger projects will perform with Bun.

## Conclusion

This guide is merely a starting point for developers looking to leverage the speed of Bun and the flexibility of Vite for frontend development. As both tools continue to evolve, they promise to be a formidable duo for building efficient, high-performance web applications.

* For more detailed information on Vite and its capabilities, the [Vite documentation](https://vitejs.dev/guide/) offers extensive guides and tutorials.
    
* This guide was inspired by the [Bun documentation](https://bun.sh/guides/ecosystem/vite) on using Vite and Bun.