title: Frictionless Change
subtitle: Envisioning speed in from organization - part 3
date: 2024-03-20
category: software design
tags: knowledge, uncertainty, smart goals
status: published

[TOC]

> What if a company wanted speed to market to be one of its primary advantages?

[At first]({filename}frictionless-change-part-1.md), I explored the idea that being able to quickly pivot and ship software to market can be a competitive advantage. [Last time]({filename}frictionless-change-part-2.md), I started a thought experiment about the technical choices that might make fast turnaround a true competitive advantage.

Today, I'm continuing that thought experiment into the organizational choices that would complement the technical choices to achieve this kind of technical advantage.

# Intentional change

The technical practices I suggested last time (e.g. modularity, clearly established patterns, boring flexible technologies) won't just happen. And despite our desires, technologies well change -- Microsoft won't maintain Windows 95 forever.

This means we'll want a careful thoughtful approach to selecting and changing tooling - frameworks, libraries, tools, languages and the like. How do we evaluate a technology? How do we begin to roll it out? How do we evaluate its effectiveness as we roll it out? When do we abort a rollout?

In particular, we want to avoid the [Lava Flow anti-pattern](https://exceptionnotfound.net/lava-flow-the-daily-software-anti-pattern/), either choosing to move fully through with conversions or choosing to fully roll them back.

# Cadence: ebb and flow

So far, I've posited two contradictory directions:
1. The company leverages quick feature turnaround as a competitive advantage.
2. The company carefully builds the capability to quickly turn deliver features.

These ideas are in tension -- as I discussed in my first article, many of the modern attempts to ship features fast to market result in technical debt that slows down future features.

My solution is a rhythm between shipping features and refining capabilities. Yes, each round of quickly shipped features may add to the tech debt. Somewhere along the line, a developer will use that library maintained by that [random person in Nebraska](https://xkcd.com/2347/). That's fine when we're shipping quickly. But the refinement cycle needs to go back and find a sustainable solution.

Likewise, some engineer will realize that the logging statements aren't right, or that the metric latency is too low, or something. And there will need to be capability improvements in order to continue to rapidly ship features.

> It's like a sword -- battle dulls the sword, but no one sharpens a sword just for looks.
>
> _Alan, reflecting on the balance between shipping software quickly and maintaining capabilities_

This sense of cadence needs to be more than an engineering goal; it needs to be a company goal. If the company leadership doesn't understand and support the competitive advantage, engineering will constantly be tasked with other priorities -- like shipping more features. The result is that if quick turnaround isn't part of the company strategy, the engineering capability will gradually erode[^erode].

# Employees retention: Turnover and the Peter principle

A large part of the company's strategy for being able to roll out fast changes is well-defined patterns, careful technology transitions, and strong technical decision making. As with most companies, we want employees who learn from their experiences. However, we particularly want employees who have a long-term view to maintaining a key competitive advantage -- the speed at which we can ship features.

This means we want to think carefully about the [Peter principle](https://en.wikipedia.org/wiki/Peter_principle) -- employees get promoted to their level of incompetence and salary ranges. Suppose we have a manager, Jane, who excels at leading a small team on difficult technical projects. That's an incredibly valuable skill, even if she doesn't have the skills or temperament to be a director with a wide span of control. So we want to design a system where she isn't constantly eying a promotion to a director position, either within our company or elsewhere. That starts with compensation, but also includes the kind of respect, latitude, and discretion a manager is given.

As an example, suppose that a group of managers have a scheduled meeting with a director in a typical organization. The director likely feels far greater freedom to say "Let's reschedule; something has come up." than any of the managers do. If it's a group of developers and a director, this discrepancy is larger. Why does this tendency arise?

* The director is assumed to have more important work to do, being higher in the organization.
* The director is assumed to have a better understanding of what is most important across the company.
* The director's time is far harder to schedule because their calendar is busier.

This kind of signaling -- that one's time would be more valuable if one had this other role -- constantly nudge motivated employees into looking elsewhere, even if it isn't a great fit.

Likewise, many companies communicate that having a larger span of control is better than having a smaller one. That means that leaders are motivated to grow their headcount, regardless of whether it is actually good for the company. I've seen one company, for example, where a department grew tenfold. Each time it grew, there were excellent metrics for how much was getting done -- how many tickets were being handled, how heavy the department's load was, and how great the need for more personnel was. Yet nobody questioned why the there were so many tickets or why the load was heavy; those were simply accepted as givens. Yet behind the scenes, the department was taking on more work and designing workflows that increased their workload. In a different company where importance wasn't linked to size, conversations would have happened about what work the department actually needed to do, and whether different practices could have reduced the overall workload rather than constantly growing the department.

At a company that wants to sustain a long-term competitive advantage by having knowledgeable long-term employees in many positions, we want to carefully consider how we're going to communicate about the relative importance of roles. We don't want people to be motivated to grow a department except when it actually benefits the company. We don't want people motivated to seek promotions outside of their skills.

As an aside, I'm not suggesting that every employee needs to be a long-term employee, but the organization also needs to be very good at recognizing and developing talent, all the better to keep it.

# Profit margins and market landscape

So far, we've repeatedly made expensive decisions in order to support speed to market. We're paying non-standard salaries to employees. We're retaining employees over the long haul. We've chose common tools that don't necessarily offer economies of scale. We're spending a lot of time to remove tech debt and obstacles to speed. All of these choices take money.

And the corollary is that we need to be able to afford it. Assuming we're not able to print money or run a deficit more or less consequence free like the United States government, that means we need profit margins. We need to be doing software development in a space where there are large profit margins that can be capitalized on for a long time -- and have a need for being able to swiftly ship new features.

Not every [market landscape](https://www.blueoceanstrategy.com/tools/red-ocean-vs-blue-ocean-strategy/) needs both of these criteria. This business approach is probably best situated for a marketplace with low barriers to entry that can't sustain many competitors. The lack of competitors makes it profitable, and our ability to swift deliver new features when needed allows us to undercut emerging competitors with a unique offering.

# Minimize obstacles to change

One of the most successful collaborations I had was with an information architect/designer who knew HTML. I was working with him on a project that needed to communicate highly technical detail to non-technical customers. Our process ended up being like this:

1. We ended up hammering out the key concepts together
2. He'd implement or change the layouts.
    * Often, this step completed the worked because the underlying information was already available to the page; it just needed to be displayed.
3. He'd mark any places where he didn't know how to get the information he wanted.
4. I'd implement the code that provided the necessary information.
    * Often, this step completed the work because the design and formatting was already in place.
5. If necessary, he'd go back and do a second formatting pass, especially if the information wasn't exactly in the format he'd anticipated.

Why did this strategy work so well? Because it was often a 0 person handoff process, sometimes a 1 person process, and occasionally a 2 person process.

Why did this approach work in this case but not in many other situations?

1. The information architect was enthusiastic about learning an unusual skillset (HTML/Angular) for the work.
2. I designed the project so that it was trivial for the information architect to make changes directly to code. For example, I setup a very simple git workflow just for the architect that bypassed a lot of the normal developer complexities.

In software development, hands offs and collaboration are expensive. That's not to say they aren't vitally important, but if our goal is fast feature development, we want to think carefully about where and when they are necessary.

* Are there non-standard skills we could give certain roles that would streamline work?
* Could certain collaboration be delayed until after features ship?

Overall, the goal is to reduce the obstacles to shipping quality features, not eliminate collaboration or minimize interaction.

# User expectations and change management

> How quickly can we drop or change features?

_"Let's stop collecting the date of their first pet's birth so that we can drop the Python 2.3 analysis module. It'll let us ship the new pet friendship feature six months earlier."_

_"We can't do that without a feature-equivalent alternative. CustomerUno depends on that capability."_

I've lost track of how often the ability to make fast changes is sidelined by an old feature that just happens to be critical to one particular customer that's important to someone in marketing. In short, once a feature gets released and adopted by a customer, it tends to be unremovable.

On the one hand, this is understandable. Customers buy a product, and seeing features go away feels bad. Seeing them just disappear without notice is worse. On the other hand, this friction is bad for our goals as a company of being able to move fast.

So what might we do?

- Make it really easy to write feature help, onboarding, and change documentation[^change].
- Make significant changes frequently so customers expect it of us.
- Publicize popularity stats for our features so that changes are foreseeable by customers. (I considered making longevity guarantees, but that likely conflicts with our key competitive advantage of being able to ship new features quickly).

[^change] - I see very few live services that do this well. The most common approach seems to be popups that introduce me to new features when I'm in a hurry to get something done, which is, well, suboptimal. This topic probably deserves an article of its own.

The overall goal is to condition customers to expect change and a certain amount of disruption, and develop a relationship with our customers where they are clear that the disruption with new functionality is a net win for them.

# So what

Somewhere I read that you can't beat the industry by following standard industry practices. That is, by definition, standard industry practices produce standard industry results. That doesn't make standard practices bad. They are, after all, standard for a reason. But sometimes it's beneficial to take a step back and say "If our goal was really to do such-n-such, how might we structure our company to achieve that goal?"

I'm certain what I've outlined here isn't the exhaustive list of approaches to achieving fast feature delivery, but I hope readers have enjoyed the thought exercise. What else would you do to optimize for lightning quick feature delivery?
