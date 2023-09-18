title: Stripe Review
date: 2022-06-13
category: technology experience reviews
tags: stripe, reviews, exemplars
subtitle: Serving well with technology
status: published

[TOC]

All too often, integrating with a third-party technology is a pain: The product doesn't reliably work, the documentation is inadequate, the solution lacks essential concepts, the customer support disappears once the purchase has been made, and so on. Most developers have felt this pain, I think, whether it is using an open source library or a purchased solution.

Thus on the rare occasions when a company knocks it out of the park with an effective product that is a joy to work with technically, I want to reflect on how that win was achieved -- and what lessons I can learn.

Today I'm reviewing [Stripe](https://stripe.com/). As background, I've worked with Stripe for about four years; my introduction to it was investigating it as a potential 3rd-party replacement for an in-house billing system (henceforth _The Billing Project_). After it beat out the other options the company looked at, I led the project to implement Stripe across the company, including satisfying accounting audits and customer service interfaces. And after the initial implementation, I oversaw the maintenance and iterative improvement of the new Stripe-based billing system.

# Big Takeaways

My three big takeaways from Stripe:

* _Excellence matters_: Across the board, Stripe is an excellent product. Given a choice, they seem to prefer to do the essentials well, rather than having more features with a less solid experience. The result is that while I did, at times, want more from the product, I was confident that what I had to work with was rock solid.
* _Intertwine process with product_: The "things" Stripe produced (such as APIs, features, and documentation) also enabled processes (such as onboarding, prototyping, testing) to work well.
* _Integrate multiple disciplines_: Stripe reflects excellence in the disciplines of development, architecture, user experience, quality assurance, customer support, business intelligence, and law. I'm pretty sure they aren't hiring individuals who have mastered all these fields; rather, they are effectively integrating expertise from many different people.

# Strengths

So what did Stripe do well? I'll split this discussion into two views:

* What processes do customers need to do well?
* What product features do customers need?

## Processes

In this section, I'm looking at the different stages of a project to implement Stripe, and how Stripe strongly supports each stage.

### Technology Vetting / Selection

First, a billing system platform needs to be selected. Build in-house? 3rd-party? Which one?

Stripe makes it easy to understand what it is capable of, how it works (e.g. events), and how to use it. This is largely based on its excellent documentation system, but also because anyone can spin up a fully functional sandbox in a few minutes. The result is that:

* Ideas can be quickly prototyped and verified.
* Any concerns or uncertainties can be turned into specific technical questions for Stripe to answer -- and those answers can then be tested to make sure they produce the desired result.

