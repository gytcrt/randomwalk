---
date: 2026-11-14
draft: false 
title: "Upgrade my old MacBook turned home server"
description: "Upgrades after almost a year of running a 2014 MacBook Pro as a home server: Ethernet for 4K Plex, new storage, Pi-hole ad blocking, and a security routine."
tags: ["tech", "engineering", "home server"]
category: "engineering"
ShowToc: true
cover:
  image: "home-server.jpg"
---


This post is a continuation of my previous post--{{< newtabref href="https://andreagao.com/posts/setup-home-server-on-mac/" title="why and how to turn a dusty old MacBook into a home server" >}}. If you are interested in the initial setup of a home server with an old MacBook, you can refer to that post. 

After almost a year of using and managing my home server, I'm quite happy with it and I've made a series of upgrades to it over time. I started treating my home server as a hobby--it's an ever evolving project depending on my interest and needs.  

## Starting point

Here are the specs of my initial setup:

```text
Machine   : MacBook Pro (Retina, 13-inch, Mid 2014)
CPU       : Intel Core i5-4278U, 2 cores / 4 threads, 2.6 GHz
Memory    : 8 GB
Storage   : 256 GB Apple SSD
OS        : Ubuntu 24.04.5 LTS

Network   : Verizon 5G(up to 300Mbps), Wi-Fi, Tailscale
Storage   : 1 TB Seagate Expansion + 500 GB Toshiba
Apps      : Docker, Plex, Miniflux
Battery   : Capped at 80%
```

## Why and what I upgraded

### Network: switched from Wi-Fi to Ethernet for better speed

#### Problems
- **4K movie buffering on Plex**: I have collected some 4K movies, but failed to play them smoothly on TV due to insufferable buffering. I suspected it's due to network bandwidth since both my TV and server were connected to the Internet through Wi-Fi. 
- **Transfer files between my devices**: It took up to 10 minutes to copy a 4K movie from my laptop to the server, which is quite annoying. 

#### Upgrade

I got two Ethernet cables--one from Amazon and one from Taobao. The one from Taobao is less than $1 USD. It was shipped to my friend's address in China, and I picked it up during a wedding trip in September. 

Unfortunately, I didn't plan well and had to buy a second cable from Amazon after my China trip, which cost more than $8 USD. 

Other than paying extra on Amazon, switching from Wi-Fi to cable was fairly easy for both the server and the TV. I mostly just put the server next to my router and plugged the cable in both devices. After confirming my server was connected to the internet via Ethernet, I disabled its Wi-Fi connection to keep the network setting of the server simple.  

The 4K movie buffering issue was solved immediately after the TV was hooked up with the router. File transferring between my server and laptop is also 10 times faster than using Wi-Fi.

{{< figurelightbox src="ethernet-taobao.png" caption="My $1 USD Chinese cable from Taobao" align="center" width="100%" >}}

{{< figurelightbox src="ethernet.png" caption="My $8 USD cable from Amazon" align="center" width="100%" >}}

### Storage: more space and data safety

#### Problem
My hard drives are over 10 years old and have moved with me across the globe multiple times. I have decades of photos on the drives--it's unwise if I don't back up my data with some new hard drive ASAP. 

#### Upgrade

- **Hard drive enclosure**

Before purchasing a new hard drive, I ordered two hard drive enclosures from Taobao to pick up during my same trip in China. For the same brand and the same model, the price on Taobao is about 1/3 to 1/2 the cost on Amazon. 

{{< figurelightbox src="enclosure.png" caption="UGREEN enclosure cost me $13 USD on Taobao" align="center" width="100%" >}}

{{< figurelightbox src="enclosure-amazon.png" caption="The same UGREEN enclosure is $30 USD on Amazon" align="center" width="100%" >}}

- **Hard drive**

I plan to buy two 4TB hard drives (one for daily operation and one for backup) to replace my old portable ones, but the price of a hard drive has risen almost 100% in the last 12 months. I'm still holding off and waiting for Black Friday deals. In the worst case scenario, I will only buy one and wait for a future deal. 

