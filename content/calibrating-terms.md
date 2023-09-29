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

# Low wonder

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

# Variations

> "All of you should watch this video."
>
> _Alan's re-creation of an excited coworker after learning something awesome._

This style of communication isn't just about praise. For example, has a coworker ever said something like?

_"Everyone should read this book."_

But is that really the case? Almost certainly not. The book may have been a great book. It may have really connected with someone. Does that really mean it changed that coworker's work? Probably not.

Here's a table summarizing my observations:

| Observation | Value |
|-|-|
| Coworkers who read books | Lots and lots |
| Coworkers who read lots of books | Many |
| Coworkers significantly by a book | 0ish |

In short, my observation is that people often believe that the short-term impact of learning is far higher than it actually is.

I once had a boss who thought it was really important that I attend the periodic manager's training meeting. The material was solid, but I already intellectually knew most of it. And the company wasn't providing augmenting the training with the necessary support to apply the material:

* No psychologically safe space to talk about specific challenges or struggles or concerns.
* No reduced workload so that attendees had the necessary time to learn the skills being taught.
* None of the managers or senior leadership (including my boss) seemed to actually care if the attendees grew in these areas; they had their own priorities.

And the feedback I was getting from those around me was that I needed to work on other areas -- like having too much on my plate. So I tried to convince my boss to let me skip the trainings. Oh no, it was critically important that I be there -- but not vitally important that I be well-supported in mastering them.

# So what

[Intentional directed learning](./learning-to-learn.md) and growth matters. Likewise, communication is a challenge, especially when mixing cultures, generations, and backgrounds. It's a wonder it works at all.

Here's a few adjustments I make to better align in these situations:

## Communication calibration

1. Some people like to use hyperbolic praise; give them space to do so. 2. Cultivate a vocabulary of praise and encouragement that is not dependent on wonder. I've written [elsewhere](/my-best-managers.md) about the importance of thought reviews, and that principle applies more broadly here: Can I point to specific praiseworthy behaviors and connect the dots to specific praiseworthy outcomes?
3. Do not fake wonder or hyperbolic praise. It comes across insincerely (because I am insincere when I do it) and undermines my main strengths -- a thoughtful straight shooter.
4. Intentionally lower my expectations, especially when they are stratospherically high, and concretely verbalize my expectations[^goals].
5. Let people know when I'm struggling to recalibrate. It's easy for people to read my hesitation as disapproval of their plan when I'm actually trying to rapidly assess an unanticipated approach and decide if there's any blockers to moving forward.

[^goals]: This topic could be its own article. There are different kinds of expectations (e.g. important immediate goals, important long-term goals that I'm afraid will slip way if they aren't addressed, but aren't necessarily central to the work, beliefs I have about the work that I'm very certain of, beliefs I suspect are true, etc.) Often my expectations will shift based on feedback. For example, I've often had developers tell me something like "I looked into such-n-such technology and we can't do this, but it solves a bunch of our other problems and gives us this cool new capability." And that's enough ROI for me to change my expectations. Beyond that, there's a whole topic about expressing reservations about a path and equipping others to recognize the wrong path while still genuinely giving them the freedom to make their own choices and supporting the outcome.

# Learning calibration

1. Again, recognize that just because someone says something is essential doesn't make it so, even if they have a really important title[^social].
2. Ask clarifying questions.
   * What idea(s) from the book/training resonated with you? When is a time you wish you had applied them? What would that have looked like / how would things have gone differently?
   * How have you applied these ideas to your daily work? How long have you been applying these ideas? What have been the upsides and downsides of the change for you?
   * If you were in my shoes, which ideas would you focus on? What do you think it might look like if I really applied myself to those ideas?
3. Consider following up on the impact in a few months. Are they still doing the new practice? How is that working out[^remember]? What additional adjustments have they made? What kind of people would most benefit from the idea? Is there anybody who might not benefit?
4. Learn to recognize when growth is not the primary goal. Take advantage of the opportunity to learn something, but it's okay to stick to your well-considered plan for growth.

[^social]: On the other hand, people with important titles often like to feel important: Telling them that their recommendation was really meaningful to you is often a great approach; especially if they don't have the attention span to realize that you aren't actually applying said lessons any better than before.

[^remember]: Do they actually remember anything about the book?

And I'd love to get other people's take on what style of enthusiasm they appreciate in leaders. Maybe I need to add comment support to this blog so I can end with discussion questions.
