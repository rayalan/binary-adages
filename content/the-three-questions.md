title: The Three Questions
subtitle: Thinking Well
date: 2023-10-09
category: practices and principles
tags: management, knowledge, uncertainty
status: published

I'm a bit of a natural contrarian.

A few years back, a coworker gave an enthusiastic presentation over how amazing Pixar's approach to innovation was, and by, implication, how our software development department should adapt the same approach that Pixar described in their  book [Innovate the Pixar Way](https://www.amazon.com/Innovate-Pixar-Way-Corporate-Playground/dp/0071638938).

I didn't know much about Pixar and I'd never read the book. So my question was: Did the book discuss any prerequisites or requirements for this approach to work? in other words, is this approach really a one-size-fits-all solution for both large movie companies and small software development companies?

In the years since then, the vaunted "Pixar Way" hasn't been nearly so successful (see [this article](https://screenrant.com/pixar-movies-what-went-wrong-problems-explained/) for one take).

I still know almost nothing about Pixar, but I've pondered what the right response is. Here's three takes:

# Selection (sampling) bias

A classic example of sampling bias is to interview a hundred successful startups about how they survived when others fail, look for similarities, and then attribute the startups' success to those attitudes and behaviors. Sounds great, right?

Not so fast; it's possible that all the failed startups also exhibited those same qualities. So unless failed startups are also surveyed, it's easy to report a characteristic that both successful and failed startups share as a characteristic of a successful startup.

Another variation of this is to e-mail 50,000 people that the stock market will go up next week, and another 50,000 people that the stock market will go down. The next week, look at what the stock market did. Drop the people who received the mistaken prediction to. Then e-mail half of the remaining people that the stock market will go up, and the other half that it will go down.

Repeat this step a few times and there will be several hundred people who you can reach out to and say "Look at my track record; I correctly predicted the stock market every week for two months -- wouldn't you like to invest your money with me?"

By hiding the entirety of the track record, it's easy to generate the illusion of expertise.

# Correlation is not causation

There's a [whole page for logical fallacies linked to correlation and causation on Wikipedia](https://en.wikipedia.org/wiki/Questionable_cause). There's also some fascinating studies on how powerful the illusion of doing something can be for causing change -- for example, there's an [article](https://www.medicalnewstoday.com/articles/306437) discussing the effectiveness of placebo drugs.

I'll just add that many corporate structures incentivize turning correlation into causation. After all, if a leader isn't successfully making decisions, why keep them on the payroll? And so leaders are heavily motivated to find causal relationships between their actions and good outcomes -- and to neglect correlation between their actions and suboptimal changes.

And, of course, I imagine it's a lot more fun to write about how my brilliant decisions led a company to greatness than to write the sequel about how those same decisions just happened to work for those particular circumstances but might not be more widely applicable.

# Mark Twain

And then there's the underlying problem that data is just messy, even with the best intentions. Reality is often complex and doesn't tell neat stories. It's fun to write the blog article where the trend line on a major metric changes at the exact moment, but that's not always the story.

> There are three kinds of lies: lies, damned lies, and statistics.
>
> Maybe Mark Twain ([source](https://en.wikipedia.org/wiki/Lies,_damned_lies,_and_statistics))

There's the question of how accurate is the underlying data. Maybe the reworked Android app doesn't report data through the old system any more. Maybe the graph only tracks error rates from the server point of view, not from the client point of view. Or maybe the system is throwing out large values as being "unrealistic," masking a key system problem. I've seen all of these -- and more -- happen.

# So what

One of my favorite engineering jokes is that an engineer has two excuses to avoid work they don't like. First, the idea is technically impossible. And secondly, if that excuse fails, it is technically possible -- but the solution will cost way too much.

Sometime I wonder if an emphasis on data-driven decision making has replaced "it's technically impossible" with "the data doesn't support it" where data is being unconscientiously selected to support the opinion I already have.

To counter-act this, my three favorite questions are:

_Why?_

_So what?_

_But is that really the case?_

The first two are exploratory, seeking out the causation and correlation. But the third one is my nudge to step back and consider the bigger picture: Does the picture make sense? Do I have the right data? What technical choices might be distorting the data? It's the attempt to not just accept an answer because it is the accepted wisdom, but actually evaluate if and how the common wisdom applies to my scenario.

And as a final note, I want to highly recommend _[How to Measure Anything](https://www.amazon.com/How-Measure-Anything-Intangibles-Business/dp/1118539273)_ by Douglas Hubbard. THe book helped me change how I measure in many business contexts.

With that, I encourage my readers to ponder if what I've said is really the case.
