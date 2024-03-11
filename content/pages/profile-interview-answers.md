title: Answers to common interview questions
subtitle: Alan Ray Profile
status: hidden
slug: profile-interview-answers
layout: page

[TOC]

There are some great interview questions out there. This page gives employers my answers to some common ones[^common] before the interview[^interview].

[^common]: I have mixed thoughts about the standardization of so many interview questions. Done right, it helps everyone be on the same page -- employers get thoughtful answers that tell them what the employee will be like, and employees get to prepare answers that best represent them. The dark side is that it may favor employees with certain skills (e.g., recalling prepared stories under pressure, viewing their experiences as dynamic stories) that aren't really relevant to the job.

[^interview]: Here's an outline for a blog article:
  - At one point, I saw understanding how people thought on their feet as one of the main points of interviews.
  - Over time, though, I've shifted my perspective to caring far more about how the person sees the world, how they act in a variety of situations, and what they are capable of.
  - In this view, experience and knowledge are far more important signals about who the candidate is than ends in and of themselves.
  - While quick thinking on the fly is a valuable skill, especially in crisis situations, it isn't the only skill that matters.
  - The ideal interview involves accurately understanding what the candidate brings to the company (both strengths and liabilities) and whether the company is a good fit for the candidate.

# Past behavior

_Past behavior is the best predictor of future results, after all._

I love these questions when I have enough time to think of the right stories and share enough context that the makes sense.

## Tell me about a time when you've made a mistake.

_Alternatively, tell me about a time when things haven't gone according to plan._

Here are three different stories of when software projects have gone badly haywire under my watch.

### A tough technical decision

I was project manager and architect on a project to replace a brittle legacy in-house system with a modern third-party solution. Many of the project requirements were non-functional requirements -- easily modifiable, maintainable by any developer rather than specialized database experts, testable in a non-production environment, able to make incremental changes without impacting all users -- the sorts of usual goodness one wants from software systems.

After investigating the options, researching the existing code, listening to coworkers, and doing a few prototypes, I had a plan. The basic idea was to build a microservice with its own standalone data storage. This microservice would interface with the 3rd-party solution, which would do the bulk of the work, as well as our other systems. This approach allowed the microservice to isolate the solution from everything else, and by virtue of having a well-designed microservice, we'd pick up the non-functional requirements along the way.

Now the company had a brilliant database architect named Kaden. And he had a vision for the database as a well-connected, well-designed monolith -- a single database fully interconnected with foreign keys. The legacy system already had tables in the database, and the new solution could designed to be compatible with those tables. (For context, Kaden was also the original designer of the legacy system, and it was very much his baby.)

In a vacuum, Kaden's solution wasn't a bad one. It might have even been the superior technical vision. But it required steps that the company wasn't prepared to make. For example, it required hiring a large number of SQL experts to help write the supporting functions and triggers as well as ensure data integrity.[^sql] Furthermore, many of the non-functional requirements, such as being easily modifiable or maintainable by developers, simply could not be met with this approach.

[^sql]: The reasons why this was true are particular to this company and beyond this story.

I went back and forth with Kaden about the direction for weeks. I steelmanned his approach. I presented my understanding of his approach and its advantages to him to see if I'd properly heard his idea. (I had.) I presented my concerns and asked if I was misunderstanding something. I asked if there were consequences to my approach that I wasn't seeing. I stalled on making a final decision -- I hoped more time would help Kaden come around or perhaps one of us would figure out a third way. I had my team do a prototype of my approach with an emphasis on finding any difficulties or unforeseen problems -- the prototype suggested that my approach would do exactly what I expected.

After all of that, the choices seemed clear:

1. Isolate the implementation behind a microservice, achieving the non-functional requirements while also picking the easier approach to implement.
2. Embark on an approach that might eventually result in a superior result, but would add significant risk and complexity to the project while also making it very difficult if not impossible to achieve many of the project's goals.

Technically, the choice was obvious. As a project manager, the choice was obvious. But Kaden remained unmoved, persuaded that option 2 was the better choice.

_I chose option 1._

#### The aftermath

The project was a brilliant success. The architecture did everything I expected of it and more. Internal departments were delighted. Customers barely knew we'd made a change. I won awards!

And throughout the project, I went out of my way to acknowledge the value of the legacy project and Kaden's contributions in bringing the company to where it was. It's never easy to see one's work replaced, and I wanted to highlight the value of Kaden's contributions.

_But Kaden and I never figured out how to work together again._

I don't think he ever understood why I made the choice that I did. I suspect he saw my choice as not appreciating his database expertise. And I don't think he appreciated how much the company benefitted from the new capabilities, such as testability in staging or easy modification. Rather, I think he saw how I'd made his vision of a unified database far, far more challenging -- perhaps even impossible. And I think he was waiting for me to come around and agree with him that his vision for a centralized database was far better than a distributed set of databases.

