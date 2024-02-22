title: Recognizing Expertise
subtitle: Madman or genius
date: 2023-09-18
category: practices and principles
tags: management, knowledge, uncertainty
status: published

Suppose someone sends you a beautifully hand-crafted letter[^email].

> I can double your company's profits in six months. My going rate is $100,000 per month.
>
> _Joe, an expert in the field of quarks, charms, and particle entanglement._

[^email]: Or an email. But we know in this day and age that all strange email is a scam, so that doesn't work for this illustration.

What would it take for you to hire Joe?

First, we'd do some back-of-the-napkin math to see how long it'd take for doubling our company's profits to pay off a $600,000 bill. Let's assume that hiring Joe would be a good deal and that the business has the money -- it won't destroy our cash flow or anything like that.

That brings us to a second question: Is Joe legit? Does he really know how to make the company profitable? Is he trying to scam us? Or perhaps, worse yet, he's just deluded -- a madman.

# The dilemma

So what now?

* We could look for signs of credibility. Does he have a university degree? Or some training certificates? Do other experts recognize his knowledge in some way?
* We could ask about past results - has he done this sort of work in the past? What kind of results has he had?
* We could rely on our own experience. Are have we seen this practice anywhere? How did it work out?
* We could ask our business connections if they've heard of particle physicists increasing business profits; have they hired anyone like this?

References are a bit tricky these days. If Joe is at all smart, he'll likely cherry-pick contacts who think the world of him. And then there's the question of the stranger's judgement: Would they actually recognize business-revolutionizing particle physics?

Self-experience is clearly a better approach -- after all, most of what I know has been taught to me by others. And I'm still striving to [learn]({filename}/pages/unlinked.md), which usually means either:

* Learning from others in some form (e.g., book, video, conversation)
* A mixture of staring at the computer screen and intermittently bashing my head against the wall, trying to figure why the computer is undertaking some undesirable and bizarre behavior.

### Credentials

Certification is a tricky beast. On the one hand, it's a fairly objective[^fair] way to evaluate someone's expertise. On the other hand, there are a few problems:

[^fair]: Not be confused with _objectively fair_.

* Plenty of accused criminals and scam artists have excellent qualifications. See, for example, [Elizabeth Holmes](https://en.wikipedia.org/wiki/Elizabeth_Holmes), [Bernie Madoff](https://en.wikipedia.org/wiki/Bernie_Madoff) , or [Sam Bankman-Fried](https://en.wikipedia.org/wiki/Sam_Bankman-Fried).
* In many fields such as software development, self-taught individuals are just as skilled if not more so than accredited ones.
* There can be quite a gap between an individual's academic ability and their day-to-day performance. My scores on a number of graduate school engineering exams were significantly better than my actual understanding of electromagnetic fields.
* The lack of certification doesn't say much -- in many software fields, many qualified people can do the work, or learn to do the work (thanks Google + StackOverflow) without ever earning the credential.

But the big problem is this:

_Knowing how to do something right isn't the same as knowing the right thing to do._

Huh?

Let's say I have a problem and a certified AWS expert. The AWS expert is likely to tell me that the solution to my problem is to use AWS. They'll likely give me exactly the right way to solve my problem with AWS.

But is that the right solution for my company? Should I commit to having a permanent AWS expert on staff? What ramifications will that have on the company's ability to update the product? Or make it accessible in remote locations?

Perhaps the problem could be solved differently with a chemist. Or by marketing acquiring a telegenic eight year old and livestreaming her using the product. Or by overhauling the manufacturing process.

And certification says nothing about a person's ability to assess a problem in the broader business context and make a good decision.

For example, I've seen fantastic database designs -- that didn't match the company's desired development pace, align with the kinds of employees that the company could hire, or give the kind of product flexibility that the product managers wanted. The designs were not a bad solution in a vacuum; they were just a bad solution for that company at that time.

# So what

First, signals do matter. They aren't everything, but a person's credentials, references, and communication skills all matter.

> What would it take for this to work?

Second, it's worth taking even crazy ideas and thinking through "What would have to happen for this to work well?"

For example, one of the major sources of delay in shipping code to production is code reviews. There are good reasons for this -- ensuring quality code, knowledge sharing, preventing malicious code injection, etc. But it's still a bottleneck. And the easiest way of improving the situation -- getting developers to do reviews sooner -- is highly disruptive to developers' work habits.

So what would it take to do code reviews after code was shipped to production rather than before? Feature flags? State-of-the-art code scanners? Every line of code covered by a test? Rigorous static typing and API contracts? Doubling software salaries and only hiring the best of the best? Some combination? The answer probably varies by industry[^heart].

Or as someone once said: You don't get world-class results by following industry-standard operating procedures; you get standard results. If you want non-standard results, you need non-standard practices[^until].

[^heart]: I'm not sure I'd ever want this approach with, say, my pacemaker.

[^until]: At least until they become the new industry standard, at which point it is time to innovate again.

# Soapbox bonus

A crafty owner might try to carefully negotiate a results-based contract with Joe. "We'll pay you $600,000 in six months if the profits are at least double, plus 5% of any profit gain beyond that."

Joe, knowing that business results aren't guaranteed, is likely to want guarantees. "Okay, but if you don't do exactly what I tell you, then I get my $100,000/month regardless of results."

Of course, the owner probably isn't comfortable with having to do everything Joe says to avoid invoking the fallback clause. And this brings us to the fun topic of structuring incentives, which shall have to remain to consider at another time.
