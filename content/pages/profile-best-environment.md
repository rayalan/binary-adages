title: My Best Environment
subtitle: Alan Ray Profile
status: hidden
slug: profile-best-environment-hidden
layout: page

[TOC]

> Productivity.  The amount of work Alan is able to put out would be incredible if he was a rank-and-file employee relatively free to focus on tasks.  The fact that he's tied up at least half to two-thirds of his time in meetings (if not more, some weeks, looking at his calendar) and is able to _still_ be highly productive is mind-boggling.
>
> _Peer feedback on Alan's strengths._

While I pride myself thriving in all sorts of environments[^range], I recognize that I do my strongest work when a few factors are present:

[^range]: And in fact, I've done so -- I've established new teams, run solo projects, built up teams to maintain mission-critical systems, and established architectures and practices for entire engineering departments.

# Commitment to pragmatic long-term excellence

I build software, complete with systems and processes such that it:

* Delivers frequent rapid value.
* Achieves durable long-term efficiencies of scale

I write elsewhere (e.g. [here]({filename}/pages/about.md)) about my approach to software. But for this discussion, I'll highlight four principles:

1. That which is done automatically and frequently will be correct (c.f. DevOps principles)
2. Undelivered software doesn't have any value. (c.f. [see the time value of money](https://www.investopedia.com/ask/answers/032715/why-does-time-value-money-tvm-assume-dollar-today-worth-more-dollar-tomorrow.asp)).
3. Most software design plans are [gold plating](https://en.wikipedia.org/wiki/Gold_plating_(project_management)): They aren't really going to be needed. The vision will change or the business priority will change or the customer will want something different.
4. Some long-term planning and investments are essential to sustaining quality software at economical prices.

The first three principles push toward an [Agile style](https://agilemanifesto.org/principles.html) of development. I don't mean any particular system Agile development -- some of those systems, in fact, are so rigid that they undermine the very principles of Agile.

But left to their own devices, the first three principles repeatedly produce locally optimal solutions that constantly increase the amount of tech debt. The increasing tech debt decreases software velocity and quality -- each improvement, developers do the fast thing to make the change, increasing the complexity and brittleness of the system.

While there are make-shift solutions such as hiring more people, these approaches generally have diminishing returns (c.f. [The Mythical Man-Month](https://en.wikipedia.org/wiki/The_Mythical_Man-Month)). While more people can do more, they are also harder to coordinate and can make a bigger mess.

Often the pain and development friction results in limited efforts to correct the situation. For example, one of my favorites is a series of uncoordinated short-term initiatives to introduce a new technology or approach. Each time, the technology is the way of the future and will have an incredible return on investment after the initial one year or two year investment. One of these "investments" is introduced every year or six months, each superseding the previous one. The result is that the company continuously invests in the long-term while reaping none of the benefits. Instead, the continual build up of different technologies mixed together often reduces the benefits of each individual choice while slowing developers down even further (c.f. [the lava flow anti-pattern](https://exceptionnotfound.net/lava-flow-the-daily-software-anti-pattern/).

Worse yet, management is unaware of the reasons for the problem. They see the consequences (development velocity is low, quality is low), but not the long-term causes of the problem (e.g. tech debt, inadequate tooling, poor practices, inadequate mentorship) -- see also the [Iceburg of Ignorance](https://thinkdev.org/blog/the-iceberg-of-ignorance). Sometimes management doesn't really understand how software development works or how an agile-like risk is supposed to reduce risk. The result is a lot of top-down initiatives such as reorganizations, new rules about quality, arbitrary deadlines, or additional reporting about project progress.

The solution is an engineering culture that is:

1. Pragmatically focused on short-term projects.
2. Resourced to invest in necessary long-term efforts.

> Just because your car burns through oil a bit more often than it should, does that mean you'd buy a new car?
>
> _Alan, on why rewrites aren't always the right solution._

So I do my best work in this in-between space -- I'm not an ivory tower architect, wanting to develop the perfect solution. Once when arguing with a developer about the necessity of a rewrite, I made the comparison to oil changes: Just because your car burns through oil a bit more often than it should, does that mean you'd buy a new car?"

Sometimes, yes, if the car is really old or unreliable, replace the car. But often it is a lot more economically viable to drive that old car around and periodically add an extra quart of oil.

On the other hand, I also want the freedom to invest in significant long-term engineering initiatives. I am not nearly as effective when I'm constantly fighting to justify every engineering initiative against the latest customer-facing improvement. I've seen places where executives under-invest in engineering processes and practices, creating a situation where engineering quality increasingly falls behind industry standards[^industry].

[^industry]: Falling behind is bad, but for companies whose success is dependent on state-of-the-art engineering, the problem is even worse -- cutting edge engineering isn't found by following standard practices; it is found by blazing a trail and improving on them.

And at times, I amplify the problem like this:

* First I talk to other leadership and they all talk about how import certain business results and customer-facing outcomes are.
* Then I work hard to make plans that support those initiatives and scale back my own engineering initiatives to try and create space.
* Then the executives, assuming that I'm asking for more than I need, make further cuts.
* Now engineering initiatives are badly under-resourced, and (unsurprisingly) often produce corresponding results.

I prefer to treat my coworkers, even those in other departments, as partners. This means my default stance is to negotiate in good faith, asking for what I actually need, not inflating my ask so that when I'm negotiated downward, I get what I ask. (Part of this has to do with calibrating what words like "essential" and "critical" and "important" mean, see LINK.) And yes, this approach is terrible game theory when others are negotiating with a different strategy.

So while I'm glad my coworkers bring a broad array of different strengths to the table, I really thrive when there's a deep desire to both figuring out how to deliver a lot of value as often as possible as well as to establishing sustainable engineering practices.

# Straightforward communication

I do my best work when I clearly understand the world around me: The business objectives. The technical realities. The financial constraints. The legal requirements. The ambitions of my coworkers. Any hard timelines.

> Compassion and he is driven to serve all well. Alan will hash it out til the cows come home so he has clarity and then he will make decisions based on quality for the entire company not just one aspect of a team.
>
> _Peer feedback on Alan's strengths_

However, when what is said doesn't align with the actual priorities, I can waste a huge amount of time and energy. Here's a real life example from a while back:

### "Prioritize user experience"

At one company, the executives had a big announcement about how we were going to prioritize user experience. And everything that was customer-impacting needed to go through a UX-approved process. And Kelly would be the UX person held responsible for all the ways customers interact with the company -- effective immediately.

Okay. The decision had been made, and it was time to [commit and support](https://en.wikipedia.org/wiki/Disagree_and_commit) this direction[^kelly]. As part of my work, I had a lot of influence over technical processes as well as being directly responsible for a number of systems that interacted with customers. So I set about figuring out how to implement this direction.

[^kelly]: From the start, it was clear this situation sucked for Kelly. It was a massive responsibility over which Kelly had very little actual control. The organization needed to develop, almost from scratch, processes, workflows, and culture to implement direction. Kelly wasn't positioned to make those changes, especially when key decision makers were already overloaded with other "higher" priority work. And overall, the implicit expectation was that by and large, the rate of software delivery would continue more or less unchanged.

Now the company had a lot of touch points with customers, many of them indirect.

* Upfront contact points such as applications and websites.
* Backend algorithms that controlled content so any change to those systems impacted customers.
* Systems that supported customer service, so changing those systems would impact how agents could help customers, which would change the customer experience.
* Billing systems which impacted the customer experience when they didn't pay for whatever reason (e.g. expired credit cards).

So I started with the basics:

- I repeatedly reached out to Kelly to find time to learn about how he wanted to handle a variety of these situations.
- I proposed technology and process experiments to facilitate UX seeing what customers saw and being able to directly update it without going through development. Separate plans looked at facilitating rapid prototyping with actual customers as well as streamlined A/B testing.
- I briefed my team on the change, listened to their pushback, and started working on necessary changes to support my team. For example, many teammates were concerned it would interfere with the speed and quality of our work, which had been major criteria by which performance was judged. So I made sure my boss knew about the anticipated changes to throughput, told my team I would adjust my expectations, and starting making sure there was a document trail in case there was later pushback.
- I put together a proposal to start training the development team on basic UX principles and outlining scenarios when my team was authorized to autonomously make a change. This was particularly important because the company frequently places where the existing user interaction was just wrong -- the link went to an outdated page, the data loaded as 'n/a', etc. Almost any change would have been better than the status quo.

(Now a reasonable reader might suspect that I'm being overly literal and a bit pedantic with this interpretation of executive direction. Surely they didn't mean this directive so expansively. I certainly thought so. But when I sought to clarify what we meant by _"everything that was customer-impacting"_ and pointed out many of these complexities, my boss told me that we meant everything and all these scenarios needed UX approval. All right, then, supporting this direction and making sure Kelly wasn't left hanging was an urgent priority.)

_And I promptly ran into a brick wall._

* Executive support and interest waned within a couple weeks.
* Kelly (and the rest of the UX team) was far too busy with their current work to worry about this added responsibility or new processes.
* Engineering teams were perfectly fine sticking with their current processes.

And after a few months, I realized that all my work in this area was a waste. I'd held up valuable changes because they needed UX approval that UX didn't have time to get. I'd wasted time writing proposals and soliciting feedback. I'd created unnecessary angst on my team about a change that wasn't really. And my attempt to be a team player by supporting this initiative had probably backfired because I'd been more of a pain by pushing forward than if I'd just ignored it. Ouch.

One of my takeaways from this experience is that I do much better when I'm given the actual priorities. For example, a boss who said: "Yes, this is the announced new initiative, but it isn't a priority for me, and I'm not going to hold you or your team responsible for any changes to process until we've worked out a way forward. I know you touch a lot of customer-impacting systems, both directly and indirectly. Your team adds significant value by rapidly fixing the problems you come across, and making things better than they were before. Please continue to do so using whatever process you see fit."

# Space to maneuver (and a willingness for necessary structure)

Much of engineering proficiency comes down to two questions:

1. Can you create the necessary process?
2. Can you eliminate the unnecessary process?

As an example of this ideas, I once worked at a company where upper management would only look at project status through the official project manager. And any project that concerned upper management in any way had to be visible to them.

> Alan uses his analytical mind to go after process questions, building his team, and finding ways to push us forward as a larger team.
>
> _Peer feedback on Alan's strengths._

Now on the one hand, this makes sense. Leadership needs visibility. And a unified project manager makes sure everything consistent. But it also meant that a certain significant amount of friction was baked into every project. Worse yet, the cards didn't really have the information that upper management needed or cared about. For example, the cards didn't provide the overall project status. In many cases, a [hill chart](https://www.hillchart.co/blog/project-management-chart-why-you-should-use-a-hill-chart/) was far more what management needed -- a view that our project management software didn't trivially do.

And as is common, engineering time was an incredibly scarce resource. And officially, the company agreed and was committed to buying whatever tooling were needed to streamline the developer experience.

 Yet the engineering team was stuck filling out inadequate Jira cards because management could not be bothered learn another software system, or even to sit down and talk about what they actually needed from the project tracking system. Additionally, two important messages were sent:

 * Management was more important than engineers because managers couldn't be bothered to be part of dynamic iterative innovation. Only if engineering had a rock-solid proposal could management perhaps be bothered.
 * While the company talked a lot about bringing joy to the developer experience, when rubber hit the road, manager convenience mattered a lot more.

In this case, the inability to alter the project management system made it very difficult to create a better process for developers.[^process]

[^process]: For projects that didn't involve upper management, my squad actually found hill charts and an ultra-light weight project manager that integrated with pull requests was far more effective, proving that it was possible to do significantly better than the company-wide solution.

There are lots of good reasons not to make any particular change at any particular moment -- available funds, limited return on investment, lack of time, too much change already in flight, etc. However, as the inability to make change moves from a situational limitation to a permanent condition, I struggle. I really thrive in a place where I can streamline engineering by changing systems and process -- and serve not just engineering with those improvements, but also those who interact with engineering. Sales, marketing, product, customer service, user experience -- all these groups benefit from better ways to interact with software development.

# Relational connectors

> Highly communicative and easy to talk to
>
> _Upward feedback from Alan's reports_

My style is to build strong, deep working relationships with coworkers over time based on candid conversation, shared goals, and working alongside each other. I ask questions, I learn, I propose ideas. I have my ideas and conclusions examined and challenged. And I push others to refine their views as well.

> Communicating critical information. I think I've seen this strength the most through encouraging group discussions in Slack channels and things you share when you speak up in meetings. Even before I was working on your team, the thing that stuck out to me the most about you is your ability to analyze a situation thoroughly and communicate the most critical pieces of information effectively.
>
> _Upward feedback from Alan's reports_

While this style has enormous strengths, it has a few holes:

* I'm not great at establishing team bonds or promoting casual conversation.
* I generally don't read emotions quickly with strangers or in large groups.
* I'm rarely one of those people who instantly connects with others.
* I tend to strongly irritate people who are uncomfortable with their ideas being challenged, especially when I don't know them well.

What I love to have on my team or around me is people for whom relational connection is natural. They will naturally build bridges and connect me more quickly to others, especially if I enable and support them. For example, on team, one of the developers would put together weekly drawing contests. And I made it a priority to encourage them in this and to make sure that the team knew that I supported taking that time each week to have fun and get to know each other.

> Open-minded
>
> _Upward feedback from Alan's reports_

In another case, a developer joined the team whose style was much more social, and the team added a few minutes of social banter to our stand-ups. Eventually we switched to written recaps of what we'd done and focused the standup a bit more on socializing and technical challenges.

In both cases, having more relationally-oriented individuals helped the team bond, and I recognize that I thrive when I have people like that working closely with me (e.g. as a close peer or report).

# Advocates

I hate self promotion. It seems arrogant and cocky -- my work should speak for itself. And every moment spent on communication is one moment that I'm not doing I do best to create value -- analysis, design, engineering, mentoring, understanding the customer needs, etc.

I sometimes joke that engineering follows the [Heisenberg uncertainty principle](https://byjus.com/jee/heisenberg-uncertainty-principle/) -- the more you know where the project is at, the less momentum the project has.

On top of that, I have a good memory and tend to be annoyed by redundant communications -- as a listener, I should bear significant responsibility for active listening, especially I'm given a way to look up the information. Likewise, I want to simply tell it as is rather than massage the message for particular audiences.

I know the above isn't the whole picture. Non-technical audiences shouldn't be buried in technical detail, although a few accessible details to help communicate the complexity of the problem space is golden. Executives have a different set of concerns than customer service or managers or engineers. And nobody is a mind-reader -- most of the complexities of good engineering are unseen unless someone speaks up -- someone needs to explain how the software development resulted in reduced errors, increased customer satisfaction, and lower maintenance costs in addition to bringing in revenue. Everyone wants to be reassured that their interests are being looked after.

> Alan is very straightforward and unyielding in ensuring that communication through his team is strong. He is always thinking about that, as well as having the foresight to think through the entire process to ensure the process is good as well.
>
> _Feedback on communication from Alan's peers_

> Alan's sprint reviews were the best things going in tech visibility until just the last few weeks, when other SOs began to adopt a similar rhythm.
>
> _Feedback from Alan's boss_

While I'm good at communication, it isn't my first joy and I'm known to forget how much people forget or how much trust decays without active outreach. Or I'll simply assume that everyone is keeping an eye on the error rates and know that my team has been reducing them by 200% over the last month.

And that's where having advocates for my work who enjoy promotion and sharing are fantastic. By letting others advocate for my work, my natural style of good communication plus great work becomes great communication and great work.

# Realistic expectations

I naturally have high expectations. I'm also hyper-responsible to follow-through on commitments I make. And I naturally absorb vision -- when someone says "The next move is ship an amazing product that triples our revenue and doubles the market share," I instantly start thinking everything that involves -- better error handling so customers don't have to call customer service, better metrics so developers know about problems ahead time, revamping the billing system to be able to handle the load, and so on.

All too often, I grab onto a whole complete vision, when the actual intent is more of a initial foray or perhaps to inspire rather than set an actual goal.

As a result, it's incredibly helpful to have people around who can level set expectations for me and say "Actually, I don't think we need to (x) or (y) because the actual goal is (z)."
