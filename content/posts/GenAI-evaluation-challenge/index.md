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
- **Lack of framework**: GenAI application is not GenAI foundation model; it requires different framework to evaluate them. 
- **Unstructured and subjective outputs**: GenAI apps produce unstructured data (text, images, etc.), making objective, automated evaluation far more challenging than for classic ML models.
- **Foundation model unpredictability**: Foundation models are not deterministic, so repeated runs can yield different results, complicating GenAI application evaluation.
- **High cost and slow iteration**: Building high-quality evaluation datasets and running continuous and large-scale tests is resource-intensive, both in terms of time and money. 

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
<div style="text-align: center; margin-bottom: 20px;">
<strong><em>Table 1: Common evaluation metrics for LLM applications with examples</em></strong>
</div>

Given the complex nature of LLM application evaluation, many people started using LLMs to evaluate output of their LLM application. Many GenAI evaluation packages like [DeepEval](https://www.deepeval.com/) and [ARTKIT](https://github.com/BCG-X-Official/artkit) offer automated AI evaluation (I have participated in the development of ARTKIT). I do think using LLM to evaluate LLM applications is necessary and helpful, given the amount of output data can be beyond human's capacity to process and LLMs are generally good at language understanding. **However, I think overly relying on LLMs to evaluate LLM application is not realistic and even dangerous.** No matter whether you are using the same family of LLMs to evaluate your LLM application (OpenAI GPTs to evaluate application built on OpenAI GPTs), or using different LLMs to evaluate the LLM application(Google Gemini to evaluate application built on OpenAI GPTs), you are essentially introducing another LLM while evaluating the target LLM application. Would you assume the evaluator LLM's outputs are 100% correct or would you build another evaluation process to evaluate the evaluator LLM? :) The problem become more philosophical now.

I think it's necessary to use LLMs to evaluate LLM applications, but through a carefully design process. I will elaborate on this maybe in another future article.

## GenAI foundation models introduce unpredictability 
Unlike traditional ML models, GenAI models are non-deterministic. It means even for the same input, the GenAI models can return different results on different runs. The non-deterministic nature of GenAI models adds extra difficulty on GenAI application evaluations. 

### Image generation example
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

### Classification example
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
<div style="text-align: center; margin-bottom: 20px;">
<strong><em>Table 2: Accuracy comparison across multiple evaluations for ML models vs LLM classifier</em></strong>
</div>

The accuracy stays consistent for logistic regression model and SVM, since they are deterministic models and the validation set is unchanged through out 10 rounds. However, the accuracy of LLM classifier fluctuates over time. The fluctuating acc

**How should the Food Coop compare the new LLM classifier with traditional ML models for this classification task?** 

In theory, the Food Coop needs to model accuracy of LLM classifier as:

`Observed accuracy = Accuracy + variance of the LLM application`

In practice, the Food Coop might compare average accuracy of the 3 models and decide the SVM model preforms better than the LLM classifier. However, this is not an ideal approach since many businesses are required to provide expandability to their model outcomes. 

### New bias-variance paradigm

[The bias-variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff) is a classic paradigm in supervised machine learning. One of major tasks of ML evaluation is to find the optimal model complexity for a ML problem. The image below is a text-book visualization of the paradigm.

{{< figurelightbox src="Bias_and_variance_contributing_to_total_error.png" caption="Bias and variance as function of model complexity" align="center" width="80%" >}}
<div style="text-align: center; margin-bottom: 20px;">
<em>Image by Bigbossfarin - Own work, CC0, via <a href="https://commons.wikimedia.org/w/index.php?curid=105307219">Wikimedia Commons</a></em>
</div>

However, when GenAI applications are introduced to the paradigm, I think the visualization should be updated as following:
{{< figurelightbox src="new_bias_variance_paradigm.png" caption="Updated bias and variance as function of model complexity" align="center" width="80%" >}}

The purple interval around the total error means total error is not a fixed number based on variance and bias anymore, the unpredictability(variance) of GenAI model makes the total error fluctuate within the interval. In Table 2 example, the purple interval represents the variance of accuracy of the same LLM classifier.

By comparing the two paradigms, I hope the complexity of GenAI application evaluation is more clear to you. 

## GenAI application evaluation is expensive and time consuming
Besides the complexities elaborated above, building an proper process to evaluate a GenAI application is also expensive and time consuming. 

The best practice of developing a machine learning system is to start from proof-of-concept and built towards [continuous delivery and automation pipelines](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) over time. The same framework can be adopted to GenAI application as well. **The modern MLOps practice requires you to test your application on data, improve your application, generate new test data, and iterate the process rapidly.** If one iteration of evaluation is costly and slow, continuous iteration is naturally challenging.

### Evaluation dataset building
However, generating evaluation dataset or golden dataset for GenAI application and iterating on it is more complex than previous ML systems. For example, if you want to build an effective GenAI Q&A system, you have to build a list of golden Q&A dataset to test your system. Curating a high-quality golden Q&A dataset is significantly more difficult than labelling objects on an images, because reading texts requires more time and context understanding. Sometimes, only certain people with expertise are capable of curating a golden Q&A dataset, and the task cannot be out sourced to internal or external data labelers.

Therefore, building proper an evaluation dataset for a GenAI application and updating the dataset can be expensive and slow.

### Evaluation cost
Even when a good evaluation dataset is built, running tests on it can be challenging. Conventionally, training a ML model can take long time and considerably amount of resources, but inference on the trained model is fast and cheap. However, when evaluating a GenAI application built upon a 3rd party foundation model provider, you will encounter:

- **API latency**: GenAI foundation model APIs typically have much higher latency than traditional ML model inference. While a conventional ML model might return results in milliseconds, GenAI APIs can take seconds or even minutes for complex prompts. This latency significantly slows down the evaluation process, especially when testing hundreds or thousands of examples.

- **API rate limit**: Most foundation model providers impose strict rate limits on their APIs to manage server load and prevent abuse. These rate limits force you to implement complex batch processing, asynchronous logic, queuing mechanisms, and retry logic in your evaluation pipeline. You may need to spread your evaluation over longer periods or request (and pay for) higher rate limits, further extending the time and cost of thorough testing.

- **API cost**: Even though LLM like GPT4 has decreased significantly, it is still very costly comparing to traditional ML like OCR. Especially, when the input and output of the system contain large size of texts or high-resolution images, the cost of running tests continuously is not economically wise.   

Hosting an open-source GenAI foundation model might help you avoid API related issue, but it still requires intense resources and expertise. You might finding your organization spending more money and time on cloud resources and debugging its configuration than using an API from a foundation model provider. 

## Conclusion 
Evaluating GenAI applications is a different challenge than evaluating traditional machine learning systems or even GenAI foundation models themselves. The unstructured nature of GenAI outputs, the inherent unpredictability of foundation models, and the high cost and effort required to build robust evaluation datasets all contribute to this complexity. While automated tools and LLM-based evaluators can help, they are not a panacea and must be used thoughtfully to avoid introducing new sources of error or bias.

In future articles, I would love to deep dive into my advice on GenAI application evaluation. 

## References

- [Anthropic's guide on GenAI foundation model evaluation](https://www.anthropic.com/news/evaluating-ai-systems): Anthropic shared the challenging they've faced when evaluating GenAI models. 
- [Levels of AGI for Operationalizing Progress on the Path to AGI](https://arxiv.org/abs/2311.02462) <!-- tbd -->
- [ML metrics cheatsheet by Stanford](https://stanford.edu/~shervine/teaching/cs-229/cheatsheet-machine-learning-tips-and-tricks)