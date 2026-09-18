---
title: "A Short History of Bi-Directional Links"
author: Maggie Appleton
url: https://maggieappleton.com/bidirectionals
kind: essay
published: 2020
clipped: 2026-09-18
capture_quality: medium
capture_note: >
  正文取自渲染后的 HTML 页面并经文本抽取（剥离 script/style 后按块级标签断行）。
  原文是 Next.js 站点，抽取过程可能丢失部分强调标记与图片说明；
  行内链接保留为 URL 形式。已剔除站点头部导航与文末的 webmention 列表。
  本文是「双向链接史」这一题目的权威通俗文献，作者为设计人类学背景的
  Maggie Appleton（Digital Garden 概念的主要推广者之一）。
---

Seventy years ago we dreamed up links that would allow us to create two-way, contextual conversations. Why don't we use them on the web?

 Design 

 Digital Gardening 

 The Web 

 Web Development 

Planted over 6 years ago 
Last tended over 5 years ago 

 Table of Contents 

 Bi-directional links are not new 

 Bi-direction Linking in Personal Digital Gardens 

 Building Your Own Bi-Directionals 

 Bi-Directional Linking with WebMentions 

 Table of Contents 

 Bi-directional links are not new 

 Bi-direction Linking in Personal Digital Gardens 

 Building Your Own Bi-Directionals 

 Bi-Directional Linking with WebMentions 

 With the recent rise of Roam Research https://roamresearch.com/ 

 , the idea of bi-directional linking is having a bit of a moment. 

 We’re all very used to the mono-directional link the World Wide Web is built around. They act as one-way pointers we follow in a linear sequence.

 While we can link to any site, the destination page hasn’t a clue we’ve done so.

 We set up all these single-direction paths, trying to signal relevance and context, only to have the other side completely ignore our efforts.

 Our monolinks are trying to establish relationships in vain.

 We’re starting to look around our mono-linked environment and wonder why it’s so hard to surface relevant contextual relationships.

 Manually interlinking content takes an awful lot of human curation and effort. Efforts we should probably slog off onto our systems.

 ✶ Enter the bi-directional link ✶

 A bi-directional link has social awareness - it knows about other pages or ‘nodes’ that point to it, and can make them visible to people. This means we get a two-way conversation flowing between our web locations.

 Bi-directional links are not new

 The idea of the bi-directional link goes back to 1945 81ya when Vannevar Bush https://en.wikipedia.org/wiki/Vannevar_Bush 

 dreamed up the Memex https://en.wikipedia.org/wiki/Memex 

 machine.

 Vannevar outlined this hypothetical gadget in an essay in The Atlantic called As We May Think https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/ 

 . He wanted a system capable of “associative indexing… whereby any item may be caused at will to select immediately and automatically another… [so that] numerous items have been thus joined together to form a trail.”

 This essay turned out to be a foundational document for the ideologies that directly led to both the internet and the Web. Yes, those are two entirely separate pieces of technology. Vannevar was one of the key movers and shakers rallying folks to help build the original internet infrastructure. He corraled folks at MIT, the US Department of Defence, the National Science Foundation and various research labs like the Standford Lincoln Lab, Bell Labs, the RAND Corporation, and Xerox PARC to get involved. Walter Isaacson, The Innovators https://www.librarything.com/work/15179823 

 : How a Group of Hackers, Geniuses, and Geeks Created the Digital Revolution (London: Simon & Schuster, 2015 11ya ). 

 Suffice to say, the guy was driven by a belief that enabling people to connect information and share knowledge would expand the scope of human understanding. The Memex was one idea of how that might manifest in material form.

 Vannevar even created a small informative diagram of this desk-bound vision. Marketing chops 101. 
 Vannevar’s evocative description of the Memex is especially impressive given that digital computers had only come into existence 5 years earlier. Most were still the domain of large military operations like Bletchley Park, and were seen as inconveniently large calculators.

 Implementing a wildly interactive computational personal knowledge base wasn’t much of an option.

 So the idea went into hiberation and didn’t resurface until the idea of personal computing began blooming in the sixties and seventies. Ted Nelson https://en.wikipedia.org/wiki/Ted_Nelson 

 , an unlikely film director and sociologist, stumbled into a series of computing lectures and began to imagine how graphical interfaces might reinvent the way we write and connect ideas. He took inspiration directly from Vannevar’s essay, and in 1965 61ya when he coined the term hypertext to describe his vision for a sprawling network of interlinking information.

 Nelson planned to implement these hypertextual dreams in his perpetually-imminent Project Xanadu. If you have some time, this is quite the internet history rabbit hole https://en.wikipedia.org/wiki/Project_Xanadu 

 to run down. Ted Nelson is on another level https://www.youtube.com/watch?v=F0NgV3yNd2o 

 . 

 The Xanadu project was a hypertext system that imagined that every sentence, block, and page would be part of a vast bi-directionally linked network.

 A design mockup of how Project Xanadu might visually connect pieces of text across multiple documents 
 😳

 You’d be able to trace information back to its origin the way current web links do. But you’d also be able to see who had referenced, remixed, and expanded off that original. The full Pattern Language of Project Xanadu The Pattern Language of Project Xanadu

 Project Xanadu as a pattern language, rather than a failed software project expands far beyond just bi-directional links to include features like Transclusions Transclusion and Transcopyright Dreams

 The lost permissioning and copyright system of the Web , but we won’t dive into it all here.

 Suffice it to say, Xanadu didn’t pan out.

 Instead, we got the less fancy, but far more real and useable World Wide Web that currently does not support bi-directionals on an infrastructure level.

 While Sir Tim Berner’s Lee wrote himself a note https://www.w3.org/DesignIssues/Topology.html 

 debating their pros and cons back in 1999 27ya , there is an obvious design issue with letting two-way connections flow freely around the web.

 If every site that linked to yours was visible on your page, and you had no control over who could and couldn’t link to you, it is not hard to imagine the Trollish implications…

 Figuring out how we might filter, moderate, and set permissions around link visibility turned into quite the challenge https://dl.acm.org/doi/epdf/10.1145/74224.74236 

 . The design details https://dl.acm.org/doi/epdf/10.1145/74224.74229 

 grew complex https://dl.acm.org/doi/epdf/10.1145/74224.74245 

 .

 It became clear implementing the Web with simpler mono-directional links was the right thing to do, given that its creators wanted universal adoption. Lots of people are still mad about it. Let’s not venture too far down that historical wormhole.

 The TLDR is technology is hard .

 Until Xanadu ships https://www.wired.com/1995/06/xanadu/ 

 and we’re all immersed in the universe of multi-linked, version-controlled nodes of remixable micro-content (that somehow solves the problems of permissions and moderation), there are still plenty of ways we can resurrect the possibility of bi-directional links on the web.

 Bi-direction Linking in Personal Digital Gardens

 Most of the design issues with adding bi-directional links to the global web were related to moderation and permissions. However, adding them within the bounds of a single website with one author sidesteps that problem.

 There’s been a flurry of interest around bi-directionals among people involved in the Digital Gardening A Brief History & Ethos of the Digital Garden

 A newly revived philosophy for publishing personal knowledge on the web movement.

 Much of this was originally sparked by Andy Matuschak’s notes . Go have a good browse through them.

 Andy's linked notes stack on top of one another, allowing you to browse to new notes while previous notes are still visible 

 There’s plenty to admire here. It should be noted Andy is an experienced developer and interaction
