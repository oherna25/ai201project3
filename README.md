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
misc
recommendation 

the labels matter since when browsing for particualar content you want to be to distinguish between what is offical and whats just reviews/discussions

discussion - discussion - episode discussions, rewatches, or opinion/debate questions 
about a specific anime, episode, or scene.

news - anime related news, must have a source ( link) or it could just be promo content for an anime (video or image)


misc - basically an other category, covers non discussion posts, general questions ,questions asking for help ( but not for a recommendation ) community announcements , daily community posts and anything that wouldnt fit the other 3 labels (not a recommendation request, not an episode discussion)

recommendation - any post that wants an anime recommendation
# hard edge cases

the issue might be that a lot of posts might end up in misc so i might need to better define each one and find extra examples of the other labels. to help further define that since it feels more like an other.





# data collection

i plan to scrape r/anime. the issue is that i need the offical api to get title and post content so i need to use an offical API to get that data then. using regular scraping requires going into the actual post to get content.
i plan to get as much as i need. will start at 200 and work my way up till i have enough to fill each category with 50-100 posts.


# eval metrics

precision also matters. if post are being labeled incorrectly then the model needs more data and more refined defintions and examples to ensure the number of false postives are reduced.


# success

i plan on keeping 20-30 posts from training so i can have some posts that can be used to ensure the model is working as intended. im aiming for 95% accuracy


#  AI tool plan

i used claude to help me label my first of example posts ,i did 50 myself and then had ai finish the other 200. it mostly did ok i had to change about 20 since i felt they should be labeled in a different manner.

i used claude to further refine the label definitions by feeding it the metric results

# section 5 notes

🎯 Baseline accuracy: 0.864  (evaluated on 59/60 parseable responses)

Per-class metrics (baseline):
                precision    recall  f1-score   support

    discussion       0.88      0.88      0.88        17
          news       1.00      1.00      1.00        13
          misc       0.90      0.75      0.82        12
recommendation       0.74      0.82      0.78        17

      accuracy                           0.86        59
     macro avg       0.88      0.86      0.87        59
  weighted avg       0.87      0.86      0.87        59

the model did ok. i think i need further refine misc since it had the worst recall metric and f1 score. i also only had 4 misc posts so i should prob feed it more posts to further refine the category along with further refining.


# section 4 notes

🎯Fine-tuned model accuracy: 0.733

Per-class metrics (fine-tuned model):
                precision    recall  f1-score   support

    discussion       1.00      0.46      0.63        13
          news       0.78      0.78      0.78         9
          misc       0.56      0.82      0.67        11
recommendation       0.79      0.92      0.85        12

      accuracy                           0.73        45
     macro avg       0.78      0.74      0.73        45
  weighted avg       0.79      0.73      0.73        45

Wrong predictions: 8 / 30

