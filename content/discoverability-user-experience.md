title: Tier I Customer Support - Why Improve?
subtitle: Tales of user experience
date: 2024-06-10
category: software design
tags: user experience, system design, incentives
status: published

The other day I reached out to a top tier monitoring platform with a "peculiarity" about how one of their widgets performed. In a fairly standard scenario, a particular widget behavior linked to the wrong dashboard -- yet everything about their documentation and dashboard interfaces suggested I was using the product in the expected way.

For those not familiar with the industry, the first layer of customer service at such companies tends to be [ID-10T check](https://en.wikipedia.org/wiki/User_error): Is the power on? Did you read the documentation? Did you read all the documentation? Do you understand how the product is supposed to work?

I'm not unsympathetic; I've asked and received my own fair share of question where the problem was user error and a basic Google search would have turned up the answer. My solution to having an extended back-n-forth with tier I support is to carefully write my questions with reproducible cases, expected behaviors, actual behaviors, and applicable documentation. Basically, a classic bug report, except instead of saying "This is a bug", I center the question around "How do I achieve the result I want?" Usually this bypasses most of the prepared prompts and demonstrates sufficient knowledge of the product that my question gets immediately bumped to the system experts.

So I did that here. I carefully linked to the widget in question. I showed the two different scenarios, one which worked as expected and the other of which completely didn't work. And I linked to the documentation and the UI, neither of which suggested the observed behavior was anything remotely like what I should expect.

And I got reply describing an answer to a problem involving 404s (something I completely had not mentioned) and pointing me at some irrelevant documentation. In short, tier I either didn't read my question at all, or sent me back the standard response from some randomly selected keywords.

Ugh.

For the reader's amusement, when the system experts got back with me, they agreed that the behavior was undocumented, dysfunctional, and best all, already known by them. Someday, improvements might be a priority on their roadmap.

# Can we do better?

Clearly, this experience wasn't the best. It isn't the experience I want as a customer when I have a real question. And I don't believe the typical service provider wants to answer legitimate questions with friction or misinformation.

So how could we do better? If, at least on paper, both the customer and the provider would like a different experience, could we make one that works?

One answer would be contracts with a clause like "If you ask us a question that is answered in documentation, you'll pay $500. For every documentation hole or legitimate bug you find, we'll credit you $500." That could work, but is likely to lead to a lot of wrangling over whether something is a documentation gap or a legitimate bug. That's probably not the synergistic back-n-forth that either party wants.

# Discoverability

The issue, I believe, is discoverability. If it is easier and faster for me to ask an expert a question than to find the answer myself, I'm likely to ask the expert. This reality suggests two approaches:

1. Make it harder and more painful to ask experts a question.
2. Make it far faster and easier to discover the answer in the service or documentation than to ask an expert.

# A gameplan

Let's pretend we're running a provider and our ambition is to provide an amazing user experience through discoverability and highly responsive customer support. What's our strategy?

Our goal is to scale our service without significantly scaling our customer support. That is, if we double the number of customers, we don't want to increase our customer representative count.

This means that every common question needs to be ruthlessly turned into a discoverable fact:

* If I'm in the system and want to know what a widget can do, I need to be able to easily discover that.
* If I'm writing a project plan and want to know what a widget can do, I need to be able to easily discover that.
* If I want to know the best way to achieve an outcome, I need to be able to discover that.
* If I want to know if my question already has answer, I need to be able to quickly discover that.

To support this, we'll want to hire customer service representatives from fields such as product design, user experience, and software development.

The key outcome of every customer question is not "How do we answer this question?" It is:

> How do we make the answer so discoverable that nobody every asks this again?

# The concept

So instead of having a traditional customer service department, we'll integrate customer interactions with a group focused on product usability, from interested prospects to long-term users. With this scope, the group should have the ability to guide discoverability through product design, user interfaces, and documentation.

As one example, consider a company taking the [playground idea](https://www.typescriptlang.org/play/) to the next level: Every feature had links to a playground environment with realistic dummy data that demonstrated the capability.

Solving this space is still a hard problem. While fast rapid iterations works for many software solutions, there's often weak integration between code and documentation, or between user interfaces and explanations of behaviors, or between products and the explanations. Many companies struggle with information architecture, organizing their documentation in ways that users do not quickly understand[^four].

[^four]: I've found the [four kinds of documentation](https://www.writethedocs.org/videos/eu/2017/the-four-kinds-of-documentation-and-why-you-need-to-understand-what-they-are-daniele-procida/) to be a fantastic idea, and wish far more companies used that as guiding principle.

# Troublemakers

So far, we've talked about the carrot approach: How can we make our software so delightful, so easy to understand, that our customers prefer self-discovery to asking questions.

> Some people hate to read.

But there's always a few people who prefer to ask the question and push work onto customer service rather than do their own research. Maybe they haven't actually used the software to understand how discoverable it is. Maybe they don't realize how much overhead there is to asking a question. Maybe they don't understand our business model and how it relies on people not asking questions that are already answered.

As a first layer of defense, let's make it standard practice to run a usability test with a customer that asks us a question. Tell them a bit about our ambition that users should be able to entirely discover the product without customer support, and then observe how they approach answering the question.

Since our customer support department is full of user experience specialists, we have the expertise for this. If we've done our product design right, this exercise will demonstrate to users how easy it is to find their own answers. And if we've missed some expectation, well, observing what the user is actually trying to do is a great way to fix our assumptions and let us iterate on an even more discoverable product.

Finally, add a clause to contracts that lets us not respond to questions from users who persist in asking questions that they could easily answer themselves.

# So what

Ironically, if a company succeeded at this approach[^stripe], one of their most valuable products might be the framework, techniques, and tooling that supports highly discoverable software along with rapid iterative development. Yes, it might be opinionated and limited on which frameworks it worked with. But the ability to simultaneously develop software, manage beta features, offer demonstration/playground environments, and reduce customer support staffing -- that could be a killer product.

[^stripe]: [Stripe](https://stripe.com/) is the company that I've seen that comes closest to this. I've [written before]({filename}stripe-review.md) about how this kind of discoverability moved them from being an afterthought vendor to being the preferred vendor.

What do you think? Would your company be interested in such a product?
