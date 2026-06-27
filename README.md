# TakeMeter — r/anime Post Classifier

Fine-tuned DistilBERT text classifier that labels r/anime posts into four categories: `discussion`, `news`, `misc`, and `recommendation`. Evaluated against a zero-shot Groq baseline (llama-3.3-70b-versatile).

---

## Community

**r/anime** — chosen because it's a large, active community with existing flair labels that provide a strong starting point for taxonomy design.

---

### Final label set
```
discussion | news | misc | recommendation
```

---

## Label Definitions

**discussion** — episode discussions, rewatches, or opinion/debate questions about a specific anime, episode, or scene. Does NOT include posts that are recommending something.

> Example: `[Spoilers] Familiar of Zero 20th Anniversary Rewatch -- Season 4 Episode 1 (Episode 38)`
> Example: `One Piece - Episode 1167 discussion`

**news** — anime related news with a source (link), or promo content for an anime (video or image). Includes official interviews.

> Example 1: `"BanG Dream! Yume∞Mita" Anime | Main Visual`
> Example 2: `"THE RIBBON HERO" Trailer 2 | Streaming Worldwide Exclusively on Netflix from August 8, 2026`

**misc** — catch-all for everything else. Covers fan content (AMV clips, covers), general questions, help requests (that are not recommendation requests), community announcements, daily/weekly community posts, and anything that doesn't fit the other three labels.

> Example: `r/anime Karma Ranking & Discussion | Week 12 [Spring 2026]`

> Example 2: `No.6 Rewatch 15 Years Anniversary Rewatch Announcement/Index/Schedule Thread`

**recommendation** — any post that wants an anime recommendation or an anime-related recommendation (e.g. best X lists, what should I watch next, suggest anime with Y quality).

> Example: `What anime is so bad that it's actually fun to watch?`
> Example 2: `Military Politics or Strategy Anime`

---

## What I Built

A 4-class text classifier fine-tuned on 394 manually annotated r/anime posts. The model takes a post's flair, title, and body as input and predicts which of the four labels best fits the post. An inference UI (`takemeter_inference.py`) lets you classify new posts interactively.

---

## Labels

| Label | Description |
|---|---|
| `discussion` | Episode discussions, rewatches, or opinion/debate questions about a specific anime, episode, or scene |
| `news` | Anime-related news with a source, promo content (video/image), or official interviews |
| `misc` | Everything else — fan content, help requests, community posts, daily/weekly threads |
| `recommendation` | Any post asking for an anime recommendation or anime-related suggestion |

---


##  3 difficult-to-label examples

example 1: 
Share Your Favorite Anime Soundtracks

this is one could be discussion or recommendation , i was flip floping this was during many runs and while i was redefining labels. at first it was misc but later became discussion and then recommendation. even claude thought it could be either or 2 of the labels. after finally getting the definitions down i put this one under recommendation

example 2: 

One piece for DANDADAN?

very unique post. could be discussion or misc. claude kept putting it under discussion based on my definition in the end i put it under misc since it was asking for help and suggest ( misc)

exmaple 3: 
Now that the season is over/almost over what are everyone's favorite/must watch?

feels like a discussion based on the title but if you read the body its asking for shows to watch aka its asking for recommendations. i had this under misc at first but open further reflection i felt recommendation is the better label




#

## Results
# Prompt

You are classifying <posts> from r/anime.
Assign each post to exactly one of the following categories.

discussion:  discussion - episode discussions, rewatches, or opinion/debate questions ( but not if they are recommendating something )
about a specific anime, episode, or scene.

Example 1: "[Spoilers] Familiar of Zero 20th Anniversary Rewatch -- Season 4 Episode 1 (Episode 38)"


news:  anime related news, must have a source ( link) or it could just be promo content for an anime (video or image) , can include interviews if its an offical interview.

Example: ""BanG Dream! YumeâˆžMita" Anime | Main Visual"

misc:  basically an other category, covers non discussion posts, Fan content (like covers and AMV clips) , general questions ,questions asking for help ( but not for a recommendation ) community announcements , daily community posts ( like karma ranking posts ) and anything that wouldnt fit the other 3 labels (not a recommendation request, not an episode discussion)
Example: "r/anime Karma Ranking & Discussion | Week 12 [Spring 2026]"

recommendation:  any post that wants an anime recommendation or wants an anime related recommendation.
Example: "What anime is so bad that it's actually fun to watch?"

Respond with ONLY the label name.
Do not explain your reasoning.



