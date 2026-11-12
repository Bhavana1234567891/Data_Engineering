# Day 5 — Exit Ticket

| Field | Rally Cam, if you adopt the example | My project |
|---|---|---|
| Domain | Synthetic two-player video | Synthetic two-player video |
| Decision unit | One video frame | One video frame |
| Classes | active, passive, and nobody (empty label) | active, passive, and nobody (empty label) |
| Labels that already exist | Blue and orange player boxes | Blue and orange player boxes |
| Label I will generate | Which player is closer to the ball, if either is within 150 pixels | Which player is closer to the ball, if either is within 150 pixels |
| Match rule | IoU ≥ 0.5 against an existing player box | IoU ≥ 0.5 against an existing player box |
| Trainable statuses | `matched` and `no_positive` | `matched` and `no_positive` |
| Split unit | One video ID, not one frame | One video ID, not one frame |
| Model input | 12 channels: 3 RGB frames plus 3 candidate masks | 12 channels: 3 RGB frames plus 3 candidate masks |
| Application metric | correct, missed, wrong instance, false positive | correct, missed, wrong instance, false positive |
| Audit size | 5 frames I will look at, standing in for a 50-frame benchmark | 5 frames I will look at, standing in for a 50-frame benchmark |