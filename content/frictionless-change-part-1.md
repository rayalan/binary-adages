title: Frictionless Change
subtitle: Is speed the goal? Part 1
date: 2024-02-25
category: software design
tags: knowledge, uncertainty, smart goals
status: published

[TOC]

> Being first to market doesn't matter if you can replicate your competitors' features instantly.
>
> _Joel Spolsky?_

A long time ago, someone[^article] --[Joel Spolsky](https://www.joelonsoftware.com/), if I recall correctly -- made a basic point about being in a software business:

[^article]: I can't find the original article; the article on Lisp I reference later is related, but not the one I'm thinking of.

_He didn't worry about competitors rolling out new features._

**He worried about competitors who could quickly copy his new features.**

Corollary: What matters in one's own software is the ability to quickly implement the same functionality that a competitor rolls out[^copy].

[^copy]: The assumption here is that the features being copied are worthwhile and valuable.

After all, if one can announce the release of feature _boil-chicken-with-dumplings_ a couple weeks after it makes a big splash, one can:

* Keep one's existing customers (after all, is anyone really leaving over having a new feature two weeks later?)
* Gain new customers who are interested in the feature
* Benefit from the competitor's hype and marketing around this new capability

In short, pivoting and reacting quickly mattered. And the main point of Joel's article was that selecting tools and approaches that enabled that reactivity was a competitive advantage.

> "Selecting tools and approaches that enabled that reactivity was a competitive advantage."
>
> _My premise_

[This article](https://www.joelonsoftware.com/2006/08/01/can-your-programming-language-do-this/) about Lisp, also by Spolsky, makes a similar point -- the more easily one's language can express complex concepts, the faster one can develop.

In a rudimentary sense, the whole art of software development is about how to quickly make a computer system do what we want. After all, all software can be reduced to a set of inputs, a set of transformations, and the corresponding outputs. And a [Turing machine](https://en.wikipedia.org/wiki/Turing_machine) executes every known program.

But since writing machine instructions on punch cards isn't fast, a whole industry of tools has emerged: assembly languages, compilers, high-level languages, libraries, memory management and garbage collectors, editors and IDEs, virtual machines, cloud computing -- companies adopt these in an attempt to make writing correct software faster[^faster][^exception].

[^faster]: I'd categorize security as a form of correct software -- software that can be abused for nefarious purposes isn't correct software. Likewise, since the cost of developers is one of the main costs of development, writing software faster is one of the main ways to reduce costs.

[^exception]: There is exception to this claim that comes to mind, which I'll address a bit later.

# Is development faster? A shifting goalpost

In the years since I've read that article, I've often encountered the ideas of speed and agility. In fact, I've never met a software executive who wanted engineering to ship features slower or take longer to fix a bug[^marketing].

[^marketing]: Emphasis on engineering taking longer; I've certainly seen marketing or other business reasons for a feature getting delayed.

_So has software development gotten faster?_

I don't know -- trying to answer that question is beyond the scope of this article. But there are at least three trends the push in the opposite direction:

* Increased expectations.
* Software as a service and vendor lock-in.
* Short-term change with long-term costs.

And I want to posit a fourth emergent problem:

> Expecting frictionless agility from friction-based tooling.

In the rest of this article, I'll break down these three trends pushing against faster development and then explore the emergent problem in the next entry.

# Increased expectations

As technology has advanced, expectations have increased for software. For example:

* Customers expect responsive designs that adapt to their device rather than everyone running a universal 640x480 resolution.
* Developers expect meaningful compiler errors, not cryptic "program encountered an error somewhere" messages.
* Gamers expect to easily connect with their online friends, not fight through hours of network configuration menus.
* Designers expect to refresh the look of an application after a few years when it is looking tired.
* Sales expects to be able to create sandbox environments for their prospective enterprise customers to try out.

On top of that, software has become ubiquitous everywhere - doctors and dentists have them, truckers have them, police officers have them, plumbers have them. And that means software needs to be accessible to almost anyone, not experts who have dedicated their lives to using computers.

And finally, expectations have increased as people see more what software can do. Once I realize how convenient it is to be able to track packages online, I want that ability from every shipping provider. Once I realize how convenient online banking is, I want all my financial institutions to support it. And so on.

All of these increased expectations makes software harder and slower to develop.

# Software-as-a-service and vendor lock-in

Every business wants recurring customers. But this creates some weird incentives -- if I invent a light bulb that never burns out, how many of them can I sell?

Maybe 5 per person? Maybe more if I can identify an industrial use for them? But ultimately, the longevity of my lightbulb will cap how many of them I can sell. And so it's far more profitable for my light bulb to last longer than my competitors' bulbs...but not forever.

In many cases, software has hit a similar point. How much better can document writing be? How much better can presentation software be? How much better can home budgeting software be? The reality is that in most cases, the incremental improvements just don't justify the upgrade price.

And so many companies, being run by sensible people, have moved to software-as-a-service. And since these companies aren't interested in losing customers, they're motivated to make it hard to leave, but not so hard that customers won't sign up. Sometimes it is forcing people to call rather than being able to cancel a service online. Sometimes it is Apple's walled garden. Sometimes it is the friction of adapting one's internal systems.

Whatever the case, it creates friction to change.

For example, suppose that my company is currently using GitHub and someone discovers that we will ship software three times as fast if do reviews after code is merged. How quickly can we roll out that change?

Not very fast. GitHub's offering is fundamentally rooted in the assumption that pull requests and reviews happen prior to merging. So I basically have three options:

1. Switch providers.
2. Hack together a custom system using various GitHub capabilities.
3. Don't improve the speed we deliver software at.

None of these are great solutions -- (1) and (2) are time consuming and expensive, while (3) doesn't realize the benefit.

# Short-term changes with long-term costs

Finally, a lot of software engineering is driven by short-term needs.

* The key question is often: How quickly can this feature ship? Time is money, after all.
* Performance reviews often cover six or possibly twelve months -- not the cumulative effects of years of decisions.
* People rarely stay at a company -- let alone a single position -- for more than a few years.

Almost by definition, this creates a situation where there is very little incentive for engineers to make decisions with long-term ramifications in mind. And bizarrely, I'm incentivized to hope that my predecessor left some easy-to-resolve problems so that I can chalk up some easy wins.

I've certainly put others in this situation. In one scenario, for example, I introduced [waf](https://waf.io/book/) as a non-Makefile solution for complex build patterns. At the time, it was a fantastic solution. But as the company shifted directions over the years, there wasn't much need for a cross-language Makefile alternative that excelled at minimizing local build times with excellent dependency graphs. The result was that waf slowed down development -- too expensive and time consuming to remove, but also too complicated and convoluted for developers to easily make their desired changes.

There's even a common architectural anti-pattern that results from this -- [lava flow](https://exceptionnotfound.net/lava-flow-the-daily-software-anti-pattern/).

And while lava flows can happen in many different ways, here's a common large-scale pattern I've observed:

1. Observe that a current framework or library is difficult to develop in.
2. Propose a new approach that will be far easier and faster to develop in.
3. Develop a cost comparison showing that for six months of developer effort, we can save years and years of labor.
4. Because backporting all of our existing systems is too time consuming, we'll only backport a few key systems and do the rest on an as-needed basis.
5. Management signs off on the effort.
6. The initiative mostly succeeds[^succeeds], although only about 70% of the porting gets done and some promised functionality ends up getting cut for scope.
7. Priorities shift, personnel changes, and someone notices that there's a framework or library that's difficult to develop in...
8. Repeat the process.

> The reality is that each initiative never achieves the expected benefits because it is being constantly sabotaged by the next attempt at improvement.
>
> _Alan, assessing actual vs. expected benefit_

[^succeeds]: Let's assume success. Such projects can be a complete disaster, too, of course.

# So what

A cynic might look at this evidence and ask: Do companies really believe that speed of delivery is essential to their success?

Yes, practices such as DevOps, continuous integration, continuous deployment, infrastructure as code, and feature flags are all big steps forward. All too often, though, pressures[^pressures] such as increased expectations, limited tooling options, and short-term business needs overwhelm the ability to quickly pivot.

[^pressures]: This list isn't exhaustive either. Software validation (i.e., testing) and personnel turnover are at least two more areas that push against rapid development.

And perhaps the cynic has a point -- after all, most public companies are set up to reward quarterly or yearly profits, not decades of sustained profit. Likewise, when was the last time an employee offer included a significant bonus for hitting a decade-long performance metric? How many performance metrics even last a decade?

But suppose a company really wanted to hone speed to market as a competitive advantage. What might they do? That's what I'll consider in [part 2]({filename}frictionless-change-part-2.md).

