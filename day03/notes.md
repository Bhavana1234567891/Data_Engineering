1. What does an IoU of 1 mean? What does an IoU near 0.14 mean at a 0.5 threshold?

IoU of 1 means that both the bounding boxes completely overlap, intersection area is equal to the union area and also the predicted bounding box and the groundtruth bounding box are same.

2. Why is an empty file different from a missing file?

Empty file: when the status is no_positive(nothing to identify inside the bounding box)
Missing file: when the status is unmatched(the predicted bounding box don't match with the correct bounding box in the ground truth).

3. What do the four numbers after the class id mean?

The four numbers after the class id in yolo representation are the x_center, y_center, width and the height for the bounding box.