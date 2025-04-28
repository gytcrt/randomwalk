---
title: "Rebuild my website with GenAI's assistance"
date: 2025-04-24
draft: true
tag: ["tech", "GenAI", "AI", "website"]
ShowToc: true
cover: 
    image: "images/day_scene.png"
    alt: "a day scene of Hong Kong in pixel"
    caption: "AI generated pixel art of Hong Kong"
    width: 75% # Controls the image size, adjust as needed
    description: If anyone wants to set up a personal website, it's way easier to use AI tools now.
---

<!-- ## Introduction (TODO: need update on this) -->
Building a personal website in 2025 has become significantly easier with modern tools and GenAI assistance. In this post, I'll share my experience rebuilding my personal website.

## Why?
When I was in graduate school, I set up a [personal blog](https://github.com/gytcrt/gytcrt.github.io) to show case my project and share thoughts. I've planned to keep developing that site but it has taken a back seat ever since. 

I have got more time lately and decided to pick up this project. It turned out to be so much fun, and I want to share how I have re-built this website.

## Choose domain name and domain registrar
Choosing a domain name is like choosing a [brand name](https://www.shopify.com/blog/domain-seo?term=&adid=647967866337&campaignid=19683492884&utm_medium=cpc&utm_source=google&gad_source=1&gclid=CjwKCAjwwqfABhBcEiwAZJjC3poWT02q2-7_BJRlCqsvGTnMw5UM1d8tee_OgW0UnffVvSXugolTdBoClrwQAvD_BwE#) for your website. Luckily, I don't share name with some celebrities. I was able to register for andreagao.com in 2017 via Google Domain. I generally had a good experience with Google Domain. But unfortunately, they have been [acquired by Squarespace](https://www.theverge.com/2023/6/16/23763340/google-domains-sunset-sell-squarespace). So I had to find another domain registrar.

I quoted on both [GoDaddy](https://aboutus.godaddy.net/about-us/overview/default.aspx) and [Namecheap](https://www.namecheap.com/), and figured the price on Namecheap is more sensible to me. From usability standpoint, I think Namecheap is not different from Google Domain. 

There is a [reddit thread](https://www.reddit.com/r/webdev/comments/1bjfqse/whats_the_best_domain_registrar_in_2024/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) about the best domain registrar in 2024. If you are thinking about getting a domain, you can consider the advice from the thread too. 

## Framework selection
There are millions of ways to build a personal website in 2025. If you want to be relieved from coding and deploying front-end, [Wix](https://www.wix.com/), [Wordpress](https://wordpress.com/) and [Squarespace](https://www.squarespace.com/) are all classic options. Or you can consider GenAI website builder like [replit](https://replit.com/) too. 

I decided to use [static website builder](https://en.wikipedia.org/wiki/Static_site_generator), since I want to code more and have more control over my website. Similar to no-code option in last paragraph, there are many static website builder frameworks too. [Hugo](https://gohugo.io/) and [Jekyll](https://jekyllrb.com/) are the most popular ones. Comparing to Jekyll, Hugo is relatively younger and way faster than Jekyll. I have used Jekyll to build my previous website, so I thought exploring Hugo would be interesting. For anyone who wants to try static website builder, I'd recommend both of them. There are a lot of templates and resources available online for both of them. You cannot go wrong either way. 

Both Hugo and Jekyll provide a lot of themes(like PPT template) for you to build upon. Here are two good resources to find a theme for you:

- Jekyll themes: https://jekyllthemes.io/jekyll-portfolio-themes
- Hugo themes: https://themes.gohugo.io/tags/blog/

<!-- TODO: I want more space here -->
**I also found it very helpful to browse other people's websites created from the themes.** Some of them serve as a great inspiration for me, and many folks wrote blogs about their website set-up and customization too. I will link some reference at the end of this post. 

After browsing 100+ websites, I picked [PaperModX](https://reorx.github.io/hugo-PaperModX/) to start my website. PaperModX is an enhanced version of [PaperMod](https://adityatelange.github.io/hugo-PaperMod/). I like the clean aesthetic of the theme, and it is the [top stared GitHub theme](https://github.com/QIN2DIM/awesome-hugo-themes) for Hugo. Similar to other design choice in software development, Choosing a popular framework with a mature community makes your life easier. 

## Hosting and deployment: Github Pages + Github Actions
Since I'm building a static website, which doesn't contain dynamic content. The best and most economic place to host my website is [Github pages](https://pages.github.com/). It is free if you are using public repo or some premium version of Github account. 

In addition, [Github Actions](https://github.com/features/actions) has made deployment so easy along with Github Page. Hugo has a page on [hosting on Github Pages with Github Actions](https://gohugo.io/host-and-deploy/host-on-github-pages/). I recommend following the page to deploy your static website. 

If you are not familiar with deployment or CI/CD tools like Github Actions, don't get scared by it. With Github Copilot and AI coding tools like Cursor, configuring the deployment files has been way easier than it used to be. 

## Analytics set up: Umami + DigitalOcean
In modern product/software development, feedback is essential for improvement. My website aims to serve myself and my audience, so I'd love to take feedback from my audience. There are direct and indirect feedbacks. Website traffic is in direct feedback, and comments from visitor are direct feedback. In this section, I will talk about my analytics platform set up(indirect feedback).

Hugo PaperMod provides very easy integration with [Google Analytics 4](https://support.google.com/analytics/answer/10089681?hl=en). I believe using Google Analytics would be the most straight forward and time-saving set up. However, I do want to have more control over my traffic data, and I did more research on potential analytics tools. 
[Plausible Analytics](https://plausible.io/) and [Umami](https://umami.is/) are two of the popular tools. I picked Umami since it's open-source, free and self-hostable. 

As for hosting, I prefer minimal set up and effort for Umami, since it's an internal tool for my website and I don't have billions of visitors. I chose DigitalOcean to host my Umami server and managed database. DitialOcean provides very [detailed tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-umami-web-analytics-software-on-ubuntu-20-04) on setting up Umami on its Ubuntu machine. I found it almost effortless to set Umami on DigitalOcean.

{{< figure src="umami.png" alt="Umami dashboard for a day's visit" caption="Umami dashboard for a day's visit" align="center" >}}

## GenAI coding tools: Cursor + Dall-E 3 + Runway + LLMs
<!-- TODO: maybe i should move this section to the front -->
I majored in mathematics and statistics in college and graduate school, and my major programming languages were Matlab and R then. When I built my first website with Python and Jekyll, it was challenging to pick up a new framework by myself. 

When it comes to GenAI tools for coding, I'm so grateful of having them in 2025. GenAI coding tools plus LLMs have made solo web development experience significantly easier this time. **Cursor and other GenAI tools free me from typing code, and enables me to focus on design, which include system design, web design, and UX design.**

Therefore, I want to detail my experience with using GenAI tool for this website. This section is not meant to be a comprehensive review of GenAI IDEs, and I plan to write another article about programming with AI tools.

### IDE
I have heard from friends and online community that Cursor + Claude is the best GenAI IDE in the marketing at this moment. Nevertheless, I looked into that options too. 

**TL;DR: for anyone considering using a GenAI IDE, I recommend checking out latest discussion on this online and experiment a bit with different IDEs and models. Pick the one you like the most.**


#### Replit: AI app builder
[Replit](https://replit.com/) is like a no-code GenAI based app builder platform, and it allows user to use natural language prompt to build app. You can use it as an IDE if you have to access terminal and code. 

I experimented with Replit for a couple of hours. For example, I asked it to build a personal website based on Hugo PaperModX theme. **I think if someone without coding skills might be able to build a decent static website in Replit with more time.** For people with programming experience, GenAI Editor makes more sense. 

#### Trae.ai
[Trae.ai](https://www.trae.ai/) is a free GenAI editor, which provide unlimited free access to Claude 3.7 Sonnet model. It sounds very attractive, since Cursor requires $20 monthly subscription for.

However, as and old(internet) saying goes, "when a product is free, you are the product". If you carefully read [Trae.ai's privacy policy](https://www.trae.ai/privacy-policy) or ask a LLM to summarize it for you, you can infer that **they will collect all your conversation and code and potentially use them for model training.** Here are 2 quotes from the term:

> When you interact with the Platform's integrated AI-chatbot, we collect any information (including any code snippets) that you choose to input.

> To review, improve, and develop the Platform, including by analyzing how you are using the Platform, conducting voluntary surveys and research, and training and improving our technology.

I didn't feel comfortable with the terms, and decided to not try it. 

#### Cursor
Before I started using [Cursor](https://www.cursor.com/), I have tried other GenAI coding tools like Github copilot, Colab with Gemini, etc. But Cursor is a game changer for me, and I'm paying $20 subscription for it. It means a lot since I'm a person with no Amazon Prime account 🙂.  

I've been using Cursor + `Claude-3.5/3.7-sonnet` while developing this website. In my experience, `Claude-3.7-sonnet` and `Claude-3.7-sonnet-thinking` perform better than `Claude-3.5`. But I don't recommend sticking to this config, if you are considering using Cursor. The development of LLM moves so fast, that my current experience won't be relevant in 3 months.  

For anyone considering using a GenAI IDE, I recommend checking out latest discussion on this online and experiment a bit with different IDEs and models. Pick the one fits your need the most. 

Regarding privacy and data usage, [Cursor's privacy policy](https://www.cursor.com/privacy) is reasonable to me and I turn on "Privacy Mode" the whole time. 

### Image and video generation
I always spend tons of time on finding the image I like for my post. Using GenAI model to create image or video for my website has been a great experience to me.

I want arts relevant to the website and my interest on the landing page. It occurred to me a labyrinthian and retro scientific art would be perfect, because someone can only walk randomly in a labyrinth and I love movies like [The Shining](https://www.imdb.com/title/tt0081505/) and [Blade Runner](https://www.imdb.com/title/tt0083658/?ref_=fn_all_ttl_1). 

Initially, I want to use GenAI to create some pixel art version of nostalgic screen saver like the GIF below. When I was a kid, I could watch this for long time. [And I am not alone on this](https://www.theparisreview.org/blog/2017/05/23/salvation-mode/). 

{{< figure src="maze_animation.gif" alt="90s Windows 3D Maze ScreenSaver" caption="90s Windows 3D Maze ScreenSaver" align="center" >}}

I made a few attempts, and the outcomes were not ideal. So I pivoted to another idea: **a pixel art of Hong Kong street view.** Hong Kong is my all time favorite city and it is an iconic retro-sci-fi symbol. Hong Kong is a maze itself in many art work like [Chungking Express](https://en.wikipedia.org/wiki/Chungking_Express). 

Then I used GPT 4.0 to generated some prompts for Dall-E 3, and input the prompts to Dall-E 3 for image generation. Here are selected outputs from Dall-E 3:

| ![Hong Kong night scene 1](Hong_Kong_night_scene_1.gif) | ![Hong Kong night scene 2](Hong_Kong_night_scene_2.png) | ![Hong Kong night scene 3](Hong_Kong_night_scene_3.png) |
|:-------------------------------------------------------:|:-------------------------------------------------------:|:-------------------------------------------------------:|
| *Hong Kong night scene 1* | *Hong Kong night scene 2* | *Hong Kong night scene 3* |

I really love the pixel arts Dall-E 3 created for me. Here is the prompt I used:

>Minimalist pixel art of a Hong Kong street at night for a personal website landing page, with simple, blocky buildings and glowing neon signs in pink, blue, and yellow. The scene has a dark background and features small pixel art people walking on the sidewalks and a few cars on the street. Use an 8-bit retro style with clean lines and minimal details. Leave open space at the top for a website title.

After I got the pixel arts, I felt very pleased by the progress already. However, I went along and tried to animate the pixel art into GIF. 


{{< figure src="/images/day_scene_optimized.gif" alt="Animated Hong Kong street scene pixel art" caption="Animated Hong Kong street scene pixel art" align="center" >}}

### LLMs: OpenAI + Gemini



## Features in backlog
- [ ]Enable comments section
- [ ]Add an archive tag
- [ ]Add buttons to share to social media
- [ ]Combine Tag and Search into one tag
- [ ]Other advice? 

