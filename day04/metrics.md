For this worked example:

- Total candidates = 10
- Actual positives = 2
- Actual negatives = 8
- Predicted positives = 3
- Of those 3 predicted positives, only 1 is correct.

### Completed table

| Quantity             | Value  |
| -------------------- | ------ |
| True positives (TP)  | 1      |
| False positives (FP) | 2      |
| False negatives (FN) | 1      |
| True negatives (TN)  | 6      |
| Accuracy             | 70%    |
| Positive precision   | 33.33% |
| Positive recall      | 50%    |

Accuracy = (TP + TN) / Total
         = (1 + 6) / 10
         = 70%

Precision = TP / (TP + FP)
          = 1 / (1 + 2)
          = 1/3
          = 33.33%

Recall = TP / (TP + FN)
       = 1 / (1 + 1)
       = 1/2
       = 50%

Remember the difference: Precision tells us how many of the model's positive predictions were correct. Recall tells us how many of the actual positives the model successfully found.


## Four possible prediction outcomes

Consider a video frame where the **true active player is A**.

| Actual truth | Model prediction | Outcome           |
| ------------ | ---------------- | ----------------- |
| A            | A                | Correct detection |
| A            | nobody           | Missed detection  |
| A            | C                | Wrong instance    |

Now consider a second frame where the **true active player is nobody**, but the model predicts A.

| Actual truth | Model prediction | Outcome        |
| ------------ | ---------------- | -------------- |
| nobody       | A                | False positive |

### Explanation

1. **Correct detection:** The model correctly identifies the actual active player.
2. **Missed detection:** An active player is present, but the model predicts nobody.
3. **Wrong instance:** The model identifies a player as active, but it is the wrong player.
4. **False positive:** Nobody is active, but the model incorrectly predicts a player as active.

**Key takeaway:** The model should not only detect whether someone is active; it should also identify the correct active player.
