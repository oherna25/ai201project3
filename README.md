# ai201project3
project3repo

# Descripton of community , labels and reasoning

# Description
for the community im going to use i choose r/anime since its a huge community and they already have labels in place to help with labeling.

# Labeling
they currently have the following possible labels for their posts:
discussion
help
what to watch?
official media
news
video
video edit
clip
short film
fanart
cosplay
rewatch
review
essay
infographic
misc
contest
weekly
meme
merch

i plan to reduce the label count since A: some of the labels can be reduced , like video ,clip , and short film can be reduced down to just video. some of them like infographic and cosplay are seldom used anymore and would be hard to catergorize so they might just end up being put into misc. contest and merch can also be rolled into misc. what to watch and help can slo be rolled into discussion. essay also feels like discussion so that can also be rolled into discussion. weekly is just weekly discussions so that could be put into discussion. 

this reduces the possible labels to :
discussion
official media
news
video
rewatch
misc
review
reviews seem to be more like discussions so we can get rid of that and put it under discussion

discussion
official media
news
video
rewatch
misc

official media can be news but news could be anything , so i do belive it can be rolled into news

discussion
news
video
rewatch
misc

rewatches are just new episode discussions about old anime so that can also be reduced into rewatch

discussion
news
video
misc

the labels matter since when browsing for particualar content you want to be to distinguish between what is offical and whats just reviews/discussions

discussion - posts that talk about anime and anime related stuff. must be a question or review , a question 

news - anime related news, must have a source ( link) or it could just be promo content for an anime

video - video shared on the platform, will usually consist of a video link and some basic info on what i covers.

misc - basically a other catergory. covers non discussion posts, 

# hard edge cases

the issue might be that a lot of posts might end up in misc so i might need to better define each one and find extra examples of the other labels. to help further define that since it feels more like an other.

some videos could fall between news and fanmade videos/edits. offical media videos generally seem to have a short title that mentions the title of the anime and what it is ( visual , trailer) that should help in placing posts in news ( official media ) and regular clips/fan edits.




# data collection

i plan to scrape r/anime. the issue is that i need the offical api to get title and post content so i need to use an offical API to get that data then. using regular scraping requires going into the actual post to get content.
i plan to get as much as i need. will start at 200 and work my way up till i have enough to fill each category with 50-100 posts.


# eval metrics

precision also matters. if post are being labeled incorrectly then the model needs more data and more refined defintions and examples to ensure the number of false postives are reduced.


# success

i plan on keeping 20-30 posts from training so i can have some posts that can be used to ensure the model is working as intended. im aiming for 95% accuracy


#  AI tool plan

