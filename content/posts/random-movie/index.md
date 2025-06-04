---
date: 2025-06-04
draft: true
title: 'Get out of mainstream and personalized movie recommendation'
tags: ["movie", "personalization"]
ShowToc: true
cover:
    image: "metrograph.png"
    width: 70%
---
## TL;DR
As a movie lover, I have got frustrated by my experience with streaming services in the last few years. I developed an app to help me discover hidden gems. You can check out the app [here](#try-it-out) or on [hugging face space](https://huggingface.co/spaces/gytcrt/random-movie-hf).

## My frustration with streaming services
If you know me as a friend, most likely you have noticed that I am a big movie fan. I track what's going on in independent movie theaters(I will them in reference section) in NYC, go to the [New York Film Festival](https://www.filmlinc.org/about-us/new-york-film-festival/), and watch some movies over and over again. 

I don't watch as many movie as I hope in recent years, since I frequently find myself in the following situation: 
Open a streaming service app, browse for 10 mins, but find nothing interesting to watch and cannot find any interesting movie to start
Switch to another streaming service app, continue step 1
Close the TV after 30 minutes of searching and exhausting my streaming services End and close the TV until I exhaust all my streaming services after 30 minutes search

Not surprisingly, I feel very disappointed and annoyed at the end of the loop. I have been thinking about this question for a long time: **Why is it so hard for me to find an interesting movie at home?** And I have a few hypotheses:
- **Market saturation**: unlike 10 years ago, the streaming service market is overly saturated now. Interesting movies (old and new) are distributed across different platforms. The situation hurts the user's experience and wallet.
- **Personalized recommendations**: almost all streaming platforms present their contents to users via a personalization system. I think personalization systems are brilliant and helpful in many ways, but often prevent us from discovering movies outside of our comfort zone. 
- **Content skewing**: streaming platforms tend to onboard mainstream or critically acclaimed films, because those contents generally serve a large audience. For a movie snob like me, it's hard to find edgy or cult movies on the streaming platforms.  

Therefore, I decided to build something to help me discover movies that are unknown and interesting to me. Here is what I want:
- Show me movies that would not normally show up on my feeds.
- Include the movie's meta information and some reviews from critics and audience.
- Tell me where I can stream the movie if it's on a streaming platform.

I spent a few hours coding up the idea and I've landed an MVP. I have been using the app for the last few days and happily discovered many unknown and interesting movies. Feel free to play and let me know if you find it helpful or have feedback.

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
- [**Metrograph**](https://metrograph.com/): locating in Two Bridges neighborhood, they show a lot of classic Asian movies.
- [**Film Forum**](https://filmforum.org): best artistic selection in the city
- [**Film at Lincoln Center**](https://www.filmlinc.org/): NYFF is hosted here every year, so it's a special place in NYC.
- [**IFC**](https://www.ifccenter.com/): very convenient location with unique selection at times
- [**Angelika**](https://angelikafilmcenter.com/nyc): go there if you happen to be in So-Ho
- [**Nitehawk**](https://nitehawkcinema.com/): the definition of hipster movie theater in Brooklyn
- [**BAM**](https://www.bam.org/): I go there for both independent and commercial movies when I prefer staying in Brooklyn. 