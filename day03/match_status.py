import csv
from pathlib import Path

from iou import iou

CASES = [
    {"id": "a", "existing": (0, 0, 2, 2),
     "generated": (0, 0, 2, 2), "nobody": False},

    {"id": "b", "existing": (0, 0, 2, 2),
     "generated": (1, 1, 3, 3), "nobody": False},

    {"id": "c", "existing": (0, 0, 2, 2),
     "generated": None, "nobody": True},
]

THRESHOLD = 0.5


def main():
    results = []

    for case in CASES:

        if case["nobody"]:
            score = None
            status = "no_positive"

        else:
            score = iou(case["existing"], case["generated"])

            if score >= THRESHOLD:
                status = "matched"
            else:
                status = "unmatched"

        trainable = status in ("matched", "no_positive")

        results.append({
            "id": case["id"],
            "iou": "" if score is None else score,
            "status": status,
            "trainable": trainable
        })

    # Create and write the CSV file
    output_path = Path(__file__).with_name("status.csv")

    with open(output_path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "iou", "status", "trainable"]
        )

        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    main()