--- #1 ---
Text:      No.6 Rewatch 15 Years Anniversary Rewatch Announcement/Index/Schedule Thread Well, there are a handful turned around here in the [interest thread](https://old.reddit.com/r/anime/comments/1u8oduo/makin...
True:      misc
Predicted: discussion  (confidence: 0.37)

--- #2 ---
Text:      Oasis increases its stake in Kadokawa, bringing its ownership to 15.25% 
True:      news
Predicted: discussion  (confidence: 0.36)

--- #3 ---
Text:      "Goodbye, Lara" Original Anime | Main Visual 
True:      news
Predicted: discussion  (confidence: 0.35)

--- #4 ---
Text:      Mistress Kanan Is Devilishly Easy Season 2 Announced 
True:      news
Predicted: misc  (confidence: 0.36)

--- #5 ---
Text:      ONE PIECE HEROINES | Official Trailer 
True:      news
Predicted: misc  (confidence: 0.36)

--- #6 ---
Text:      Ecchi Animes & Co. Hello everyone

Soo.....it seems that I have been missing out big time.

At the end of last year, I decided to try out anime.

Now I don't remember how I came to it ( probably throu...
True:      misc
Predicted: discussion  (confidence: 0.36)

--- #7 ---
Text:      I Want to Love You Till Your Dying Day - Episode 1 Preview 
True:      news
Predicted: misc  (confidence: 0.36)

--- #8 ---
Text:      An Apothecary Diaries rewatch Given that in this current season (Spring 2026) I had nothing to watch, and a season 3 of the Apothecary Diaries is in for the Fall season, I thought I would go for a bin...
True:      misc
Predicted: discussion  (confidence: 0.35)

# section 6 notes
Wrong predictions: 8 / 30

--- #1 ---
Text:      No.6 Rewatch 15 Years Anniversary Rewatch Announcement/Index/Schedule Thread Well, there are a handful turned around here in the [interest thread](https://old.reddit.com/r/anime/comments/1u8oduo/makin...
True:      misc
Predicted: discussion  (confidence: 0.37)

--- #2 ---
Text:      Oasis increases its stake in Kadokawa, bringing its ownership to 15.25% 
True:      news
Predicted: discussion  (confidence: 0.36)

--- #3 ---
Text:      "Goodbye, Lara" Original Anime | Main Visual 
True:      news
Predicted: discussion  (confidence: 0.35)

--- #4 ---
Text:      Mistress Kanan Is Devilishly Easy Season 2 Announced 
True:      news
Predicted: misc  (confidence: 0.36)

--- #5 ---
Text:      ONE PIECE HEROINES | Official Trailer 
True:      news
Predicted: misc  (confidence: 0.36)

--- #6 ---
Text:      Ecchi Animes & Co. Hello everyone

Soo.....it seems that I have been missing out big time.

At the end of last year, I decided to try out anime.

Now I don't remember how I came to it ( probably throu...
True:      misc
Predicted: discussion  (confidence: 0.36)

--- #7 ---
Text:      I Want to Love You Till Your Dying Day - Episode 1 Preview 
True:      news
Predicted: misc  (confidence: 0.36)

--- #8 ---
Text:      An Apothecary Diaries rewatch Given that in this current season (Spring 2026) I had nothing to watch, and a season 3 of the Apothecary Diaries is in for the Fall season, I thought I would go for a bin...
True:      misc
Predicted: discussion  (confidence: 0.35)

# section 3 notes

i changed num_train_epoch from 3 to 5



# ── TODO ──────────────────────────────────────────────────────────────────
# Define YOUR label map below.
# Keys are the string labels in your CSV; values are integers starting at 0.
# Add or remove entries to match your actual labels (2–4 labels supported).
#
# The example below is ILLUSTRATIVE ONLY (the r/nba taxonomy from the project
# page). DELETE it and use your own community's labels — submitting the
# example unchanged will not pass.
# ────────────────────────────────────────────────────────────────────────

LABEL_MAP = {
    "discussion":  0,   # ← Replace with your first label
    "news":  1,   # ← Replace with your second label
    "misc":  2,   # ← Replace with your third label (remove if you have 2 labels)
    "recommendation": 3,  # ← Uncomment if you have a fourth label
}

SYSTEM_PROMPT = """
You are classifying <posts> from r/anime.
Assign each post to exactly one of the following categories.

discussion:  posts that talk about anime and anime related stuff, must be a question or review , a question that ask for a recommendation.

Example: "[Spoilers] Familiar of Zero 20th Anniversary Rewatch -- Season 4 Episode 1 (Episode 38)"

news:  anime related news, must have a source ( link) or it could just be promo content for an anime (video or image)
Example: ""BanG Dream! YumeâˆžMita" Anime | Main Visual"

misc:  basically a other catergory. covers non discussion posts, general questions , community announcements.
Example: "r/anime Karma Ranking & Discussion | Week 12 [Spring 2026]"

recommendation:  any post that want an anime recommendation. 
Example: "Please please help me with starting anime. I will be very grateful if you took out the time to read my post because I am kind of desperate"

Respond with ONLY the label name.
Do not explain your reasoning.



Valid labels:
discussion
news
misc
recommendation
"""