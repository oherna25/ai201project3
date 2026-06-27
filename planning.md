# TakeMeter — Planning Notes

## Community

**r/anime** — chosen because it's a large, active community with existing flair labels that provide a strong starting point for taxonomy design.

---

## Label Design Process

### Starting point: r/anime's existing flairs
```
discussion, help, what to watch?, official media, news, video, video edit,
clip, short film, fanart, cosplay, rewatch, review, essay, infographic,
misc, contest, weekly, meme, merch
```
the end i decided to remove flair since it added complexity to labeling and felt like it was getting in the way of labeling and classifying 

### Reduction reasoning

| Original flairs | Decision | Reason |
|---|---|---|
| video, video edit, clip, short film | → merge | all fan/media video content |
| infographic, cosplay | → misc | seldom used, hard to categorize consistently |
| contest, merch | → misc | too infrequent to warrant their own class |
| what to watch?, help | → recommendation / misc | help = misc unless it's a rec request |
| essay, review | → discussion | these are opinions about specific anime |
| weekly | → misc | community infrastructure, not episode discussion |
| rewatch | → discussion | episode discussions about older anime |
| official media | → news | promo content is a subset of news |

### Final label set
```
discussion | news | misc | recommendation
```

---

## Label Definitions

**discussion** — episode discussions, rewatches, or opinion/debate questions about a specific anime, episode, or scene. Does NOT include posts that are recommending something.

> Example: `[Spoilers] Familiar of Zero 20th Anniversary Rewatch -- Season 4 Episode 1 (Episode 38)`

**news** — anime related news with a source (link), or promo content for an anime (video or image). Includes official interviews.

> Example: `"BanG Dream! Yume∞Mita" Anime | Main Visual`

**misc** — catch-all for everything else. Covers fan content (AMV clips, covers), general questions, help requests (that are not recommendation requests), community announcements, daily/weekly community posts, and anything that doesn't fit the other three labels.

> Example: `r/anime Karma Ranking & Discussion | Week 12 [Spring 2026]`

**recommendation** — any post that wants an anime recommendation or an anime-related recommendation (e.g. best X lists, what should I watch next, suggest anime with Y quality).

> Example: `What anime is so bad that it's actually fun to watch?`

---

## Hard Edge Cases & Annotation Rules

### discussion vs recommendation
- "Is X worth watching?" or "Does X get better?" → **discussion** (opinion about a specific anime)
- "What are some anime with [quality]?" → **recommendation** (asking for a list)
- "I recommend this anime" / "pick this up" → **recommendation** (promoting/suggesting an anime)
- Personal opinion posts about a specific named anime → **discussion**

### discussion vs misc
- Rewatch episode threads → **discussion**
- Rewatch interest/schedule/announcement threads → **misc** (organizing logistics, not discussing an episode)
- "Have I grown out of anime?" → **misc** (not about a specific anime)
- Opinion about a specific anime triggered by real-world events (e.g. author controversy) → **discussion**

### misc vs news
- Official promo content (key visuals, PVs, trailers) → **news**
- Fan covers, AMVs, video edits → **misc**
- Third-party interview articles → **news** (if it's reporting on an official interview)
- Karma ranking posts, weekly community threads → **misc**
- "Top 10 Anime of the Week" aggregator posts → **misc** (not a primary news source)

### misc vs recommendation

- "Should I watch X?" → **recommendation**
- "Is netflix better than crunchyroll?" → **misc** (platform question, even if body asks what to watch)

---

## Data Collection Plan

- Source: r/anime via the official Reddit API (required to access post body text; standard scraping only gets titles)
- Starting target: 200 labeled examples, scaling up until each category has 50–100 posts
- Final dataset: ~394 labeled examples after multiple scraping and labeling passes

---

## Evaluation Metrics Reasoning

- **Primary metric: accuracy** — overall correctness across all classes
- **Also tracking: precision and recall per class** — precision matters because false positives mean the model is confidently wrong; recall matters because a collapsed class (e.g. misc recall = 0) signals the model has given up on that label entirely
- **Target: beat the zero-shot baseline** (Groq llama-3.3-70b-versatile)

---

## AI Tool Plan

- Used Claude to help label the first batch of example posts — labeled 50 manually, had Claude finish the remaining ~350. Reviewed and corrected ~20 labels where Claude's judgment differed from the annotation rules.
- Fed evaluation metric results back to Claude to iteratively refine label definitions and resolve recurring boundary cases.
- Claude suggested hyperparameter changes (epochs, warmup steps, learning rate) based on observed training curves and per-class recall patterns.