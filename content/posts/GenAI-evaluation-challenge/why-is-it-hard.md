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

**Essentially, ML is what we are used to and have been evaluating in last decades, and GenAI and LLM are the new technology we want to evaluate against.** AI is a umbrella term for everything🙃. 

## GenAI Model vs GenAI Application Evaluation

In my experience, when people talk about GenAI evaluation, they might not be aware that there is significant difference between GenAI foundation model evaluation and GenAI application evaluation. Both of them are on-going and evolving problems in industry and academia. However, GenAI application evaluation is less talked about comparing to GenAI foundation model evaluation. 

- **GenAI foundation model evaluation**: evaluation and benchmarking of foundation models like GPT-4, Dall-E, and Sora, etc.
- **GenAI application evaluation**: 
    - Evaluation and measurement of application enabled by GenAI foundation models like Cursor, a customized call center AI chatbot, etc. 
    - Foundation models are critical part of the GenAI application, but other modules like a vector database or external tools in the application significantly impact the performance of the whole application as well. 

**Not distinguishing the difference between GenAI foundation models and GenAI applications is one of the reasons leading to challenging GenAI application evaluation.** For example, you might use the latest and best LLM model to build a customer service chatbot using a RAG architecture. But if the knowledge base stored in the vector database is not well engineered, I'm confident that whole customer service chatbot will underperform your expectation. 

There are many academic articles and blogs detailing GenAI foundation model evaluation already. I will link some helpful ones in references section, and focus this article on GenAI application evaluation.

However, as the following architecture diagram shown below, a GenAI application is a software application built with GenAI foundation model/models along with other modules. Generally, the objective of a GenAI application is to make end user's life easier by improving their producibility or automate some processes. It usually contains some system logic layer and interface layer. The system logic layer contains internal and external tools, databases, pipeline, and business logic, etc. The interface layer is where the application communicates with the end users. It could be a chatbot UI or command line tool.

To evaluate a GenAI application end to end is to understand:
- **Quantifiable Benefit**: how much incremental gain the application brings to target end users. For example, if an AI coding tool can improve engineers productivity by 50%, it can (ideally) translate to 50% revenue gain. 
- **Isolate and Evaluate**: Build a framework to independently evaluate the performance of each module in the architecture diagram, so that you can identify where the gaps are in the system and improve upon the result. 
- **Cost of adopting GenAI**: Evaluate the operation cost of the GenAI application including engineer effort, external GenAI API cost, human labeller cost, and iteration opportunity cost, etc.

{{< figure src="/posts/GenAI-evaluation-challenge/GenAI-abstract-architecture.svg" alt="An abstract architecture of GenAI applications" caption="An abstract architecture of GenAI applications" align="center" >}}

After I explained what GenAI application evaluation entails, I hope you've realized it's an indeed complex problem. Therefore, it's inherently hard to tackle. 

## References:

- [Anthropic's guide on GenAI foundation model evaluation](https://www.anthropic.com/news/evaluating-ai-systems): Anthropic shared the challenging they've faced when evaluating GenAI models. 
- [Levels of AGI for Operationalizing Progress on the Path to AGI](https://arxiv.org/abs/2311.02462) <!-- tbd -->