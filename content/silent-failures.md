title: A Tool -- Or a Puzzle?
subtitle: Cryptic failures
date: 2023-10-30
category: practices and principles
tags: knowledge, uncertainty
status: published

The other day I went to run my local blog server and got this:

```
> pelican -r -l
>
```

That's not the normal output. Normally it spews some text about building articles, maybe a few lines about syntax errors, and a message about listening on port 8000.

This time it just failed silently. No error. No message. Just returning to the prompt.

_Ugh._

After a moment's thought, I remembered that I'd recently upgraded Python from 3.10 to 3.12, which probably had broken something. No worries, I have this handy-dandy readme that explains how to install the prerequisites for my blog.

```
> pip install -r requirements.txt
[snip]
```

Fantastic, everything is updated. Let's run the server again.

```
> pelican -r -l
>
```

_Wait, what? Still nothing?_

Eventually, after some more poking, I discovered that my path still contained the path to the old Python 3.10 scripts. And although the Python 3.12 path was primary, I assume _something_ about the old install was interfering with running everything in 3.12.

The main evidence? After I removed the old 3.10 path, everything started working. Hurray!

# Tool vs. puzzle

Sometimes, I love these challenges. Can I carefully follow the cryptic instructions to make the technology work on not-quite-standard system?

Success is a sign of expertise; something I can brag about with my fellow programmers when we're discussing what bizarre realms we've traveled.

But as I've studied user experience, the more I've grown to ponder: Why does software behave like this?

I don't mean the specifics of this problem, the way that paths and imports and libraries intersected to produce this particular bizarre behavior. I mean, who wants this sort of complexity from their software?

Has any developer ever sat down and thought "Now that I've upgraded my language, I want some bizarre interactions between the old and new installations so that my command silently fails with no error output? For that matter, has any developer ever wanted to mix library imports between Python versions?

Yes, probably somewhere that's a very useful capability for some scenario. But most of the time, [basic UX heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) like _error prevention_ and _visibility of system status_ are far more important.

After all, I'm trying to use my computer as a tool to accomplish work, not to entertain myself for an afternoon.

# A modern medieval guild

I don't mean to pick on Python libraries -- although these are certainly easy targets. Not too long ago, I discovered that some operating systems don't ship Python with pip -- and that it can't be readily installed without ``sudo`` because _distutils_ also isn't shipped with the operating system. Again, I'm sure there's a good reason for this -- security or modularity or intellectual property rights or something. But as an end user, it's just pain and complexity for me (and, I suppose, gainful employment).

Every language has its own collection of pain and misery, whether it is figuring out how to configure webpack or specifying the TypeScript configuration or passing library parameters to the C++ compiler.

However, the frequency of this kind of pain, even in more modern tools[^modern], sometimes leads me to wonder if computer science is actually a medieval guild that carefully guards its knowledge through lots of obscure hoops. And once one masters enough hoops in a particular area, one can be a gainfully employeed guild member.

[^modern]: Yes, there are advancements. More meaningful error messages. Automatic garbage collection. Widespread IntelliSense. But that's not to say that there aren't a lot of sharp edges.

# So what

And that, in turn, leads me to wonder what software development that was more fully centered on the user experience might look like...

- The interface would deal with inputs, outputs, and costs, seamlessly covering over technical complexities such as databases, data types, CSS, parallelism, or CAP theorems. No [leaky abstractions](https://en.wikipedia.org/wiki/Leaky_abstraction).
- Simulate and visualize the software in any state (including errors or outages), making real-time adjustments to the behavior.
- Interact in natural human language with a deep understanding of real-world relationships. "Display the user's address in a standard format" rather than having to deal with all the different ways that states, counties, oblasts, or even post office boxes are handled across the world.

Fortunately for software developers, even the most recent versions of Copilot don't seem capable of offering that kind of help. At least, not yet.
