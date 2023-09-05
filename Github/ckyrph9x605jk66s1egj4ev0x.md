## How to Host a Site With a Subdomain on GitHub Pages

## Subdomain Background

Have you ever noticed some websites [www.seancoughlin.me](http://www.seancoughlin.me), [link.seancoughlin.me](https://link.seancoughlin.me), or [blog.seancoughlin.me](https://blog.seancoughlin.me) have extra text at the front? The first bit of all of these is called a **subdomain**. [Subdomains](https://en.wikipedia.org/wiki/Subdomain) are domains that are a part of other domain names. They can be helpful ways of organizing sites and are easier to remember for users. 

GitHub Pages has great support for free website hosting but creates new pages as `[username].github.io/example-page` by default. Subdomains are a great way to make the URL easier to understand.

## GitHub Pages Subdomain Tutorial

*Note: this tutorial assumes you already have a custom domain setup.* Check [GitHub Pages documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages) to setup your custom subdomain.

First, open your domain name provider and add a CNAME record. A CNAME is an alias for another URL. In the CNAME, add your desired subdomain as the host and username.github.io. as the target. Note the *extra dot* after the end of io. For this tutorial, [Namecheap](https://www.namecheap.com) was my domain name registrar. Creating a CNAME record will look different depending on your domain name provider.

![CNAME record example](https://cdn.hashnode.com/res/hashnode/image/upload/v1642965712201/mGdUHkY8qK.png)

You will be able to see the new subdomain propagate across the world with a tool like https://www.whatsmydns.net.

![DNS propogation](https://cdn.hashnode.com/res/hashnode/image/upload/v1642964303128/tO9DEiSvN.png)

We now need to tell GitHub to host our site at the subdomain we just created. Open the repository you would like to host at a subdomain and head to the Pages tab in settings. Select your source branch and type your subdomain in the custom domain field.

![Pages in settings](https://cdn.hashnode.com/res/hashnode/image/upload/v1642963983042/kg18uFXlf.png)

Initially, GitHub Pages will throw an error saying the domain name is "improperly configured." This error should resolve itself after a few minutes as the DNS records update. If the error doesn't go away, try editing the custom domain, clicking save, then reverting to your desired custom subdomain. Editing the custom domain will trigger GitHub Pages to recheck the DNS records.

![Add subdomain to GitHub Pages](https://cdn.hashnode.com/res/hashnode/image/upload/v1642964231106/D9ZmQQBgZ.png)

Once GitHub Pages has verified the DNS records, the website will be live at an HTTP link. Now Pages will automatically certify the site to create a secure HTTPS version. The process completes after a few minutes. 

![Certifying for HTTPS](https://cdn.hashnode.com/res/hashnode/image/upload/v1642964687361/c_plKr6qZ.png)

That's it! Your Pages site is hosted at your custom subdomain.

![Complete subdomain in GitHub pages](https://cdn.hashnode.com/res/hashnode/image/upload/v1642966048549/gM7AIJlu7.png)
