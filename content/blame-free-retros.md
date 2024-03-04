title: Blame Free Retrospectivs
subtitle: A problem of scope
date: 2023-11-07
category: practices and principles
tags: knowledge, uncertainty
status: published

I'm a huge fan of [blamefree retrospectives / postmortems](https://www.blameless.com/blog/what-are-blameless-postmortems-do-they-work-how). Why?

Because I believe that:

1. High-trust environments are incredibly important to productivity in fields such as software development that involve a high degree of both judgement and technical complexity[^complex].
2. An essential part of high-trust environments is assuming good intent by all parties.

[^complex]: Ideas like the [Andon cord](https://www.sixsigmadaily.com/what-is-an-andon-cord/) suggest a similar idea is more broadly true, but speaking about best practices for postmortems at a cracker factory or a political campaign is a bit beyond my expertise.

In contrast, it's really hard to understand what is happening in a world where everyone is trying to cover for themselves. And even worse is a world where management is using the guise of blamefree conversations to covertly gather evidence against specific individuals with a goal of blaming them for outcomes. I've been on the receiving end of that, and, unsurprisingly, it's incredibly toxic.

# Scope (or lack thereof)

Even when postmortems are conducted blamefree with the best intentions, though, there's often a more subtle problem: _All of the players aren't in the room._

> _All of the players aren't in the room._

Yes, all of the team is in the room. But consider who else likely made decisions:

1. Did the team have complete control over architecture?
2. Did the team have complete control over their own priorities?
3. If there were any inter-team dependencies, did the team have complete control over how those were resolved?
4. Did the team choose their own budget and timelines?

In most companies, teams don't have complete autonomy. There are company standards. There are pressing business priorities. Product needs new features to ship. A key initiative will be blocked if such-n-such doesn't ship. Money is tight. Management wants to see results.

And that means that teammates aren't the only people who made decisions contributing to the outage. Someone decided that the increasingly complex monolith wasn't worth splitting as the company grew. Someone decided that hiring more teammates wasn't important. Someone decided that the company wasn't going to offer 6 weeks of vacation a year as an incentive to attract the best people. Someone decided that the company focus was going to be the new feature launch, not testing and quality. Someone decided not to challenge the cultural norms around what was acceptable redundancy and prevention.

Some of these decisions are certainly made by the team. And the team certainly could manage upward better. But in every company I've heard of, some of those decisions are beyond the team. And yet I find blamefree retros rarely step into the bigger picture, instead focusing on the tactical decisions.

> Blamefree retros rarely step into the bigger picture, instead focusing on the tactical decisions.

# Was the failure a bad outcome?

I once had a conversation with the C-suite that went like this:

_Me: My team released a bug that cost us a five-figure amount from such-n-such date to such-n-so date, when we corrected the bug. Here's a bit of technical background on what happened..._

_C-suite: So what actions are being taken to prevent this from recurring in the future?_

_Me: Nothing. Here's why..._

So why no changes?

From the postmortem, we'd released a software change where customers hadn't been billed, resulting in a five-figure loss. There was no viable way of recouping those losses[^recoup]. And conveniently, customers don't get upset with not being charged, so this was probably the most straight-forward cost calculation I've encountered.

[^recoup]: Basically, losses couldn't be readily recouped because charging the customers retroactively would have led to bad publicity and far more customer service calls. It was better to eat the loss than to compound the problem.

As is often the case, there was a complex history behind this bug -- prior decisions stacking on top of one another that contributed. I'd made my own contributions as team lead such as incorrectly assuming what was common knowledge and focusing on more delegation. And there were other factors as well.

The greater context of the bug was that company wanted a particular feature to market as soon as possible. And by cutting some corners, we'd successfully gotten the feature to market at least a month, possibly two months, earlier than expected. And each month earlier was worth about what the bug cost to the company. So it's pretty easy to put together a chart summarizing possible outcomes:

| Time to market | Shipped bug | Net outcome |
|-|-|-|
| -2 months | No | 2x profit|
| -2 months | Yes | 1x profit|
| -1 months | No | 1x profit|
| -1 months | Yes | 0 profit|
| 0 months | No | No profit|
| 0 months | Yes | 1x loss|

So if we'd taken another week to ship the feature, that week needed to generate at least a 25% reduction in the chance the bug would ship in order to pay for itself. If we'd taken another 2 weeks to ship, those two weeks needed to generate at least a 50% chance to not ship the bug. And so on.

Now clearly in hindsight, knowing exactly what to look for and why the bug was missed, the bug could have been easily caught. But in foresight, I think it's pretty likely we could have taken a couple more months to ship and still missed the bug.

And given that scenario, the most profitable decision was to ship the feature as soon as possible. Normally, there are other considerations such as whether the bug was likely to repeat and how to avoid it in the future. However, given the particulars of the bug, it wasn't likely to recur.

Admittedly, this situation was atypical. But it highlight a really important question for a blamefree retrospective: Was this bug worth paying the price to prevent?

> Was this bug worth paying the price to prevent?

# So what

First, [some scenarios](https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/) are so bad for the company that the risk needs to be basically zero. For comparison, there's an [interesting article](https://www.osti.gov/servlets/purl/1426902) about nuclear weapon tolerances and complexity of calculating the actual risk. Most of us don't handle nuclear weapons, but certain failures modes -- e.g. data leaks, data loss, prolonged outages -- may be just as catastrophic for a company. If so, I suggest it's worth architecting the necessary protections, redundancies, and verifications deeply into the systems. That way, instead of being an afterthought vulnerable to being lost in the quest for speed, those checks are a "given" for the company[^givens].

[^givens]: This is, of course, very hard to do. Many companies don't have an actual understanding of how much risk they are prepared to tolerate, and that tolerance can rapidly shift based on market conditions or personnel changes. I've found [How to Measure Anything in Cybersecurity Risk](https://www.amazon.com/How-Measure-Anything-Cybersecurity-Risk/dp/1119085292) a fantastic study on how to normalize the conversation.

Secondly, the overall postmortem process shouldn't just be about the team's choices, but the context that the team was placed into.

Finally, despite my reflections about a broader context, a blamefree mindset shared across the company is still essential in effectively evaluating what happened and what could go better next time.

What else should have been my lessons learned?
