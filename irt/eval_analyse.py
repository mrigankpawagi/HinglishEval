import csv
from binary_matrix import irt_data, irt_data2


# This is a custom evaluator for IRT parameters to compare results accross languages and models.

# Load the IRT data for GPT-4 models in Hinglish and English
gpt_4_hinglish = irt_data2["gpt_4"]
gpt_4_english = irt_data["gpt_4"]

# Any other model's data can be added too.


def diff_ques():
    """
    Prints the problems which have different answers in the English and Hinglish prompts.
    -- Correct in Hinglish but wrong in English
    -- Correct in English but wrong in Hinglish.
    """
    with open(
        "./irt_ratings/Combined_sorted_irt_itemparams.csv", newline=""
    ) as csvfile:
        csvreader = csv.DictReader(csvfile)
        csv_data = list(csvreader)  # Convert to list for easier access
        for i in range(164):
            diff = gpt_4_hinglish[i] - gpt_4_english[i]
            if diff == 1:
                for row in csv_data:
                    if int(row["PROBLEM"]) == i:
                        print(
                            f"1. PROBLEM: {i}, DIFFICULTY: {row['DIFFICULTY']}, DISCRIMINATION: {row['DISCRIMINATION']}"
                        )
            if diff == -1:
                for row in csv_data:
                    if int(row["PROBLEM"]) == i:
                        print(
                            f"-1. PROBLEM: {i}, DIFFICULTY: {row['DIFFICULTY']}, DISCRIMINATION: {row['DISCRIMINATION']}"
                        )


def diff_csv():
    """
    Create a csv which contains the diffs between English and Hinglish prompts for a given model.
    Also evaluates some average statistics related to the data.
    """
    # Open the input CSV file
    with open("./irt_ratings/Hinglish_irt_itemparams.csv", newline="") as csvfile:
        csvreader = csv.DictReader(csvfile)
        hinglish_csvdata = list(csvreader)  # Convert to list for easier access

    with open("./irt_ratings/English_irt_itemparams.csv", newline="") as csvfile:
        csvreader = csv.DictReader(csvfile)
        english_csvdata = list(csvreader)  # Convert to list for easier access

    # Initialize lists to store differences
    difficulty_diffs = []
    discrimination_diffs = []

    # count for which Hinglish has higher difficulty and discrimination
    diff_hinglish_count = 0
    disc_hinglish_count = 0
    # Loop through the range of problems and calculate differences
    for i in range(164):
        hinglish_row = next(
            (row for row in hinglish_csvdata if int(row["PROBLEM"]) == i), None
        )
        english_row = next(
            (row for row in english_csvdata if int(row["PROBLEM"]) == i), None
        )

        if hinglish_row and english_row:
            difficulty_diff = float(hinglish_row["DIFFICULTY"]) - float(
                english_row["DIFFICULTY"]
            )
            discrimination_diff = float(hinglish_row["DISCRIMINATION"]) - float(
                english_row["DISCRIMINATION"]
            )

            # update count
            if difficulty_diff > 0:
                diff_hinglish_count += 1
            if discrimination_diff > 0:
                disc_hinglish_count += 1

            difficulty_diffs.append(difficulty_diff)
            discrimination_diffs.append(discrimination_diff)

    # Write the differences to a new CSV file
    with open("differences.csv", mode="w", newline="") as csvfile:
        fieldnames = ["PROBLEM", "DIFFICULTY_DIFF", "DISCRIMINATION_DIFF"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(164):
            writer.writerow(
                {
                    "PROBLEM": i,
                    "DIFFICULTY_DIFF": round(difficulty_diffs[i], 3),
                    "DISCRIMINATION_DIFF": round(discrimination_diffs[i], 3),
                }
            )

    # Calculate the NET average differences
    net_avg_difficulty_diff = sum(difficulty_diffs) / len(difficulty_diffs)
    net_avg_discrimination_diff = sum(discrimination_diffs) / len(discrimination_diffs)

    print(
        f"NET Average DIFFICULTY Hinglish - English Difference: {net_avg_difficulty_diff}"
    )
    print(
        f"NET Average DISCRIMINATION Hinglish - English Difference: {net_avg_discrimination_diff}"
    )
    print("Hinglish has higher difficulty for", diff_hinglish_count, "questions")
    print("Hinglish has higher discrimination for", disc_hinglish_count, "questions")


if __name__ == "__main__":
    diff_ques()
    diff_csv()