With many products (including several of Stripe's competitors that I looked at), it was not possible to properly validate the functionality before purchase. With Stripe, I had vetted the functionality and architecturally designed about 95% of the billing project by the time Stripe was settled on as a vendor. Because of good documentation and strong alignment between the documentation and Stripe functionality, that initial design was an accurate high-fidelity design to what ended up being implemented.

### Onboarding / Initial Implementation

After selecting Stripe, the next big area is the initial implementation and rollout of Stripe. In The Billing Project, this work involved everything from accounting audit processes to rolling out a new customer service solution (including training them on it). The big win here was that, overwhelmingly, Stripe JustWorked. The software behaved the same for the sandbox as it did in production. It scaled well. There weren't weird hiccups. When strange circumstances arose, there was a trail of events and logs to understand what happened.

!!! note "Aside"

    While in theory, JustWorks shouldn't be so noteworthy, the reality is that many software solutions work fine in limited testing but don't work well when scaled into production. So a product that consistently performs as documented gets high marks from me.

The ability to fully test code and functionality[^clock] in a fully functional sandbox was an enormous win. I'm a huge fan of continuous-delivery style approaches, and Stripe sandboxes allowed code to be well tested before release. Additionally, very little Stripe behavior required manual intervention, which meant the project could be heavily automated, streamlining many processes and training procedures.

[^clock]: One problem during the project was testing long-running operations (such as monthly billing). My team implemented some solutions such as daily billing as a stop gap; since then Stripe has added accelerated clocks to better support such operations.

### Maintenance and Upgrades

Finally, Stripe was incredibly low maintenance after the initial launch. Stripe showed excellent legacy support, so even though Stripe released a number of new capabilities -- in some cases replacing existing features -- upgrades were only needed when the new capabilities were designed. In a few cases, the documentation got a bit rusty about old features, but that's a minor gripe. The other big wins in this category:

* Stripe proved to be exceptionally reliable.
* Stripe went above and beyond to communicate when something went wrong and make it right.

The last couple points aren't just technical capability, but reflect a culture -- and employees -- who make the choice that wins long-term trust, even accepting a short-term cost (e.g. admitting a mistake).

## Product

I've covered why the Stripe process was so enjoyable. But what qualities made it such a good product to work with?

### Documentation

Stripe does a really good job -- among the best I've seen -- at its documentation across multiple angles: The introduction to the concepts, the initial implementation, and then the technical reference for any additional -- perhaps more complex -- work. They recently open sourced their documentation system, [Markdoc](https://markdoc.dev/). The fact that they have a customized documentation language gives a sense of how much they invested in thinking through their documentation. Besides the completeness and solid organization, touches such as code samples in most common languages along with solid open source library support made it easy to use Stripe.

### Appropriate Abstraction

The second observation I'll make is that, generally, Stripe found ways to appropriately abstract billing into easy-to-understand concepts. Billing scenarios can be complicated. Tax law almost always is. Financial regulations and banking networks certainly are. But repeatedly, Stripe found ways of making these complex systems be understandable black boxes. For example, having a unified payment concept for payments across the globe is incredibly useful, instead of pondering how to handle prepaid credit cards vs. ACH or when and how to apply the new European secure payment requirements. This reduction of complexity into an appropriate usable unified abstraction is incredibly powerful.

### Reliability

I've previously mentioned the JustWorked characteristic of Stripe as it scaled upward. Beyond that, though, Stripe had clearly thought through their common failure modes and how to minimize the customer impact. For example, it wasn't uncommon to get an e-mail telling us that access to some set of data for audits would be delayed longer than usual (typically 2 days instead of 1). That notification wasn't great, but Stripe was quick and upfront to tell us when the delays occurred -- and the data accessibility wasn't on the critical path to the rest of Stripe's capabilities. It probably helped that originally, that data typically took 3 days to become available, but over time, Stripe improved it so that it was typically available within a day. Likewise, the handful of times that something went wrong (e.g. a tax law miscalculation), Stripe was quick to own the mistake, give a clear statement of impact, and work with my company to make it right. Sure, I'd prefer not to ever have anything go wrong, but that's likely impossible with the complexity of what Stripe is dealing with. If flawless isn't possible, Stripe's approach of contained fallout, good ownership, and amazing reliability is a close second.

### Customer Support

Stripe's customer support was consistently friendly, responsive, and able to understand/resolve concerns and questions. Some of the questions that I threw at them were fairly complex, and they were able to get meaningful responses, often from the development teams. I didn't always like the answer (e.g. no, we're not changing that behavior), but I was confident that they understood the concern and why it wasn't user friendly. In many ways, this behavior seems like it should be a baseline, especially when customer support is a paid feature, but too often customer support is more like an [Eliza instance](https://en.wikipedia.org/wiki/ELIZA) than an actual person. Again, doing the basics with excellence gets high marks here.

### Testability and Debugging

Stripe has also clearly thought through the engineering challenges around testing and debugging a complex system. Three examples of this consideration:

* The fully functional sandbox, which can be spun up in minutes for prototyping, for example, is not just good for sales and prototyping, but provides a reliable way to almost completely test code prior to release. (Stripe has been gradually adding capabilities, so it may now be fully testable.) The sandbox can be configured via the API, which facilitates a configuration-as-code approach.
* The webhooks have automatic retry (up to 3 days in production), which makes it very easy to recover from outages in the receiving system. That is, start with the requirements that (a) webhook handling be idempotent and (b) that the webhook response is only a 200 if all parts of the handler successfully complete. Then Stripe will keep retrying the webhook until it succeeds or expires, which gives a long window to recover. As a bonus, Stripe will e-mail if it detects a sudden spike in the error rate.
* Stripe provides an excellent set of event and call logs for each object (e.g. invoice, account, customer). These are sufficient to reconstruct the story of how some scenario or another ended up happening. They are also fantastic for reporting bugs to Stripe - "See event log X12345 where Y, then 10s later event log X54321 where Y' -- how is that possible?"

### Improvements, Legacy Support, and TLC

I learned a lot more about how to make a good product from Stripe, but I'll note just a few more points:

1. Stripe continued to deliver improvements. In fact, I'd guess that some of the annoyances I allude to in this article have been corrected by now[^feb]. From improved payment models to faster Sigma data availability to improved clocks for testing to updates for different financial regulations, there was a stream of new and useful capability. In the last few years, Stripe has put enormous work into their codeless capabilities where they host a lightly-branded subscription management system, which I would take a close look at with an eye toward minimizing project complexity if I were to take on another billing project.
2. Stripe maintained excellent legacy support. While Stripe's API changes are generally backward compatible, each API call is allowed to specify which version of the API it is using. This means that Stripe has excellent backward API support for years, even if a variable name or call is deprecated or changed. I don't believe Stripe ever required an upgrade to continue operating; all upgrades were to either keep current or access new functionality.
3. Stripe makes smart choices in features. For example, the metadata fields are incredibly useful in reducing development complexity; the ability to export [Sigma data](https://stripe.com/newsroom/news/stripe-data-pipeline) to Snowflake[^snowflake] goes a long way to make Stripe a great tool rather than a walled garden.
4. Stripe iterates. Having seen some of their betas, the questions they ask, and the way the product changes, they clearly have a customer-centric view where they are evaluating customer response and adjusting the product. I wouldn't necessarily call it Agile -- probably hard to be fully Agile with financial regulations -- but there is clearly a build-test-react-test-react mentality behind their work rather than a build-it-once approach.

[^feb]: For example, maybe unpaid February subscriptions will actually cancel when they are not paid in 28 days rather than issuing the March invoice mere moments before they expire. Yes, this is probably my largest unresolved gripe with the system.
[^snowflake]: Judging by that link, they've added Redshift as an option as well; I'd anticipate other popular options will be added at some point.

# Weaknesses

As one might expect from my review so far, Stripe nails so much. I'd overwhelmingly recommend using Stripe. That said, there are a few points that keep me from giving it an A+:

* _Complex scenarios_: My experience was that when it comes to the intersection of multiple features (e.g. taxes plus schedules plus prorations), Stripe too often had not adequately considered the proper behavior or tested outcomes. I realize this is nit-picky -- most customers clearly aren't leveraging multiple features simultaneously in their billing systems -- and stems from so much that Stripe does well, but I wish they would go just a bit further.
* _Documentation of complex behaviors_: While Stripe's documentation is fantastic, both for introducing topics and providing references, complex behaviors involving three or four features are often underdocumented and difficult to reconstruct.
* _Development speed_: Stripe is cautious in adding new features. Given their dedication to quality, the unforgiving nature of financial transactions, their excellent abstractions, and wanting practical real-world feedback, I get why development sometimes seems slow on obvious features. That said, I wish they'd move a bit faster at times.
* _Pricing model_: My experience with Stripe is that complex technical bugs didn't get attention without paid customer support. I'm sure there is good business rationale behind this choice, but I would rather see a company that considered product excellence to include complete documentation and bug fixes as part of the product itself.
* _Configuration-as-code_: While Stripe provides many excellent sandboxes and even ways of migrating sandbox settings to production, there isn't true configuration-as-code support where one can define all the settings in a repository and then push those settings to any sandbox (or production). I get the challenges in supporting this, but it would make it a lot easier to guarantee that the sandbox testing was exactly configured correctly -- and that the tested configuration was then exactly the one deployed to production.
* _Android/iOS gardens_: One of Stripe's great strengths is the ability to be a one-stop-shop for all-things-billing - payments, refunds, taxes, and so on. The exception to this is the Google and Apple application stores, which require[^require] certain transactions to go through Google or Apple systems. Google and Apple almost certainly want to keep their slice of the pie and not share with Stripe, so I can't fault Stripe here. Nevertheless, it introduces a hole: If I have to deal with the Apple and Google payment systems anyway, do I still need Stripe?

# Recap

So that's a breakdown of what made Stripe a fantastic product from project inception to launch to maintenance: A combination of attention to excellence, understanding the needs of the customer both in product and process, and applying many different disciplines well. It's a good case study for thinking through a software product and how to make it exceptional.

[^require]: Or at least, effectively give the option to go through the stores. Recent court rulings may have introduced some changes here.
