---
date: 2025-05-08
draft: true
title: 'Why Is It Hard To Evaluate GenAI Applications?'
tags: ["tech", "GenAI", "AI", "testing"]
ShowToc: true
---
## TL;DR

## Introduction
I have spent last 2.5 years on listening to what business wants from GenAI, building GenAI applications and delivering value from the applications. It has been interesting journey for me, and I realized the advent of ChatGPT is a paradigm shift for ML/AI practitioners like me. I started believe GenAI would change our lives like personal computer in 90s or modern search engine in 2000s.

Before I dive into evaluation of GenAI, I want to define a few key terms for this article. These terms are used interchangeable and over-used nowadays, but I found it difficult to discuss any AI related topic without clearly defining the scope of these terms. Please find my definition below:

{{< figure src="/posts/GenAI-evaluation-challenge/AI-terms.svg" alt="What AI, ML, GenAI and LLM mean in this article" caption="What AI, ML, GenAI and LLM mean in this article" align="center" >}}

**Essentially, ML is what we are used to and have been evaluating in last decade, and GenAI and LLM are the new technology we want to evaluate against.** AI is a umbrella term for everything🙃. 

## Model vs Application Evaluation

In my experience, when people talk about GenAI evaluation, they might not be aware that there is significant difference between GenAI foundation model evaluation and GenAI application evaluation. Both of them are on-going and evolving problems in industry and academia. However, GenAI application evaluation is less talked about comparing to GenAI foundation model evaluation. 

- **GenAI foundation model evaluation**: evaluation and benchmarking of foundation models like GPT-4, Dall_E, and Sora, etc.
- **GenAI application evaluation**: evaluation and measurement of application enabled by GenAI foundation models like Cursor, a customized call center AI chatbot, etc. 

Not distinguishing the difference between GenAI foundation model and GenAI application is one of the reason leading to challenging GenAI application evaluation. For example, you might use the latest and best LLM model to build a customer service agent, 