---
date: 2026-01-16
draft: true
title: "A year of coding with AI"
description: "A senior engineer reflects on a year of coding with AI tools like ChatGPT and Cursor—what worked, what failed, and how AI actually fits into real-world infrastructure, frontend, backend, and analytical workflows."
tags: ["AI", "vibe coding", "engineering"]
category: "engineering"
ShowToc: true
cover:
  image: "musicforprogramming.png"
  width: 100%
---

## Introduction

I have coded a lot with the help of AI/LLM in 2025. These AI tools have dramatically changed how I code and my workflow, which I have been doing for more than 10 years. If you take a look at my blog list, it is full of AI related content. My blog is taken over by AI not because I treat it as part of my job, but rather because my working style and daily life has been constantly evolving with AI. I found it fascinating to think and write about it.

This article will be focused on AI coding. In the context of this blog, AI coding means using conversational AI like ChatGPT and AI coding IDE/agent like Cursor to facilitate coding.

Coding with AI tools feels like raising a kitten or playing a competitive game - the dynamics between you and the subject grow and change together. Sometimes I wonder whether the experience is more similar to raising a human baby. AI companies are tirelessly launching new models and features; users test their ideas on the new features, impressed or annoyed, and jump between different AI products for better performance or to save money. Coders around me commonly switch between Cursor, OpenAI Codex, Microsoft Copilot or Google's AI coding tools.

I enjoy the thrills of solving a complex problem by giving clear instruction, combining multiple techniques and pressure testing with several AI tools. But I have also lost one or two days of work due to misjudgement of mine and poor performance of AI tools. Nevertheless, it is very exciting.

## My background

Giving a comprehensive review on AI coding is impossible, since it would be similar to thoroughly reviewing all cloud service providers and their products. This article is meant to share my experience and what works or does not work for me. Therefore, I think it is worth sharing my background in coding, so that you can calibrate my thoughts based on your experience.

In the past, I've majorly coded in Python and SQL for backend development, ML modeling, analytics, database management. I am fluent in major cloud services, DevOps and MLops. I deliver production solutions along with my team or on my own depending on the scope of the solution.

## AI in a software system

When we talk about modern softwares deployed on cloud, they commonly consist of 3 main layers: infrastructure that provides foundations including computing resources, internet connection and security; front-end that interacts with users; back-end that manages data, ML models and other complex logic.

In any sizable company, these three layers are managed by different engineers or teams. But for independent developers or start-ups, one person might own everything.

### Infrastructure

I found it easy to offload some infrastructure tasks to AI including estimating size of cloud instance required by my use case, configuring a docker container, helping me understand and debug my AWS CloudWatch dashboard etc.

Recently, I noticed someone in Singapore could not access my website via his internet provider. I asked ChatGPT to help me diagnose the issue. It guided me through a few troubleshooting steps including inspecting browser logs and checking potential HTTP issues, but no obvious problem was found. ChatGPT proposed adding Cloudflare in front of my site, which would serve as a trusted layer between my site and any mobile/internet carrier. Then I researched whether Cloudflare is a suitable layer for my website infrastructure and used ChatGPT to set it up step by step. My friend in Singapore confirmed he could access my site smoothly the next day.

{{< figurelightbox src="cloudflare.png" caption="Cloudflare instruction is hard to follow" align="center" width="80%" >}}

When I need to configure infrastructure on providers like AWS, NameCheap and Cloudflare, I usually upload a screenshot of the context and have AI explain and guide me through the process. Let us be honest, many engineers feel overwhelmed and intimidated by the AWS console - most of us do not need to deal with cloud infrastructure when there is a dedicated CloudOps team and the AWS console is labyrinthine.

Nevertheless, I must stress caution when using AI tools on infrastructure changes since it could be expensive or even fatal to your project. Unlike front-end and back-end which you can test in a dev environment before deployment, unexpected changes in infrastructure can be more costly.

### Front-end

Coming from a data scientist and MLE background, I have worked on many solutions that do not require front-end interface for end users. However, being able to work on the front-end and understand the front-end is fun and sometimes critical.

I have taken online front-end courses and managed a front-end team in the past. But I believe practice is the only way to master engineering. AI has enabled me and my friends to work on the front-end with less friction. Developing the front-end together with AI is like having an interactive tutor. If some function or feature is unclear to me, I ask AI to explain it at my preferred pace.

### Back-end

You must know the objectives of your solutions, the plan to get there, and an ideal style guide before jumping into AI coding for back-end. Otherwise, AI coding agents might output over-engineered bibberish code.

Why do I insist on that?

Last year I spent a few days on building a data ingestion pipeline with Cursor, and felt pretty good after finishing it. However, I almost never use the pipeline afterwards. I thought I needed the data pipeline and I could build it fairly quickly with Cursor, then I rushed into developing. Later on, I realized I could use some open source packages to pull similar data without maintaining the data pipeline code. Leveraging the widely used open source packages is significantly easier than using my pipeline for my project at the initial phase. When it comes to the later phase of the project, the data pipeline is not useful either because we have developed new constraints on the data and they need to be reflected in the data ingestion process as well.

