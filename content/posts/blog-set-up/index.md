---
title: "Rebuild my website with AI's assistance"
date: 2025-04-24
draft: true
tag: ["tech", "GenAI", "AI", "website"]
cover: 
    image: "images/day_scene.png"
    alt: "a day scene of Hong Kong in pixel"
    caption: "AI generated pixel art of Hong Kong"
    width: 50% # Controls the image size, adjust as needed
    description: If anyone wants to set up a personal website, it's way easier to use AI tools now.
---

# Why?
When I was in graduate school, I set up a [personal blog](https://github.com/gytcrt/gytcrt.github.io) to show case my project and share thoughts. I've planned to keep developing that site but it has taken a back seat ever since. 

I have got more time lately and decided to pick up this project. It turned out to be so much fun, and I want to share how I have re-built this website.

# Choose domain name and domain registrar
Choosing a domain name is like choosing a [brand name](https://www.shopify.com/blog/domain-seo?term=&adid=647967866337&campaignid=19683492884&utm_medium=cpc&utm_source=google&gad_source=1&gclid=CjwKCAjwwqfABhBcEiwAZJjC3poWT02q2-7_BJRlCqsvGTnMw5UM1d8tee_OgW0UnffVvSXugolTdBoClrwQAvD_BwE#) for your website. Luckily, I don't share name with some celebrities. I was able to register for andreagao.com in 2017 via Google Domain. I generally had a good experience with Google Domain. But unfortunately, they have been [acquired by Squarespace](https://www.theverge.com/2023/6/16/23763340/google-domains-sunset-sell-squarespace). So I had to find another domain registrar.

I quoted on both [GoDaddy](https://aboutus.godaddy.net/about-us/overview/default.aspx) and [Namecheap](https://www.namecheap.com/), and figured the price on Namecheap is more sensible to me. From usability standpoint, I think Namecheap is not different from Google Domain. 

There is a [reddit thread](https://www.reddit.com/r/webdev/comments/1bjfqse/whats_the_best_domain_registrar_in_2024/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) about the best domain registrar in 2024. If you are thinking about getting a domain, you can consider the advice from the thread too. 

# Framework selection
There are millions of ways to build a personal website in 2025. If you want to be relieved from coding and deploying front-end, [Wix](https://www.wix.com/), [Wordpress](https://wordpress.com/) and [Squarespace](https://www.squarespace.com/) are all classic options. Or you can consider GenAI website builder like [replit](https://replit.com/) too. 

I decided to use [static website builder](https://en.wikipedia.org/wiki/Static_site_generator), since I want to code more and have more control over my website. Similar to no-code option in last paragraph, there are many static website builder frameworks too. [Hugo](https://gohugo.io/) and [Jekyll](https://jekyllrb.com/) are the most popular ones. Comparing to Jekyll, Hugo is relatively younger and way faster than Jekyll. I have used Jekyll to build my previous website, so I thought exploring Hugo would be interesting. For anyone who wants to try static website builder, I'd recommend both of them. There are a lot of templates and resources available online for both of them. You cannot go wrong either way. 

Both Hugo and Jekyll provide a lot of themes(like PPT template) for you to build upon. Here are two good resources to find a theme for you:

- Jekyll themes: https://jekyllthemes.io/jekyll-portfolio-themes
- Hugo themes: https://themes.gohugo.io/tags/blog/

<!-- TODO: I want more space here -->
**I also found it very helpful to browse other people's websites created from the themes.** Some of them serve as a great inspiration for me, and many folks wrote blogs about their website set-up and customization too. I will link some reference at the end of this post. 

After browsing 100+ websites, I picked [PaperModX](https://reorx.github.io/hugo-PaperModX/) to start my website. PaperModX is an enhanced version of [PaperMod](https://adityatelange.github.io/hugo-PaperMod/). I like the clean aesthetic of the theme, and it is the [top stared GitHub theme](https://github.com/QIN2DIM/awesome-hugo-themes) for Hugo. Similar to other design choice in software development, Choosing a popular framework with a mature community makes your life easier. 

# Hosting and deployment: Github Pages + Github Actions
Since I'm building a static website, which doesn't contain dynamic content. The best and most economic place to host my website is [Github pages](https://pages.github.com/). It is free if you are using public repo or some premium version of Github account. 

In addition, [Github Actions](https://github.com/features/actions) has made deployment so easy along with Github Page. Hugo has a page on [hosting on Github Pages with Github Actions](https://gohugo.io/host-and-deploy/host-on-github-pages/). I recommend following the page to deploy your static website. 

If you are not familiar with deployment or CI/CD tools like Github Actions, don't get scared by it. With Github Copilot and AI coding tools like Cursor, configuring the deployment files has been way easier than it used to be. 

# Analytics set up: Umami + DigitalOcean
In modern product/software development, feedback is essential for improvement. My website aims to serve myself and my audience, so I'd love to take feedback from my audience. There are direct and indirect feedbacks. Website traffic is in direct feedback, and comments from visitor are direct feedback. In this section, I will talk about my analytics platform set up(indirect feedback).

Hugo PaperMod provides very easy integration with [Google Analytics 4](https://support.google.com/analytics/answer/10089681?hl=en). I believe using Google Analytics would be the most straight forward and time-saving set up. However, I do want to have more control over my traffic data, and I did more research on potential analytics tools. 
[Plausible Analytics](https://plausible.io/) and [Umami](https://umami.is/) are two of the popular tools. I picked Umami since it's open-source, free and self-hostable. 

As for hosting, I prefer minimal set up and effort for Umami, since it's an internal tool for my website and I don't have billions of visitors. I chose DigitalOcean to host my Umami server and managed database. DitialOcean provides very [detailed tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-umami-web-analytics-software-on-ubuntu-20-04) on setting up Umami on its Ubuntu machine. I found it almost effortless to set Umami on DigitalOcean.

<!-- This part should be moved to AI tool and advice part -->
<!-- # Font set up -->

# Vibe coding and advice
I majored in mathematics and statistics in college and graduate school, and my major programming languages are Matlab and R. When I built my first website with Python and Jekyll, it was challenging to pick up a new framework by myself. 

When it comes to AI tools for coding, I'm so grateful of having them in 2025. Vibe/AI coding tools plus LLM have made solo web development experience easier this time.  

# Features in backlog
- [ ]Enable comments section
- [ ]Add an archive tag
- [ ]Add buttons to share to social media
- [ ]Combine Tag and Search into one tag