Valid labels:
discussion
news
misc
recommendation
"""

used prompt to get eac post labeled by the LLM then ran had it try to re label the examples to see if it could re label them accurately


# difficult cases


----

example 1:

title: Best/Worst faithful manga adaptation

body: Best/Worst faithful manga adaptation


Hi! 


What's the best and the worst anime adaptation from manga that stick to the original work? 


For me 

Best: Fullmetal Alchemist Brotherhood and Attack on Titan (to a degree, since they censored some bloody scenes that had a bigger impact in the manga) 



Worst: Tokyo Ghoul (like... It's the worst adaptation out there, the manga is a masterpiece, so why waste such an opportunity to gain gold out of it and make a shitshow?) 

-----

thoughts: 

### Fine-Tuned Model (DistilBERT)

**Accuracy: 0.917**

| | precision | recall | f1-score | support |
|---|---|---|---|---|
| discussion | 1.00 | 0.88 | 0.94 | 17 |
| news | 0.85 | 0.92 | 0.88 | 12 |
| misc | 0.79 | 0.85 | 0.81 | 13 |
| recommendation | 1.00 | 1.00 | 1.00 | 18 |
| **accuracy** | | | **0.92** | **60** |
| macro avg | 0.91 | 0.91 | 0.91 | 60 |
| weighted avg | 0.92 | 0.92 | 0.92 | 60 |

### Zero-Shot Baseline (Groq llama-3.3-70b-versatile)

**Accuracy: 0.883**

| | precision | recall | f1-score | support |
|---|---|---|---|---|
| discussion | 0.94 | 1.00 | 0.97 | 17 |
| news | 0.92 | 1.00 | 0.96 | 12 |
| misc | 1.00 | 0.46 | 0.63 | 13 |
| recommendation | 0.78 | 1.00 | 0.88 | 18 |
| **accuracy** | | | **0.88** | **60** |
| macro avg | 0.91 | 0.87 | 0.86 | 60 |
| weighted avg | 0.90 | 0.88 | 0.87 | 60 |

### Comparison

| Model | Accuracy |
|---|---|
| Zero-shot baseline (Groq) | 0.883 |
| Fine-tuned DistilBERT | **0.917** |
| **Improvement** | **+0.034** |

The fine-tuned model outperforms the baseline overall and beats it significantly on `misc` (F1 0.81 vs 0.63), which was the hardest class throughout the project.

---

## Confusion Matrix

|              | **discussion** | **news** | **misc** | **recommendation** |
|---|                        ---|       ---|       ---|                 ---|
| **discussion** |    15 |             0 |          2 |            0 |
| **news** |           0 |            11 |          1 |            0 |
| **misc** |           0 |             2 |         11 |            0 |
| **recommendation** | 0 |             0 |          0 |           18 |

`recommendation` was classified perfectly. The remaining errors are concentrated on the `discussion`/`misc` boundary, which is the hardest distinction in the taxonomy.

---

## Error Analysis

Wrong predictions: 5 / 60

--- #1 ---
Text:      Smoking Behind the Supermarket with You Opening (Violin Cover) 
True:      misc
Predicted: news  (confidence: 0.92)




--- #2 ---
Text:      WELSH & SHEDAR [TEASER] 
True:      news
Predicted: misc  (confidence: 0.54)

--- #3 ---
Text:      In a Clevatess rewatch I noticed the sound effects are less prominent in the dub. I want to preface this post with I am not a sub elitist and this isn't a sub/dub debate post I'm just pointing out wha...
True:      discussion
Predicted: misc  (confidence: 0.92)

--- #4 ---
Text:      Chainsaw Man Character Designer Kazutaka Sugiyama responds to fans asking him about bringing back CSM Season 1's art style/designs, "Sorry but I've gone all-in on steering it completely toward mimicki...
True:      news
Predicted: discussion  (confidence: 0.91)

--- #5 ---
Text:      I need help making a decision (dragon ball beerus) Hey guys I started watching the dragon ball anime franchise last month and now I just finished dragon ball Kai , I was told to watch daima next becau...
True:      misc
Predicted: recommendation  (confidence: 0.78)



## Training Configuration

```python
model            = "distilbert-base-uncased"
num_train_epochs = 12
batch_size       = 16
learning_rate    = 3e-5
weight_decay     = 0.01
warmup_steps     = 50
split            = 70% train / 15% val / 15% test (stratified, random_state=42)
input_format     = "[flair] title body"
```

Key finding from hyperparameter tuning: the model peaked at epoch 12 on this dataset. Earlier runs with the default 3 epochs severely undertrained the model (warmup consumed most of the training budget). Flair was included as an input prefix, which meaningfully improved `misc` recall by giving the model a direct categorical signal for post types like `Video Edit`, `Weekly`, and `Official Media`.

---

## Dataset

- **Source:** r/anime (Reddit API)
- **Size:** 394 labeled examples
- **Label distribution:** discussion (111) · recommendation (114) · misc (87) · news (82)
- **Annotation:** 50 examples labeled manually, remainder labeled with Claude assistance and reviewed/corrected by hand. Label definitions were iteratively refined based on model error analysis across multiple training runs.

See `planning.md` for full label definitions, edge case rules, and annotation decisions.

# Evaluation report

## Confusion Matrix

|              | **discussion** | **news** | **misc** | **recommendation** |
|---|                        ---|       ---|       ---|                 ---|
| **discussion** |    15 |             0 |          2 |            0 |
| **news** |           0 |            11 |          1 |            0 |
| **misc** |           0 |             2 |         11 |            0 |
| **recommendation** | 0 |             0 |          0 |           18 |

`discussion`/`misc` boundary, which is the hardest distinction in the taxonomy.
due to the losser definiton of misc some posts were getting classfied under misc and not discussion i was planning to add more but decided to keep it as 400 examples. with more examples that could be either one i could have better defined the diffrence between each. i refined the misc and discussion many times before reaching the current results.
### Sample classification 

Wrong predictions: 5 / 60

--- #1 ---
Text:      Smoking Behind the Supermarket with You Opening (Violin Cover) 
True:      misc
Predicted: news  (confidence: 0.91)

the model saw the word opening and thought it was news ( an offical content) even though it was really just a fan cover. messed with the model's prediction. without other examples it very confident it was news.

--- #2 ---
Text:      In a Clevatess rewatch I noticed the sound effects are less prominent in the dub. I want to preface this post with I am not a sub elitist and this isn't a sub/dub debate post I'm just pointing out wha...
True:      discussion
Predicted: misc  (confidence: 0.94)

since the post is talking about a particular show it should count as discussion but since for the 4th label i choose misc which covers non discussion posts the model was confident it was a misc post. i think i needed more posts like this to further expand on the what misc vs discussion i refined my definitions to better define each but this post clearly should be discussion but without more samples of similar ones the model choose misc

--- #3 ---
Text:      Chainsaw Man Character Designer Kazutaka Sugiyama responds to fans asking him about bringing back CSM Season 1's art style/designs, "Sorry but I've gone all-in on steering it completely toward mimicki...
True:      news
Predicted: misc  (confidence: 0.82)

offical interview from an offical source aka news. but not enough news posts that are just interviews to better distingusih it so the model put in under misc since that was my catch all label

--- #4 ---
Text:      Can't bring myself to watch Rurouni Kenshin anymore after learning about the author **Disclaimer: If you haven't watched or finished Rurouni Kenshin, you may want to avoid this post for now. It contai...
True:      discussion
Predicted: misc  (confidence: 0.74)

post talking about their feeling towards an naime. a major issue is that it talking about a particular anime but also contains the posters views on the anime so it could be either one since its not really a post that wants to discuss the issue more so it wants to share their views. could be either but falls under discussion since it is about a particualar show

--- #5 ---
Text:      Bleach tybw AMV - hollywood forever #bleach #amv By Sempai amv 
True:      misc
Predicted: news  (confidence: 0.87)

not an offical video but since i said a news post should be labeled as such if that was a video link then it the model labeled as news but since it was a video that was fan made it was put under news


# reflection: what the model learned vs. what you intended

if i had more labels i could better define what the model should be looking for. overall after much relabeling and changing around parameters i was able to get it above 90%. my worst run was at 56% and for most my runs the one shot model had better scores than the fine tuned. it
 was a tough assignment if i could i would have picked a community with a smaller niche. 
i wanted it to better see the diffrence between posts and label them as accurately as possible but i found it hard to do so without more examples. i was planning to add more examples but felt that the best thing to do is 
# spec reflection 

my spec could have been more refined before actually starting. rerunning the model became an issue after google began to limit the number of runs per day to just 1 or 2. next time i would spend more time refining the spec and finding ways to test out my theory that let me have unlimited chances to reflect and further refine.


## AI Tool Plan

- Used Claude to help label the first batch of example posts — labeled 50 manually, had Claude finish the remaining ~350. Reviewed and corrected ~20 labels where Claude's judgment differed from the annotation rules.
- Fed evaluation metric results back to Claude to iteratively refine label definitions and resolve recurring boundary cases.
- Claude suggested hyperparameter changes (epochs, warmup steps, learning rate) based on observed training curves and per-class recall patterns.

## other thoughts

if i had more labels i could better define the possible posts i feel i was limited with just 2-4 labels. a 5th one would have let me reduce misc down. it took me  runs to get my fine tune model to better than my one shot model
