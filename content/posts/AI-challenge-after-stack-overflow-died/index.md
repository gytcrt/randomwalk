---
date: 2025-06-20
draft: true
title: "How do LLMs and AI coding tools solve new problems when Stack Overflow is dead?"
tags: ["tech", "GenAI", "data"]
ShowToc: true
cover:
  image: "copying-and-pasting-2.png"
  width: 70%
---

## TL;DR

Stack Overflow used to be the place to search for solutions, when developers encounter bugs. But Stack Overflow is almost dead now. LLMs might enter uncharted areas when new frameworks and bugs are released. LLM providers need to navigate the uncharted areas via:

- Frequently collect tech documents and source code to update their models
- Source alternative data from other technical forums(Reddit, Github, and Hugging Face, etc) and user interactions
- Adapt to a new product – Stack Overflow 2.0 in AI era

## Stack Overflow WAS essential for coders

As someone starting coding in the 2010s, Stack Overflow was my best buddy. When I just started my career as a data scientist, 50% of my coding skills were learned from working itself, 30% were from Stack Overflow, and 20% were from university or structured courses. I don’t remember how many times I encountered a configuration issue and it subsequently led to a Stack Overflow rabbit hole journey for hours – especially early in my career.

{{< figurelightbox src="stack-overflow-is-dead.png" align="center" width="80%" >}}

<div style="text-align: center; margin-bottom: 20px;">
<em>Number of questions asked per month on StackOverflow. Data source: <a href="https://gist.github.com/hopeseekr/f522e380e35745bd5bdc3269a9f0b132?ref=blog.pragmaticengineer.com#file-stackoverflow-new-questions-over-time-2009-2024-csv">this Gist</a></em>
</div>

