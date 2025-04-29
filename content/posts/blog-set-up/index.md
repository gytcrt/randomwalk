---
title: "Rebuild my website with GenAI's assistance"
date: 2025-04-24
draft: true
tag: ["tech", "GenAI", "AI", "website"]
ShowToc: true
cover: 
    image: "Hong_Kong_day_scene.png"
    alt: "a day scene of Hong Kong in pixel"
    caption: "AI generated pixel art of Hong Kong"
    width: 75% # Controls the image size, adjust as needed
    description: If anyone wants to set up a personal website, it's way easier to use AI tools now.
---

## Introduction 
When I was in graduate school, I set up a [personal blog](https://github.com/gytcrt/gytcrt.github.io) to showcase my project and share thoughts. I planned to keep developing that site but it has since then taken a backseat while I became busy with work.

I have got more time lately and decided to pick up this project. It turned out to be so much fun, and I want to share how I have re-built this website with GenAI tools. **If you are only interested in the part related to GenAI, check out the [**GenAI coding tools section**](http://localhost:1313/posts/blog-set-up/#genai-coding-tools-cursor--dall-e-3--runway--llms).**

## Choosing and registering a domain name 
Choosing a domain name is like choosing a [brand name](https://www.shopify.com/blog/domain-seo?term=&adid=647967866337&campaignid=19683492884&utm_medium=cpc&utm_source=google&gad_source=1&gclid=CjwKCAjwwqfABhBcEiwAZJjC3poWT02q2-7_BJRlCqsvGTnMw5UM1d8tee_OgW0UnffVvSXugolTdBoClrwQAvD_BwE#) for your website. Luckily, I don't share a name with any celebrities or public figures. I was initially able to register for andreagao.com in 2017 via Google Domain, and generally had a good experience using the service. But unfortunately, they have been [acquired by Squarespace](https://www.theverge.com/2023/6/16/23763340/google-domains-sunset-sell-squarespace). So I had to find another domain registrar.

I quoted on both [GoDaddy](https://aboutus.godaddy.net/about-us/overview/default.aspx) and [Namecheap](https://www.namecheap.com/), and figured the price on Namecheap is more sensible to me. From a usability standpoint, I think Namecheap is comparable to Google Domain.

If you are thinking about obtaining a domain for your own website, you can also check out this helpful [Reddit thread](https://www.reddit.com/r/webdev/comments/1bjfqse/whats_the_best_domain_registrar_in_2024/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) on the best domain registrars in 2024.

## Framework selection
There are millions of ways to build a personal website in 2025. If you are inclined to avoid coding and deploying front-end, [Wix](https://www.wix.com/), [Wordpress](https://wordpress.com/) and [Squarespace](https://www.squarespace.com/) are all classic options. Or you can consider a GenAI website builder like [replit](https://replit.com/) too.

I decided to use a [static website builder](https://en.wikipedia.org/wiki/Static_site_generator), since I want to code more and have more control over my website. Like the no-code options in the last paragraph, there are many static website builder frameworks too. [Hugo](https://gohugo.io/) and [Jekyll](https://jekyllrb.com/) are the most popular ones. Compared to Jekyll, Hugo is younger and faster. I used Jekyll to build my previous website, so I thought it would be interesting to explore Hugo. For anyone who wants to try a static website builder, I recommend either. There are a lot of templates and resources available online for both of them. You cannot go wrong either way.

Both Hugo and Jekyll provide a lot of themes (like a PPT template) for you to build upon. Here are two good resources for finding themes:

- Jekyll themes: https://jekyllthemes.io/jekyll-portfolio-themes
- Hugo themes: https://themes.gohugo.io/tags/blog/

**I also found it very helpful to browse the themes as used on other people's websites.** Some of them serve as a great inspiration for me, and many folks wrote blogs about their website set-up and customization. You can find some references linked at the end of this post.

After browsing over a hundred websites, I picked [PaperModX](https://reorx.github.io/hugo-PaperModX/) for my own. PaperModX is an enhanced version of [PaperMod](https://adityatelange.github.io/hugo-PaperMod/). I like the clean aesthetic of the theme, and it is the [top starred GitHub theme](https://github.com/QIN2DIM/awesome-hugo-themes) for Hugo. **Similar to other design choices in software development, choosing a popular framework with a mature community makes your life easier.**

## Hosting and deployment: Github Pages + Github Actions
Since I'm building a static website, which contains no dynamic content, the best and most economical place to host it is [Github pages](https://pages.github.com/). It is free if you are using a public repo or some premium version of Github account.

In addition, [Github Actions](https://github.com/features/actions) has made deployment very easy along with Github Pages. Hugo has a page on [hosting on Github Pages with Github Actions](https://gohugo.io/host-and-deploy/host-on-github-pages/). I recommend following the page to deploy your static website.

**If you are not familiar with deployment or CI/CD tools like Github Actions, don't be scared by it. With Github Copilot and AI coding tools like Cursor, configuring the deployment files is now way easier than it used to be.**

## Analytics set up: Umami + DigitalOcean
In modern product/software development, feedback is essential for improvement. My website aims to serve both myself and my audience, so I'd love to take feedback from readers. In this section, I will talk about my analytics platform set up.

Hugo PaperMod provides very easy integration with [Google Analytics 4](https://support.google.com/analytics/answer/10089681?hl=en). I believe using Google Analytics would be the most straightforward and time-saving set up. However, I do want to have more control over my traffic data, so I did more research on potential analytics tools. [Plausible Analytics](https://plausible.io/) and [Umami](https://umami.is/) are two of the popular tools. I picked Umami since it's open-source, free, and self-hostable.

As for hosting, I prefer minimal setup and effort for Umami, since it's an internal tool for my website and I don't have billions of visitors. I chose DigitalOcean to host my Umami server and managed database. DigitalOcean provides a very [detailed tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-umami-web-analytics-software-on-ubuntu-20-04) on setting up Umami on its Ubuntu machine. I found it almost effortless to set up Umami on DigitalOcean.

{{< figure src="umami.png" alt="Umami dashboard for a day's visit" caption="Umami dashboard for a day's visit" align="center" >}}

## GenAI coding tools: Cursor + Dall-E 3 + Runway + LLMs

**TL;DR:** 
- **Choose the right tools for you:** for anyone considering using a GenAI IDE, I recommend checking out the latest discussions online and experimenting a bit with different IDEs and models. Pick the one you like the most.
- **Programming skills are still valuable:** For anyone considering a non-trivial project, it's important to master one programming language and know the fundamentals of the language in which you are programming. [Andrew Ng's recent post](https://www.deeplearning.ai/the-batch/issue-298/) gives an in-depth breakdown of what this means for developers. 
- **GenAI enhances creativity:** using image generation and video generation models to create visual content is amazing!
---

I majored in mathematics and statistics in undergrad and graduate school, respectively, and my major programming languages back then were Matlab and R. When I built my first website with Python and Jekyll, it was challenging to pick up a new framework by myself.

I'm so grateful for the wide range of GenAI coding tools available in 2025. GenAI coding tools plus LLMs have made solo web development experience significantly easier this time. **Cursor and other GenAI tools free me from typing code, and allow me to focus on all aspects of design: including system design, web design, and UX design.**

Therefore, I want to detail my experience using GenAI tools for this website. This section is not meant to be a comprehensive review of GenAI coding tools, which will be the subject of a separate article I plan to write.

### IDE
I have heard from friends and online communities that Cursor + Claude is the best GenAI IDE in the market at this moment. Nevertheless, I looked into other options too.

#### Replit: AI app builder
[Replit](https://replit.com/) is like a no-code GenAI based app builder platform, and it allows the user to use natural language prompts to build. You can use it as an IDE if you have to access terminal and code.

I experimented with Replit for a couple of hours. I asked it to build a personal website based on Hugo PaperModX theme. **I think someone without coding skills might be able to build a decent static website in Replit with more time.** For people with programming experience, a GenAI Editor makes more sense.

#### Trae.ai
[Trae.ai](https://www.trae.ai/) is a free GenAI editor, which provides unlimited free access to Claude 3.7 Sonnet model. This sounds particularly attractive in comparison to Cursor, which requires a $20 monthly subscription.

However, as an old (internet) saying goes, "when a product is free, you are the product." If you carefully read [Trae.ai's privacy policy](https://www.trae.ai/privacy-policy) (or ask a LLM to summarize it for you), you can infer that they retain the right to collect any information and code to potentially use for model training. Here are two quotes from the policy:

> When you interact with the Platform's integrated AI-chatbot, we collect any information (including any code snippets) that you choose to input.

> To review, improve, and develop the Platform, including by analyzing how you are using the Platform, conducting voluntary surveys and research, and training and improving our technology.

I didn't feel comfortable with these terms, and decided to not try it.

#### Cursor
Before I started using [Cursor](https://www.cursor.com/), I tried other GenAI coding tools like Github copilot, Colab with Gemini, etc. But Cursor is a game changer for me, and I'm paying the $20 monthly subscription for it. It means a lot since I'm a person with no Amazon Prime account 🙂.

I've been using Cursor + `Claude-3.5/3.7-sonnet` while developing this website. In my experience, `Claude-3.7-sonnet` and `Claude-3.7-sonnet-thinking` perform better than `Claude-3.5`. But I don't recommend sticking to this config if you are considering using Cursor. The development of LLM moves so fast that my current experience won't be relevant in three months.

For anyone considering using a GenAI IDE, I recommend checking out the latest discussions on this online and experimenting a bit with different IDEs and models. Pick the one that best fits your needs.

Regarding privacy and data usage, I found [Cursor's privacy policy](https://www.cursor.com/privacy) to be reasonable, and keep "Privacy Mode" enabled while using the editor.

### Image and video generation
I always spend tons of time on choosing the best images for my post. Using a GenAI model to create images or videos for my website has been a great experience for me.

I wanted some art on the landing page that was relevant to both the website and my interests on the landing page. It occurred to me that something labyrinthian and retro-futuristic would be fitting: someone can only walk randomly in a labyrinth and I love the aesthetic of movies like [The Shining](https://www.imdb.com/title/tt0081505/) and [Blade Runner](https://www.imdb.com/title/tt0083658/?ref_=fn_all_ttl_1).

Initially, I wanted to use GenAI to create some pixel art versions of nostalgic screensavers like the GIF below. When I was a kid, I could watch these animations for a long time. [And I am not alone in this fascination](https://www.theparisreview.org/blog/2017/05/23/salvation-mode/)!

{{< figure src="maze_animation.gif" alt="90s Windows 3D Maze ScreenSaver" caption="90s Windows 3D Maze ScreenSaver" align="center" >}}

The outcomes of my first few attempts were not ideal. So I pivoted to another idea: **a pixel art of a Hong Kong street**. Hong Kong is my favorite city and it is an iconic retro-futuristic symbol. Hong Kong itself is a maze, as seen in film settings like [Chungking Express](https://en.wikipedia.org/wiki/Chungking_Express).

I used GPT 4.0 to generate some prompts, and input the prompts to Dall-E 3 for image generation. Here are selected outputs from Dall-E 3:

| ![Hong Kong night scene 1](Hong_Kong_night_scene_1.gif) | ![Hong Kong night scene 2](Hong_Kong_night_scene_2.png) | ![Hong Kong night scene 3](Hong_Kong_night_scene_3.png) |
|:-------------------------------------------------------:|:-------------------------------------------------------:|:-------------------------------------------------------:|
| *Hong Kong night scene 1* | *Hong Kong night scene 2* | *Hong Kong night scene 3* |

I really love the pixel arts Dall-E 3 created for me. Here is the prompt I used:

>Minimalist pixel art of a Hong Kong street at night for a personal website landing page, with simple, blocky buildings and glowing neon signs in pink, blue, and yellow. The scene has a dark background and features small pixel art people walking on the sidewalks and a few cars on the street. Use an 8-bit retro style with clean lines and minimal details. Leave open space at the top for a website title.

After I had the pixel arts, I felt very pleased by the progress already. However, I went along and tried to animate the pixel art into GIF using GenAI tools. I tried two popular AI video generation tools: [Kaiber](https://www.kaiber.ai/superstudio) and [Runway](https://runwayml.com/). Kaiber is not intuitive to use and I was not able to generate a video with the trial credits for a new user. However, I found Runway to be quite impressive and I really like the animated video it produced, seen below. This gif is my landing page cover picture now.

{{< figure src="/images/day_scene_optimized.gif" alt="Animated Hong Kong street scene pixel art" caption="Animated Hong Kong street scene pixel art" align="center" >}}

### LLMs: OpenAI + Gemini

Besides Cursor + `Claude-3.5/3.7-sonnet`, I still use other LLMs including `Gemini 2.5 Pro` and `GPT-4` to help with my development, considering:

- **Price/Value:** Compared to using limited premium models with a request quota on Cursor, those LLMs are free. I can reserve my quota to more important questions that require access to my codebase.
- **Guide code from AI with second opinion:** None of the GenAI tools or LLMs are a silver bullet for coding. Code from LLM can be very redundant, and lacks holistic design consideration. I found it critical to use my own engineering experience to direct the development process and take a second opinion from friends or another LLM/GenAI system.

## Conclusion

It has been an interesting journey for me to restart an old project and reflect on my current process. AI tools have totally changed how I code, but they still require guidance and creativity at this moment. Like any other pivotal moment in history, it could be scary or exciting; but it will certainly bring about major changes. I will continue to use this website to log the changes.

## Features in backlog
- [ ] Enable comments section
- [ ] Add an archive tag
- [ ] Add buttons to share to social media
- [ ] Other advice?

