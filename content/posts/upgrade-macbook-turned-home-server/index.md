---
date: 2026-11-01
draft: true
title: "Upgrade my old Macbook turned home server"
description: ""
tags: ["tech", "engineering", "personal"]
category: "engineering"
ShowToc: true
cover:
  image: "plex.png"
---


This post is a continuation of an early post (andreagao.com/posts/setup-home-server-on-mac/). If you are interested in initial set up of a home server with an old macbook, you can refer to that post. 

After almost a year of using and managing my home server, I'm quite happy with it and I've made a series of upgrades to it over time. I started treating my home server as a hobby--it's a every evolving project depending on my interest and needs.  

## Starting point

```text
Machine   : MacBook Pro (Retina, 13-inch, Mid 2014)
CPU       : Intel Core i5-4278U, 2 cores / 4 threads, 2.6 GHz
Memory    : 8 GB
Storage   : 256 GB Apple SSD
OS        : Ubuntu 24.04.5 LTS

Network   : Verizon 5G(up to 300Mbps), Wi-Fi, Tailscale
Storage   : 1 TB Seagate Expansion + 500 GB Toshiba
Apps      : Docker, Plex, miniflux
Battery   : Capped at 80%
```

## Why and what I upgraded

### Network: switch from Wi-Fi to Ethernet for better speed

#### Problems
- **4K movie buffering on Plex**: I have collected some 4K movies, but failed to play them smoothly on TV with Plex--streaming keeps buffering. I suspected it's due to network bandwidth since both my TV and server were connected to the Internet through Wifi. 
- **Transfer files between my devices**: It took up to 10 minutes to copy a movie from my laptop to server, which is quite annoying. 

#### Upgrade: 

I got two Ethernet cables--one from Amazon and one from Taobao. The one from Taobao is less than $1 USD. It was shipped to my friend's address in China, and I picked up during a wedding trip in September. 

Unfortunately, I didn't plan well and had to buy a second cable from Amazon after my China trip, which I paid more than $8 USD. 

Other than paying extra on Amazon, switching from Wi-Fi to cable was fairly easy for both server and TV. I mostly just put the server next to my router and plugged the cables in both devices. After confirming my server was connected to the internet via Ethernet, I disabled its Wi-Fi connection to keep the network setting of the server simple.  

The 4K movie buffering issue was solved immediately after the TV was hooked up with the router. File transferring between my server and laptop is also 10 times faster than using Wi-Fi.

{{< figurelightbox src="ethernet-taobao.png" caption="My $1 USD Chinese cable from Taobao" align="center" width="100%" >}}

{{< figurelightbox src="ethernet.png" caption="My $8 USD cable from Amazon" align="center" width="100%" >}}

### Storage: more space and data safety

#### Problem
I'm pretty confident that my hard drives are over 10 years old and they've been moving around aross the globe multiple times. I have decades of photos on the drives--it's unwise if I don't back up my data with some new hard drive ASAP. 

#### Upgrade

- **Hard drive enclosure**

Before I purchase a new hard drive, I've ordered two hard drive enclosure from Taobao to pick up during the same trip in China. For the same brand and the same model, the price on Taobao is about 1/3 to 1/2 on Amazon. 

{{< figurelightbox src="enclosure.png" caption="UGREEN enclosure cost me $13 USD on Taobao" align="center" width="100%" >}}

{{< figurelightbox src="enclosure-amazon.png" caption="The same UGREEN enclosure is $30 USD on Amazon" align="center" width="100%" >}}

- **Hard drive**

I plan to buy two 4TB hard drives(one for daily operation and one for backup) to replace my old portable ones, but the price of hard drive has raised almost 100% in last 12 months. I'm still holding off and waiting for Black Friday deals. In the worst case scenario, I will only buy one and wait for a future deal. 

{{< figurelightbox src="seagate-price.png" caption="Price of Seagate IronWolf 4TB skyrocketed thanks to AI booms" align="center" width="100%" >}}

### Apps: Pi-hole + Plex clean up

#### Problem

- **Plex cluttering**: I have hundreds of movies and TV series in my hard drives, which I acquired over the years. Not surprisingly, their names and all other metadata were messy. I often struggled to find a movie on Plex even though I know it exact name. Therefore, I knew it would be nice to clean up the metadata of my media collection.

- **Ads**: I've been using ad-blocker on my browser, which works pretty well. But I still saw ads on Apps like Reedit, NYTimes and WSJ on my phone. The ads bother me, and I want to further block them.

#### Upgrade

- **Plex decluttering**

This is a great task for AI--tedious and repetitive, but with manageable risk. I briefed Claude on the task and my risk tolerance (I don't want to accidently delete any of the media files). Claude came up a plan with fallback option. I accepted the plan and reviewed the output in each step, which declusttered my media collection within an hour. 

Honestly, it might take me a whole day or weekend to decluster my media files without AI, and I might never start doing it. 

- **Pi-hole**

Pi-hole is a network-wide ad blocker on Linux hardware--it's popular among folks hosting server at home. Pi-hole serves as a light-weighted {{< newtabref href="https://en.wikipedia.org/wiki/Domain_Name_System" title="DNS" >}}, which looks up IP addresses and blocks ads, tracking, device telemetry and malwares. Users can define what they want to block, but it's easy to use open-sourced blocklists as well. For example, I use this {{< newtabref href="https://github.com/stevejenkins/pi-hole-lists" title="pi-hole-lists" >}}. 

Pi-hole makes me feel good, since it not only blocks ads, but also allows me to be tracked less online. I am nostalgic for the internet in the 90s and early 2000s.

{{< figurelightbox src="pi-hole.jpg" caption="My pi-hole blocks 17.5% of all queries" align="center" width="100%" >}}

### Security & maintenance

#### Problem
- Hackers exploited/are exploiting {{< newtabref href="https://www.reddit.com/r/DataHoarder/comments/vnxwbi/how_long_do_external_hard_drives_last_on_average/)" title="4 vulneralibities of Plex in October 2026" >}}. 
- I wanted to self-host my server since I prioritze privacy and control over convinience. But none of them matters if security is at risk, which urges me to strengthen my server and set up an upgrade routine. 

#### Upgrades

**A routine on sticker**

Upgrading applications on my server(actually any device including phone and laptop) regularly can lower security risk. By the time the Plex exploitation happened, if I had not upgraded my Plex to 1.43.3 or above, I might be a target of hackers. 

I created a upgrade routine sticker for my server. I don't want to set up an automatic upgrade job since I don't have that many apps and I dislike unnecessary overheads. 

{{< figurelightbox src="upgrade.png" caption="This sticker is on my laptop and I go through the steps every month" align="center" width="100%" >}}

**Network access**

I used to host a Umami server on Digital ocean to track my website traffic, but it was attacked and down a few months in. Therefore, I have gone extra mile to ensure my home server is not accessible to the public internet. The following list is example steps I took to control the network access to my server:

- UPnP disabled
- Router firewalls enabled
- No port forwarding
- Plex remote access diabled
- Tailscale funnel inactive