1. Why is a frame shuffle a leak for video?

Frames from the same video can appear in both training and validation, making the model perform better on validation because it has already seen similar frames.

2. What does seed 42 buy you, and what does it not guarantee about quality?

Seed 42 makes the random split reproducible, but it does not guarantee a balanced split or good model performance.

3. When is accuracy a misleading score?

When the dataset is imbalanced. A model can achieve high accuracy by predicting only the majority class while missing the minority class.

4. Which score answers "Did we mark the right player?"

Player-level or instance-level evaluation checks whether the model identified the correct active player. Precision and recall can also help evaluate active-player detection.