My attempts to pull Kaden into other projects that would take advantage of his expertise fizzled out. And those projects were worse off for his absence. On more than one occasion, good proposals that would have helped developers move faster died on the vine for one reason or another. I can't help but think that Kaden's support would have made some of them successes.

Looking back, I'm torn. On the one hand, I made the right choices for the company and what I'd been tasked to do. I tried hard, really hard, to find a way to bridge the gap with Kaden. Maybe that's more than could be expected of me.

On the other hand, the long-term relational breach really hurt development. Would it have been better to pick a subpar solution that significantly increased the project risk, made development far harder, and decreased the project's success for the sake of long-term relationships?

Was there something else I could have done? More time talking it through? An award for Kaden? A token or gesture of some sort?

Or perhaps my view on this story is warped. Maybe I wasn't as open minded and charitable as I present myself. Maybe I didn't really understand Kaden's view or dig deep enough into his arguments.

In the end, I don't lose sleep over the technical choice. It was the right one. But I do spend a lot of time pondering how I could have won over Kaden. And I don't have any good answers.

### That would have paid for my college degree!

On my first project as an official project manager, I was tasked with overhauling a complex system that deeply impacted customers, several departments, and a number of technical decisions. According to the way teams were supposed to work, this kind of work "should" have input from user experience practitioners. But the UX department didn't have any resources to spare. So I did what I thought any good project manager should do -- I pushed the critical resource shortage up the chain. Eventually, I got told that "it wasn't my job to say how UX resources should be allocated" (oops, maybe I got a little too pushy?).

