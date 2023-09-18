title: Time: The Greatest Challenge
date: 2023-09-04
category: architecture
tags: architecture, software
status: published

_Time, the software engineer's greatest challenge._

Is that too strong a statement? There certainly are other candidates such as:

* Money (although if time is money, maybe this supports my thesis).
* Communication and division of labor, especially as the organization grows larger and larger.
* Office politics

But time uniquely permeates the software development.

# Coding time

In writing software, time is rarely easy:

* Finding out the true time is non-trivial. Maybe the system clock (or the possibly hijacked browser) can't be trusted. Or maybe they just aren't synced NIST time. Or maybe one wants to figure out the latency between a client and server and isn't sure both clocks are synced.
* Periodically someone forgets to store data in UTC, which leads to fun and easy-to-get-wrong timezone manipulation operations.
* Or perhaps one needs to be able to reliably plot events on a timeline, including that 1980 October 26 1:01a record happened before or after day lights savings time ended? And periodically governments change the rules around time, so a locale that practices daylight savings time now might not in a year -- or five years ago.
* Even questions like "What does it mean for event A to happen before event B?" get weird in computer systems. If I receive event A before event B, does that mean event A happened first? What if event B was sent first, but was lost, and only arrived an hour later? What if I'm working in a distributed system where I only know about one of the events?

And don't get me started on trying to write tests that involve time. Benchmarks are predictable until they aren't. Tests work fine until that one moment when an operation didn't take as long as expected resulting in equality instead of an ordered sequence. Or someone sticks in a `if is_daylights_savings_time` check that makes it through code review, resulting in  mysteriously test failure four months later.

# State

And then there's the problem of state. Almost every system has some form of persistent state - e.g. settings, same games, profiles, collected data. And this persistent state needs to be maintained across updates. All too often this state goes back years (e.g. Windows maintaining MS-DOS compatibility) or cannot be abandoned (imagine if your bank account periodically reset itself to zero[^zero]).

[^zero]: Actually, for some people, overdraft coverage plus a periodically resetting bank account could be a feature. But banks probably wouldn't like it.

Even if there's no persistent state, there's often transient state such as a data pipeline where events are in transient so the new software needs to be able to handle the old format.

# Customer expectations

And then once the software has been released, customers develop expectations - how the software works, what features it supports, and how those features work. Three months later, I may have figured out a totally better way to display time and realize that only five people use the `ping` mechanism. But that doesn't mean my existing customer base wants their time display to change overnight. And those five people who use the `ping` mechanic aren't going be very happy if it goes away, even if they never would have noticed if I'd never introduced the capability.

And of course it takes a customer almost no time to notice a change that they don't like, while it takes a great deal of engagement for them to read my release notes, my tutorial tips, or whatever migration mechanism I put in place.

# Organizational changes

On top of all of this, the organization changes over time. Bob, who designed the system from the ground up, gets promoted and isn't around to answer questions. Jane made a few fundamental changes to Bob's design, but then left to work at her friend's company. The sales department wants to change the pricing model, which breaks fundamental software assumptions. The user interface team discovered their initial information architecture actually had several key misconceptions and want to overhaul the design.

Meanwhile, the the customer service department is significantly over budget and the number of customer complaints have to be cut in half -- even though easy access to customer service was one of the bedrock principles of the initial design.

Or if it's a very, very, bad day, a key software dependency horrifically changes their pricing model -- effective in three months -- and it is all hands on deck to learn and migrate to the competition.

# So what?

So time is a headache across all levels of software, and that's why it's my candidate for a software engineer's greatest challenge. What can be done about it?

For some scenarios, there are best practices. For example, use UTC to pass and store time values; translate to a user-specific timezone at the display level.

But best practices don't solve most of these problems. Instead, the challenge fo architects is to mitigate the problem through three practices:

1. Educate. Both engineers and stakeholders (especially the non-technical ones) need to understand the problem and the trade-offs with other priorities such as features. Most people, even non-technical ones, can understand these challenges, but won't consider them without prompting.
2. Articulate. Take the company's strategy when it comes to priorities and risk tolerances and put it into writing. Some companies, for example, can afford to invest deeply in employee retention, documentation or well-tested wrappers around 3rd-party software to mitigate risks. For other companies, the immediate priority may be getting to market, and business continuity is a priority for another day.
3. Translate. Take the strategic principles and turn them into day-to-day development principles. (See this discussion on tenets and principles.)

Those steps don't seem like enough, though. What else have you seen done to solve the problem of time?
