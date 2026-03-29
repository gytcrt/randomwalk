---
date: 2026-03-29
draft: false
title: "Why and how to turn a dusty old MacBook into a home server"
description: "Repurpose your dusty old Mac as a home server: install Ubuntu Server, set up Docker, run Plex and Miniflux, and access your services securely from anywhere"
tags: ["tech", "engineering", "personal"]
category: "engineering"
ShowToc: true
cover:
  image: "plex-on-tv.jpg"
---

## Why?

I have been using Miniflux and Plex for a couple of years. Miniflux serves as a blog and news feed, since I can control who I follow and how information is presented to me. Plex allows me to enjoy my local movie collections similar to any other streaming service. 

In my article {{< newtabref href="https://andreagao.com/posts/cut-back-amazon-instagram-netflix-google/" title="Convenience vs Agency" >}}, I discussed how I want more agency over my digital life and assets. In addition to Proton Mail and Firefox, Miniflux and Plex are the services I chose to meet that need. 

However, Miniflux and Plex need to be hosted on a server; before this month, the server was my main work laptop. I frequently felt annoyed when I needed to open my laptop and plug it into the charger whenever we wanted to watch a movie from Plex or I noticed the Docker container for my Miniflux was running in the background and taking up memory. 

Meanwhile, I have a retired MacBook Pro from 2014 sitting on my bookshelf and collecting dust. I’ve thought about recycling it, but that idea makes me sentimental. Finally, it occurred to me that I can use my old laptop as a home server for Miniflux and Plex. This solves two problems for me at once:

* I don’t need to get rid of my old MacBook anymore  
* I can free my main laptop from Miniflux and Plex

## How?

### Step 1: back up and reset my MacBook Pro

Before you turn an old laptop to a home server, be sure to back up any important or sentimental documents from the old laptop. You don’t want to lose the only copy of the tax return for 2020 or a love letter of your first love. 

I have backed up and migrated data from the old laptop years ago, but I still took some time to sort through the files before I finally reset it. 

After you are 100% sure you don’t need anything from the laptop, you are ready to wipe out its past. The easiest way to restore a MacBook to factory settings is to follow Apple’s instructions {{< newtabref href="https://support.apple.com/en-us/102664" title="here" >}}.

{{< figurelightbox src="oldmac.jpg" caption="Restore my dusty Mac to factory settings" align="center" width="80%" >}}

### Step 2: Install a new operating system for the home server

The next step is to choose an appropriate operating system for your repurposed home server. This step is critical, since everything downstream depends on this choice. For my case, I had two options:

* MacOS: upgrade my MacBook Pro to a more modern MacOS and set up my applications like my current main laptop. This approach is relatively easy and straightforward. However, the newer version of MacOS will take a decent amount of RAM and storage, even though I only need it as a server.   
* Another Linux-based system like Ubuntu, Debian or Raspberry Pi: this is a more technical approach. If I install a Linux-based system on my old laptop, it will essentially operate as a headless server—its monitor, keyboard or trackpad is not necessary anymore and I can control it with my main laptop via ssh on a terminal. With this set up, my home server will be quite similar to a cloud VM except it sits in my home network and is physically close to my TV. 

I initially wanted the easy approach—macOS—since my needs for the home server are simple, and I thought my old laptop should be able to handle it. However, it turned out to be quite painful to install any newer version of applications on the laptop, since Apple has stopped providing upgrades to it and applications like Docker require modern macOS. After 30 minutes, I realized it was not worth using macOS for my home server—Apple wants me to recycle my ancient Mac and upgrade to the newest model every 3 years anyway.  

{{< figurelightbox src="macos.jpeg" caption="macOS was not a viable option for me" align="center" width="100%" >}}

Then, I installed the latest LTS(long-term support) Ubuntu server from {{< newtabref href="https://ubuntu.com/download/server" title="here" >}}, and used ChatGPT and Google to guide me through the installation process. One thing you will need here is a USB drive with at least 4GB storage to serve as a bootable media. The following screenshot from Google illustrates the process step by step.      

{{< figurelightbox src="install-ubuntu.png" caption="" align="center" width="90%" >}}


### Step 3: Configure the home server

#### Internet connection

After installing Ubuntu on my old laptop, it’s essentially a headless computer except it was not connected with the Internet yet. Ideally, it would be quite easy if I had Ethernet and a proper Ethernet cable, but I didn’t have the cable nor did I want to buy one. So I used my phone as a hotspot to upgrade my Ubuntu system and set up Wi-Fi to connect to my home network. 

#### Set up Docker

Before installing Plex, Miniflux, or any other application, I installed Docker. Docker is a lightweight virtual machine (container) that simplifies environment management across different software. Docker is widely used in both enterprise software development and open source projects. 

Follow Docker’s {{< newtabref href="https://docs.docker.com/desktop/setup/install/linux/ubuntu/" title="official instruction" >}} to install it on a server.

#### Install Plex and Miniflux

Both Plex and Miniflux provide detailed instructions to install them on an Ubuntu server. And I found it even easier to install them with Docker. The following pages are from Plex and Miniflux’s official instructions; using the documents along with ChatGPT made the process smooth for me.

- {{< newtabref href="https://miniflux.app/docs/docker.html" title="Miniflux installation with Docker" >}}
- {{< newtabref href="https://support.plex.tv/articles/200288586-installation/" title="Plex installation" >}}

#### Install Tailscale

Since Miniflux serves as my personal news feed, ideally I can access it outside of my home internet securely. Tailscale can help you easily set up your own VPN for your devices and access the home server from everywhere. 

{{< figurelightbox src="my-device.jpg" caption="My devices on Tailscale" align="center" width="50%" >}}

{{< figurelightbox src="miniflux-phone.PNG" caption="Accessing miniflux from my phone" align="center" width="50%" >}}

#### Mount an external hard drive 


I mounted a 1TB hard drive to my server, which contains most of my movie collections. 

#### Migrate data and movies to my new home server

```bash
rsync -avh --progress ~/02_Areas/movie/[movie_name] andrea@6street:/home/andrea/movies/
```

- `~/02_Areas/movie/[movie_name]` is the path to the movie or file on your local machine.
- `andrea@6street` is the user name and server name.
- `/home/andrea/movies/` is the path on the server.


## Finally 

I’ve been happily using my home server for a month now, and I highly encourage you to repurpose an old laptop to a small AI agent or home server. It’s a fun home project. 
