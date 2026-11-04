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

### Network: switch from Wifi to Ethernet for better speed
- 4K movie on Plex: I have collected some 4K movies, but failed to play them smoothly on TV with Plex--streaming keeps buffering. I suspected it's due to network bandwidth since both my TV and server were connected to the Internet through Wifi. 
- Transfer files between my devices: It took up to 10 minutes to copy a movie from my laptop to server, which is quite annoying. 

### Storage: more space and data safety
I'm pretty confident that my hard drives are over 10 years old and they've been moving around aross the globe multiple times. It's simply unwise if I don't back up my data in them. 

### Apps: 

- Pi-hole

- Plex media collection clean up: I have hundreds of movies and TV series in my hard drives, which I acquired over last 2 decades. Not surprisingly, their names and all other metadata were messy. I often struggled to find a movie on Plex even though I know it exact name. Therefore, I knew it would be nice to clean up the metadata of my media collection. 
### Security & maintenance
- Hackers exploited/are exploiting 4 vulneralibities of in October 2026(https://www.reddit.com/r/DataHoarder/comments/vnxwbi/how_long_do_external_hard_drives_last_on_average/). 
- I wanted to self-host my server since I prioritze privacy and control over convinience. But none of them matters if security is at risk, which urges me to strengthen my server and set up an upgrade routine. 

## Upgrades

- Apps: 
    - pi-hole: block ad and tracking
    - Plex: re-formated and indexed my movie and TV collections
- Internet:
    - Server to router: Ethernet. 
    - TV to router: Ethernet. 
- Hard drive: 
    - I've bought 
    - I plan to buy one or two 4TB hard drive to replace my old portable ones, but the price of hard drive has raised almost 100% in last 12 months. I'm still holding off and waiting for Black Friday deals. In the worst case scenario, I will only buy one 

{{< figurelightbox src="seagate-price.png" caption="Price of Seagate IronWolf 4TB skyrocketed thanks to AI booms" align="center" width="100%" >}}

- Upgrade routine