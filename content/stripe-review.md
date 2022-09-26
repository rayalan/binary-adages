title: Stripe Review
date: 2022-06-13
category: technology experience reviews
tags: stripe, reviews, exemplars
subtitle: Serving well with technology
status: published

[TOC]

All too often, integrating with a third-party technology is a pain: The product doesn't reliably work, the documentation is inadequate, the solution lacks essential concepts, the customer support disappears once the purchase has been made, and so on. Most developers have felt this pain, I think, whether it is using an open source library or a purchased solution.

Thus on the rare occasions when a company knocks it out of the park with an effective product that is a joy to work with technically, I want to reflect on how that win was achieved -- and what lessons I can learn.

Today I'm reviewing [Stripe](https://stripe.com/). As background, I've worked with Stripe for about four years; my introduction to it was investigating it as a potential 3rd-party replacement for an in-house billing system (hence forth _The Billing Project_). After it beat out the other options the company looked at, I led the project to implement Stripe across the company, including satisfying accounting audits and customer service interfaces. And after the initial implementation, I oversaw the maintenance and iterative improvement of the new Stripe-based billing system.

# Big Takeaways

My three big takeaways from Stripe:

* _Excellence matters_: Across the board, Stripe is an excellent product. Given a choice, they seem to prefer to do the essentials well rather doing more poorly. The result is that while I did, at times, want more from the product, I was confident that what I had to work with was rock solid.
* _Intertwine process with product_: The "things" Stripe produced (such as APIs, features, and documentation) also enabled processes (such as onboarding, prototyping, testing) to work well.
* _Integrate multiple disciplines_: Stripe reflects excellence in the disciplines of development, architecture, user experience, quality assurance, customer support, business intelligence, and law. I'm pretty sure they aren't hiring individuals who have mastered all these fields; rather, they are effectively integrating expertise from many different people.

# Strengths

So what did Stripe do well? I'll split this discussion into two views:

* What processes do customers need to do well?
* What product features do customers need?

Stripe : Exemplar
  Pros
    Onboarding
    Reliability
    Webhooks w/retry
    Errors (logging, events)
    Appropriate Abstractions --> UX,
    Sandboxing
    Iterations
      Improving clarity
    Customer Fit
    Codefree solutions
    Documentation
    Good technical resources (once paid)
    Good iterations
    Legacy support
    Metadata (nosql w/transactions)
    Changelog

## Processes

In this section, I'm looking at the different stages of a project to implement Stripe, and how Stripe strongly supports each stage.

### Technology Vetting / Selection

First, a billing system platform needs to be selected. Build in-house? 3rd-party? Which one?

Stripe makes it easy to understand what it is capable of, how it works (e.g. events), and how to use it. This is largely based on its excellent documentation system, but also because anyone can spin up a fully functional sandbox in a few minutes. The result is that:

* Ideas and be quickly prototyped and verified.
* Any concerns or uncertainties can be turned into specific technical questions for Stripe to answer -- and those answers can then be tested to make sure they produce the desired result.

