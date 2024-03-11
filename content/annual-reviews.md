title: Annual Performance Reviews (Part 1)
subtitle: Rethinking the problem
date: 2024-01-15
category: systems
tags: brainstorming
status: published

Annual performance reviews are one of those staples of American corporations. As far as I can tell, they haven't changed much in decades.

Sometimes they're done semiannually. More recently it's popular to do the "360 degree" reviews to get feedback from peers and direct reports, not just one's boss. They're typically linked to compensation adjustments and promotions. Occasionally their integrated with practices such as [stack ratings](https://insight.kellogg.northwestern.edu/article/performance-review-ranking-system-best), making it easy for employers to cull the "bottom" performers[^mystery].

[^mystery]: Stank rankings seem like a terrible idea because one is incentivizes people to be the best person on a terrible team. I'm sure that there is more to it than that, but a bit of marketing to make the upsides more obvious would go a long way. After all, engineers are generally known for understanding complex systems and problem solving; does one really want them gaming the performance evaluation system?

> Can we do better than the traditional performance review?

Beyond that, they often cause a massive amount of work for people in writing reviews. Worse yet, that work often seems disproportional to the benefit. I mean, when was the last time someone wrote "writes great performance reviews" in their review of someone?

So with decades of corporate experience, the modern internet, and a bit of thought, can we do better than the traditional performance review?

# The goal

As is often the case, it's worth asking "What's the purpose of performance reviews?" Or perhaps better yet: "What should the purpose of performance reviews be?" I find companies often have a multitude of goals:

* Formally document unofficial sentiment. Everyone knows Jane has been doing a good job, but the review gives a way to document it and acknowledge it at a corporate level.
* Give valuable feedback for employees to grow and learn from.
* See the forest for the trees. Periodic reviews can be a chance to look at trends and patterns, not just individual moments. This helps us avoid the fallacies such as [composition](https://en.wikipedia.org/wiki/Fallacy_of_composition), looking instead of whether the sum of the many moments is more -- or perhaps less -- than the individual moments.
* Force managers to give feedback. Ideally, of course, an employee knows at all times what is thought of their performance, especially with regard to their boss. But sometimes that communication doesn't go very well for whatever reason, and formal reviews force feedback to at least at some frequency.

# The struggles

At their worst, employee reviews become a performative dance where the question of "How much does my boss like me?" gets translated in a corporate justification. If the employee is liked, then corresponding weight is given to the employee's accolades. A disliked employee finds more attention given to their short-comings. And given the complexity of software development, it's pretty easy to justify either perspective.

Nobody wants to say this; it's the stuff of law suits and HR nightmares. But it can be really easy to create a review system that sanitizes the manager's opinion rather than giving real feedback.

What else can go wrong?

* Many (most?) people aren't good at tracking trends over time. This gives many reviews a heavy recency bias. (And there's often very little training on this topic.)
* Many people lack the full picture when they give feedback. For example, suppose I notice that John seems courteous but distant when I interact with him. Is that because he's busy prioritizing more important work? Is that because he doesn't want to help me more? Is that because he has a different baseline for what friendly looks like?
* People are often implicitly pressured to not give critical feedback. People may avoid high-quality criticism for a number of reasons, from a fear of feedback being blown out of proportion in the review to a fear of breaking social expectations.
* 360-style reviews often allow employees to choose their peer reviewers. Given the impact reviews can have on performance and compensation, there's heavy incentive to select those who seem most likely to give a positive review -- not necessarily those that will give the most thoughtful feedback.

# The ideal system(s)

Let's imagine we're starting a new company that is recreating performance reviews from scratch. We want to create a product -- and a system of reviews -- that's tailored to the modern business world. What would would we want?

- As a business owner, I want a way to formally document performance that informs compensation adjustments and promotions[^departures] so that quality employees are appropriately recognized and legal entanglements are avoided.
- As a business owner, I want my managers to have timely and relevant feedback so they can make good decisions around employee growth.
- As a manager, I want reviews to be straightforward and low hassle.
- As an employee, I want my review to highlight my strengths and best work.
- As an employee, I don't want to be surprised by negative feedback.
- As an employee, I want a chance to correct negative perceptions before they influence my annual review.
- As a company selling this product, I want there to be a simple transition path for new customers from their current system so that we can gain customers.
- As a company selling this product, I want our product to be profitable so that I make a profit.
- As a company selling this product, I want companies to stick with my product so that I'm confident the product is at least good enough to retain its current users.

[^departures]: And when employees need to be let go, the business wants a documentation trail that avoids lawsuits and similar unpleasantness.

Part of the challenge is that different parts of the system have different goals. Managers would like to know everything as soon as possible, but employees often don't want to prematurely escalate concerns. As someone giving feedback, I want my experience to be taken seriously. But as someone receiving feedback, I don't want a single person's critique to unfairly dominate my review. And with each company and individual having their own style for how quickly and vocally to speak about issues, conflicting objectives easily arise, such as a manager wanting faster feedback, but individuals wanting to give more time for patterns to play out.

However, as a company wanting to sell a product, we'd prefer to develop a product that is culture agnostic. Not only does this approach give us a broader customer base, but changing company culture is a hard problem -- and it's far more complex if we're selling a review system paired with a particular cultural approach.

# The product

So what might our product do? Let's give it a set of features:

1. Regular, low-effort collection of feedback from employees.
2. Trend-based alerting for management.
3. Directed prompts for specific feedback.
4. AI-assisted writing (because everything is cooler with AI).

Let's call our product SmartReviews.

Next time, in [part 2]({filename}annual-reviews-part-2.md), I'll unpack more of my ideas of how these features would work.
