# Day 15 — Python Automation Project

# B) Report Generator — reads a CSV and produces a formatted text summary

import csv

def read_scores(filename):
    """Function 1: Safely reads the CSV scores using column names"""
    scores = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file) # Uses column names instead of row index
            for row in reader:
                if row.get('score'): # Finds the score column directly
                    scores.append(float(row['score']))
        return scores

    except FileNotFoundError:
        print(f"Edge Case 1: The file '{filename}' was not found.")
        return[]
    except ValueError:
        print("Edge Case 2: Found invalid, non-numeric data in the CSV file.")
        return[]
    except ValueError:
        print("Edge Case 2: Found invalid, non-numeric data in the CSV file.")
        return[]

def calculate_stats(scores):
    """Function 2: Calculates the required statistics"""
    if not scores:
        return None

    return{
        "total": len(scores),
        "average": round(sum(scores) / len(scores), 2),
        "highest": max(scores),
        "lowest": min(scores)
    }

def save_report(stats, output_filename):
    """Function 3: Writes the results to a text file"""
    if not stats:
        print("Automation stopped: No valid data available to save.")
        return

    with open(output_filename, 'w') as file:
        file.write(f"Total Records: {stats['total']}\n")
        file.write(f"Average Score: {stats['average']}\n")
        file.write(f"Highest Score: {stats['highest']}\n")
        file.write(f"Lowest Score: {stats['lowest']}\n")

    print("Report generated successfully!")


# Main Execution Lineup
if __name__ == "__main__":
    # 1. Input
    scores_list = read_scores("data/students.csv")

    # 2. Process
    report_stats = calculate_stats(scores_list)

    # 3. Output
    save_report(report_stats, "data/report.txt")
    