---
date: 2025-05-08
draft: true
title: 'Why Is It Hard To Evaluate GenAI Applications?'
tags: ["tech", "GenAI", "AI", "testing"]
ShowToc: true
cover:
    image: "GenAI-abstract-architecture.svg"
    # width: 80%
---
## TL;DR

## Introduction
I have spent last 2.5 years on listening to what business wants from GenAI, building GenAI applications and delivering value from the applications. It has been interesting journey for me, and I realized the advent of ChatGPT is a paradigm shift for ML/AI practitioners like me. I started believe GenAI would change our lives like personal computer in 90s or modern search engine in 2000s.

Before I dive into evaluation of GenAI, I want to define a few key terms for this article. These terms are used interchangeable and over-used nowadays, but I found it difficult to discuss any AI related topic without clearly defining the scope of these terms. Please find my definition below:

{{< figurelightbox src="AI-terms.svg" alt="What AI, ML, GenAI and LLM mean in this article" caption="What AI, ML, GenAI and LLM mean in this article" align="center" >}}

**Essentially, ML is what we are used to and have been evaluating in last decades, and GenAI and LLM are the new technology we want to evaluate against.** AI is a umbrella term for everything🙃. 

## GenAI Model vs GenAI Application Evaluation

In my experience, when people talk about GenAI evaluation, they might not be aware that there is significant difference between GenAI foundation model evaluation and GenAI application evaluation. Both of them are on-going and evolving problems in industry and academia. However, GenAI application evaluation is less talked about comparing to GenAI foundation model evaluation. 

- **GenAI foundation model evaluation**: evaluation and benchmarking of foundation models like GPT-4, Dall-E, and Sora, etc.
- **GenAI application evaluation**: 
    - Evaluation and measurement of application enabled by GenAI foundation models like Cursor, a customized call center AI chatbot, etc. 
    - Foundation models are critical part of the GenAI application, but other modules like a vector database or external tools in the application significantly impact the performance of the whole application as well. 

**Not distinguishing the difference between GenAI foundation models and GenAI applications is one of the reasons leading to challenging GenAI application evaluation.** For example, you might use the latest and best LLM model to build a customer service chatbot using a RAG architecture. But if the knowledge base stored in the vector database is not well engineered, I'm confident that whole customer service chatbot will underperform your expectation. 

There are many academic articles and blogs detailing GenAI foundation model evaluation already. I will link some helpful ones in references section, and focus this article on GenAI application evaluation.

However, as the architecture diagram shown below, a GenAI application is a software application built with GenAI foundation model/models along with other modules. Generally, the objective of a GenAI application is to make end user's life easier by improving their producibility or automate some processes. It usually contains some system logic layer and interface layer. The system logic layer contains internal and external tools, databases, pipeline, and business logic, etc. The interface layer is where the application communicates with the end users. It could be a chatbot UI or command line tool.

To evaluate a GenAI application end to end is to understand:
- **Quantifiable Benefit**: how much incremental gain the application brings to target end users. For example, if an AI coding tool can improve engineers productivity by 50%, it can (ideally) translate to 50% revenue gain. 
- **Isolate and Evaluate**: Build a framework to independently evaluate the performance of each module in the architecture diagram, so that you can identify where the gaps are in the system and improve upon the result. 
- **Cost of adopting GenAI**: Evaluate the operation cost of the GenAI application including engineer effort, external GenAI API cost, human labeller cost, and iteration opportunity cost, etc.

{{< figurelightbox src="GenAI-abstract-architecture.svg" caption="An abstract architecture of GenAI applications" align="center" >}}

After I explained what GenAI application evaluation entails, I hope you've realized it's an inherently complex problem. This article aims to demystify the problem.

## Evaluating text, image, or other media as output 
Most classic machine learning problems fall into 2 categories: **Classification** or **Regression**. When we encounter a real world problem, and want to use machine learning to solve it, we usually start with translating the problem to the classic machine learning framework. 