AI code agents can deliver back-end code, but the tasks need to be modular and well-defined within the context of a project. Uncontroversially, developing tests and ensuring output from AI code agents passes the tests is another good QA method.

## How I work with AI

<div class="tenor-gif-embed" data-postid="1747207714643625346" data-share-method="host" data-aspect-ratio="1.79104" data-width="100%"><a href="https://tenor.com/view/ngoding-mulu-gif-1747207714643625346">Ngoding Mulu GIF</a>from <a href="https://tenor.com/search/ngoding+mulu-gifs">Ngoding Mulu GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

Coding is not typing in strings following the syntax of a programming language, but a means to solve a defined problem. For the sake of this post, let us assume the problem is well defined (since finding and defining a valuable problem is an important subject of its own). When you solve a problem, you generally follow an iterative process that consists of brainstorming, analyzing the situations, engineering and reviewing the solutions. In this section, I will break the problem solving process down to 3 parts and discuss how I view the usage of AI in each of the processes.

### Brainstorming

ChatGPT and Google Gemini are very helpful brainstorming tools. I use them to research the context of a problem, identify popular technical frameworks, and find reference materials. This is particularly useful if you start working on a new topic. For example, I am generally a passive investor, but I decided to spend some time on developing Bitcoin quantitative trading strategy in 2025. ChatGPT and Gemini helped me quickly find initial directions and valuable reference books.

However, as I picked up foundational knowledge and started solving more complex problems in quant research, ChatGPT and Gemini became less reliable. When I asked them to provide feedback on my strategy backtesting results, they could produce seemingly convincing but illogic advice. Embarrassingly, both my coworker and I have been fooled by AI in situations like that, and we have had {{< newtabref href="https://www.coursera.org/articles/what-is-retrospective" title="retrospective conversations" >}} on how to avoid being misled by AI.

Frankly, I have not found a silver bullet to avoid being misled by AI yet, and I think this struggle will continue given the nondeterministic nature of AI (precisely Generative AI). Critical thinking, expertise and continuous learning are more important than before, especially, when working with AI.

### Analytics

To start this section, I want to quote Citadel's founder Ken Griffin: {{< newtabref href="https://www.bloomberg.com/news/articles/2025-10-15/ken-griffin-says-genai-fails-to-help-hedge-funds-produce-alpha" title="GenAI fails to help hedge funds generate alpha." >}} I found it difficult to use AI to produce quantitative analyses, which is a shared view by my other statistician friends.

{{< figurelightbox src="citadel.jpg" caption="" align="center" width="60%" >}}



"Quantitative analysis" means solving a problem by analyzing given structured or unstructured data independently. For example, if I have per-minute OHLC (Open, High, Low, Close) data of Bitcoin in 2025, and I want to know the frequency of Bitcoin price falling 3% within an hour in 2025, an AI coding agent will struggle with solving the problem on its own. In my experience, I need to give AI step by step instructions and review every line of code produced by AI to ensure its accuracy for the example question.

AI is good at generating SQL queries much like it generates natural language, but it does not apply logic the way humans do. I would advise you to be careful with AI in analytics.

### Code review and refactoring

I am pretty happy with using AI for code review and refactoring. Code review and refactoring are essential to quality code base, but most engineers find them less enjoyable than developing a new feature or solving a problem. It means they are suitable for AI augmentation - humans should be free from tedious tasks and delegate them to AIs.

Similar to my ideas in other sections of the article, you need to know your goals of review/refactoring and guide AI with some pre-defined principles, especially when you work on a large or enterprise codebase.

### Limitations and failure modes

#### Common vs Niche packages

In my previous blog, How do LLMs and AI coding tools solve new problems when Stack Overflow is dead? I have questioned how AI addresses new coding problems. Now I have more lived experience to add more color on this topic. AI is more helpful with common languages and packages like Python and Pandas than specialized packages.

When I use the inline question feature to ask Cursor for some quick analysis in Pandas, it usually produces decent and accurate code. However, when I ask Cursor to change parameters for functions from {{< newtabref href="https://vectorbt.dev/" title="vectorbt" >}} or {{< newtabref href="https://www.freqtrade.io/en/stable/" title="freqtrade" >}}, it is usually worse than me directly looking up package documentation. I think it is due to lack of enough trading data for those nicher packages.

I have found a workaround: pass the documentation page to AI and ask AI to plan its answer based on the documentation. It is not perfect, but better than asking AI for help without context.

#### Debugging

Using AI for debugging can be hit or miss. Sometimes it can identify unfamiliar root causes for me, but sometimes it takes an AI agent a long time to understand the context of a project over and over again. Especially for nicher packages, AI is generally bad at debugging them. It is easier to seek help on the package forum or Discord group.

As a rule of thumb, when I encounter an unfamiliar bug, I start by asking the AI to identify the root cause. If the AI cannot give me a convincing result in 2 minutes, I will start digging into the issue on my own. AI tends to run in circles and hallucinate when you keep asking it to solve a bug beyond its capability.

## Conclusion

Thanks for reading to the end of this post, which serves as a good reflection on my interaction (collaboration?) with AI. It's possible that many of the shortcomings of AI coding in this post will be solved in a couple of years, but it's fun to be an active participant and thinker throughout this process. 