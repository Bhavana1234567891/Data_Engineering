<!-- Task 4 -->

The missing field is `camera_id`.\
It identifies which camera recorded each video.\
We should retain videos from both cameras because they provide different perspectives.\
However, `match_id` should group videos from the same match during dataset splitting.\
This ensures all camera views of one match stay together in either training or validation.

Accepted suggestion:  Add match_id, camera_id

1. match_id: Identifies the actual tennis match. Multiple videos recorded by different cameras can belong to the same match. This field helps group related videos together during training/validation splitting and prevents data leakage.

2. camera_id: Identifies which camera recorded a particular video. Since different cameras capture the same match from different angles, we should retain both perspectives rather than discard one.




1. What is a manifest?

It has record of the dataset samples and their metadata.
it also stores information about classes, train/validation files, and the source of the data.

2. Why do rejected rows stay in the file?

Rejected rows are not deleted. We mark them as non-trainable using trainable = false
We can understand why a particular sample was rejected.
We maintain traceability of all samples.
We avoid losing useful information.

3. Why does the second run get a new folder?

 The 2nd run get a new folder,as we dont want the new values replace the old result we want to keep all those results. That's why we will keep the 2nd run as well along with the 1st run and we can also analyze whether the 1st run value change after the 2nd run and we can even verify whether the values are same or not. 

 4. Which two statuses are trainable, and why is unmatched not one of them?

The two trainable statuses are:
1. matched
2. no_positive

unmatched is not one of the because A label is generated, but matching fails.