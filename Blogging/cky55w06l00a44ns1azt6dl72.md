## Building a Personal Website with GitHub Pages

# Why use GitHub Pages 

[GitHub Pages](https://pages.github.com) is an easy to use tool built right into GitHub. The tool is entirely free and it can be used to create [individual, organization, or project websites](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#types-of-github-pages-sites). The only prerequisite needed to create a GitHub Pages site is a [GitHub account](https://github.com). Once you have a GitHub account you can have a website live on the internet within minutes.

# Getting Started

1. Create a new GitHub repository. Name the new repository with the form ```[user].github.io``` where ```[user]``` is your GitHub username. Make sure the repository visibility is set to Public.
2. Navigate to the newly created repository.
3. In the new repository create either an ```index.html``` or ```index.md``` file. The index file will be homepage for the site. For the greatest control over the site use [HTML](https://en.wikipedia.org/wiki/HTML). HTML can be combined with CSS and JavaScript to create fully responsive, attractive websites. [MD or Markdown](https://en.wikipedia.org/wiki/Markdown) is a basic text editing language that can be combined with [Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll) to create styling. It is somewhat more friendly and faster to build with than HTML but offers less customization.
4. After creating an index file, open the Settings tab in the top bar. Then under Settings open the Pages tab from in the left sidebar.
5. Choose a branch to be the source branch. The source branch should be where you created the index file.
6. Once the source branch its selected, GitHub will automatically start building your site and after just a few minutes GitHub will notify you that your site is published at the URL ```[user].github.io```.
7. The index file will always be the homepage, but more pages can be added to the website by creating additional files in the source branch. Each file will be accessible at the URL containing its name. If you created a new file call ```second-page.html```, that page would be visible at the URL ```[user].github.io/second-page.html```.
8. Additional steps to customize your new site can be found in the [documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#next-steps).

# Custom Domains

A [domain name](https://en.wikipedia.org/wiki/Domain_name) is used to identify and access a website. For example, [google.com](https://google.com) or [seancoughlin.me](https://seancoughlin.me) are domain names. By default the created website will be hosted at the domain ```[user].github.io```. However, GitHub Pages comes with [support for custom domain names](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1641604572879/7Wrv5B0mQ.png)

A custom domain name is helpful for branding and search engine rankings. Domain names can be purchased through [domain name registrars](https://en.wikipedia.org/wiki/Domain_name_registrar) such as [GoDaddy](https://www.godaddy.com/domains) or [NameCheap](https://www.namecheap.com).

# Conclusion 

GitHub Pages is a great option for quickly creating and hosting a personal website. It is easy to use and you can have a site live in just a few minutes.

## Pros
- Pages comes with great [documentation](https://docs.github.com/en/pages).
- The entire build process is automated and runs quickly so site changes are up and visible within minutes.
- Site can be fully created and customized with HTML, CSS, and JavaScript or created from [Jekyll themes](https://docs.github.com/en/pages/getting-started-with-github-pages/adding-a-theme-to-your-github-pages-site-with-the-theme-chooser).
- GitHub Pages supports [HTTPS](https://en.wikipedia.org/wiki/HTTPS) to protect your site and users from malicious tampering.
- Totally free!

## Cons
- Using GitHub Pages to run an online business or e-commerce site is prohibited by the  [terms of service](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#prohibited-uses). 
-  [GitHub limits the usage of the tool](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#usage-limits). Published sites are limited to 1GB in size and there is a 100 GB *soft* limit on bandwidth per month.
- GitHub Pages can only create [static web pages](https://en.wikipedia.org/wiki/Static_web_page).
