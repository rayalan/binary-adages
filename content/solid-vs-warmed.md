title: SOLID vs. WARMED
subtitle: What actually matters?
date: 2024-04-29
category: software design
tags: knowledge, uncertainty
status: published

[TOC]

Some time ago, I caught this [Molly Rocket video](https://www.youtube.com/watch?v=7YpFGkG-u1w) about where bad code comes from. It's a great video and well worth watching in its entirety. But today I want to highlight his critique of SOLID and his WARMED counter-proposal.

# SOLID

For those unfamiliar with it, [SOLID](https://en.wikipedia.org/wiki/SOLID) is a set of software design principles. Per Wikipedia, these are the single-responsibility principle, the open-closed principle, the Liskov substitution principle, the interface segregation principle, and the dependency inversion principle.

In many circumstances, I've found these are good principles. However, there are some very sharp edges. Here are a few that I've encountered:

## Language fit

Not every language supports these principles well. For example, not every language supports the interface concept well. With C++, for example, the use of abstract parent classes to implement interfaces led to headaches in many situations because of the intricacies of class inheritance, especially if a class implements multiple interfaces. Even a simple change such as the addition of the _auto_ keyword made it a lot easier to use abstractions rather than concrete types because developers no longer had to type out (or update) the complex template types that could occur. Elsewhere, other languages don't have first-class support for functions or perhaps make partial functions and lambdas challenging to write.

Because specifics of the language impact how easy it is to implement and refactor code, trying to follow the SOLID principles can significantly increase the time to develop code. And sometimes it's really clear that the extra complexity just isn't worth the time -- it's a form of [gold-plating](https://en.wikipedia.org/wiki/Gold_plating_(project_management)).

## Methodological rigidity

I've worked with a few developers who rigidly adhered to SOLID principles. In one case, a relatively simple piece of code got rewritten over and over in an attempt to implement increasingly pure approaches to SOLID. The programmer was delighted when they successfully abstracted out all of the if statements. While I appreciate the [factory pattern](https://medium.com/@unclexo/factory-method-dealing-with-object-creation-and-conditional-switch-or-if-else-nested-statements-2ea9956fd671), the result here was overkill. Instead of perhaps 30 lines of code, the result was multiple files filled with boilerplate which was hard to understand. While this might have been justified for a critical component, this wasn't that -- just some out-of-the-way chunk of code that never got updated again, despite years of use.

While [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) is always easier to recognize in hindsight, I've found that overreliance on SOLID principles often makes it harder to see the forest for the trees.

## Overreliance on experts

Software development, like every field, relies on expert advice. And there's incredible value in learning from them. But software development is a rapidly changing field, and expert advice is often conditioned on certain assumptions -- the software development process, the programming language, the underlying architecture. And the best advice for a standalone application developed in a waterfall model with no internet with an engineering team of 5 may not totally apply to a networked application running in the cloud by a team of 500 executing in an Agile fashion.

A difficulty with SOLID is that there's no way to know if the principles aren't working. If your boss complains that development is too slow, the answer can easily become "Well, we're not following SOLID enough ... because that's the right way to develop software." This creates a self-reinforcing loop where software development is hard because it isn't SOLID enough, leading to more time spent implementing SOLID, leading to even slower development.

To be fair, the extreme reliance on SOLID can be overcome with being more widely read; there are plenty of other of schools of thought. But if one latches onto SOLID being the one true north star for development principles, then other experts are implicitly wrong, and it's easy to develop tunnel vision.

This kind of tunnel visioning isn't unique to SOLID, but for some reason, I've encountered it more around SOLID than other frameworks.

# WARMED

In contrast, WARMED talks about the six activities that need to happen to code. It needs to be:

* Written
* Agreed upon (or argued about)
* Read
* Modified
* Executed
* Debugged

The nice thing about these activities is that they closely connect to business objectives. Want a new feature? Well, the code needs to be written in a way that it will execute the desired functionality. And then when a bug occurs, it needs to be debugged and modified.

This framework also gives us language for talking about trade-offs. Code can be written faster if it isn't as readable. It may be more modifiable, but harder to debug. These are real considerations in writing code. Sometimes, for example, I've written very complex functions with code that I know is almost impossible to read, but the tradeoff is worth it because the company needs the functionality to ship quickly to satisfy a contract.

The WARMED model is also helpful for giving younger developers ways to consider the quality of their code. Often, for example, when reviewing code, I ask "What happens if this line errors?" In effect, I'm asking "Aside from the happy path, how could this code execute?" That is, the review isn't just about whether or not a certain set of principles was followed, but what outcomes are possible in a production environment. I like that WARMED explicitly highlights execution as a concern.

# So what

I don't mean to suggest that SOLID is bad. I often leverage the principles in my work. But I do believe that they have a time and a place. And I strongly prefer a more outcome-oriented approach such as WARMED when mentoring younger developers.

What have I missed? When can the WARMED framework be problematic for developers?