If the AI bubble bursts, I hope at least the price of hard drives will go down.

{{< figurelightbox src="seagate-price.png" caption="Price of Seagate IronWolf 4TB skyrocketed thanks to AI booms" align="center" width="100%" >}}

> Update: I bought a 4TB Seagate BarraCuda for $149.99 from Newegg during the week of Thanksgiving. It's not the fanciest hard drive or the cheapest price I can get, but I'm just pleased that I can migrate my data away from my 10 year old hard drives now.  


{{< figurelightbox src="barracuda-front.jpg" caption="My new 4TB Seagate BarraCuda, $149.99 from Newegg" align="center" width="100%" >}}
{{< figurelightbox src="barracuda-back.jpg" caption="The back of the BarraCuda" align="center" width="100%" >}}

### Apps: Pi-hole + Plex clean up

#### Problem

- **Plex cluttering**: I have hundreds of movies and TV series in my hard drives, which I acquired over the years. Not surprisingly, their names and all other metadata were messy. I would often struggle to find a movie on Plex even though I know its exact name. Therefore, I reckoned it would be nice to clean up the metadata of my media collection.

- **Ads**: I've been using an ad blocker on my browser, which works pretty well. But I still saw ads on apps like Reddit, NYTimes and WSJ on my phone. The ads bother me.

#### Upgrade

- **Plex decluttering**

This is a great task for AI--tedious and repetitive, but with manageable risk. I briefed Claude on the task and my risk tolerance (I don't want to accidentally delete any of the media files). Claude came up with a plan and a fallback option. I accepted the plan and reviewed the output in each step, which decluttered my media collection within an hour. 

Honestly, it might have taken me a whole day or weekend to declutter my media files without AI, and I might never have started doing it. 

{{< figurelightbox src="plex.png" caption="My Plex after decluttering" align="center" width="100%" >}}

- **Pi-hole**

Pi-hole is a network-wide ad blocker on Linux hardware--it's popular among folks hosting servers at home. Pi-hole serves as a lightweight {{< newtabref href="https://en.wikipedia.org/wiki/Domain_Name_System" title="DNS" >}}, which looks up IP addresses and blocks ads, tracking, device telemetry and malware. Users can define what they want to block, but it's easy to use open-source blocklists as well. For example, I use this {{< newtabref href="https://github.com/stevejenkins/pi-hole-lists" title="pi-hole-lists" >}}. 

Pi-hole makes me feel good, since it not only blocks ads, but also allows me to be tracked less online. I am nostalgic for the internet in the 90s and early 2000s.

{{< figurelightbox src="pi-hole.jpg" caption="My pi-hole blocks 17.5% of all queries" align="center" width="100%" >}}

### Security & maintenance

#### Problem
- Hackers exploited/are exploiting {{< newtabref href="https://www.reddit.com/r/selfhosted/comments/1x9trfc/plex_being_actively_exploited_plex2shell_on_32400/" title="4 vulnerabilities of Plex in October 2026" >}}. 
- I wanted to self-host my server since I prioritize privacy and control over convenience. But none of that matters if security is at risk, which urges me to strengthen my server and set up an upgrade routine. 

#### Upgrade

**A routine on sticker**

Upgrading applications on my server (actually any device including phone and laptop) regularly can lower security risk. By the time the Plex exploitation happened, if I had not upgraded my Plex to 1.43.3 or above, I might have been a target of hackers. 

I created an upgrade routine sticker for my server. It's manual and I plan to execute it once a month since I don't have that many apps and I dislike unnecessary overhead. 

{{< figurelightbox src="upgrade.png" caption="This sticker is on my laptop and I go through the steps every month" align="center" width="100%" >}}

**Network access**

I used to host a Umami server on DigitalOcean to track my website traffic, but it was attacked and went down a few months in. Therefore, I have gone the extra mile to ensure my home server is not accessible to the public internet. The following lists example steps I took to control the network access to my server:

- UPnP disabled
- Router firewalls enabled
- No port forwarding
- Plex remote access disabled
- Tailscale funnel inactive

Through these processes, I picked up some network engineering knowledge, and it's also fun.