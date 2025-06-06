---
date: 2025-06-04
draft: false
title: 'Get out of mainstream and personalized movie recommendation'
tags: ["movie", "personalization"]
ShowToc: true
cover:
    image: "metrograph.png"
    width: 70%
---
## TL;DR
As a movie lover, I have got frustrated by my experience with streaming services in the last few years. I developed an app to help me discover hidden gems. You can check out the app [here](#try-it-out) or on {{< newtabref href="https://huggingface.co/spaces/gytcrt/random-movie-hf" title="hugging face space" >}}.

## My frustration with streaming services
If you know me as a friend, most likely you have noticed that I am a big movie fan. I track what's going on in independent movie theaters ([checkout this section](#beloved-independent-movie-theaters-in-nyc)) in NYC, go to the {{< newtabref href="https://www.filmlinc.org/about-us/new-york-film-festival/" title="New York Film Festival" >}}, and watch some movies over and over again. 

I don't watch as many movie as I hope in recent years, since I frequently find myself in the following situation: 
- Open a streaming service app, browse for 10 mins, but find nothing interesting to watch
- Switch to another streaming service app, repeat step 1
- Close the TV after 30 minutes of searching and exhausting my streaming services

Not surprisingly, I feel very disappointed and annoyed at the end of the loop. I have been thinking about this question for a long time: **Why is it so hard for me to find an interesting movie at home?** And I have a few hypotheses:
- **Market saturation**: unlike 10 years ago, the streaming service market is overly saturated now. Interesting movies (old and new) are distributed across different platforms. The situation hurts the user's experience and wallet.
- **Personalized recommendations**: almost all streaming platforms present their contents to users via a personalization system. I think personalization systems are brilliant and helpful in many ways, but often prevent us from discovering movies outside of our comfort zone. 
- **Content skewing**: streaming platforms tend to onboard mainstream or critically acclaimed films, because those contents generally serve a large audience. For a movie snob like me, it's hard to find edgy or cult movies on the streaming platforms.  

Therefore, I decided to build something to help me discover movies that are unknown and interesting to me. Here is what I want from an app:
- Show me movies that would not normally show up on my feeds.
- Include the movie's meta information and some reviews from critics and audience.
- Tell me where I can stream the movie if it's on a streaming platform.

I spent a few hours coding up the idea and I've landed an MVP. The main function of the app is to recommend a list of movies to a user based on time period, region, and genre. I intentionally made it simple and random to mimic movie discovering experience in a physical movie rental store. I have been using the app for the last few days and happily discovered many unknown and interesting movies. Feel free to play and let me know if you find it helpful or have feedback.

## Try it out
<div class="gradio-embed-container">
<iframe
	src="https://gytcrt-random-movie-hf.hf.space"
	frameborder="0"
	width="100%"
	height="800"
></iframe>
</div>

<style>
  .gradio-embed-container {
    width: 100%;
    margin: 30px 0;
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 3px;
  }
  
  .gradio-embed-container iframe {
    width: 100%;
    border: none;
    display: block;
  }
</style>

## Beloved independent movie theaters in NYC
- {{< newtabref href="https://metrograph.com/" title="**Metrograph**" >}}: locating in Two Bridges neighborhood, they show a lot of classic Asian movies.
- {{< newtabref href="https://filmforum.org" title="**Film Forum**" >}}: best artistic selection in the city
- {{< newtabref href="https://www.filmlinc.org/" title="**Film at Lincoln Center**" >}}: NYFF is hosted here every year, so it's a special place in NYC.
- {{< newtabref href="https://www.ifccenter.com/" title="**IFC**" >}}: very convenient location with unique selection at times
- {{< newtabref href="https://angelikafilmcenter.com/nyc" title="**Angelika**" >}}: go there if you happen to be in So-Ho
- {{< newtabref href="https://nitehawkcinema.com/" title="**Nitehawk**" >}}: the definition of hipster movie theater in Brooklyn
- {{< newtabref href="https://www.bam.org/" title="**BAM**" >}}: I go there for both independent and commercial movies when I prefer staying in Brooklyn. 