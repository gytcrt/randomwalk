---
date: 2025-12-25
draft: true
title: "How much money is Cursor losing to keep users?"
description: ""
tags: ["AI", "vibe coding", "start-up"] # does this actually show up in tag/search section?
category: "start-up"
ShowToc: true
cover:
  image: "cursor-2025-models.png"
---

## TL; DR

Cursor has published a 2025 report for every user, and I enjoyed reviewing it. I couldn't stop thinking how the economics works for Cursor given the numbers. Therefore, I did some analysis based on my report and other reports from X. Here are the key takeaways:

* Even consuming 250 million tokens in 2025, I am an average user compared with other Cursor users. It means many enthusiastic vibe coders or professional coders are taking advantage of or exploiting Cursor.   
* As an average user, I paid $180 for my subscription to Cursor, but used $838.55 to $2,014.95 worth of token. Cursor is spending more money on other power users.  
* Users' engagement is subsidized by investors' money like how Amazon, Uber and Airbnb acquired and retained their users. As history tells us, the current spending is not sustainable and will shift in future. 

## Introduction

AI has changed my workflow as an engineer in the last 3 years. [Instead of digging through Google results and Stackoverflow](https://andreagao.com/posts/ai-challenge-after-stack-overflow-died/), I "chat" with Cursor and ChatGPT for coding problems, or directly assign tasks to AI coding agents. Below is a screenshot of my Cursor usage in 2025.  

{{< figurelightbox src="cursor-2025.png" caption="My 2025 Cursor usage report showing 252 million tokens consumed." align="center" width="65%" >}}


When I first read my Cursor 2025 report, I was pretty shocked that I've used 252 million tokens within a year. I proudly texted my friend: "I'm sure Cursor is losing money on me, and I'm a power user."  However, when I looked up the Cursor 2025 report on X, I realized the top 10% Cursor users generally consume more than 5 billion tokens in 2025\. From a token consumption perspective, I might be an average user for Cursor. 

*How could Cursor justify their business model if an average user like me consumes more than 250 million tokens?* 

I could not wrap my head around the question, so I decided to guesstimate the economics behind Cursor. 

## My assumptions

If I want to comprehensively calculate my cost as a user for Cursor, I need to consider both variable costs and fixed costs. The variable costs include LLM API inference and Cloud infra; the fixed costs include employee salary and R\&D investment. In this article, I will only estimate LLM API inference cost per user, since it's directly linked to each user's token usage and less than the total cost of a user by definition. 

Before we dig in to the estimation, we need a few assumptions about token price, LLM model, and token mixture. 

### Token price

Cursor enables users to choose major LLMs at their will, but Anthropic Claude is the most popular model family among users (including me). Therefore, I will anchor the standard token price on [Anthropic's official API price](https://claude.com/pricing\#api).

* Input: $3 per million token  
* Output: $15 per million token

### Enterprise price discount 

Cursor is a major customer of Anthropic's, even their relationship can be very complicated – Anthropic likes to directly own AI coding use cases via [Claude Code](https://www.claude.com/product/claude-code). It's safe to assume Cursor is paying less than the public price for each token by signing enterprise deals with LLM providers, owning dedicated instances, and using token caching. 

Unless I work at Cursor and manage their operation cost, I won't know the real price per million token for them. But I will continue my analysis with 3 price scenarios:

* 30% off  
  * Input: $2.1 per million token  
  * Output: $10.5 per million token  
* 50% off  
  * Input: $1.5 per million token  
  * Output: $7.5 per million token  
* 70% off  
  * Input: $0.9 per million token  
  * Output: $4.5 per million token

### Input/output mixture

Given input and output tokens are priced differently, but the Cursor 2025 report doesn't break my 252 million token down by type, I need to estimate an input/output distribution. Obviously, users like me want to input simple but sufficient instructions and expect AI agents on Cursor to output quality code. For a more conservative estimate, I will assume my input makes up 30% of the tokens. 

* Input token: 30%  
* Output token: 70%

## Equation to calculate API cost

**Variables:**
- **T** = Total tokens = 252.5M  
- **r** = Input share = 30%  
- **(1 − r)** = Output share = 70%  
- **P_input** = $3 per 1M tokens  
- **P_output** = $15 per 1M tokens  
- **d** = Discount rate = 30% / 50% / 70%

**Formula:**

```
API cost = T × (r × P_input + (1-r) × P_output) × (1 - d)
```

## API cost vs my subscription

I started a paid subscription to Cursor in April 2025, which adds to $20 \* 9 \= $180 revenue for them.

Based on my assumptions and equation above, the estimated API cost is 

<div align="center">

| <span style="font-size:1.3em; display:inline-block; min-width:180px">**Discount rate**</span> | <span style="font-size:1.3em; display:inline-block; min-width:150px">**Cost**</span> |
| :---- | :---- |
| 30% off | $2,014.95 |
| 50% off | $1,439.25 |
| 70% off | $838.55 |

</div>

If Cursor wants to make the revenue and API cost break-even in my case, the discount rate has to be 93%. It means they must ensure P\_input is below 0.21$ per 1M input tokens and P\_output is below $1.05 per 1M output tokens.

I think Cursor is spending a lot more money on me than my subscription fee.

## Other user data I found online

As I mentioned in the first part of the post, I am not a power user based on the Cursor's own report. Here is a top 6% user from X.   

{{< figurelightbox src="cursor_x_user.jpg" caption="A top 6% Cursor user consumed 6.24 billion tokens in 2025." align="center" width="65%" >}}

Source: [X post from @jcruzfff](https://x.com/jcruzfff/status/2002257937679737079)

Now I plug in this user's token consumption in my calculation, the estimated API cost for Cursor is: 

<div align="center">

| <span style="font-size:1.3em; display:inline-block; min-width:180px">**Discount rate**</span> | <span style="font-size:1.3em; display:inline-block; min-width:150px">**Cost**</span> |
| :---- | :---- |
| 30% off | $49,795.2 |
| 50% off | $35,568 |
| 70% off | $21,340.8 |

</div>




I'm not sure what tier of subscription this user has been on in 2025, but even they have subscribed to [the highest tier](https://cursor.com/pricing), they would only pay Cursor $200 \* 12 \= $2,400 for 2025 unless they have enabled the "On-demand usage" option. It's unlikely Cursor is making a profit on this user. I guess the real question should be: how much money is Cursor losing to keep users?

{{< figurelightbox src="cursor-tier.png" caption="Cursor pricing tiers in 2025" align="center" width="100%" >}}


## Conclusion

My estimation in this post is based on a rough assumption of LLM API price and does not include any cost from platform infra or fixed cost. However, it still demonstrates that Cursor users like me are using way more resources than they are paying for their subscriptions. 

So who's paying for the users? Investors. 

While everyone else is now paying more for Uber, Amazon, and food delivery services than they were 10 years ago, engineers and vibe coders can technically take advantage of this AI cycle. 

How long can this last? Is this sustainable? I don't know. 

In 2025, AI has contributed a significant part of GDP growth in the US. AI coding is currently the crown jewel of broader AI adoption. Given my estimation in this article, there's still a long way to turn investment into profit.