But as a consolation prize, leadership suggested hiring a UX consultant firm. I knew nothing about such matters, so I basically let a coworker (who knew this sort of work) coordinate with leadership to get all the details worked out. The firm came in, did a bunch of interviews, asked a bunch of questions, and then went away for a few weeks. When they came back, they had lots of fancy UX diagrams explaining how to structure the problem. For their trouble, they got a paycheck that would have covered tuition along with room and board for a degree back when I was in college (and I'm not that old).

So how useful were those diagrams? A complete waste. The diagrams basically parroted back to us what I already knew, just in fancier diagrams. They didn't break the work down into iterative pieces. They heavily suggested that the first implementation needed to be far more complex than it actually did. And they weren't terribly readable, so it was hard to use the charts to share a project vision with others. After a couple weeks, the charts disappeared into someone's office and never resurfaced.

But the money ... it wasn't a complete waste. Instead, it provided me with a very expensive lesson about project management:

* _Make problems visible early._ I did the right thing by pushing the project risk up the chain. Management did need to know that the project lacked adequate resources.
* _I can do user experience work._ I saw UX as a field that required special talent -- expertise that I completely lacked and shouldn't try to acquire. In hindsight, I already had the skills at that point in my career to make the right choices when it came to system design and information architecture. But I didn't trust myself because I saw UX as too "other." In the end, I'd end up making many of those decisions myself anyway, based on input from my team.
* _Money can be both available and not available._ Sometimes money is available for certain expenditures (like hiring consultants), but can't be easily transferred where it would be most useful. For example, I would have loved to spend the same amount of money to pay one of the company's user experience practitioners for overtime for a few months. But I don't think the company would have swung for that approach, even though the money spent would have been the same and the outcome far more useful for the project.
* _Don't delegate to the point of abdication_. Because the people writing the contract had far more experience in this area and were busy -- and I felt inadequate, I didn't ask the questions I should have as project leader: What was going to be the end result? Why was it going to be useful? How would this address the concerns I raised? Could the work be structured more incrementally and perhaps aborted if it wasn't proving useful?
* _Be quick to acknowledge missteps_. Because I had approved spending the money, it was really hard for me to admit it wasn't a productive expenditure. By not being more vocal, I implicitly sent the signal that this kind of expenditure had been productive.
* _Even for executives, spending money is a form of commitment_. In the weeks before the consultants were hired, I was struggling to get adequate time with the executives to understand their concerns and get their input on the project. But once the check was written to the consultants, the executives made time to be available to the consultants. I'd been aware of this principle from sales, but I anticipated that creating and launching a six-figure software development project counted as full commitment. In hindsight, the executives likely did not see the salary cost of the project as a real commitment -- that salary was going to get paid no matter what work the developers were doing. But the check to consultants represented a different kind of expenditure.
* _Companies view money differently than individuals._ Making this kind of misstep with one's personal finances could likely be a catastrophe. But for a business expecting to spend high six figures on a project, even this kind of snafu is basically a rounding error.

Looking back, I still view the whole effort to be a failure on my part. But I also view it as a very expensive personal education in project management ... just one that doesn't come with a diploma.

### Cut twice, measure once?!?

On one project where I was project manager and architect, my team encountered an incompatibility around discounts between the old pricing approach and the new one. There were a number of ways of resolving the problem, but several resolutions would have shorted customers by a small amount of money. Another set of resolutions would have been very expensive for the company, as even though the amount per customer was small, the large number of impacted customers meant the financial total was non-trivial. To complicate the situation, there were additional requirements, such as being auditable by our finance team, easily explainable to customers, and non-disruptive to customer service.

In the end, I designed a workaround that met all the requirements, didn't hurt the company, and didn't defraud customers. However, the behavior wasn't well integrated into the system, and we didn't have good test coverage around the behavior. The project launched and all was well.

Fast forward many months and I was leading the team maintaining the new system. There was an urgent push to roll out some new functionality so that the company could rapidly bring some changes to market. Thanks to hard work by the team and my strong architectural design in the initial project, the team was able to complete the work in record time.

But the pre-launch testing didn't properly test for whether or not the workaround for discounts was working. It wasn't, of course -- otherwise this would be a story about what went right. And in the few hours it took the team to catch the problem, the system gave customers enough in additional discounts to offset the financial gains of launching earlier than expected.

Because of the nature of the discount and the way that billing worked, the loss was basically a sunk cost -- attempts to recover the money, even if legal and technically possible, would have done significant long-term damage to the company's reputation.

And then I had to write up a summary recap of what happened, acknowledge that it was my fault twice over (once for the initial problematic architecture, and secondly for missing this behavior in both development and testing), and share that with company leaders.

Looking back, I still mull over what was the right answer.

* More testing? Obvious in hindsight. But the testing on this system was light years ahead of what was previously in place, and the company didn't place much value on more thorough testing. We could easily have spent more on testing than the was lost by this mistake ... and still made the mistake.
* Pushed harder for a better solution in the initial project work? The discount design was clearly a weak spot in the architecture. Maybe I should have argued harder against some of the design parameters to allow for a better approach.
* Paid more attention to the work as the new functionality was developed? I knew that the discount calculation was a weak point. Perhaps I should have more directly intervened, reviewing the work or double-checking with testing. Then again, I was often encouraged to delegate more freely, and the team had done similar work without problem before.
* Could a different error handling have caught this scenario? I built a number of failsafes into the system such that unexpected cases resulted in no-ops that required human review. During the initial work, could I have designed a failsafe that would have applied to the later updates? Then, instead of granting the discount, the system would have gracefully waited for human intervention on problematic accounts. Or perhaps delaying billing would actually have been a worse outcome?
* Was I being too uptight in ensuring that customers got what they paid for? Was there a less rigid approach to the problem that would have still been fair to the customers but not so prone to error?
* Was this the best of all possible worlds? Both the initial project and the new functionality shipped rapidly. Nothing illegal happened; no customer was injured or inconvenienced. The mistake, while expensive to the company, was a one-time error. And it wasn't that expensive compared to alternatives (e.g., paying the team for several months to develop better tests). Maybe this is what successful development looks like?

I actually lean toward the best-possible-world hypothesis, but that seems a little self-serving because it means this time something didn't go as planned, it was actually a success and not a mishap.

## What would others say about you?

One VP wrote this about a successful project shipped that, had it gone wrong, could have critically damaged the company's reputation:

_"Thank you for leading the such-n-such[^such] project with attention to detail while always understanding and moving toward the vision! Your commitment to excellence has infiltrated the team, and their desire to serve our members and their co-workers is exemplary. Thank you for leading and delivering a better such-n-such solution."_

[^such]: Project-specific details anonymized.

### Areas of growth

Broadly speaking, my bosses, my peers, and my reports give glowing feedback -- some of which I show off below. But often the _"What do others say about you?"_ question is as much about self-awareness of weaknesses, struggles, and areas of growth. So let me share some of that feedback first:

#### What would you like Alan to start doing as your manager?

_Answer: "As I’ve been gaining confidence in my role, it’s been nice to have more affirmative feedback and less critical, but now that I’ve gained a decent amount of confidence, I think I can handle some more critical feedback."_

Commentary: I'm actually really proud of this feedback. I have really high expectations, both for myself and others, and for an employee to think that perhaps I've been under-critical is a huge win. It's also a reminder that it's possible to swing the pendulum too far in the opposite direction. I'd like to think that the way I [approach reviews](../my-best-managers) helps to ensure I'm giving consistent, thoughtful feedback that isn't overly critical, but finding the right level of feedback remains a challenge for me.

#### What can Alan improve?

_Answer: "Here is the one thing I might say to you, and I say it carefully because I realize this is actively advising you to be a worse person than you are currently, IMO. I think your tendency to make logic-driven decisions is perhaps not shared universally. I don't think you play politics in this company-that is, I don't think you trade favors; instead you let the most logical/best ideas win, and attempt to shoot down inferior ones. I hate saying this, like a lot, but you might consider, sometimes, enacting/allowing ideologically inferior ideas/practices to thrive, or trading favors, when it would prevent someone else in the company from becoming deeply unhappy with you. I know, that's despicable advice, and honestly anathema to what you stand for and what I value in you...but I think politics are played in the upper levels of this company, and you are a peer of theirs. Politics is a game of concessions, and you may have to concede more often."_

Commentary: This feedback is pretty apt at capturing both my strengths and how they can simultaneously be a liability.

_Answer: "I think Alan would do well to focus on streamlining his communications.  At times his work (e.g. Confluence pages, emails) could be cut by half (or more) in length to make the topics more understandable."_

Commentary: It's not lost on me in the middle of a (_checks word counter_) 5000+-word document that I still aim first for thoroughness and nuanced completeness. I think I've gotten a lot better at writing summaries with links to more specifics -- for example, I've deliberately aimed for short [about](./about) and [profile](./profile-hidden) pages here.

_Answer: "I think Alan at times leans towards being overly philosophical, to the point where it's difficult at times to ascertain what the problem is at hand he's attempting to solve, or what's ""the ask."" I think this can cause him to struggle at times to build a coalition for change."_

Commentary: My natural tendency is to see the whole picture, see the problem, see the solution, and simply dictate the ask and the direction. Unsurprisingly, such an approach comes across as critical and authoritarian. So somewhere along the line I developed a strategy of backing the conversation up - do we share the some philosophical presumptions? Do we see the situation on the ground? Do we see the same set of solutions? Do we see the same tradeoffs for the various solutions? But such an approach certainly can seem overly philosophical. And as one coworker pointed out to me, there are many engineers who just wanted to be pointed in a concrete direction.

So in trying to build coalition with one group of people (those who have genuine disagreements), I'm making it harder on a different group (the one that just wants an answer). I'm still working on finding the right balance between soliciting input, building consensus, and moving with appropriate speed. One tactic I particularly like is to sketch out a decision along with the rationale -- pros and cons. Then post that sketch with a request for feedback about what I may be missing in my assessment. This approach encourages feedback, especially when I'm making a bad decision or missing information, gives people time to reflect, but also avoids bogging decisions down in discussion, especially ones that aren't controversial.

### Boss's comments

Here's how a boss summarized my key contributions for one year:

_"Alan is the tip of the spear. When it comes to working on building strategy into our work, Alan is engaged. This is also true of almost any aspect of Development right now: Hiring, project work, etc.  Alan is fully engaged across the board._

_"Leadership in Crisis.  In times of crisis Alan's clear vision, effective communication style, and deep understanding of our tech make him well suited to take on this type of work."_

_"Architectural vision. Alan has the strategy and a deep understanding of our systems. He is passionate about working toward the vision in a way we need to keep it in our view."_

### My reports' comments

When asked what I did well, here's what my reports wrote about me...

_"His openness to new technologies makes our team an encouraging place to try new tools and improve on our processes."_

_"Alan is very good at making reasonable expectations for how long work will take. While I have a tendency to overestimate how much can be finished in a span of time, he continually demonstrates insight in knowing that tasks often take longer than expected._"

_"He is a great out-of-the-box thinker, able to quickly present alternative points of view on architectural and business design decisions."_

_"Alan is good at delegating work amongst team members. While it can be tempting as a manager to micro-manage tasks, Alan has a knack for assigning tasks in a way that allows the team to be independently productive and have freedom in our work."_

_"He really cares about his team members as people and is genuinely open to working with them through their individual concerns and goals."_

_"In spite of his busy schedule, Alan is highly reachable by Slack and responsive for any questions that come up about work."_

### My peers' comments

Or when asked about my strengths, here are what my peers say:

_"Technical skill.  Alan is among the most gifted folks on the entire tech team in terms of his technical ability and knowledge of his craft._

_"Compassion and he is driven to serve all well. Alan will hash it out til the cows come home so he has clarity and then he will make decisions based on quality for the entire company not just one aspect of a team."_

_"Productivity.  The amount of work Alan is able to put out would be incredible if he was a rank-and-file employee relatively free to focus on tasks.  The fact that he's tied up at least half to two-thirds of his time in meetings (if not more, some weeks, looking at his calendar) and is able to __still__ be highly productive is mind-boggling."_

_"Project management; Alan is great at taking a complex challenge and guiding it to completion. His documentation, goal setting, day-to-day problem solving and communication are all solid, which leads to successful projects with good buy-in from everyone involved."_

_"Analytical skill.  Alan is second-to-none as a troubleshooter, problem solver, and deep thinker."_

_"Attitude, oddly enough. Alan is always positive and thoughtful, with good ideas to offer on any topic. He's tactful in delivery of feedback, and makes allies easily."_

_"Critical thinking. I think Alan is exceptionally talented at thinking about all aspects of a problem and having a good understanding of a situation that is relayed to him. It seems to be easy for him to even grasp the complexity of subjects he is not familiar with at a glance."_

_"Ability to pivot. One of the things we've done a lot of on Alan's team this year is abruptly shift our workflow based on company needs. We've done a complete focus shift multiple times, and while a complete pivot is always going to be painful, Alan has done a good job of making said pivots as painless as possible. I've come out of initial planning meetings knowing exactly what initial work is expected of me[^inject]."_

[^inject]: While this comment reads as a upward review, I believe it was written by someone who was embedded on my team but didn't, strictly speaking, report to me, making it technically a peer review in the review system.

_"Respect for others. Alan is always concerned with the opinions and concerns of his teammates and of other teams within the company. He contemplates all feedback with mindfulness and makes sure that everyone he interacts with is heard and their questions are addressed (even if sometimes addressing the question is "I think that's incorrect because of xyz...")."_

_"He is organized. His teams are organized. Everything is documented and well prepared. Hands down the best project managers that I have ever worked with."_

_"Understanding - He wants to understand the nuts and bolts of everything.  I feel this is how he is so good at managing his projects.  He learns every aspect behind every decision being made."_

_"He recognizes his team in stand ups, high fives and in presentations. Gives credit where credit is due."_

# What accomplishments are you most proud of?

First, my leadership and technical design migrating a [complex billing system]({filename}profile-experience-showcase.md) processing millions from a bespoke in-house system to a extensible, testable, and turnkey solution. Achieving this outcome was not only a display of technical expertise, but leadership in building the team up from scratch as well as changing how multiple departments across the company worked. And winning an award from the customer service department for how well I served them on that initiative was particularly satisfying.

Secondly, cultivating a self-sufficient team that could successfully manage itself for long periods of time. Somewhere I heard that one mark of true success is eliminating the need to do your job because you've trained others to do it. One of the teams I ran got really good at self-management -- understanding the priorities of work, recognizing problems that need to be elevated, stepping in to help one another. It was deeply satisfying to see the time and energy I'd put into establishing the team pay such dividends.

I'm particularly proud of these accomplishments because they are me showcasing the skill. It's easy to be critical of how others run things; it's another to be able to do better yourself. And both of these accomplishments are moments where I had an opportunity to say "If I actually lead the way I think makes good leadership, will it work?" And it's immensely satisfying to see that yes, it will work, and work well.

Finally, one of my bosses -- a long-time developer and leader with decades of experience -- called me an optimist. I know that I tend to naturally see the glass as half-empty, and for a boss who had known me for years to call me an optimist was an outward acknowledgement of an attitude that I'd worked hard to cultivate.

## What have you been learning recently?

Technically, I recently grabbed a [Humble bundle](https://www.humblebundle.com/books/software-architecture-oreilly-books) with 15 books on different flavors of software architecture. I'm slowly making way through all that content.

I found _[How to Measure Anything](https://www.amazon.com/How-Measure-Anything-Intangibles-Business/dp/1118539273)_ highly impactful to how I thought about measuring software development, so I also recently picked up _[How to Measure Anything in Cybersecurity Risk](https://www.amazon.com/How-Measure-Anything-Cybersecurity-Risk/dp/1119892309)_. As someone who has often been frustrated by the vagaries of risk assessment and the ROI tradeoffs between various approaches, I'm looking forward to getting a fresh perspective, and perhaps one that can be applied to other areas with high uncertainty and seemingly intangible goals.

## How do you keep up on tech trends?

The witty answer: _I don't. If it ain't broke, don't fix it._ Every place I've worked has had plenty of challenges, and usually tracking the trends for just those problems was more than enough.

That said, I do have a number of practices that help me keep up:

* _Tangential learning._ While most of my research time goes into looking for targeted solutions to immediate problems, these resources often reference concepts or trends that I'm not familiar with. I use this as a prompt to learn more about a new trend or direction.
* _[Thoughtworks TechRadar](https://www.thoughtworks.com/en-us/radar)_. This semi-annual snapshot of the tech landscape is a great way to follow trends.
* Resumes and interviewing. For over a decade, I've been involved in hiring processes. I get to hear from candidates what they have worked on, answer their questions, and see what skills they put on their resume. While this approach suffers from selection bias (e.g., only people with certain skills apply), it still gives a lot of insight into trends.
* _The annual Stack Overflow [Developer Survey](https://survey.stackoverflow.co/2023/)_. This is very high level, but does show major trends.
* _Coworkers_. I love to compare notes and thoughts with coworkers. Between their own interests, research, and backgrounds, I learn an incredible amount about trends. This is doubly true when talking to engineers in related but slightly different specialties, like data or machine learning.
- _[Hacker News](https://news.ycombinator.com/)_. This is always a source of interesting ideas, often from areas I don't specialize in.

# Professional expertise

_What use is professional expertise if it doesn't generate thoughtful opinions?_

## What are your favorite and least favorite technology products, and why?

I wrote elsewhere about what made [Stripe one of my favorite technology products](../stripe-review.md).

For my least favorite technology product, I'll nominate _package.json and bundling_. On the one hand, package management and bundling is essential to a modern JavaScript/TypeScript project. In most cases, it's not plausible to avoid packages by repeating code over and over or writing every capability from scratch.

At the same time, package management and bundling has so many negatives:

* Doing it right is a necessity, but adds no value to software.
* Documentation and guidance is often vague or just outright missing.
* Error messages are usually unhelpful for determining the actual problem.
* The actual work is often the intersection of many technologies (e.g., yarn, tsc, webpack, and a few plugins). This amplifies the instruction problem because nobody is using the exact same setup.
* There are a lot of legacy complications -- such as why am I still specifying whether I want common modules or ES modules in the year 2023?
* Malicious packages are a security attack vector, which just adds to the joy.
* Packages use packages which use packages, creating dependency collisions, more security headaches (because packages need to update their dependencies), and gigabytes of node_modules data.
* The giant node_modules directories have secondary effects on CI/CD, such as reducing build speed while also making caching hard.
* Unless one has a really good test suite (which is time consuming and easy to get wrong), package upgrades introduce a nerve-wracking question: Has anything subtly changed about the behavior of the program?

All together, packaging and bundling is a pain, especially for any sort of combination with many tools that need to play together well. The fact that there are a couple other attempts to solve the packaging problem (e.g., yarn, pnpm) merely adds to the chaos.

## What are the benefits and the drawbacks of working in an Agile environment?

I see three big upsides to an Agile environment:

* _Rapid delivery of value_. Software doesn't sit on the shelf gathering dust; it generates value for the business.
* _Faster feedback_. Software gets used, which exposes problems or pain points.
* _Improved responsiveness to business priorities_. Business needs change rapidly, and rather than trying to predict the next two years, Agile development can quickly pivot and change priorities.

The big downside for Agile development is that it can lack adequate long-term focus. Some engineering problems, especially non-functional requirements, take a well-designed plan executed over the long term. Agile tends to avoid this kind of planning.  Likewise, constantly doing the immediately expedient solution can easily build up tech debt and gradually drag the team down. At the same time, the best solution for the company is not necessarily a series of iterations away from the current solution. Agile excels at finding the locally optimal solution, but often misses far more globally optimal approaches.

The second downside of some Agile implementations is that they are overly rigid. Agile is intended to be, well, agile and adapt to the specifics of the situation. When it doesn't do that (e.g., "we can't do that because it isn't Agile"), Agile can become an anchor. Rather than serving to help teams excel, the Agile process itself adds stress. For example, teams who take commitments extremely seriously may find themselves stressing out at the end of every sprint.

## How do you think technology advances will impact your job?

Since the punchcard and mainframe, there has been a search for an easier way for humans to describe what work they want done in a way that the computer will do it. After all, software development is similar to blacksmithing -- people want horseshoes for reliable transportation and metal hoes to produce food and swords to defend themselves. But when there are better ways to achieve those ends -- cars or tractors or tanks -- blacksmithing as an industry goes away.

Yet so far, the complexity of computer software has increased right alongside the enhancements. Yes, compilers are better, but applications are often hundreds of megabytes or gigabytes. Yes, computers are more powerful, but now we're capable of generating terabytes of data. Yes, the internet allows unparalleled interaction and connectivity, but it also introduces a whole new set of threat vectors for data to be compromised.

My guess is that this trend will continue -- tools making work easier, but complexity increasing alongside.

Copilot and machine learning being able to generate code and explain what code does are a really cool capability that accelerates solving common problems. But I see them as enhancements rather than game changers. First, they still very much need human checks. They use prediction to generate likely text; they don't actually understand what the human wants or what the code will do. And sometimes they are badly wrong, perhaps in subtle ways. Being able to read code is a harder skill than being able to write code, and so validating what the AI is doing will continue to require highly skilled humans. Additionally, a lot of software development is about the bigger picture and how all the pieces work together -- something that there are rather poor tools for managing right now, especially non-proprietary solutions.

Eventually, I think we'll see a jump to templated solutions for common problems. Just like a coding language has a set of common patterns (loops, if statements, assignments, functions), we'll gain a similar set of patterns for servers, APIs, and webhooks. Datadog's universal service monitoring that can plug into a linux kernel and monitor all incoming and outgoing http calls is an example of this idea -- it doesn't matter what the application is, the way it is monitored is consistent.

But at the moment, we're at the proliferation phase -- layers built on top of layers, and the complexity is increasing. Even trends that simplify life for some (such as microservices for developers) have introduced whole new technologies and careers (Kubernetes and cloud engineering). And even then, microservices aren't a silver bullet; distributed debugging is no joke and microservices -- or at least specific microservice implementations -- do not always align to business objectives (c.f., [Amazon Prime Video](https://devops.com/microservices-amazon-monolithic-richixbw/)).

# Professional interactions

_Sometimes these questions boil down to "Are you a reasonably self-aware person who has worked a real job before? Please give some evidence."_

## What traits do you look for in a co-worker?

Two traits:

1. Plays well with others.
2. Gets things done.

Another rendition of this idea is [Patrick Lencioni's](https://en.wikipedia.org/wiki/Patrick_Lencioni) [hungry, humble, and (people) smart model](https://medium.com/@iamsridhar/humble-hungry-and-smart-822cd5e161bf).

But in a nutshell, great co-workers deliver results, are team players, and are aware of how others are being impacted.

## What are the qualities of a successful team or project leader?

I've written in-depth on [two of the best leaders](../my-best-managers.md) I've ever worked with. Team or project leaders are successful over the long haul by:

* Creating and maintaining psychological safety, especially with the team members.
* Listening carefully and understanding the views of team members, customers, and business interests.
* Prioritizing the right work in the right order -- or, better yet, equipping the team to make these decisions.
* Flexibly adapting to changing situations and challenges.
* Providing each team member with what they need to thrive and do their best work.
* Establishing and maintaining clear expectations with customers and business interests.
* Shielding the team from unnecessary distractions and interruptions.

Doing the above draws on a host of skills, including communication skills, engineering expertise, project planning, and emotional intelligence.

## What skills or characteristics make someone an effective remote worker?

By far, the key trait is __overcommunication__. All of the normal casual interactions that happen in an office environment are harder to come by.

- Were you working late on a tough problem? Nobody was there to see you in the office as they walked out the door.
- Did you do something cool? It's easy for that Jira card or pull request to slip by without realizing the impact.
- Are you stuck on a problem? Nobody else is wandering down the hall to ask how it is going.
- Would it help to pair and chat through a problem? There's no open office door to indicate which teammates are readily disturbed.
- Feeling frustrated by how things are going? It's harder to read body language through video feeds.
- Not sure what a coworker meant by a chat? Reach out and find out, as it is easy to miscommunicate with the brief exchanges in chat tools.

That is, remote work is more disconnected than office work, and it takes an active mindset of reaching out -- often far more than it seems like should be necessary.

A few other traits:

1. __Candid reflection__. The lack of other observers makes it harder for others to know what your struggles are, which makes it harder for them to give helpful advice. It's easy to be embarrassed that some stupid typo took several hours to debug, but bringing up those problems is important for one's own growth as well as the team's health. Everyone being vulnerable helps provide the sort of training or improved practices that help everyone.
2. __Internally motivated / hard working__. Remote environments make it a lot easier to not put the time into work by cutting corners. While coworkers seeing each other in the office may not have been a good measure of who was working hard, the isolation of remote work presents real challenges for people who are not internally motivated at their work.
3. __Reader/writer__. Remote work tends to be more flexible with fewer common meetings. As a result, knowledge sharing and common reference points become more important. While there are a lot of ways of doing this, written material has three big advantages: fast to consume, highly searchable, and easily referenced. Done right, it can also be reasonably quick to create and modify. So reading well and writing competently gain importance in a remote office environment.

## How do you handle tight deadlines?

In the near term, I handle tight deadlines through:

* __Communication__. Keeping everyone -- bosses, teammates, stakeholders, reports -- in the loop as to what's happening and why is essential in tight deadlines. As much as possible, don't surprise people with "we're not meeting the deadline," especially not at the last moment. Instead, they should be briefed on coming challenges and the plans for working around them as much as is possible.[^briefed]
* __Triage__. What work can be dropped or pushed off? Often deadlines are somewhat arbitrary. Or perhaps not all the features are needed by the deadline. Do the most important work.
* __Negotiation__. Often deadlines or features can be renegotiated. Talking with people and finding out where there can be give and take is a way of easing deadlines.
* __Enlisting help__. Who else can be enlisted to help on the work? Or is there another way of accomplishing certain tasks? For example, if there's a rare edge case that won't be fixed when the software ships, maybe it's easy to write a query that finds impacted customers and then customer service can reach out and let the customer know about the problem. It isn't fancy, but it may avoid a lot of hours of upfront engineering before a deadline.
* __Extra work__. Occasionally, it's important to just put in the extra hours to make something happen, or to ask the team to put in the work. But it's really important to me that such an ask be a rarity and for a truly important cause, not just because I messed up and overcommitted the team.

[^briefed]: Software development is an unpredictable art, and there is always some moment that goes from "everything is on track" to "hrm, that's concerning" to "this is not fine." There's a bit of an art in not over-reacting to minor bumps while not burying major blockades and distinguishing between the scenarios.

Longer term, I work hard to avoid tight deadlines through a few techniques:

* __Agile-oriented delivery__. The best estimate of when the software will be complete is progress to date[^best]. Regularly showing what the software can do and what remains to be done helps keep expectations grounded. I'm also a huge fan of [hill charts](https://basecamp.com/features/hill-charts) to cleanly represent where work is at in a nice visual form.
* __Defining the value and goals of the project rather than deadlines__. Software projects tend to run long -- that is, they expand. And almost no project I've done has contracted[^contract]. More than one boss has told me that the correct approach to estimation is to take the developer efforts and have the manager multiply them by 2, and then to multiply them by 2 again. If a project is worth 16 developer weeks and the initial plan is for 15 developer weeks, there's almost no chance that project will have a successful ROI -- as soon as it falls behind even a little bit, it ceases to be a successful project.

[^best]: This is especially true when it comes to features. It is still true for non-functional requirements, but often it's harder to tell how well they are being met. The current approach to a responsive UI may be fine, but it may hit problems when the application scales 100x. So the responsive UI might be done ... or it might not be.

[^contract]: The few projects I've seen contract have all been ones where a different approach requiring far less effort was identified early on the in the project. Basically, the project plan was to do A, but the team soon realized that B would do the same thing except far faster.

# The kitchen sink

_Questions that are common enough I don't want to skip them, but don't have a clear category for me to put them in yet._

## Why do you want to work for us?

This is one of the few common questions I find works better in face-to-face interviews or a cover letter because I've had time to research the company and understand it.

But I'm also a bit weird -- when I interview, I wouldn't definitively say that I want to work for the company; I'd say there are good odds that I want to work for the company. Part of my goal in the interview process is to peek behind the curtain enough to see if the company is a good match.

But the generic answer is that I interview with companies that ...

* do something significant in the world.
* state an appealing approach to their business (e.g., corporate values, culture).
* seem likely to need my capabilities and offer a [work environment](./profile-best-environment.md) where I'll thrive.
* appear likely to be [what I look for in a position](./profile-target-position.md).

## Tell us about yourself.

I find I'm a reactive visionary -- I work better when there's a problem or goal that I clarify. I find this question, often asked early in the interview, is hard to clarify and hard to meaningfully answer. It's also a question that I've heard answered dozens of times as an interviewer, and rarely did the answer make any meaningful impact on what I thought of the candidate.

_Why do I find this question challenging?_

* The overall goal is clear (figure out if the candidate is a good fit / convince the interviewer to hire you). However, the specifics from one's experience that really matter to the company aren't clear. Partly the question is very abstract, but it also tends to be asked early in the interview process, before the candidate has a good sense for the company.
* Good candidates don't want to pigeonhole themselves into one specialty that may not be applicable to the job. They're particularly wary of limiting themselves at the beginning of the interview process.
* On a normal project, I'd look to sit down with the coworker or customer and get them to explain their situation, needs, and goals more so that I could give a tailored answer. But taking over the interviews like that isn't the cultural norm, and it completely disrupts the interviewer's time management.
* The result tends to be an attempt to generally describe one's relevant work while balancing two extremes:
    * Don't be too brief and come across as shallow with niche experience.
    * Don't take too long and come across as rambling about a lot of irrelevant details while not understanding how interviews work.

Ideally, one might have a perfect 2-3 minute story that encapsulates a great strength while also seeming like a widely capable candidate. In lieu of that, [this blog](/) and especially [my profile](./profile-hidden) provide a lot of this context.

## Tell me about a tech project you’ve worked on in your spare time.

For the most part, my work is my main technical project. An important part of a healthy work-life balance for me is being able to step away from work and have a different set of challenges. That said, I do tend to pick up some projects from time to team.

- I wrote software to connect to financial institutions and reformat financial records into [Beancount] (https://github.com/beancount/beancount) and its web interface ([fava](https://github.com/beancount/fava) because I wanted an accessible open source approach to maintaining financial records.
- Working with Stripe's webhook implementation really impressed me, so at one point I sketched out what a generic open source implementation of that capability might look like.
- One of my favorite games has a [MIPS-based scripting language](https://stationeers-wiki.com/MIPS). While there's already [an attempt](https://github.com/protective/stationeers_pymips) to convert Python scripts into MIPS, I've started thinking through what a more accessible and robust approach might look like.
