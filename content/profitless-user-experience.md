title: Modem Failure - Why Improve?
subtitle: Tales of user experience
date: 2024-05-20
category: software design
tags: user experience, system design, incentives
status: published

_Retry connection?_

Two of my "favorite" words. My home internet connection was out. I checked the outage map; there were some vague lines suggesting something or another in my area might be out. A few hours later, the internet was back on.

_Retry connection?_

Well, it was back briefly. Now it was out again. I went to bed. The next morning, the familiar words greeted me:

_Retry connection?_

Okay, now it's getting serious. Time to dig in a bit. The outage map? It shows nothing.

Frustrating. I call my internet provider. After bouncing through the menus, I'm put on hold for an extended period. Finally, a representative answers me.

_Is there a problem?_ The signal looks good, they say.

_Okay, let me try rebooting my router._ *No, don't do that. It might cause problems.*

That's strange; I've never heard about rebooting the router being a problem in decades of tech service.

_Could you tell me what time the outage ended?_ No, they're unable to access the technician's notes about the outage.

_Could you tell me if you see internet traffic from my modem? No. Could you please connect your laptop directly to the cable modem to see if that resolves the problem?

_How can I leave feedback about this experience?_ You might receive a feedback survey after this phone call.

# Reviewing the experience

The whole experience is a lesson in (bad) user experience.

__The principle:__ [Visibility of System Status](https://www.nngroup.com/articles/visibility-system-status/).

__The reality:__ There's no visibility of system status. There was no way to independently validate anything the representative was telling me. In fact, at one point, I asked the representative for my modem ID just to confirm that the user wasn't just reading rote answers from note cards.

Getting information was painful with long delays. What's particularly ironic is that my provider has a monthly data cap. So some part of their system is absolutely aware of when and how many bytes I'm using.

__The principle:__ [Match between the system and the real world](https://www.nngroup.com/articles/ten-usability-heuristics/).

__The reality:__ Why can't I access this information myself from my phone? Why do I even need to call my internet provider to find out if my cable modem has a signal connection to the world?

Are they really expecting the average customer to have a way to connect their laptop directly a cable modem to bypass a router? Yes, I can do it. I also work in the software industry, have far more computers than the average person, and years worth of random tech equipment I've collected for one reason or another. But it's not like the latest MacBook Pro comes with a CAT-5 connection.

__The principle:__ [Help users recognize, diagnose, and recover from errors](https://www.nngroup.com/articles/ten-usability-heuristics/).

__The reality:__ Oh, yes, I did eventually resolve the problem -- by rebooting my router, the one action that the customer representative distinctly told me _not_ to take.

# The importance problem

I'm sure far more could be said about why what I went through was a terrible user experience -- even if the actual underlying problem was my own equipment not properly recovering in the aftermath of an outage.

But there's a bigger problem: I don't believe my provider cares to do better. From an inability to engage except via phone calls to a customer service representative who seemed to be reading from a canned script carefully crafted to apply to everybody while helping nobody, I felt small and minimized.

Nothing suggested that the company wants feedback or cares to do better. They appear fine with my wasting my own time to get misleading information with no way to give feedback.

# The incentive problem

And this care-free attitude? It's probably a good business decision.

My internet doesn't go out very often. There aren't many providers, and some of them have worse reputations. Changing providers is a disruptive experience with little guarantee of upside. So I'm unlikely to change providers and likely to keep paying them.

Ironically, I know they have all the data they need to make this experience far better: I have a monthly data quota. They can tell me how much data I've used after a day or two delay. so somewhere, some part of their system is aware of how much internet traffic is coming from my modem. Some part of their system is aware of whether or not my cable modem is connected. And these systems could be connected together to provide a more-or-less real-time account view.

Would it be easy? Maybe not. It could be their systems aren't real-time currently. Maybe they have a mix of systems that don't easily talk to one another.

In short, it is likely expensive to do what I'm suggesting. So given little upside, why make a substantial investment? Terrible UX is likely a very good business decision.

# So what

I don't like this answer. I don't want low-quality experiences to be good business decisions.

Yet if I extrapolate this logic out, a principle suggests itself:

_Bad user experience is inevitable when customers have few choices._

That is, good user experience emerges when customers have real choices, the better experience makes a significant impact to them, and there's enough profit margin in the industry to support experience design.

Is the principle true? I don't know. I'm guessing many of my user experience coworkers would be appalled.

What do you think? What incentive would it take for my internet provider to create a decent outage experience?