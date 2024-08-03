title: Next Generation Goal Setting
subtitle: Rethinking Company Alignment, Part 1
date: 2024-08-12
category: business ideas
tags: user experience, process, experiences, system design
status: published

[EuroGames](https://boardgamegeek.com/).

[Universal Auction Theory](http://www.skotos.net/articles/TTnT_161.phtml)[^commentary].

[^commentary]: I also appreciate [this commentary](https://boardgamegeek.com/blogpost/99327/every-game-an-auction-game) on some of the implications.

[Crowd-sourced](https://questions.satisfactorygame.com/search?sort=1) [priority](https://www.slido.com/) [lists](https://www.teamblind.com/polls).

Sometimes technology allows for exponential leaps. A computer file system is model on its paper counterpart. Even names like `folder` or `file` or `desktop` reflect that heritage. Yes, it is digital, but fundamentally, it's the same idea as its physical counterpart. That is, if I was fabulously wealthy and could afford a giant library along with personal filing assistants who would fly around with wherever I went to make sure I had any document I wanted instantly on hand.

At other times, though, technology gives exponential leaps. [Git](https://git-scm.com/) is just not possible by hand. At least, not as anything other than a curiosity. But add in modern technology, and suddenly Git becomes foundational for not just source control, but a host of related concepts such as state-driven outcomes (e.g Terraform, Ansible), configuration-as-code, infrastructure-as-code, and ephemeral computing systems. Is your server in a bad state? Don't worry too much about debugging; just delete it and create a whole new copy from scratch!

# Goal setting

Sometimes, though, technology doesn't seem to have changed the space much. Company goal settings is one of those areas. There's a host of approaches to goal setting. For example, [OKRs](https://www.atlassian.com/agile/agile-at-scale/okr), [SMART goals](https://www.ucop.edu/local-human-resources/_files/performance-appraisal/How%20to%20write%20SMART%20Goals%20v2.pdf), [BHAGs](https://www.investopedia.com/terms/b/big-hairy-audacious-goal-bhag.asp), [big rocks](https://theprocesshacker.com/blog/stephen-covey-big-rocks/), and [quarterly objectives](https://lattice.com/library/4-reasons-why-workplaces-should-set-quarterly-goals).

Often, the basic problem is this: The executives want the company in head in a certain direction. They want to hit certain outcomes. But they don't know everything that needs to be done. Good executives are usually very aware that rank-and-file employees are far better positioned to understand problems and come up with great solutions. So goal setting becomes an exercise in explaining the company's objective, aligning the company around those outcomes, and then figuring out what to do. Hopefully, this happens in near zero time, since the company needs to execute on the vision, not just spend forever aligning their plans.

!!! note "Aside"

    I did once work for a company that changed its goals quarterly while its software delivery cycle -- from concept to delivery -- was about five or six months. This worked out in practice at least as badly as one would expect.

However, most of solutions to this problem are just the paper system on a computer:

* Spreadsheets
* An integrated solution like [15Five](https://www.15five.com/products/performance/okrs-and-goals/) or [Lattice](https://lattice.com/goals/okrs).
* Perhaps Jira or Linear.

None of these solutions take advantage of the unique capabilities of computers. But suppose we had these goals:

* Set high level company goals.
* Align the company around those outcomes.
* Spend minimal time on the effort.
* Encourage grass roots projects, whether they direct promote those outcomes, or merely facilitate them.

How could we leverage strategy games, auctions, crowds, and computers to solve this quandary?

# Problem analysis

A few notes on some of difficulties we face:

_"Important" work vs. everything else_

It's really easy for projects that obviously relate to the company objectives to get all the attention. Meanwhile, everything else becomes an afterthought.

All too often, I've ended up on an important long-term project that contributes nothing to the current goal. The goal is to improve customer conversions by 15% over the next quarter, and I'm on a year-long project to replace the billing system. My biggest contribution is "Don't break anything."

_Contradictory goals_

Often, the company doesn't speak with a unified voice. The company goal may be to ship the new feature as soon as possible, but the security team is probably stonewalling when it comes to committing credentials to source code. This tends to create weird push-n-pull situations where teams are invisibly being rewarded for moving in opposite directions.

_Supporting work_

Often, the big win is a feature which relied on supporting efforts which relied on yet other supporting efforts. Sometimes these dependencies show up nicely during planning. "We'll need a new microservice which will need a new redis instance which will need a new vendor selected..."

Other times, the dependencies are a bit more surprising. "What do you mean our database can handle 5000 writes per second? Our whole architecture depends on that, and we have to be live in two weeks. When will the database be able to handle such a rate?"

But the worse dependencies are the invisible projects that never get prioritized. Every developer is working on key feature, thinking "I wish our build process didn't fail half the time and take an hour." Every developer finds that build time is the bane of their efforts. But nobody ever puts together the project to fix the problem. And so the key outcome is jeopardized because the CI experts are off doing something else.

# The auction solution

The basic idea is simple:

1. Every employee gets some tokens, and bids on problems/solutions that they want done.
2. Teams are rewarded with points based on how many problems/solutions they achieve.

Want a large grass roots initiative? Give executives one-third of the tokens, give managers one-third, and distribute the remaining tokens among the other employees.

Want to prioritize security and stability? Increase the share of quality assurance and security.

An added benefit of this system is that it shows what different groups really value.

* Does the official company goal revolve around revenue increases, but the entire engineering department is bidding on paying off tech debt? That says something.
* The company goal is moving to a customer management system, but the entire CSR department is voting for an upgrade to some legacy system executives have forgotten about? Again, interesting.

One final benefit of this system: It clearly shows which teams are making recognized engineering contributions. This data can be fed into performance reviews and as well as reorganization discussions.

!!! note "Clarifications"

    "Recognized contributions" is key here. Just because a squad isn't recognized doesn't mean they aren't doing important work. Perhaps it is an opportunity to work on better communicating the value of certain work.

    Likewise, the most popular work isn't necessarily the most important work. But it certainly says a lot about what decision makers are thinking.

And because computers are really good at mass calculations and aggregating data, this kind of auction solution can easily scale across a large company.

# So what

My premise is that current approaches to company-wide goal setting, especially for executives who want something other than a strict top-down approach, aren't taking advantage of modern computing capabilities.

Instead of trying to adapt a pen-and-paper system to computers, let's borrow from gaming to create a large-scale game that creates visibility and ties neatly into performance reviews.

As a final perk, this system makes it really clear who the decision makers are (the people with the tokens) and how much their opinion matters (how many tokens they have). This means that good decision makers can be rewarded for funding projects that work out. Likewise, there's clarity on who favored projects that were delivered successfully but didn't yield significant results.

Next time, I'll look at some of the potential complications and flaws of this system and how we might overcome them.

What do you think? Could a system like this be effective for your company?
