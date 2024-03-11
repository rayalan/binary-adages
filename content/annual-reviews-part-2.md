title: Annual Performance Reviews (Part 2)
subtitle: Applying modern technology
date: 2024-01-29
category: systems
tags: brainstorming
status: published

Last time, I wrote about [the problem of annual reviews]({filename}annual-reviews.md) and started rethinking the problem if we were solving it for the first time with modern technology. By the end of the thought experiment, we were a company designing a new product, SmartReviews, with four key features:

1. Regular, low-effort collection of feedback from employees.
2. Trend-based alerting for management.
3. Directed prompts for specific feedback.
4. AI-assisted writing (because everything is cooler with AI).

Today I want to go through each of these features in detail, exploring how they streamline the annual performance review process.

How would each of these features work?

# Low-effort Feedback Collection

In places I've worked, feedback collection is hard. Every few months, I'm asked to give feedback on some people. But do I remember specifics? Was I paying particular attention to their work? Often, I have this bland "they were a good employee, what else do I say?" reaction. Meanwhile, there are employees who I have very clear praise or insight about, and I'm not prompted to submit any feedback there. Sure, I could go the extra mile to do so...but the system doesn't make it easy.

SmartReviews would solve this by being tied into all the systems. It would look at tickets, pull requests, emails, instant messages, documents, and calendars to see who had been interacting. And then it would prompt each individual for notes or observations about those interactions. It'd provide handy links to the relevant artifacts.

Feedback could either be one of two types:
  * _An observation point_: When Jane did such-n-such, it came across as unprofessional because of this-n-that.
  * _A hypothesis of a trend_: I suspect that when Joe is frustrated, he expects others to solve his problem leading him to post terse messages in Slack.

At this stage, the feedback wouldn't be shared. The goal is collecting feedback; it will be synthesized later.  The goal is to help people understand long-term trends. Individuals are prompted for feedback every couple weeks[^tune] based on who they have interacted with -- and, of course, they can make notes about other people. For trends, the individual is prompted if they've had any noteworthy interactions. Was the hypothesis supported? Or was there a conflicting example?

[^tune]: We can tune the frequency based on what gets the best responses.

As an added bonus to SmartReviews -- we can roughly track how much time people are spending on feedback, which artifacts people reference, and how helpful that feedback is to individuals. Because we sell this product to lots of companies, we can see how different designs of our software lead to different outcomes, and select the best review processes[^privacy].

[^privacy]: We will need to be very clear with users about which data will be visible just to SmartReviews as a company to make the product better vs. which data will be visible to others. Telling SmartReviews "this feedback wasn't helpful" is _very_ different than telling a co-worker "this feedback wasn't helpful."

Then when the actual review period rolls around, each employee has all of these pre-populated data points on each employee, along with any hypothesis they created about bigger behavior patterns. Now it is clear who to write a review for based on what the employee observed over the past months. An employee can look over lots of individual interactions and ask "What broader pattern emerges?" Or an employee can revisit the hypothesis, see if it was supported by the evidence, and refine or abandon it as necessary. Since all of this feedback was initially created in the context of artifacts such as messages, calendar appointments, and pull requests, reviewers don't need to go hunting for that data -- it's already included.

As an added bonus, we can give employees some help writing reviews with AI (see that feature later on) to further streamline this process.

# Trend-based alerting for management.

Typically, review systems want everyone to get reviewed. Often, this means someone gets asked to write a review about Joe who is a complete loner, and it's really hard to know what to say. Joe wasn't a problem. But nobody really knows what Joe did. And so Joe's review is very bland.

With SmartReviews, this problem can be spotted during the year, without waiting until the review period rolls around. SmartReviews can look at which individuals aren't generating any feedback -- or generating lots of negative feedback -- and alert manager to a problematic trend.

Note that the managers aren't getting specific feedback from SmartReview -- the effectiveness of our system hinges on users knowing that their individual observations are private until they share them. But we can do an aggregate analysis and alert managers that they may need to pay more attention in a particular area[^scale].

[^scale]: To help employees feel comfortable with their individual observations being used as sentiment, we might introduce a perspective for negative feedback. For example, Jane generating a lot of feedback about how they can grow is very different than Joe generating lots of feedback about how they are creating a hostile work environment.

# Directed prompts for specific feedback.

In addition to collecting feedback from individuals, SmartReviews can give directed prompts to people who interact with a certain person. For example:

> You recently read some documentation \[link\]. How would you evaluate it?

These prompts can have a variety of sources:

* Individuals wanting to grow.
* Managers looking for feedback about a specific habit.
* System owners looking for feedback about their system.

As an advanced feature, SmartReview could use sentiment analysis to generate smart prompts. For example, if one individual is giving a lot of negative feedback about a particular system, it might generate a prompt for other users of the system, specifically soliciting their experience.

# AI-assisted writing

Finally, writing reviews is hard. What's hard about them?

1. Sometimes it's hard to have anything concrete. The person is a generic good employee. They work hard, communicate decently, and ship quality code. It's good work. There's not much to critique. But there's also not many specific to praise.
2. Sometimes it's hard to get the tone right. I want this feedback to be taken as a strong trait that could get stronger, not as a weakness. I really want some other feedback to be taken as a long-term concern, but not an immediate problem.

In both these cases, we can introduce an AI-assisted review assistant (ARA). For good employees, ARA can understand the characteristics that make a good employee. Then ARA can give prompts:

* How often have you observed this behavior?
* When is a time when they illustrated this behavior?
* Have you ever seen them not exhibit this behavior?

By asking these questions, ARA can help draw out and help construct a far better review than just "I really like Jane's work."

Similarly, when I'm just frustrated, I can enter my rant into ARA and ARA can help me turn that into helpful feedback:

1. Prompt for more details (as above).
2. Prompt for other considerations, such as what the employee has done well (as above).
3. Help me understand how the feedback is likely to be received. "This feedback is likely to be seen as an unprofessional personal conflict because of these factors..."
4. Understand how I want to categorize my feedback (praise, possible long-term concern, growth opportunity, immediately problematic behavior).
5. Rewrite my review with a professional tone, according to my intent.
6. Iterate on the above feedback until I've generated some professional and helpful feedback.

This feature is hard to get right (AI hallucinations could be all sorts of headaches), but it could also really help feedback to be shared with the right context. As an added bonus, since we're dealing in a closed system (both the employees and managers are using SmartReview), we can add some tags or other metadata to help indicate the intent of the feedback, which can help everyone be on the same page when they read it.

# So what

At this point, we've got a system that is really cool:

* There is a minimal hassle when reviews come around; most of the reviews are being generated in realtime on an ongoing basis.
* Feedback is being given based on actual interactions, not based on who is selected to give reviews.
* Managers can be aware in realtime of problems or employees who may not be interacting. In particular, the system may be able to surface scenarios where everyone is struggling, but each individual thinks it is just them that is struggling, and thus nobody is speaking up.
* The system still integrates into a traditional annual or semi-annual review cycle. (This characteristic is important for adoption of our new product.)
* There is visibility into how much time and effort goes into generating feedback. Furthermore, it's possible to close the loop on that feedback and whether it was helpful or worth the time.

It won't do everything -- it won't, for example, force employees to give feedback or change a company culture where open feedback isn't welcomed.

However, it follows the DevOps principle that which is done often is done well, and turns feedback from a irregular activity into a regularly recurring activity.

What do you think -- is this a good modernization of the annual review process? What else SmartReview do?
