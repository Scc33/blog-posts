---
title: "Deploying to GitHub Pages using gh-pages"
datePublished: Sat Oct 07 2023 19:26:50 GMT+0000 (Coordinated Universal Time)
cuid: clngffdof000008lagose631r
slug: deploying-to-github-pages-using-gh-pages
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1696706645626/84fad957-8e66-4090-8971-e3d2cd9fd38f.png
tags: git, npm, yarn, github-pages, cicd-cjy1vtdk2005kjjs17n8couc3

---

## What is GitHub Pages?

[GitHub Pages](https://pages.github.com) is a static site hosting service offered by GitHub that takes files straight from a repository on GitHub and publishes them as a website. It's designed to host your personal, organizational, or project pages directly from a GitHub repository. GitHub Pages supports static HTML, CSS, and JavaScript files, as well as Jekyll, a static site generator that converts Markdown files to HTML. The service is commonly used to host personal portfolios, project landing pages, documentation, and blogs, offering a simple way to turn code repositories into publicly accessible websites.

## What is gh-pages?

[`gh-pages`](https://github.com/tschaub/gh-pages) is a Node.js package that provides a simple command-line utility for publishing files to a GitHub Pages branch in your repository. It automates the process of pushing your static assets to the `gh-pages` branch of your GitHub repository, which is then automatically published by GitHub Pages. This package is often used in combination with site generators or build tools to simplify the deployment process for static websites or client-side web apps.

`gh-pages` can easily be used to automatically release and deploy any client-side rendered code. React, Angular, Svelte, plain HTML/CSS/Javascript, etc they all work!

## Using gh-pages

### Setup your GitHub Pages Repo

1. **Open Terminal or Command Line**: Navigate to the directory where you want to initialize a new Git repository.
    
2. **Initialize Git Repository**: Run the following command to initialize a new Git repository in that directory:
    
    ```bash
    git init
    ```
    
    This will create a `.git` directory, signaling that this directory is now under Git version control.
    
3. **Add Files to the Repository**: You can add files to be tracked by Git with the following command:
    
    ```bash
    git add .
    ```
    
    This will add all the files in the directory to the staging area. Replace the `.` with specific file names if you don't want to add all files.
    
4. **Commit Changes**: Commit these changes to the repository:
    
    ```bash
    git commit -m "Initial commit"
    ```
    
    This saves your changes locally and prepares them to be pushed to a remote repository.
    
5. **Create a Remote Repository**: If you haven't already, create a new repository on GitHub. Do not initialize it with README, license, or `.gitignore` files if you're planning to push an existing repository.
    
6. **Add Remote Repository**: Back in your terminal, run the following command to link your local repository to the remote one:
    
    ```bash
    git remote add origin [Your GitHub Repo URL]
    ```
    
    Replace `[Your GitHub Repo URL]` with the URL of your new GitHub repository. This sets the remote, so "origin" now refers to the GitHub repository you just created.
    
7. **Verify Remote**: You can verify that the remote URL has been added by running:
    
    ```bash
    git remote -v
    ```
    
    This should show the URL of your GitHub repository.
    

### Setup and Configure gh-pages

1. **Download the gh-pages package**: you can use your favorite node package manager for this step. This module requires Git &gt;= 1.9 and Node &gt; 14.
    

```bash
#NPM installation
npm install gh-pages --save-dev
# YARN install
yarn add gh-pages --dev
```

1. **Update your** `package.json` **scripts**: add a `predeploy` and `deploy` script. The `predeploy` setup handles building the static content. The `predeploy` script will automatically run when the deploy script runs.
    

```json
// NPM
"scripts": {
    "predeploy": "npm run build",
    "deploy": "gh-pages -d build",
}
// YARN
"scripts": {
    "predeploy": "yarn run build",
    "deploy": "gh-pages -d build",
}
```

1. **Push the app to the GitHub repository**: once again you can use your favorite package manager tool.
    

```bash
#NPM
npm run deploy
# YARN
yarn run deploy
```

1. **Check the GitHub repo to make sure the code was pushed to remote**: gh-pages should have pushed the code to a branch named `gh-pages`.
    

### Configure GitHub Pages

1. Navigate to the GitHub Pages on the GitHub repository site
    
2. Configure the `Build and deployment` settings.
    
    1. Source: `Deploy from a branch`
        
    2. Branch: `gh-pages` and `/(root)`
        

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1696705930160/3cd85bf6-4b6d-4059-9259-ea4da8a0ac73.png align="center")

I've previously written about Github Pages configurations in one of my [very first blog posts](https://blog.seancoughlin.me/building-a-personal-website-with-github-pages). Feel free to check that out to learn more.

That's all! GitHub Actions should automatically use these configurations to take your site live to the internet.