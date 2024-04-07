title: Frictionless Change
subtitle: Envisioning speed from technology - part 2
date: 2024-03-06
category: software design
tags: knowledge, uncertainty, smart goals
status: published

[TOC]

> What if a company wanted speed to market to be one of its primary advantages?

[Last time]({filename}frictionless-change-part-1.md), I explored the idea that being able to quickly pivot and ship software to market can be a competitive advantage. I touched on the idea that languages that are better able to represent complex concepts -- such as [MapReduce](https://en.wikipedia.org/wiki/MapReduce) -- might offer a technical advantage. And I looked at three business pressures that tend to undermine a company's speed to market.

Today, I want to do a thought experiment -- suppose a business really wanted its time to market for software features to be a competitive advantage -- what might it do? This article focuses on the necessary technical choices, and [part 3]({filename}frictionless-change-part-3.md) will examine the corresponding employee and business decisions.

# Boring technology

First, [choose boring technology](https://mcfunley.com/choose-boring-technology), as described by Dan McKinley. Learning new technologies is expensive. Strange failure modes are expensive. Unknowns are expensive. And since we're building our company for being able to push features really quickly to market, technological unknowns are really bad. Instead, we want a set of common tools that can reliably and robustly solve any problem that we're likely to encounter -- and quite a few problems that we're not likely to encounter.

And yes, this means our solutions may not be performant. They don't have to be -- after all, the competitive advantage we're after is sustainable speed, not economy of scale.

# Change agnostic technology

Related to the previous point, we want to choose tools that can be used flexibly.

Git, for example, excels at this. At its core, it's a data store organized as a file system with time-oriented sequences and optimized for text.

> Why, yes, I've used Git as a makeshift database.
>
> _Alan, on how he's horrified various coworkers_

It can store code. But it can also store configuration data. Or logs. Or large binaries. Or even function as a makeshift database[^database]. I've occasionally done all of these, sometimes to the horror of my coworkers. (And we won't talk about my coworker's reaction when I suggested turning Stripe's key:value data storage into an arbitrary data store by splitting JSON strings across multiple keys.)

[^database]: High volume throughput won't work, of course, and one does need an approach for conflict resolution, preferably one that naturally works with Git's merge strategies. Or, of course, write one's own merge strategy.

My point here is not that Git (or Stripe) _should_ be used in these ways. But these kinds of generic tools are incredibly flexible, which makes it easy to adapt them to a particular problem.

In contrast, GitHub is a bad choice here. Yes, it is boring technology. But it also supports very particular workflows. Suppose, for example, that one wants to support reviewing code after it merges? Or a two-staged review process? Or even something "simple" such as unifying tickets and pull requests into a single object?

All of these changes are hard to do with GitHub. And we want more control over the developer experience so that we can optimize the process for quick turnarounds. This doesn't mean GitHub is a bad product -- it excels at what it does -- it just makes it a bad fit for our goals.

# Security and data writing approach

Anytime a company keeps customer-specific data in a centralized location, there are two big risks with shipping a new feature:

1. What if those changes give unintended access to some other data?
2. What if those changes change how data is written?

After all, a problem displaying data can easily be corrected with a new software update. But if a change goes out and starts writing data incorrectly, then bad data persists even with an update. And if that change also ensured that the correct data isn't getting written, that's likely a PR nightmare.

> Company loses week's worth of data
>
> _Alan, on how **not** to earn customer confidence_

So in order to quickly turn around new features, we're going to want guarantees that our changes don't alter how we write data (and thus potentially break features) and that they don't open up privilege escalation or other security vulnerabilities.

Ideally, we're going to want those guarantees to be provable through automation. We don't want to take the time for a human to validate each change, or to risk that the human makes a mistake. Better yet, reliable automated checks here mean that we need less code review before changes are made -- if a change can be certified to only impact how data is displayed, then many of the risks to a change go away.

This implies that we want a very clear architecture for writing and storing data. Perhaps a data store that knows about the individual permissions for each row of data. Each query comes with the intended user, and so a query is incapable of returning results that should not be displayed to the user.

No doubt that this is a hard problem -- that is, in part why there are so many security vulnerabilities -- but it's the kind of problem that we'd solve in order to make truly quick turnaround a competitive advantage.

# Established patterns

The idea of modularity and well-established patterns extends beyond security and data protection. For example, if one is shipping a new feature, there need to be metrics -- is the feature working as expected? Is anyone using it? Does anyone like it?

In a fast turnaround environment, the way that these questions {{{VERB}}} can't be recreated each time. Instead, the very act of writing a new feature should add the necessary dashboards and metrics. When I write code like this:

```
if FEATURE_FLAG_COOL_NEW_THING:
  page.add(myNewFeature(options))
```

then that needs to result in the a dashboard for CoolNewThing showing page loads, errors, latency, user interactions, and customer satisfaction -- as well as details for how the feature is being used. Maybe there's even a number correlating the NPS score for users who interact with my feature vs. those who don't. If there are significant business costs associated with my feature, those should be visible, too. If there are asynchronous behaviors such as outgoing events or generated reports, those should likewise be tracked in the dashboard.

Likewise, when there is a problem, logging, data lineage, and other debugging resources should have been naturally been populated just by writing the new feature.

# Modularity

One implication of this approach is careful modularity -- the deep awareness of which data writes are going to be affected by a change or the ability to be certain that code only impacts users with a particular feature flag enabled implies a careful attention to the modularity of the software. Pages are going to be written in a particular way so that it is easy to tell -- via automated tooling -- that these changes only impact one feature's flags. Data writes are going to be written in a particular way so that code inspection can guarantee that only particular records will be written differently. Certain classes will be used in very particular ways to ensure the right metrics are properly generated.

And of course, these features need to be easy to use. If they aren't, the whole idea of fast turnaround for features goes out the window.

# So what

So far, I've looked at a few of the technical aspects of speed as a competitive advantage. [Next time]({filename}frictionless-change-part-3.md), I'll look at some of the underlying business considerations.