With many products (including several of Stripe's competitors that I looked at), it was not possible to properly validate the functionality before purchase. With Stripe, I had vetted the functionality and architecturally designed about 95% of the billing project. Because of good documentation and strong alignment between the documentation and Stripe functionality, that initial design was an accurate high-fidelity design to what ended up being implemented.

### Onboarding / Initial implementation

After selecting Stripe, the next big area is the initial implementation and rollout of Stripe. In The Billing Project, this work involved everything from accounting audit processes to rolling out a new customer service solution (including training them on it). The big win here was that overwhelmingly, Stripe JustWorked. The software behaved the same for the sandbox as it did in production. It scaled well. There weren't weird hiccups. When strange circumstances arose, there was a trail of events and logs to understand what happened.

!!! note "Aside"

    While in theory, JustWorks shouldn't be so noteworthy, the reality is that many software solutions work fine in limited testing but don't work well when scaled into production. So a product that consistently performs as documented gets high marks from me.

The ability to fully test code and functionality[^clock] in a fully functional-sandbox was an enormous win. I'm a huge fan of continuous-delivery style approaches, and Stripe sandboxes allowed code to be well tested before release. Additionally, very little Stripe behavior required manual intervention, which mean the project could implement

[^clock]: One problem during the project was testing long-running operations (such as monthly billing). My team implemented some solutions such as daily billing as a stop gap; since then Stripe has added accelerate clocks to better support such operations.

### Maintenance and Upgrades

Finally, Stripe was incredibly low maintenance after the initial launch. Stripe showed excellent legacy support, so even though Stripe released a number of new capabilities -- in some cases replacing existing features -- upgrades were only needed when the new capabilities were designed. In a few cases, the documentation got a bit rusty about old features, but that's a minor gripe. The other big wins in this category:

* Stripe proved to be exceptionally reliable.
* Stripe went above and beyond to communicate when something went wrong and make it right.

The last couple points aren't just technical capability, but reflect a culture -- and employees -- who make the choice that wins long-term trust, even accepting a short-term cost (e.g. admitting a mistake).

## Product

I've covered why the Stripe process was so enjoyable. What product qualities made it such a good product to work with?

### Documentation

### Improvements

### Legacy Support

### Appropriate Abstraction

### Testability

### Debugging

### Reliability

### Customer Support

Good problem / abstraction in a complicated space.

# Weaknesses

As one might expect from my review so far, Stripe nails so much. I'd overwhelmingly recommend using Stripe. That said, there are a few points that keep me from giving it an A+:

* _Complex scenarios_: My experience was that when it comes to the intersection of multiple features (e.g. taxes plus schedules plus prorations), Stripe too often had not adequately considered the proper behavior or tested outcomes. I realize this is nit-picky -- most customers clearly aren't leveraging multiple features simultaneously in their billing systems -- and stems from so much that Stripe does well, but I wish they would go just a bit further.
* _Documentation of complex behaviors_: While Stripe's documentation is fantastic, both for introducing topics and providing references, complex behaviors are often underdocumented and difficult to reconstruct.
* _Development speed_: Stripe is cautious in adding new features. Given their dedication to quality, the unforgiving nature of financial transactions, their excellent abstractions, and wanting practical real-world feedback, I get why development sometimes seems slow on obvious features. That said, I wish they'd move a bit faster at times.
* _Pricing model_: My experience with Stripe is that complex technical bugs didn't get attention without paid customer support. I'm sure there is good business rationale behind this choice, but I would rather see a company that considered product excellence to include complete documentation and bug fixes as part of the product itself.
* _Configuration-as-code_: While Stripe provides many excellent sandboxes and even ways of migrating sandbox settings to production, there isn't true configuration-as-code support where one can define all the settings in a repository and then push those settings to any sandbox (or production). I get the challenges in supporting this, but it would make it a lot easier to guarantee that the sandbox testing was exactly configured correctly -- and that the tested configuration was then exactly the one deployed to production.
* _Android/iOS gardens_: One of Stripe's great strengths is the ability to be a one-stop-shop for all-things-billing - payments, refunds, taxes, and so on. The exception to this is the Google and Apple application stores, which require[^require] certain transactions to go through Google or Apple systems. Google and Apple almost certainly want to keep their slice of the pie and not share with Stripe, so I can't fault Stripe here. Nevertheless, it introduces a hole: If I have to deal with the Apple and Google payment systems anyway, do I still need Stripe?

# Recap

So that's a breakdown of what made Stripe a fantastic product from project inception to launch to maintenance: A combination of attention to excellence, understanding the needs of the customer both in product and process, and applying many different disciplines well. It's a good case study for thinking through a software product and how to make it exceptional.

[^require]: Or at least, effectively give the option to go through the stores. Recent court rulings may have introduced some changes here.
