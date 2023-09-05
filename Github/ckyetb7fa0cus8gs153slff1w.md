## Hosting an API with GitHub Pages

## Background

[GitHub Pages](https://pages.github.com/) is a free website hosting tool provided by GitHub. [I previously wrote about GitHub pages being an excellent place to host a personal website or project page.](https://blog.seancoughlin.me/building-a-personal-website-with-github-pages) Additionally, it is a great choice to host a JSON API. 

An [API](https://en.wikipedia.org/wiki/API) is a connection between computers. An example API would be the [Spotify API](https://developer.spotify.com/documentation/web-api/) which provides music data.

## Tutorial 

First, you will need to create a special `[username].github.io` repository. This repository will be home to your GitHub Pages website. The repository name must **exactly** match the format `[username].github.io`, otherwise GitHub will not generate a live website.

![Create a new GitHubPages Repo](https://cdn.hashnode.com/res/hashnode/image/upload/v1642186114174/26yRishrk.png)

I have already made a GitHub Pages repository so the name is taken for me. Your custom `[username].github.io` will be available.

After creating `[username].github.io` open the terminal, clone the repository, and cd into the directory.

```
git clone https://github.com/Scc33/Scc33.github.io.git
cd Scc33.github.io
```

Inside the repository you can create a `.json` file. That `.json` file will become your publicly accessible JSON API.


![Example json file](https://cdn.hashnode.com/res/hashnode/image/upload/v1642187567249/8-aI-Cce4.png)

After adding a `.json` file add, commit, and push your changes to GitHub.

```
git add .
git commit -m "Create JSON API"
git push -u origin master
```

Once you commit and push your changes to the codebase, GitHub will automatically build your changes and publish the code to the internet. It should only take a few minutes for the changes to become visible.

That's all it takes! You now have a JSON API for the world to see. Your new JSON API will be located at the URL `[username].github.io/[file-name].json`. Your API can be seen using any web browser or an API testing tool like [Postman](https://www.postman.com/).

## Conclusion

GitHub Pages is a great tool for quickly creating a JSON API. In just a few minutes it's up and running! 

### Pros

- The entire build process is [automated](https://github.com/features/actions) and site changes are published to the internet within minutes.
- GitHub Pages supports [HTTPS](https://en.wikipedia.org/wiki/HTTPS) to protect your site and users from malicious tampering.
- Best of all, it's free!

### Cons

- [GitHub limits page traffic.](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#usage-limits) Published sites are capped at 1GB in size and there is a 100 GB *soft* limit on bandwidth per month.


