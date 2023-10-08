---
title: "Publishing a SvelteKit App to GitHub Pages"
datePublished: Sun Oct 08 2023 14:08:35 GMT+0000 (Coordinated Universal Time)
cuid: clnhjhyga000g08jrelbdbtit
slug: publishing-a-sveltekit-app-to-github-pages
tags: github, git, svelte, static-website, sveltekit

---

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1696773973033/9dbab7b7-9cab-4942-b35d-908a6f3d6f75.png align="center")

### What is SvelteKit?

[SvelteKit](https://kit.svelte.dev/docs/introduction) is a framework for building web applications that are built on top of Svelte, a modern JavaScript UI library. Unlike traditional frameworks that operate mainly on the client side, SvelteKit provides a unified approach to building apps that can be rendered on the server, statically generated at build time, or even rendered client-side. It comes with built-in features like routing, layouts, and server-side rendering (SSR), making it a comprehensive solution for building everything from small, static websites to large, complex web applications. With a focus on performance and a simplified developer experience, SvelteKit aims to streamline the process of building robust and scalable web apps.

### Build a SvelteKit App!

This tutorial just spells out how to configure and deploy a SvelteKit web app to GitHub Pages. If you never have created a Svelte application before, the [docs](https://kit.svelte.dev/docs/creating-a-project) are great!

### Configuring SvelteKit for GitHub Pages

1. Build your application using Svelte and SvelteKit
    
2. GitHub Pages is a static site host. Therefore, we need to install the [Svelte static site adapter](https://kit.svelte.dev/docs/adapters).
    

```bash
# NPM install
npm i -D @sveltejs/adapter-static
# YARN install
yarn add @sveltejs/adapter-static --dev
```

1. After installing the static adapter, at that to your `svelte.config.js`.
    

```javascript
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    kit: {
        appDir: 'app', // Required as the default is _app
        adapter: adapter()
    },
    preprocess: vitePreprocess()
};
export default config;
```

1. Add an app directory output to the `svelte.config.js`. The typical output is `_app` so I think something like `app` makes sense but this can be anything without an underscore. GitHub Pages cannot serve content from directories with special characters like underscores.
    
2. If you are deployed to `https://[username].github.io` step 2 is all that is required for configuration. If you are deploying to `https://[username].github.io/your-repo-name` you will need to supply a `paths.base`. See the [SvelteKit docs](https://kit.svelte.dev/docs/adapter-static#github-pages) for more details.
    

```javascript
import adapter from '@sveltejs/adapter-static';

const dev = process.argv.includes('dev');

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter(),
		paths: {
			base: dev ? '' : process.env.BASE_PATH,
		}
	}
};
```

1. Add an empty `.nojekyll` file in your `static` folder to prevent GitHub Pages provided Jekyll configurations from managing the site.
    

![No-Jekyll](https://cdn.hashnode.com/res/hashnode/image/upload/v1696772807659/1143e923-067a-4f8c-bf25-72291a131ac9.png align="center")

1. Manually build and push your output directory to GitHub or use a tool like [gh-pages](https://blog.seancoughlin.me/deploying-to-github-pages-using-gh-pages).
    
    ```json
    "scripts": {
        "build": "vite build"
    }
    ```
    
2. Configure GitHub pages to [deploy your app with the repo settings](https://blog.seancoughlin.me/building-a-personal-website-with-github-pages).
    
    ![GitHub Pages configurations](https://cdn.hashnode.com/res/hashnode/image/upload/v1696705930160/3cd85bf6-4b6d-4059-9259-ea4da8a0ac73.png?auto=compress,format&format=webp align="left")
    
    And that is it! You should be good to go and see your site live! This is how I deploy my personal site [seancoughlin.me](https://seancoughlin.me). If you want to check out a code example you can find that in my [Git repo](https://github.com/Scc33/Scc33.github.io).