# hackaday-prize-vote-randomnessy

Hackaday does their Hackaday Prize thing for the 2nd time. They do community voting, too. The voting page shows two different projects to choose the better one from under a certain aspect.

I *guess* that they use this as some sort of user-driven sorting algorithm. People complained that they *always* get the same projects, so it *looks* like the chance for one of the entries to the Hackaday Prize showing up in the voting are not equal.

From http://hackaday.com/2015/06/05/astronaut-or-astronot-community-voting-begins/#comment-2595456 and http://hackaday.com/2015/06/05/astronaut-or-astronot-community-voting-begins/comment-page-1/#comment-2598812 I conclude:

+ all Hackaday Prize entries should show up
+ the same projects should not pop up again and again (only after voting one time for it)
+ projects that are newer (fewer votes) are more likely to show up

For me, from these simple rules, it sounds like the voting system prefers to show the projects the user does not like (does not vote for) as the liked ones are removed from the possible items showing up, but the non-liked are not.

It is possible to check two of the three rules by just retreiving and analyzing the vote page. For the third rule, it would be neccesary to post a sufficient amount of (fake) votes and analyze the results. For that, a more complex setup (and a number of fake accounts etc.) would be neccesary. As this would be unfair and I am lazy, I won't go into this third rule further.



Analyzing the other two rules is done by the attached python script as requested by Brian Benchoff:
"[...]If anyone wants to write a script to constantly refresh the page and get a distribution of how often all projects are presented, that would be some major hackaday blog cred. Maybe a tshirt. certainly some stickers."

So, here I am, "constantly refreshing" the page (looks like there is a load time of approx 1 second until the answer comes out of the pipe).
