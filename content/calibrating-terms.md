title: Calibrating Expectations
subtitle: Amazing engineering or standard operating procedure?
date: 2023-10-02
category: practices and principles
tags: vocabulary
status: published

> __"You all doing amazing work. I can't believe how much is getting done and everything you are accomplishing."__
>
> _Some engineering leader in some context, fairly routinely._

My thought process goes something like this:

* Has the definition of amazing changed recently? _Checks Google._ Nope, still "causing great surprise or wonder; astonishing."
* Okay, recent brain injury or trauma?
* No? Unfamiliar with the field of software engineering?
* Still no? Perhaps the [pod people](https://en.wikipedia.org/wiki/Pod_People_(Invasion_of_the_Body_Snatchers)) invaded?

Okay, so aliens aside, what's happening here?

# Low Wonder

First, I'm simply a low wonder person, especially in areas that I understand.

_Reusable rockets._

Yep, I find recoverable rockets amazing. Shoot them far away, land them without a fireball or metal pancake, and then do it again and again? That's amazing!

Of course, I know very little about rockets -- I know a few basic physics principles like "go up ==> come down" and "go far up ==> come down fast" and "fast thing + earth ==> earth + not much left." And perhaps that for most of my parents' lifetime, rockets were largely (entirely?) single use and often reentry vehicles landed in the ocean.

So it's pretty easy to impress me with these rockets making precise landings at precise locations such as the middle of a barge. Is it actually hard? I don't know (but probably -- it is rocket science after all).

Software engineering, on the other hand, is not a mystery to me. I know what I can do. I have a lively imagination. And I can multiply. So I can easily envision what thirty or fifty or a hundred of me could achieve[^ego]. And usually whatever the company has done is less than what I can envision a hoard of Alan-clones achieving.

[^ego]: A bit of ego and an overestimation of what I can accomplish probably inflate the estimate a bit too.

Beyond that, though, I also know all the holes. I know that despite "graceful degradation" being one of the requirements, there are 153 ways that it can fail without any degradation, graceful or otherwise. I know that the graphics aren't scalable, so they only look right at the demo resolutions. I know that the whole data storage approach will have to be rewritten before launch because it can't handle much more than the demo load. And I know that half the metrics are missing key information.

So while the product looks good, the actual product isn't exactly what is being seen. Whether or not that matters is a different question, which brings us to...

# "World class"

What is meant when we describe software as "excellent" or "world class"? Well, a world class athlete is one who competes on a world stage -- maybe in the Olympics or the World Cup. A world class chef is one who makes the tastiest food -- perhaps a 5 Michelin chef.

Even here the definition is a bit fuzzy -- what if someone competes in the Olympics, but always places last? Could the runners up to the Olympics be considered world class? What if I really like Joe's taco truck and dislike foie gras? Does a bunch of people disagreeing with me really make the taco any less a world-class dish?

But the idea of a world class athlete or dish is really clear, even if the specifics are a bit fuzzy.

_The field of software is far worse._

What does it mean for software to be the best in the world? Cost? Low time to develop? Working as designed? Working as expected? Working as desired? Easy to modify? Easy to understand? Reliable? Reliable in extreme conditions? Something else?

I've never had to design software, for example, that reliably worked in Antarctica when operated by shivering people in thick gloves. And yet, I bet that some software is designed for those conditions. Does that mean that such software is more world class than what I've written? Would my software even be better if designed for such an environment, or would the compromises needed to function in such extremes undermine other aspects of my work?

Worse yet, the definition of excellence in software changes frequently, often on the same project. Sometimes leaders will talk about the push for excellence. Then the budget cuts come, a new leader takes over, and the push is for delivering whatever value has been achieved and moving on to the next project.

# So what

Communication is a challenge, especially when mixing cultures, generations, and backgrounds. It's a wonder it works at all. Here's a few of my takeaways when it comes to aligning:

1. Some people like to use hyperbolic praise; give them space to do so.
2. Cultivate a vocabulary of praise and encouragement that is not dependent on wonder. I've written [elsewhere](/my-best-managers.md) about the importance of thought reviews, and that principle applies more broadly here: Can I point to specific praiseworthy behaviors and connect the dots to specific praiseworthy outcomes?
3. Do not fake wonder or hyperbolic praise. It comes across insincerely (because I am insincere when I do it) and undermines my main strengths -- a thoughtful straight shooter.
4. Intentionally lower my expectations, especially when they are stratospherically high, and concretely verbalize my expectations[^goals].
5. Let people know when I'm struggling to recalibrate. It's easy for people to read my hesitation as disapproval of their plan when I'm actually trying to rapidly assess an unanticipated approach and decide if there's any blockers to moving forward.

And I'd love to get other people's take on what style of enthusiasm they appreciate in leaders. Maybe I need to add comment support to this blog so I can end with discussion questions.

[^goals]: This topic could be its own article. There are different kinds of expectations (e.g. important immediate goals, important long-term goals that I'm afraid will slip way if they aren't addressed, but aren't necessarily central to the work, beliefs I have about the work that I'm very certain of, beliefs I suspect are true, etc.) Often my expectations will shift based on feedback. For example, I've often had developers tell me something like "I looked into such-n-such technology and we can't do this, but it solves a bunch of our other problems and gives us this cool new capability." And that's enough ROI for me to change my expectations. Beyond that, there's a whole topic about expressing reservations about a path and equipping others to recognize the wrong path while still genuinely giving them the freedom to make their own choices and supporting the outcome.

4. Intentionally


- Do not fake wonder or hyperbolic praise; it doesn't work with my style and comes across as insincere.
- Intentionally lower my expectations (which are often stratospheric) and concretely verbalize what I expect.
