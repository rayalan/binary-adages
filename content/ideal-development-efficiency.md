title: Ideal Software Development Efficiency
subtitle: Applying thermodynamics
date: 2024-04-04
category: software design
tags: knowledge, uncertainty, smart goals
status: published

[TOC]

Entering college, I assumed that the reason that inefficient engines were some combination of economics -- too expensive, not enough profit. But at the end of the day, surely a great engineer could make an ideal engine.

Then I met my friend, thermodynamics[^friend].

> No, that's not how the world works.
>
> _Thermodynamics, my, uh, "friend"_

[^friend]: I use friend in the loosest possible way. We never got along well; this was quite possibly my worst college class.

At the end of the day, [ideal efficiency](https://en.wikipedia.org/wiki/Thermal_efficiency) was tied to the input temperature. Want a more efficient engine? Just increase the temperature.

This approach clearly has some downsides, especially for beings that don't thrive, above, say, 57 Celsius. In practice, designs are often 30 or 40% efficient -- maybe in particular situations a 60% design is achieved. In short, if one wants heat to do work, half of the heat -- and probably more -- is going to be wasted.

# Software development efficiency

Does any of this matter for software development? At first glance, my answer is no. I easily look around and see wasted potential -- the extraneous effort it takes to schedule and coordinate meetings, the time spent duplicating documentation, the time spent waiting for a security scanner or code review. And that's not mentioning organizational inefficiencies -- duplicated efforts, hidden pain points, reorganizations, and canceled projects.

But let's suppose all of that went away -- would software development be instantaneous? And if not, doesn't that imply some sort of "ideal software development pipeline" where a particular problem takes at least so long?

And in that case, we could express the ideal time as something like:

> Ideal development time = Complexity of problem * Required time per complexity unit
>
> Efficiency = Ideal development time / Actual development time

So if a problem has an ideal time of 1 hour and it takes me 5 hours to ship it, that's 20% efficiency. That seems reasonable enough.

# Bottlenecks

Is there anything more that can be said about ideal software time? After all, measuring the complexity of a problem is a very hard problem. For the rest of this article, I'll explore a couple limiting factors and see if there are any implications for engineering better ways to develop.

## Abstraction

> How concisely can software design be expressed?

The first bottleneck is what level of abstraction our technology supports. If we're limited to punch cards with basic CPU instructions such as add, subtract, and branch, then development is going to be far slower than if there's a modern language with garbage collection and common data structures such as arrays, queues, and maps.

Conceptually, the abstraction level could be even higher. Perhaps the ability to enter a prompt "Let the user enter personal information about themselves and make it retrievable by administrators." And then an AI-based system could reliably turn that into a smart object that gathered the right user data (e.g. first name, last name, title, birthday), created the corresponding tables in the database, and made the corresponding visualization for administrators.

A closely related question is how leaky these abstractions are. In modern languages, for example, it's far easier to model the internet as a fully reliable pipe. But that promptly falls apart at scale when throughput limitations, long latencies, server failures, outages, and other disruptions wreak havoc with a poorly designed system.

## Human understanding

> How quickly can a human understand a software system?

Even if the act of designing software can be near instantaneous, a person is likely to be able to understand the system, the implications of changing it, and how it interacts with other systems. Today a common problem like billing is sufficiently complex that Stripe has pages and pages of documentation dedicated to communicating billing concepts. And then pages more dealing with the technical implementation.

Even if the technical part can be fully abstracted by our futuristic AI, can the conceptual part? For example, consider details such as understanding how much notice a customer has before their card is charged, how long customers can be in arrears before service is terminated, or whether expired credit cards will be automatically updated to their replacement. Such details are not merely technical nuances, but likely impact the customer experience as well as the company expenses as well as cash flow.

As a simple example, suppose one is running a software-as-a-service startup with very high cloud expenses per customer and low profit margins[^startup]. As a startup, cash may be at a premium and giving overdue customers months to catch up on payments may not be financially viable. Someone in the company certainly should be caring about the grace period and how it impacts finances, and that means at least one human (and probably more) needs to understand how the billing system works.

[^startup]: Let's set aside the question of whether or not this is a good business model.

The need for this sort of human understanding of how the software system works repeats for many different facets of many different systems, and the time it takes to understand the current behavior and then decide on the correct new behavior will be a bottleneck, even if the implementation is instantaneous.

## Handoffs

Closely related to the question of human understanding is how many handoffs are needed to make a software change. In [Galaxy Quest](https://en.wikipedia.org/wiki/Galaxy_Quest) -- a Star Trek / sci-fi parody -- there's a character whose sole perhaps is to ask the computer questions. If anyone else wants to ask the computer a question, they need to ask this character to ask the computer the question. This handoff is completely pointless, and merely adds inefficiency and a bottleneck to getting things done.

Unfortunately, such situations aren't limited to comedic movies. I've a designer want to update a logo. This turns into a Jira ticket, which doesn't get prioritized. So the designer talks to their boss, who talks to the software director, who talks to the team manager, who slots the ticket into the the next sprint. Then the develop goes to update the file and finds out that the ticket doesn't contain the right format, so the developer goes back to the designer to get the right files, disrupting the designer from their current work. And then the developer spends a few minutes to commit the files and run the change through the CI/CD system.

> Yes, that's five people and a half a dozen handoffs for five minutes of work.

That's at least five people disrupted and hours of organizational overhead for 5 minutes of work. In a more streamlined system, the designer could have made the change themselves with no handoffs.

## Entanglement

Another problem is the one of entanglement. Once, for example, a company had an account field called _is_active_. On the surface, this indicated whether or not the account was active. But behind the scenes, business intelligence also used the field to determine when the account had subscribed.

This approach meant that business intelligence was looking for the first transition point of _is_active_ of false --> true for many of their analytics. Due to some billing changes and improved error handling, developers changed this _is_active_ to start as true, and then change it to false after a grace period.

The change was good for customer experience, good for retention, good for revenue...and absolutely terrible for business intelligence because now their metrics were doing weird calculations everywhere.

This scenario illustrates entanglement in a nutshell -- there were multiple unwritten undocumented assumptions about how the flag behaved, and when someone changed the behavior, even for a good reason, chaos resulted.

With modern software development practices, these surprises naturally emerge. They're typically painful and time consuming to discover and resolve. Could some ultra-smart tool completely analyze a software system, summarize these sorts of complexities, and then instantly write the appropriate code to resolve them when prompted by a human?

If not, the speed of resolving entanglements will bottleneck software development.

## Human limitations

How many subjects can a human master?

Search engine optimization. Social media presence. Branding. Affiliate management. Pricing strategy. Brand management. Product strategy. Information architecture. Visual design.

These are just some of the areas that go into an ideally designed product. Many of these fields can be subdivided into additional specialties. Even supposing that software development becomes so trivial that a five-year old child can do it with no training, executing the business strategy well through software will remain. As the business scales up, as customers want it customized in conflicting ways, as competitors change their offerings, the software requirements will change.

Maybe someday engineers will take over the world [bland text-based documentation](https://git-scm.com/docs/git-help) will become all the new style for every product page.

> If engineers took over the world, would [text-based documentation](https://git-scm.com/docs/git-help) become the latest in product placement?

Until then, though, the limitations of human expertise will force collaboration as a company grows, creating bottlenecks as to how quickly software can be developed.

# So what

While I don't believe we'll ever discover a law describing the maximum efficiency for software development, I see value in considering why there are bottlenecks and how they might be overcome.

For example, one company refused to require its designers to learn git, HTML, or CSS despite having a top-notch CI/CD system. The result:

* Designers constantly complained about how long it took their changes to make it to production.
* Many design changes never happened at all.
* Developers were often distracted with making minor changes, which were disproportionately expense with very high overhead.
* Business leaders were frustrated by the outdated look-n-feel in the user interface along with inconsistencies.

Yes, the problem went more deeply than simply teaching designers a few basic development skills. But the fact that some leaders had decided "Designers don't do software develepmont, at all, in any way." meant that many easy wins were lost. Instead of engineering and design both getting more of what they wanted, both got loss.

In contrast, I read about company that offered git-based services (think GitLab or GitHub). And they expected every employee to learn how to use git. Not just developers, but designers and marketing and lawyers -- even HR. Part of that was just [dogfooding](https://en.wikipedia.org/wiki/Eating_your_own_dog_food), of course. But I wonder how many operations were faster when, for example, a lawyer could just update the legal statements in code rather than having to through others[^update].

What else could be done to streamline software development?

[^update]: Legal updates can have a lot of entanglements, though. So some updates are still likely to be very complicated.