title: Learning to Learn
subtitle: Progress or mobius strip?
date: 2023-09-25
category: practices and principles
tags: growth
status: published

Learning is a strange topic in software. On the one hand, everyone talks about how essential it is, especially with technology changing so fast. And on the other hand, nobody really talks about how to learn what to learn[^close].

[^close]: This topic is closely related to last week's topic on [recognizing expertise]({filename}/recognizing-expertise.md).

Consider a few different scenarios...

# Largely ignorant

In some circumstances, we're largely ignorant of what we need to know. As a young child, we are guided by parents and teachers into basic knowledge such as reading, writing, and arithmetic. Similarly, vocational training and college degrees provide significant guidance in what skills need to be mastered. Sometimes these choices are good -- my college classes on information theory, statistics, and game theory have been referenced throughout my career.

Others, less so -- did Calculus IV help me be a great software developer? Well, I've never used it and forgotten most of it by now, so at most it serves as a way to score points on how smart I am or how tough my education was. (And strangely, scoring points is often an anti-social behavior, aside from job interviews and professional bios, so even there Calculus IV hasn't been very practical.)

Assuming one's education leads into one's career[^career], one's first job introduces a whole bunch more skills - some just missed by education, others that just come from real-world scenarios that school can't replicate. Some of these skills are technical (e.g., source control wasn't taught back in my day), but others are more professional skills -- real-world software development is very different than coursework. For example, in a class, the solution and complexity to problems are always well-known. But on the job, nothing forces the customer to ask for something that can be delivered in a week.

[^career]: This certainly isn't the case for many, and the way that people end up in degrees without a good sense of whether that career trajectory is a good match for their strengths would make for a fascinating social commentary. But that's a bit beyond this blog at the moment.

# Professional sponge

I encourage people to think of their early career as a sponge -- one finally has the tools to start learning their field in depth, and to observe and learn about related professions. At a job with user experience? Grab lunch with someone and ask them to tell you about it, how it interacts with software development, what they wish software developers would do to make user experience better. Just about everyone has opinions, and it's a fantastic way to create connections, build a repertoire of knowledge, and assemble a reading list.

If one is lucky, they'll get a thoughtful boss who will get to know them well and give detailed, specific feedback on how to grow. If not, working alongside thoughtful coworkers and actively soliciting feedback can be a a great source of input[^habits].

[^habits]: Both of these habits (soliciting feedback and sitting down with others) are great career habits to maintain. But their purpose morphs slightly over time. Often the feedback, especially the positive feedback, gets repetitive. In that case, it serves as more of a reality check that you are still coming across as you expect, rather than novel information. Likewise, the 100th conversation about user experience probably won't tell you that much more about the field -- but it'll tell you a lot about the individual and the specific challenges facing the company and be a great connection-building opportunity.

# Independent thinker

At some point, though, learning becomes harder. I see three big reasons for this:

* The difficulty of application significantly increases.
* The difficulty of discerning what to learn increases.
* The difficulty of discerning style from wisdom increases.

## Difficulty of application

The classic dilemma for new graduates is that they need experience in order to find a job. And how does one find experience without a job? The same problem applies to major jumps in career:

* How do you demonstrate that you can effectively direct a 200-person engineering team? Well, by effectively directing a large engineering team.
* How do you demonstrate that you can effectively architect maintainable software systems? Well, by doing so.
* How do you demonstrate that you can effectively run a large project? Well, by running one.

In some areas of software development, it's easy to bridge from one area into another. If one can write a few functions, one is probably dabbling in writing classes. One can start debugging easy problems, try their hand at harder bugs, and eventually prove their debugging skills.

But other jumps are more 0 to 1 jumps. Effectively running a small or medium team is very different than running a large department. Effectively designing a small internal application is very different than designing a company-wide microservice architecture. And these jumps are far harder because much of the knowledge comes from doing, and the ability to do often requires being in the right position.

I've been fortunate to work at a number of smaller, understaffed companies where I could drift into this kind of work. For example, I ended up as both architect and project manager on a major initiative when my co-leader (who I had worked with before) saw me taking the lead, thought I was doing great, and decided he had more important work to do. So now I can point to that experience and say "I've done that, and I got awards for doing so." So while that worked out great for me, it's not an easy way that anyone can demonstrate their capabilities.

And even in that work, my head knowledge exceeds what I've applied. There are industry standards for APIs that I know about but have never done. So when some hiring manager goes and writes out a job description wanting architects who have done this practice and that practice and this other practice, I don't exactly have the right experience.

# Difficulty of what to learn

At some point, I realized that there's basically an infinite amount to learn and improve. I can get better at almost any skill, and there are countless skills that would make me better at what I do. The question becomes: Where do I focus my energy?

* On shoring up my weaknesses?
* On amplifying my strengths?
* On a skill that seems largely absent in my current job?
* On a skill that is highly valued in my current job?
* On a skill that I expect will be highly valued in my next job?

I don't have a good answer. Here's what my current plan looks like:

* I have a plan and at least small action steps for whatever feedback I've gotten from my boss and close workers, regardless of whether I agree with the feedback. If I agree with the feedback, this is easy to focus on. Otherwise, it's a way of experimenting with a change to see what happens while showing that I'm taking them seriously.
* I strive to be attentive to my perennial weaknesses (e.g., coming off as brusque) and follow up in scenarios where I may not have done well.
* Up to 20% of my time working on my weaknesses. Sometimes these are the perennial ones (especially if feedback suggests they are problem areas again). At other times, I'll tackle a common practice that I've never been able to implement (like [Obsidian](https://obsidian.md/)).
* The rest of my effort goes to learning to better do what I love and excel at.

In short, I mostly work on amplifying my strengths, while being conscientious of my weaknesses.

# Difficulty of discerning wisdom from style

Finally, I've learned that people are very bad at distinguishing their style from best practice.

At one point in my career, I joined a company where many developers, including those who I worked closely with, were deeply into object-oriented design. And I wasn't. While I certainly appreciated the value of a good class, I wasn't an object-oriented purist. They didn't want to engage in a conversation on the topic, though, and I significantly altered my style (or who I requested to do my code reviews) to accommodate their style.

Fast forward a couple years, and I no longer worked closely with those individuals. I also became more aware of other schools of thought and realized that there were many professionals who would agree with me. In the years since then, I've largely worked with similarly minded individuals, and my lack of object-oriented purity has never come up.

Looking back, I overestimated the level of experience of those who wanted to guide me down a route of object-oriented purity and confused their preferences for wisdom[^purity].

[^purity]: Looking back, I also wish I had more carefully considered my choice to adapt my style. It may have been the right choice to get along, especially as the new person at the company. But that preference led to some unfortunate expectations at the company, such as interview questions focused on one's understanding of object-oriented design. In hindsight, pushing against that expectation, as uncomfortable as it would have been, might have been better for the engineering culture and hiring high-quality candidates.

In another case (before I was a manager), I had a reviewer write about me that "my people skills limit how 'managerial' my role is, both in managing people and in interacting with other teams." Ouch! And yet within a couple years of that review, I was managing a small team, getting glowing reviews from those who reported to me, and architecting critical software systems that had an eight-figure impact on the company.

> He really cares about his team members as people and is genuinely open to working with them through their individual concerns and goals.
>
> Anonymous upward feedback on Alan's top strengths

Did I radically overhaul my approach to dealing with people? Was the reviewer wrong? What happened?

_No, not exactly, and circumstances changed._

I certainly continued to work on my people skills. I got bit smarter about when "What do you think?" wasn't really an invitation to share my opinion. And I got a bit better at phrasing questions so they wouldn't be heard as having critical implication. But I don't think much changed in my actual style -- certainly nothing significant enough that anyone commented on it, for example.

Instead, I think the reviewer confused his style (which definitely conflicted with mine) with my broader people skills. I also strongly suspect that the extent to which I could have been an effective manager under him was indeed severely limited.

_One final caveat_: My point in both these stories is not "I was right, ignore feedback." In both instances, the feedback was valuable, and I was better off for having it and growing from it. But in both cases, the feedback wasn't a full view of the situation. Had I simply taken the feedback and said "Ah, I too must be an object-oriented purist," I would have stunted my growth and limited my engineering abilities.

# So what

As with many complex issues, there aren't many silver bullets here. But here are a few of my takeaways:

* Be quick to learn new skills from 0 to 1 whenever possible. And beware [the Dunning-Kruger effect](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect).
* Grow skills from 1 to 2 when convenient.
* Learn many variants for core skills.

The purpose of the last point is to achieve mastery of the concept independent of the implementation. By the 5th or 6th software language, the concept of a loop is really clear, even if one language has `while` and another doesn't. It also makes compare and contrast far easier -- how does C++'s value vs. reference system compare to the de facto reference approach used by many modern languages? How does having a `const` keyword change how one programs? Or, in the case of JavaScript, how does it turn out to have a `const` keyword in an object-based language that doesn't prevent the object from being changed?

_Finally, think deeply about the feedback you receive, and seek out feedback from multiple thoughtful sources._
