---
date: 2025-06-23
draft: false
title: "How do LLMs and AI coding tools solve new problems when Stack Overflow is dead?"
description: "Exploring how LLMs and AI coding tools navigate new problems as Stack Overflow declines. How can AI providers adapt when traditional Q&A forums are dying?"
tags: ["tech", "GenAI", "data", "vibe coding"]
ShowToc: true
cover:
  image: "copying-and-pasting-2.png"
  width: 70%
---

## TL;DR

Stack Overflow used to be the place to search for solutions, when developers encounter bugs. But now, Stack Overflow is almost dead. LLMs might enter uncharted areas when new frameworks and bugs are released. LLM providers need to navigate the uncharted areas by:

- Frequently collecting tech documents and source code to update their models
- Sourcing alternative data from other technical forums (Reddit, Github, and Hugging Face, etc) and user interactions
- Adapting to a new product – Stack Overflow 2.0 in AI era

I will explain the challenge for coding LLMs and the 3 approaches to address it in this article.

## Stack Overflow was essential for developers

As someone who began coding in the 2010s, Stack Overflow was my best buddy. When I just started my career as a data scientist, 50% of my coding skills were learned from working itself, 30% were from Stack Overflow, and 20% were from university or structured courses. I can't remember how many times I encountered a configuration issue and subsequently went down a Stack Overflow rabbit hole journey for hours – especially early in my career.

{{< figurelightbox src="stack-overflow-is-dead.png" align="center" width="80%" >}}

<div style="text-align: center; margin-bottom: 20px;">
<em>Number of questions asked per month on StackOverflow. Data source: {{< newtabref href="https://gist.github.com/hopeseekr/f522e380e35745bd5bdc3269a9f0b132?ref=blog.pragmaticengineer.com#file-stackoverflow-new-questions-over-time-2009-2024-csv" title="this Gist" >}}</em>
</div>

For the last 10-15 years, Stack Overflow has been the essential website for whoever codes or wants to code. But now, {{< newtabref href="https://blog.pragmaticengineer.com/stack-overflow-is-almost-dead/" title="Stack Overflow is almost dead" >}}, and I think it's due to a few key reasons after {{< newtabref href="https://news.ycombinator.com/item?id=41364798" title="some research" >}} online:

- **The advent of LLMs**: Nowadays, coders can easily ask LLMs like ChatGPT or Gemini to debug most issues. I personally have not used Stack Overflow for debugging anymore. The number of questions asked on Stack Overflow has dropped sharply after ChatGPT's launch at the end of 2022.

- **Rigid Moderation**: Stack Overflow has incredibly rigid moderation, which has led to bad user experience. Many users complained about the difficulty of updating their own answers or asking similar questions on Stack Overflow.

- **Outdated answers**: A significant number of solved questions are over 5 years old due to the rigid moderation. Although, technical packages and frameworks are constantly updated and 5 years are forever in the modern technology universe.

- **Toxic community**: Stack Overflow has been an unfriendly place to users (especially new users). Although the vibe varies across sub-communities, the comment section can be hostile and dismissive.

I don't remember the last time I fixed a bug via Stack Overflow, but I feel nostalgic about it already. LLMs and AI coding tools have changed my coding workflow, but they are not a cure-all for all coding problems.

## New codes and bugs are uncharted areas for AI companies

Large Language Models(LLMs) are impressively good at coding because:

- **LLMs come with limitless memory**: LLMs are trained on a large corpus of online content including Stack Overflow, Reddit, and various coding forums. The training process enables LLMs to "memorize" the content, which is almost infinite for the human brain.
- **Most bugs come with a pattern**: most coding problems/bugs have appeared and been solved by developers online. LLMs can easily leverage their endless memory to come up with solutions created by someone in the past.

However, new releases and bugs are shipped daily, and the training schedule of LLM providers cannot catch up with the speed of collective coding of the internet. In my view, the new releases and bugs after a LLM's latest update are uncharted areas, and we don't yet know whether LLMs can solve problems in the uncharted areas since they are not trained on the new code.

I recently asked Cursor to guide me on a custom MCP(a standard for sharing user context with AI models to improve personalization and continuity) set up on Cursor, but the experience was not ideal. On the one hand, Cursor is a fast growing AI coding IDE, and they have major releases almost every month. On the other hand, MCP is a new and quickly evolving part of the GenAI ecosystem. Cursor chat was not able to provide me with the correct instructions to set up the custom MCP, and I went the route of Google, Reddit, and Cursor's latest documentation.

{{< figurelightbox src="cusor-mcp-2.png" caption="The instructions from Cursor didn't lead me to a smooth set up " align="center" width="80%" >}}

Hypothetically, if the number of coding questions and answers on other forums like Hugging Face and Reddit follows Stack Overflow's trend and goes down by 95%, will LLM providers have enough new data to update their LLMs to solve future unseen coding problems?

## How can this challenge play out?

