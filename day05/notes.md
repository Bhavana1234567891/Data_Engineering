1. What is in channels 0, 4, 8, and 11 of today's sample?

Today's sample contains 12 channels:
- Channel 0: Red channel of the oldest frame (t-2).
- Channel 4: Green channel of the previous frame (t-1).
- Channel 8: Blue channel of the current frame (t).
- Channel 11: Candidate mask of the current frame (t).
We have 9 RGB channels from three frames and 3 additional candidate mask channels.

2. Why is an empty label file a real sample?

An empty label file represents a frame where there is no active player or positive object to label. It is still useful training data because the model needs to learn not only when an active player exists but also when nobody should be identified as active.

3. What would go wrong if you scored a model only against the generator?

The generator can sometimes produce incorrect labels. If we evaluate the model only against generator labels, we might think the model is performing correctly even when those labels are wrong. This can give us misleading evaluation results.

That is why we need human-verified labels to check the generator's accuracy.

4. Which exit-ticket row are you least sure about? That row is the first thing you re-read on Day 6.

I am least sure about the Application metric row. I want to understand more clearly how correct, missed, wrong instance, and false positive are used to evaluate whether the model identifies the correct active player.