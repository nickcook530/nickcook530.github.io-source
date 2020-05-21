Title: Minimum viable product
Date: 2020-04-04
Modified: 2020-05-21
Category: product-management
Tags: product management, software
Slug: minimum-viable-product
Authors: Nick Cook
Summary: *"If you're not embarrassed you've waited too long to release."*
<!-- modified: 2020-05-21 -->

*"If you're not embarrassed you've waited too long to release."*

---
**Lesson Learned:**

Nobody likes being embarrassed. Nobody wants to open their project up to scrutiny when they know so many obvious flaws exist. It feels unnatural, which makes sense considering most of us spend the first 20ish years of our life in school, working tirelessly to perfect assignments before we hand them in for evaluation. Imagine how different it would be if you could hand in the assignment, get some feedback, rework it, hand it in again, get more feedback, rework it, etc. until you got that coveted 100%. Maybe my Fluid Dynamics grade wouldn't have been so bad... Anyways, while we didn't get that opportunity with our homework we do get it when developing software.

You may have heard of the term "minimum viable product" (MVP). It's a term most commonly used for winning arguments about feature inclusion. Just drop a casual "Yeah, but is that really MVP?" and watch the features get dropped left and right. Everyone in the world seems to have their own definition of MVP so I'll refrain from adding another to the mix. I'm partial to the definition provided by Eric Ries of Lean Startup fame. Eric defined an MVP as "that version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort." As we discussed in the [last post](/assumptions), we want to avoid making assumptions, and instead let our customers tell us what needs to be improved. Our goal should be to do the least work possible to get a product (MVP) to our customers in order to start the learning process.

I think we are all probably thinking the same thing... the Wizard of Oz would be a great analogy here. You see, the man behind the curtain had two choices, he could either become a great and powerful wizard (sounds time consuming) or he could create the illusion of being one (much less work). We can take this same approach when thinking about an MVP. Let's imagine we want to build an application where users input recipes and receive a grocery list containing the required ingredients. We could just build the input portion of the application, manually create the grocery lists ourselves, and then email the grocery list back to the user. Taking it a step further we could skip building the input interface all together and complete both the input and output process over email. In either case you are replacing the part that is time consuming to develop with a human, a "man behind the curtain" if you will. Obviously this is not sustainable but that's okay because we are simply trying to do the least amount of work to learn something, which in this case would be if people are actually interested in this grocery list making service.


**Learning Experience:**

As I did in my last post, I will again use our new application home screen as an example. As we were planning out our new home screen, the first feature of the new application, we had to decide how many widgets (tiles of information) we were going to launch with so users could customize their home screen. We started with 17 planned widgets but being savvy PM's we knew about the whole "minimum viable product" thing so we cut it down to six widgets. Genius! Of course the widgets would be complete with search, sorting, filtering, dynamic sizing, and links to areas of the old application that weren't available in the new one, but those are essentials to the MVP... right?

The development teams worked incredibly hard over multiple months and we built the perfect home screen complete with six widgets, just like we planned! We publicized the release to our customer base, excitement built, we released, and customers logged in to our new application!...and then they stopped logging in. Why would they stop logging in? Were the widgets not awesome enough? We started talking to customers about the home screen and found out that it had nothing to do with the home screen itself, it's just that customers wanted to be able to complete their work in one interface, so until an entire user flow was available in the new application they preferred to just use the old application.

Turns out it didn't matter how many widgets there were or how many bells and whistles they had, that wasn't enough to get customers to keep coming back. Good thing we learned that before building the seventh widget, but it likely didn't need to take us six widgets with search, sorting and filtering to figure that out either. Maybe we could have released one simple widget and gotten that same feedback with a fraction of the work and then shifted our development efforts accordingly. Well, as they say, "hindsight is 20/20" so we'll just have to chalk it up to another lesson learned and soldier on.

In the [next post](/build-less-learn-more) we will see just how "minimum" we can make an MVP...and hopefully use a learning experience that doesn't make me look so bad...