Even though LLM has been the crown jewel of the entire tech industry in the last three years, LLM providers like OpenAI, Google, Meta and Microsoft are still trying to find a way to monetize the magic.

AI coding tools are the most successful use case of LLMs so far, and many tech companies and developers themselves are {{< newtabref href="https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html" title="embracing the tools" >}}. As a developer myself, I do find AI coding tools revolutionary for this profession; I can focus on high priority design and leave some tedious typing to AI. I don't think the AI coding tools are in a mature stage yet, and the developer community is still navigating the new ways of coding and adopting the technology.

Despite the imperfections of existing AI coding tools, developers are nevertheless the earliest and earnest adopters of this AI wave. Therefore, the market will surely prioritize developers' needs and catch up on the uncharted areas. I think the challenge will play out in the following ways.

### Frequent updates on model

For LLMs specialized in coding, their providers need to rigorously collect technical documentation and source code for major languages and frameworks, and frequently update their LLMs. By doing so, the coding LLMs or the AI tools built upon the LLMs can help developers by leveraging the latest documentation and source code. Hopefully, the coding LLMs can recognize the latest information and past bug patterns to infer a solution to a new bug. Although my wishful hope still requires empirical experiment's support.

This approach is similar to addressing data drifting(changes in the distribution of input data over time) and model staleness(when a model becomes outdated) in ML model development and MLOps. However, training and serving LLMs is a specialized subset of machine learning that requires a distinct workflow, pipeline, and infrastructure. This is now often referred to as AIOps.

### Alternative data source

#### Reddit and other forums

Developers still ask questions, just maybe not on Stack Overflow anymore. In my personal experience, I rely more on online platforms like Reddit, Github, Hugging Face forums, and Discord groups, etc. along with AI coding tools. Questions about new releases or new bugs can be found in those spaces.

{{< figurelightbox src="question-hugging-face-2.png" caption="Question about error caused by new release is asked on Hugging Face Forum" align="center" width="80%" >}}

Similar to collecting documentation and source code, LLM providers need to source and clean content from different technical communities and forums for better model performance. It sounds tedious, but from what I know, data sourcing is a significant part of a LLM provider's job. Otherwise, Meta would not pay nearly {{< newtabref href="https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html" title="$15 Billion for Scale AI" >}} in recent weeks.

#### Data from users

Currently, many paid AI coding tools like Cursor allow its users to turn on `Privacy Mode` and thereby enable zero data retention for LLM training . However, as I mentioned in my [previous post](http://andreagao.com/posts/blog-set-up/#traeai), editors like Trae.ai are likely to use users' code for LLM training. This is not a piece of news on the Internet; when users are not paying for a product, they are the product.

Therefore, where terms permit, I think LLM providers will collect user interaction data from IDE or Slack or Github to train their coding LLMs.

### New product – Stack Overflow 2.0 in AI era

Stack Overflow was in decline before developers started using LLMs and AI coding tools because of its own management. Now with the advent of endless AI coding tools, developers are voluntarily or involuntarily learning new ways of coding. I believe there will be a new paradigm for developers in the near future; or should I say, the best coding practice is always evolving, but the changes brought by LLMs are faster and more dramatic.

A new product similar to Stack Overflow but tailored to the AI era with better user experience might emerge to bridge the gaps. Developers could ask questions in a centralized place and LLM providers could access the difficult coding questions

I look forward to seeing a product like this emerging soon. If not, maybe I should build it myself🤔.

## Conclusion

Quality data are the foundation of LLMs, and they are as important as innovative model architecture like {{< newtabref href="https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/" title="Transformer" >}} and computing resources like Nvidia chips. As traditional Q&A forums like Stack Overflow die down and developers change their workflow, LLM providers need to continue inventing new ways to address new problems in programming. This article discussed a few approaches, and I believe more approaches will come.

## Reference

- Cover picture is from {{< newtabref href="https://orlybooks.com/" title="Search O'RLY Covers" >}}, and I just love the site.
- {{< newtabref href="https://blog.pragmaticengineer.com/stack-overflow-is-almost-dead/" title="Stack overflow is almost dead" >}}
- {{< newtabref href="https://tomazweiss.github.io/blog/stackoverflow_decline/" title="Which topics on Stack OverFlow are affected the most?" >}}
- {{< newtabref href="https://news.ycombinator.com/item?id=41364798" title="Ask HN: Why Is Stack Overflow Fading Away?" >}}
- {{< newtabref href="https://modelcontextprotocol.io/introduction" title="Model Context Protocol" >}}
- {{< newtabref href="https://cursor.directory/mcp/postgresql" title="PostgresSQL MCP set up on Cursor" >}}
- {{< newtabref href="https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html" title="30% of Microsoft code is written by AI" >}}
- {{< newtabref href="https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html" title="Meta Invests $14.3 Billion in Scale AI to Kick-Start Superintelligence Lab" >}}
- New bug question on Hugging Face Forum: https://discuss.huggingface.co/t/js-gradio-error/160152