Stack Overflow was the essential website for whoever codes or wants to code in the last 10-15 years. However, [Stack Overflow is almost dead](https://blog.pragmaticengineer.com/stack-overflow-is-almost-dead/) at this point for a few reasons:

- **The advent of LLMs**: nowadays, coders can easily ask LLMs like ChatGPT or Gemini to debug most issues. I personally have not used Stack Overflow for debugging anymore. The number of questions asked on Stack Overflow has dropped sharply after ChatGPT’s launch at the end of 2022.

- **Rigid Moderation**: Stack Overflow has incredibly rigid moderation, which has led to bad user experience. [Many users complained about the difficulty of updating their own answers or asking similar questions on Stack Overflow](https://news.ycombinator.com/item?id=41364798). Significant number of solved questions are over 5 years old. Although, technical packages and frameworks are constantly updated and 5 years are forever in the modern technology universe.

- **Toxic community**: Stack Overflow has been an unfriendly place to users (especially new users). Although the vibe varies across sub-communities on Stack Overflow, the comment section can be hostile and dismissive.

I don’t remember when was the last time I fixed a bug via Stack Overflow, but I feel nostalgic about it already. LLMs and AI coding tools have changed my coding workflow, but they are not the key to all coding solutions.

## New bugs are uncharted areas for AI companies

Large Language Models(LLMs) are impressively good at coding because:

- **LLMs come with limitless memory:** LLMs are trained on a large corpus of online content including Stack Overflow, Reddit, and various coding forums. The training process enables LLMs to “memorize” the content, which is almost infinite for the human brain.
- **Most bugs come with a pattern:** Most coding problems/bugs have appeared and been solved by developers online. LLMs can easily leverage its endless memory to come up with solutions created by someone in the past.

However, new releases and bugs are shipped daily, and the training schedule of LLM providers cannot catch up with the speed of collective coding of the internet. In my view, the new releases and bugs after a LLM’s latest update are an uncharted area, we don't know whether LLM can solve it since it’s not trained on the new code.

Recently, I asked Cursor to guide me on a PostgresSQL MCP set up on Cursor, but the experience was not ideal. On the one hand, Cursor is a fast growing AI coding IDE, and they have major release almost every month. On the other hand, MCP is a new and quickly evolving part of the GenAI ecosystem. Cursor chat was not able to provide me with the correct instruction to set up the custom MCP, and I went the route of Google, Reddit, and Cursor’s latest documentation.

{{< figurelightbox src="cusor-mcp-2.png" caption="The instructions from Cursor didn't lead me to a smooth set up " align="center" width="80%" >}}

Moreover, if all questions and answers on coding go down 95% on the Internet like Stack Overflow over time, do LLM providers have enough new data to update their LLMs to solve our coding problems in future?

## How can this challenge play out?

Even though LLM has been the crown jewel of the entire tech industry in the last 3 years, LLM providers like OpenAI, Google, Meta and Microsoft are still trying to find a way to monetize the magic.

AI coding tools so far are the most successful use case of LLMs, but developers have a love and hate relationship with them. After [rounds and rounds of lay-offs](https://news.crunchbase.com/startups/tech-layoffs/), developers are insecure about their jobs and scared of AI replacing them. However, AI coding tools have boosted developer’s productivity as well. For example, for Python coders like [Andrew Ng](https://www.deeplearning.ai/the-batch/issue-298/) and me, now we can easily work on frontend using JavaScript and TypeScript with the help of AI coding tools. Developers are nevertheless the earliest adopter of this AI wave.

Therefore, I think the market will adapt for developers’ needs and catch up on the uncharted areas. I think the challenge will play out in the following ways.

### Frequent update on model

I believe LLMs will be more specialized in the coming years. A generalist model like GPT-4 is equipped with knowledge irrelevant to coding, and developers don’t need to pay the price for that. A specialty model is optimized for limited use cases like coding, content generation, and customer service, etc regarding its size, price, latency and performance. With a specialty model, clients or customers can pay a more reasonable price for their specific needs.

For LLMs specialized in coding, their providers need to rigorously collect technical documentation and source code for major languages and frameworks, and update their LLMs frequently. By doing so, the coding LLMs or the AI tools hooked with them can help developers by leveraging the latest documentation and source code. Hopefully, the coding LLM can recognize the latest information and past bug patterns to infer a solution to a new bug. Although my wishful hope still requires empirical experiment’s support.

### Alternative data sources

#### Reddit and other forums

Developers still ask questions, but maybe not on Stack Overflow anymore. In my personal experience, I rely more on online forums like Reddit, Github, Hugging Face forum, and Discord groups, etc besides AI coding tools. Questions about new releases or new bugs can be found in those spaces.

{{< figurelightbox src="question-hugging-face-2.png" caption="Question about error caused by new release is asked on Hugging Face Forum" align="center" width="80%" >}}

Similar to collecting documentation and source code, LLM providers need to source and clean content from different technical communities and forums for better model performance. It sounds tedious, but from what I know, data sourcing is a significant part of an LLM provider’s job. Otherwise, Meta would not pay nearly [$15 Billion](https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html) for Scale AI in recent weeks

#### Data from users

Currently, many paid AI coding tools like Cursor allow its users to turn on `Privacy Mode`, and Cursor promises to retain zero data for LLM training. However, as I mentioned in [my previous post](http://andreagao.com/posts/blog-set-up/#traeai), editors like Trae.ai are likely to use users’ code for LLM training. This is not a piece of news on the Internet. When users are not paying for a product, they are the product.

Therefore, when terms permitted, I think LLM providers will collect user interaction data from IDE or Slack or Github to train their coding LLMs.

### New product – Stack Overflow 2.0 in AI era

Stack Overflow was in decline before developers started using LLMs and AI coding tools, because of its own management. Now with the advent of endless AI coding tools, developers are voluntarily or involuntarily learning new ways of coding. I believe there will be a new paradigm for developers in the near future. Or I should say, the best coding practice is always evolving, but the changes brought by LLMs are faster and more dramatic.

A new product similar to Stack Overflow but tailored to the AI era with better user experience might emerge to bridge the gaps – developers can ask questions at a centralized place and LLM providers can access difficult coding questions on it.

I look forward to seeing a product like this emerging soon. If not, maybe I should build it myself🤔.

## Conclusion

Quality data are the foundation of LLMs, and they are as important as innovative model architecture like [Transformer](https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/) and computing resources like Nvidia chips. As traditional Q&A forums like Stack Overflow die down and developers change their work flow, LLM providers need to continue inventing new ways to address new problems in programming. This article discussed a few approaches, and I believe more approaches will come.

## Reference

- Cover picture is from [Search O'RLY Covers](https://orlybooks.com/), and I just love the site.
- [Stack overflow is almost dead](https://blog.pragmaticengineer.com/stack-overflow-is-almost-dead/)
- [Which topics on Stack OverFlow are affected the most? ](https://tomazweiss.github.io/blog/stackoverflow_decline/)
- [Ask HN: Why Is Stack Overflow Fading Away?](https://news.ycombinator.com/item?id=41364798)
- [Tech layoffs since 2023](https://news.crunchbase.com/startups/tech-layoffs/)
- [Meta Invests $14.3 Billion in Scale AI to Kick-Start Superintelligence Lab](https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html)
- New bug question on Hugging Face Forum: https://discuss.huggingface.co/t/js-gradio-error/160152