Classification and regression have standard evaluation metrics like confusion matrix, accuracy, precision/recall, and R square, etc. If you are interested to read more, please refer to [ML cheatsheet reference](https://stanford.edu/~shervine/teaching/cs-229/cheatsheet-machine-learning-tips-and-tricks). There are more nuanced derivative metrics for different types of problems like precision@k and [NDCG@K](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) for ranking problem. **The classic metrics all share one similarity: they are easily quantifiable via testing set. However, it's not the case for GenAI applications.**

For many GenAI applications, their outputs are texts, images, or videos, etc. They are [**unstructured data**](https://www.mongodb.com/resources/basics/unstructured-data). On the one hand, the new types of output format are part of GenAI magic. People can easily use natural language to interact with ML/AI technology now. On the other hand, the unstructured data formats make GenAI application evaluation more challenging than traditional ML models. For simplicity, I will use LLM applications as an example to explain it, and outputs of LLM applications are majorly texts. 

The following table is a few selected and widely used LLM application metrics with examples. Unlike metrics for classification or regression models, quantifying the LLM metrics is not a simple string comparison or arithmetical calculations. Evaluating metrics like Relevancy, Bias and Hallucination requires a lot of careful design, context understanding and even expertise. For example, if a LLM application is used for medical context, it would be difficult for someone without medical adequate training to evaluate relevancy and hallucination for the application.       
      
| Metric        |Definition                                                                                              | Example                                                                                                                               |
|---------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Relevancy** | How on-topic and directly useful the LLM application's output is to a specific task.| You ask: "Marketing slogans for a new eco-friendly water bottle."  <br> **Relevant:** "Hydrate Sustainably!" <br> **Irrelevant:** "The history of plastic manufacturing." |
| **Bias**      | Whether the application outputs biases against certain gender, races or other protected groups.| You use a LLM application to generate descriptions for job roles. <br> **Bias:** If it consistently describes "nurses" with feminine pronouns and "engineers" with masculine pronouns. |
| **Hallucination** | Whether the LLM application confidently states something as fact that is incorrect, nonsensical, or made-up.| You ask: "What was our company's Q3 revenue last year in the APAC region?" <br> **Hallucination:** The LLM replies "$5.7 million from our new Tokyo office," when your company has no Tokyo office and revenue was different. |


Given the complex nature of LLM application evaluation, many people started using LLMs to evaluate output of their LLM application. Many GenAI evaluation packages like [DeepEval](https://www.deepeval.com/) and [ARTKIT](https://github.com/BCG-X-Official/artkit) offer automated AI evaluation (I have participated in the development of ARTKIT). I do think using LLM to evaluate LLM applications is necessary and helpful, given the amount of output data can be beyond human's capacity to process and LLMs are generally good at language understanding. **However, I think overly relying on LLMs to evaluate LLM application is not realistic and even dangerous.** No matter whether you are using the same family of LLMs to evaluate your LLM application (OpenAI GPTs to evaluate application built on OpenAI GPTs), or using different LLMs to evaluate the LLM application(Google Gemini to evaluate application built on OpenAI GPTs), you are essentially introducing another LLM while evaluating the target LLM application. Would you assume the evaluator LLM's outputs are 100% correct or would you build another evaluation process to evaluate the evaluator LLM? :) The problem become more philosophical now.

I think it's necessary to use LLMs to evaluate LLM applications, but through a carefully design process. I will elaborate on this maybe in another future article.

## GenAI foundation models introduce unpredictability 
Unlike traditional ML models, GenAI models are non-deterministic. It means even for the same input, the GenAI models can return different results on different runs. The non-deterministic nature of GenAI models adds extra difficulty on GenAI application evaluations. 

For example, I used the same prompt and OpenAI Dall-E 3 to generate 4 images for my cat. And the prompt is

>**Pixel art illustration** of a silver-shaded British Shorthair cat playfully fighting with an Amazon Kindle e-reader. The scene is **charming and whimsical**, with the round, fluffy cat using its paws to swipe at or wrestle the sleek Kindle device. Render in detailed 8-bit pixel art style, using cool silver-gray tones for the cat and dark, glossy colors for the Kindle, with a simple, light-colored background.

| ![British shorthair vs Kindle 1](british_shorthair_vs_kindle_2.png) | ![British shorthair vs Kindle 2](british_shorthair_vs_kindle_3.png) | ![British shorthair vs Kindle 3](british_shorthair_vs_kindle_4.png) | ![British shorthair vs Kindle 4](british_shorthair_vs_kindle_5.png) |
|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| *image 1* | *image 2* | *image 3* | *image 4* |

Among the 4 pixel images, I personally prefer image 2. Image 3 is too realistic and not like a pixel art. The cat in image 4 seems quite concerned and the scene is not charming or whimsical. As for image 1, it's obviously an incoherent image.

Here come the questions for evaluation:

- How do I evaluate the image outputs? 
- Should I use the best output (image 2) or worst output (image 1)? 
- Who's there to evaluate the quality of the outputs? 

Even the pixel art generation example is trivial itself, the questions regarding evaluation are not trivial. **GenAI models introduce extra unpredictability to your application.**

Besides generative tasks like image generation above, I've seen GenAI models applied to classification problems by business. Applying GenAI models to classic ML problems also face challenge from unpredictability in evaluation phase. I created following example based on my observation on how businesses have tried to adopt GenAI applications into their workflow.

A grocery store called Food Coop used to use ML models to classify the category of a new product based on its meta information and description. For example, a new product named "cucumber favored Doritos" should be classified into "Food > Snack Food > Chips" category manually or by ML models. Using ML models to process most of new products has saved a lot of manual work from the Food Coop's staff. Recently, the Food Coop started exploring using LLM to classify new product category, meaning giving product taxonomy and new product information and asking LLM to return the most appropriate category for the new product. Suppose the Food Coop's engineer uses the same validation set from previous ML model to test their new LLM classification model, and run the evaluation 10 times on ML models and LLM model, the engineer will get following model score table:
| Accuracy | Logistic Regression | SVM | LLM classifier |
|-----------------|---------------------|-----------------|-----------------|
| Round 1 | 88% | 91% | 87% |
| Round 2 | 88% | 91% | 88% |
| Round 3 | 88% | 91% | 92% |
| Round 4 | 88% | 91% | 89% |
| Round 5 | 88% | 91% | 86% |
| Round 6 | 88% | 91% | 93% |
| Round 7 | 88% | 91% | 91% |
| Round 8 | 88% | 91% | 92% |
| Round 9 | 88% | 91% | 95% |
| Round 10 | 88% | 91% | 94%|
| Average |88%|91%|90%|

The accuracy stays consistent for logistic regression model and SVM, since they are deterministic models and the validation set is unchanged through out 10 rounds. However, the accuracy of LLM classifier fluctuates over time. 

**How should the Food Coop compare the new LLM classifier with traditional ML models for this classification task?** 

In theory, the Food Coop needs to model accuracy of LLM classifier as:

`Observed accuracy = Accuracy + variance of the LLM application`

In practice, the Food Coop might compare average accuracy of the 3 models and decide the SVM model preforms better than the LLM classifier. However, this is not an ideal approach since many businesses are required to provide expandability to their model outcomes. 


## GenAI application evaluation is expensive and time consuming

## Conclusion 

## References

- [Anthropic's guide on GenAI foundation model evaluation](https://www.anthropic.com/news/evaluating-ai-systems): Anthropic shared the challenging they've faced when evaluating GenAI models. 
- [Levels of AGI for Operationalizing Progress on the Path to AGI](https://arxiv.org/abs/2311.02462) <!-- tbd -->
- [ML metrics cheatsheet by Stanford](https://stanford.edu/~shervine/teaching/cs-229/cheatsheet-machine-learning-tips-and-tricks)