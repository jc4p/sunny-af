# sunny-af
sunny.af

Hi! :wave: This is a testbed for what I hope will someday be a sign-up-and-forget automatic tracker for cheap beach side destinations.

The end goal is for people to sign-up stating their location, if they have a passport or not, which airlines loyalty programs they belong to, etc. Then every Wednesday around lunch time if we've found any cheap (compared to normal rates) flights to a beach somewhere (where we've checked, and it'll be sunny), the user will get a text / FB message / whatever.

The current code looks ahead to next-next Friday and checks the weather in [all possible destinations](https://github.com/jc4p/sunny-af/blob/master/static.py#L1) using Dark Sky's API. For the days where it'll be sunny and nice. Then it uses Google's [QPX Express API](https://developers.google.com/qpx-express/) to look up flights between the two locations (currently hardcoded origin NYC/SFO) -1/+1 days from that Friday until -1/+1 days to the next Monday.

It spits out stuff like this:

![screenshot](http://i.imgur.com/Bfu1amS.jpg)