designer, and these notes should not be taken as the standard expectation
for the rest of us normal plebby internet citizens. But the key part of this system that creates interlinked context is
the “Links to this Note” section at the bottom of each post.

 Anytime Andy links to another one of their notes on the site, it’ll pop up as a related note at the bottom of the page. This is the bi-directional dream.

 It gives us a way to navigate through these ideas in exploratory mode, rather than navigating a hierarchy of categories on a main index page.

 Since it’s all contained within a single-author site, our Spammish-Troll-risk factor is at a comfortable zero. This is mildly tangential, but I love how the topic of bi-directional links
makes fully visible our “websites are locations” and “websites are
containers” conceptual metaphors with “inside” and “outside” 
links. 

 Building Your Own Bi-Directionals

 That’s all very cool, but how are you supposed to build bi-directionals into your own site? Thankfully, setting up your own public gardening bi-directional Memex doesn’t involve Xanadu.

 One fantastic option for non-developers is based around a personal wiki system called TiddlyWiki https://tiddlywiki.com/ 

 . Anne-Laure Le Cunff wrote up an easy-to-follow guide to getting your own up and running https://nesslabs.com/tiddlywiki-beginner-tutorial 

 .

 For those of us here for the hyper-customised, over-engineered JavaScript solution (that would be me 🙌), the Gatsby.js https://www.gatsbyjs.org/ 

 community has a number of active gardening enthusiasts building themes and plugins.

 I built mine using Aengus McMillin’s gatsby-theme-brain https://github.com/aengusmcmillin/gatsby-theme-brain 

 . Aengus has documented the theme well and it’s not too challenging to implement (as long as you’re comfortable in JavaScript and React).

 I also curate a list of tools for Digital Gardening A Brief History & Ethos of the Digital Garden

 A newly revived philosophy for publishing personal knowledge on the web on this GitHub repo https://github.com/MaggieAppleton/digital-gardeners/ 

 Bi-Directional Linking with WebMentions

 While I argued that Web-wide bi-directional links are unlikely to happen at a global scale, there’s a way you can add bi-directionals to your personal website that picks up on references anywhere on the web.

 WebMentions https://webmention.io/ 

 are a piece of web infrastructure the IndieWeb https://indieweb.org/ 

 community has done a lot of work to advocate for. The W3C gave the specification https://www.w3.org/TR/webmention/ 

 recommendation status in 2017 9ya .

 The system notifies a URL whenever that site is mentioned elsewhere on the web. You’re then able to show that mention and its contents on your site. It’s essentially an opt-in bi-directional linking system.

 Plenty of folks have written useful guides on how to add these to your site. Here’s one for any static site https://keithjgrant.com/posts/2019/02/adding-webmention-support-to-a-static-site/ 

 , one for Gatsby https://www.christopherbiscardi.com/post/building-gatsby-plugin-webmentions 

 , one for Next.js https://css-tricks.com/jumping-into-webmentions-with-nextjs-or-not/ 

 . There’s a whole list of implementation examples on the IndieWeb Wiki https://indieweb.org/Webmention#IndieWeb_Examples 

 you can look through.

 5 Backlinks

 A Brief History & Ethos of the Digital Garden

 A newly revived philosophy for publishing personal knowledge on the web 

 Digital Gardening for Non-Technical Folks

 How to build a digital garden without touching code 

 Transclusion and Transcopyright Dreams

 The lost permissioning and copyright system of the Web 

 The Pattern Language of Project Xanadu

 Project Xanadu as a pattern language, rather than a failed software project 

 A Meta-Tour of This Site

 A video tour through how I build the old version of this site
