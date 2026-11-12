Day 5 — Tennis Pipeline Questions
1. The existing annotations already contain player boxes. What do they not contain, that the pipeline has to generate?

The existing annotations contain the bounding boxes of the blue and orange players, but they do not tell us which player is currently active and which is passive. The pipeline has to generate this active/passive information based on the player's position relative to the ball.

Skill: IoU statuses / Data labelling

2. Which frame statuses are allowed into the training path?

Only two statuses are allowed:
- matched – The generated bounding box matches an existing player box with IoU ≥ 0.5.
- no_positive – There is no positive player label to train on, such as a frame where nobody is active.
Other statuses such as unmatched, no_box, no_generator_result, and outside_window are not allowed into the training path.

Skill: IoU statuses

3. Why does one sample use three frames instead of one photo?

One photo only shows what is happening at a particular moment. Three consecutive frames (t-2, t-1, and t) provide information about how the players are moving over time. This helps the model understand the movement and identify which player is active.

Skill: Channels

4. What do the extra mask channels tell the model?

The three extra mask channels provide additional information about the candidate regions in each of the three frames. They highlight the areas of interest so the model can use both the original RGB images and the candidate mask information.

Skill: Channels

5. Why is the train/validation split done by video?

Frames from the same video can look very similar. If we randomly split individual frames, some frames from the same video may go into training and others into validation. This can cause data leakage and make the validation results look better than they actually are.

Therefore, we split by video ID so that frames from one video stay together in either training or validation.

Skill: Source split

6. What question do correct / missed / wrong player / false active answer, that mAP does not?

These categories help us understand whether the system makes the correct application-level decision:
- Correct: The correct player is identified as active.
- Missed: The actual active player is not identified.
- Wrong player: The system identifies the wrong player as active.
- False active: The system predicts an active player when there should not be one.
mAP measures how well the model detects objects and their bounding boxes. These categories tell us whether the system actually identifies the correct active player.

Skill: Audit / Evaluation

7. Why does the write-up want a small human-labeled benchmark?

Automatically generated labels can sometimes be incorrect. A small human-labeled benchmark gives us trusted labels to compare against the generated labels. This helps us identify mistakes, measure how reliable the generated labels are, and check whether the model is learning from correct data.

Skill: Audit