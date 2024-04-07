title: Technical Strengths
subtitle: Alan Ray Profile
status: hidden
slug: profile-technical-strengths
layout: page

[TOC]

> If I don't know it yet, I'll learn it.
>
> _Alan on his technical skills philosophy_

# Solution Spaces

* _Software as a service_: I've spent over a decade in the software-as-a-service industry, both providing a reliable service as well as quickly adapting it to the current business needs.
* _Applications_: I've done both desktop Windows and MacOS applications, along with mobile applications (mostly Android).
* _Web applications_: I've built a variety of web applications (frontend and backend), including multiple single page applications.
* _Embedded systems_: I spent a number of years building mission-critical applications for the automotive industry, including commercial trucking and police vehicles. Change management looks totally different when a change potentially puts lives at risk.
* _User experience_: As part of understanding what makes good software design, I've studied (or at least dabbled in) the realm of user experience: How can the software not just technically work, but actually be a joy to work with[^users]?

[^users]: Most software actually has many users -- the end user, the company or individual making the purchase, the developers creating and maintaining a system, the sales department selling the product, and so on.

# Languages

These are my main languages in which I've done extensive work.

* _Python (15+ years)_: I've done a bit of everything, including web servers, meta programming, C/C++ interfaces, and GUIs. My go-to language for one-off work, as well as my favorite language. There are a few features in v3 (like typing) that I want to learn better.
* _TypeScript (5 years)_: My favorite way to do web-based work, as the typing vastly improves the readability of code while reducing stupid mistakes like remembering whether that variable can be `null` or not.
* _SQL (13+ years)_: While I can't compete with a guru, I can hold my own on querying, especially with Google by my side.
* _C, C++ (14 years)_: I've used this extensively, especially for embedded or performance-sensitive work, including my fair share of macros[^macros] and templates. There are a few changes in the last few years (such as lambdas) that I haven't used much.
* _JavaScript (8 years)_: It's hard to do much with the web without this language.
* _Bash/Shell (15+ years)_: While this isn't my favorite language by a long shot, I've been working with shell scripts for a long time, whether debugging someone else's work or just doing something quick to solve a problem.

[^macros]: Yes, macros are evil. But sometimes they are a necessary evil.

And then there are some that I've done a little bit of work in:

* _Java_: I pick this up every few years, typically to do some C++/Java JNI interface or solve a limited problem. One of my proudest moments was teaching myself Java in graduate school to place second in a competition to write the best [Quoridor](https://en.wikipedia.org/wiki/Quoridor) algorithm.
* _HTML/CSS_: Having done web applications for more than eight years, I know the basics, but I tend to rely on others to do the bulk of the CSS work.
* _Ruby, Go, Groovy, CoffeeScript_: I've picked these up various times to solve a problem like interfacing with Jira (Groovy) or fixing some bot extension that got written in CoffeeScript just because.

# Databases

The main databases I've worked with:

* _MySQL (12+ years)_: I've interfaced with MySQL-flavored databases for much of my work. Fantastic for transaction problems; solves most problems reasonably well.
* _Redis (8+ years)_: Probably my favorite database, as it is a fantastic multi-purpose high-speed database, especially if persistence isn't important: message queue, caching, temporary storage, and more.
* _InfluxDB (3 years)_: I stood up and maintained a multi-terabyte instance as part of an in-house telemetry stack. Learned a lot about time series as well as the upside of having an expert DBA.
* _BigCloud (1 year)_: So far, it's a very convenient but limited version of MySQL.

# Platforms

* _Distributed computing architecture_ (10+ years): For years, I've worked with designing distributed architectures, databases, and data pipelines; handling challenges such as connectivity outages; and balancing centralized sources of truth with the resulting data bottlenecks.
* _Google Cloud Platform_: My introduction to true cloud computing (as opposed to on-premises virtual machines).
* _Servers (Linux, 10+ years)_: Almost everything I've ever written has run in a Linux-like environment of some sort or another.
* _Cross-platform (10+ years)_: Much of my career has been spent writing software that will work interchangably across platforms, typically either abstracting out operating system-specific differences or writing system-specific specializations.
* _Embedded (QNX, assorted environments, 7 years)_: Writing mission-critical software in a memory-constrained environment for police cars and trucking navigation presents some unique challenges.
* _MacOS (2 years)_: I led a team in taking a dead application (all previous institutional knowledge had left the company), reestablishing best practices such as CI/CD, and doing a bit of kernel extension programming.
* _Windows (2 years)_: Two key projects stand out here - an AI-based image detection system as well as a radio control algorithm for police communications.

# DevOps

## CI/CD

I'm particularly fond of the [proprietary CD system that I built](./unlinked.md), but I've also built and maintained CI and CD systems based on Buildbot, Jenkins, BuildKite, GitHub Actions, and Harness.

## Build systems

* _[Nx](https://nx.dev/)_: I'm learning this as a modern solution to the problem of what to build, how to build it, and what to do with it once it is done.
* _[Waf](https://waf.io/book/)_: I implemented this as a cross-platform cross-language build system that served as a reliable approach to building just the necessary dependencies for over a decade. It was a solid open source choice at a time when there weren't many competitors.
* _Make/CMake_: These were great tools when there was nothing else. I'm glad there are often other choices now.

## Centralized logging/telemetry

I've set up and iterated on telemetry and logging setups in a variety of technologies, including Graylog, Datadog, Grafana, Sentry, BugSnag and [Cloud Logging](https://cloud.google.com/logging?hl=en).

## Provisioning

* _Ansible (5+ years)_: One of my big accomplishments was introducing the concept of idempotent configuration-as-code through Ansible and seeing it become the de facto standard.
* _Kubernetes (3 years)_: The staple of my work with cloud-based microservices.
* _Terraform + Helm (1 year)_: No approach to cloud-based solutions would be complete without these sorts of provisioning tools.

# Miscellaneous

And here are a few oddball technologies, mostly for SEO, along with sparking conversation and a bit of wit.

* _Google + Stack Overflow, Copilot_: In many cases, knowing how to find the answer when you need it is the essential skill.
* _Stripe_: I spent 4 years building and maintaining a complex Stripe implementation, including multiple subscriptions, prorations, and taxes.
* _Flask, Express_: Much of the API work I've done has been based on these foundations.
* _Vue.js, AngularJS (v1)_: I'm a huge advocate of these sorts of front-end frameworks that structure the application much more like a traditional computer application. At one company, I pioneered this app-like approach with AngularJS and later helped guide the selection of Vue.js as the default framework.
* _Pandas, NumPy_: For when I've done mass data crunching, such as for validating machine learning models.
* _Sphinx_: One of a handful of systems I've used to build documentation from code.
* _[OpenAPI](https://www.openapis.org/), [json:api](https://jsonapi.org/)_: A couple of tools I've used to support API development.
* _[Mermaid](https://mermaid.js.org/)_: My go-to solution for diagrams as code.
* _Git_: I had the advantage of learning Git from someone who contributed code, so I've been able to do just that little bit extra when automating around source control, such as scripts that automatically delete local branches based on whether commits have been merged to main.
* _Qt_: The primary tool I used for a cross-platform GUI on embedded platforms.
