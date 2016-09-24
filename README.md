# sunny-af
sunny.af

Hi! :wave: This is a testbed for what I hope will someday be a sign-up-and-forget automatic tracker for cheap beach side destinations.

The end goal is for people to sign-up stating their location, if they have a passport or not, which airlines loyalty programs they belong to, etc. Then every Wednesday around lunch time if we've found any cheap (compared to normal rates) flights to a beach somewhere (where we've checked, and it'll be sunny), the user will get a text / FB message / whatever.

The current code looks ahead to next-next Friday then uses Google's [QPX Express API](https://developers.google.com/qpx-express/) to look up flights between two locations (currently hardcoded to DEN and one of the listed [destination locations](https://github.com/jc4p/sunny-af/blob/master/scratch.md)) -1/+1 days from that Friday until -1/+1 days to the next Monday.

It spits out stuff like this:

![screenshot](http://i.imgur.com/Cu5PLJx.png)
