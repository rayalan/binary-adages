title: Vocabulary
subtitle: A rose by any other name
date: 2023-10-23
category: practices and principles
tags: knowledge, uncertainty
status: published

One of my favorite jokes is that there are only [two hard programs in programming](https://martinfowler.com/bliki/TwoHardThings.html) -- naming things, caching, and off-by-one errors.

# A Problem - Discovered

I particularly identify with that first problem -- how do you name something well? A few years into my career, I realized that I'd picked up a bad habit: I wasn't thoroughly learning vocabulary. I knew the concepts well, but I wasn't understanding what a _monad_ was or the difference between a _statement_ and an _expression_.

This didn't bother me in day-to-day programming -- the compiler certainly never complained about my ignorance. And most documentation is completely comprehensible without understanding a closure and an anonymous function.

I did find, though, two problems.

First, it hampered my ability to communicate precisely with my colleagues. It's a whole lot less precise to say "implement our tools in an standalone fashion so they can be upgraded independently" than it is to say something like "implement a hermetically sealed approach to tooling." Both statements may communicate about the same intent, but using the precise vocabulary links my intent to similar work done by others rather than leaving my co-workers guessing about whether I'm referencing my own idea, an standard industry practice, or something else.

Second, search engines are terrible when vague common words are substituted for industry terminology. The search results for "monorepo tooling" and "support multiple projects in one repo" are radically different. And the former one is far more useful, tapping far more quickly into the resources written by experts -- and who, because they are experts, use the right terminology.

When I lucky, my amateur lingo would find a critical word in one of the results and I could refine my search. When I wasn't lucky, I'd live happily oblivious to answers that could have dramatically improved my work.

# A Problem - Solved?

So I did what any diligent engineer would do -- I knuckled down and worked on my vocabulary. I paid attention to what other said, read more, and practiced using the terms in context, even if it was just explaining them to myself.

_Problem solved, right?_

Not so fast. First, I realized that terms are often used with varying levels of precision. For some people, a unit test means "a fast low-dependency test". For others, it means specifically testing a single function or method with no outside dependency.[^unit] For some people, invoking a specific technical term meant "something along these ideas." For others, the same technical term meant a very exact implementation -- _this_ and only _this_.

[^unit]: And no, those aren't the only definitions. Given the multitude of definitions for types of tests, I've really grown fond of the [fast or slow differentiation](https://medium.com/tsengineering/fast-and-slow-tests-bbaa3d7267e8).

Compounding the issue is that the use of technical jargon masks the differing ideas. After all, the use of the technical term implies knowledge and precision, right? Nobody would every use a technical term if it wasn't appropriately precise and meaningful, right? And certainly nobody would ever use a term that they didn't fully understand, right?

# So what

Three quick take away from this journey for me:

1. I still ask "What do you mean by _term_?" all the time. But now I ask less because I don't know what I would mean by the term, and more because I'm not sure what others mean.
2. Knowing vocabulary has made me more conversant in a number of concepts and thus helped me be a better engineer.
3. Naming things -- aka vocabulary -- really is one of the two hard problems of computer science.

What other lessons come to mind?
