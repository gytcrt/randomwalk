---
date: 2026-06-24
draft: false
title: "How to use an under-utilized Claude Max plan to save API cost"
description: "Use \"claude -p\" headless mode as a pseudo Anthropic API to run requests through an idle Claude Max plan, and the trade-offs that come with it."
tags: ["tech", "engineering", "AI", "claude"]
category: "engineering"
cover:
    image: "burning-through-api.jpg"
    alt: "The 'This is fine' cartoon dog sitting calmly in a room engulfed in flames, captioned 'Burning through API credits'"
    width: 100%
ShowToc: true
---

## Background

I've been actively developing our product lately, which consumes a lot of Anthropic tokens by repetitively inputting and outputting a set of text data for testing and iteration. As we all know, tokens are expensive (👀); I try to be mindful of the cost as a founder and for our clients. Last week, it occurred to me my Claude Max 5x ($100/month) was under-utilized. I started wondering whether I can use my Claude Max plan to save API cost, and I found the following approach.

{{< figurelightbox src="claude-max-usage.png" caption="My Claude Max 5x is under-utilized" alt="My Claude Max 5x is under-utilized and it can be used as a pseudo API" align="center" width="100%" >}}

## The method: use "claude -p" as a pseudo Anthropic API

In Anthropic's {{< newtabref href="https://code.claude.com/docs/en/headless" title="documentation" >}}, it says `claude -p` flags to any claude command to run it non-interactively. This means that `claude -p` can be used like a pseudo API—instead of calling Anthropic API, I can send the context of an API call via `claude -p` and process the request through my Claude Max plan.

What does this mean in practice, exactly? Let me demo a hello world example. In this example, we want to use Sonnet 4.5 and ask it to say hello in English and translate it into Chinese.

### Call API

- Suppose you have a Anthropic API key: sk-api-key-secret

- Use the API key and ask Claude-sonnet-4-5 model to "Say hello in one sentence and translate it in Chinese" in terminal with the following command

```bash
curl -X POST "https://api.anthropic.com/v1/messages" \
  -H "x-api-key:sk-api-key-secret" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  --data-raw '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 100,
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one English sentence
          like a GenZ and translate it in Chinese"
      }
    ]
  }'
```

- It returns:

```json
{
  "model": "claude-sonnet-4-5-20250929",
  "id": "msg_xxxxxxxxxxxxxxxxxxxxxxxx",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text":
        "**English (GenZ):** Hey bestie, no cap you're giving main
        character energy today!

        **Chinese translation:** 嘿闺蜜/兄弟，说真的你今天主角光环爆棚！
        (Hēi guīmì/xiōngdì, shuō zhēn de nǐ jīntiān zhǔjiǎo guānghu"
    }
  ],
  "stop_reason": "max_tokens",
  "stop_sequence": null,
  "stop_details": null,
  "usage": {
    "input_tokens": 22,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "cache_creation": {
      "ephemeral_5m_input_tokens": 0,
      "ephemeral_1h_input_tokens": 0
    },
    "output_tokens": 100,
    "service_tier": "standard",
    "inference_geo": "not_available"
  }
}
```

### Use "claude -p" as a pseudo API

- Ensure you are logged in claude code in terminal

- Type in

```bash
claude -p "Say hello in one English sentence like \
a GenZ and translate it in Chinese"
```

- It shows:

```bash
Hey bestie, whats good? 👋

嘿朋友，最近怎么样？
```

I think it's easier to use the `claude -p` pseudo API than curling a real API in the example above. You can ask Claude Code to apply the method to more complex cases.

## Pros and cons

Using `claude -p` to mimic API comes with pros and cons:

Pros:

- It works—`claude -p` performs like a pseudo API and I saved money on API by using my idle Claude Max plan.

Cons:

- It's slow. Anthropic is actively throttling my session when I use `claude -p` to run a batch of classification jobs. In my experience, what takes 10 mins to run via API with a single thread would take 60 minutes to run via `claude -p`.

- Anthropic is actively monitoring usage of `claude -p` and might limit this usage anytime. {{< newtabref href="https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan" title="Here" >}} is the evidence from Anthropic's own website.

## Conclusion

If you are an independent developer and building some hobby projects on the side, leverage `claude -p` to save your overhead cost. However, if you want to develop and iterate faster for a commercial project, `claude -p` might not satisfy your needs.
