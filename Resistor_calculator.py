"""
Resistor Combination Calculator
--------------------------------
Asks the user how many resistors they have, reads each value, and prints
the total resistance when connected in SERIES and in PARALLEL.

Feature: CSV Report Export
  After the results are shown, the user can save a timestamped CSV file
  containing the resistor inventory plus both totals. The file opens
  directly in Excel / LibreOffice / Google Sheets for a lab report.

Formulas:
    Series:    R_total = R1 + R2 + ... + Rn
    Parallel:  R_total = 1 / (1/R1 + 1/R2 + ... + 1/Rn)
"""
import csv                                    # used to write the report file
from datetime import datetime                 # used to timestamp the report
# ---------------------------------------------------------------
# FUNCTION 1: ask for the number of resistors (returns a value)
# ---------------------------------------------------------------
def get_resistor_count():
    """Ask for and validate how many resistors the user has."""
    while True:                                   # keep asking until valid
        text = input("How many resistors do you have? ")

        try:
            count = int(text)                     # convert to int
        except ValueError:                        # not a whole number
            print("  -> That's not a whole number. Please enter e.g. 3\n")
            continue

        # if/elif/else decision on the number entered
        if count < 1:
            print("  -> You need at least one resistor. Try again.\n")
        elif count > 1000:
            print("  -> That's too many. Please enter 1000 or fewer.\n")
        else:
            return count                          # valid -> return the number

# ---------------------------------------------------------------
# FUNCTION 2: ask for each resistor value (returns a list)
# ---------------------------------------------------------------
def get_resistor_values(count):
    """Read 'count' resistor values and return them as a list of floats."""
    values = []                                   # the LIST that holds the values

    for i in range(count):                        # LOOP once per resistor
        while True:                               # keep asking until valid
            text = input(f"  Enter value of resistor {i + 1} (ohms): ")

            try:
                value = float(text)               # convert to float
            except ValueError:
                print("    -> That's not a number. Try something like 100 or 4.7\n")
                continue

            if value <= 0:                        # resistance must be positive
                print("    -> Resistance must be greater than zero.\n")
            else:
                values.append(value)              # store the value in the list
                break                             # move on to the next resistor

    return values                                 # return the whole list

# ---------------------------------------------------------------
# FUNCTION 3: series total (returns a value)
# ---------------------------------------------------------------
def series_resistance(values):
    """Return the total resistance of the list connected in series."""
    total = 0.0
    for r in values:                              # add every value together
        total += r
    return total
# ---------------------------------------------------------------
# FUNCTION 4: parallel total (returns a value)
# ---------------------------------------------------------------
def parallel_resistance(values):
    """Return the total resistance of the list connected in parallel."""
    reciprocal_sum = 0.0
    for r in values:                              # add up 1/R for each resistor
        reciprocal_sum += 1.0 / r
    return 1.0 / reciprocal_sum

# ===============================================================
# NEW FEATURE: CSV report export
# ===============================================================

# ---------------------------------------------------------------
# FUNCTION 5: ask for the output filename (returns a value)
# ---------------------------------------------------------------
def ask_export_filename():
    """Ask the user for a filename, apply a sensible default, and return it."""
    text = input("Filename for the report (blank = resistor_report.csv): ").strip()

    if text == "":                                # blank -> use the default
        filename = "resistor_report.csv"
    else:
        filename = text

    # if/elif/else — make sure the file always ends in .csv
    if filename.lower().endswith(".csv"):
        return filename
    elif "." in filename:
        print("  -> Adding '.csv' so the extension is correct.")
        return filename + ".csv"
    else:
        return filename + ".csv"

# ---------------------------------------------------------------
# FUNCTION 6: write the CSV file (returns the filename used)
# ---------------------------------------------------------------
def export_csv(values, r_series, r_parallel, filename):
    """
    Write a report file with metadata, the resistor inventory, and both
    totals. Returns the filename written so the caller can confirm it.

    Raises OSError (e.g. permission denied) — the caller handles it.
    """
    # newline="" is required by the csv module on Windows to avoid blank rows
    with open(filename, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)

        # ---- metadata block -------------------------------------
        writer.writerow(["Resistor Combination Report"])
        writer.writerow(["Generated", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        writer.writerow(["Resistor count", len(values)])
        writer.writerow([])                       # blank separator row

        # ---- inventory + totals table ---------------------------
        writer.writerow(["Item", "Value (ohms)"])

        for i, r in enumerate(values, start=1):   # LOOP over the resistor list
            writer.writerow([f"R{i}", f"{r:.10g}"])

        writer.writerow(["Series total",   f"{r_series:.10g}"])
        writer.writerow(["Parallel total", f"{r_parallel:.10g}"])

    return filename                               # report saved successfully

# ---------------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------------
def main():
    print("=" * 44)
    print("   RESISTOR COMBINATION CALCULATOR")
    print("=" * 44)

    count = get_resistor_count()                  # ask how many
    print()
    values = get_resistor_values(count)           # collect the values in a list

    # calculate both totals
    r_series = series_resistance(values)
    r_parallel = parallel_resistance(values)

    # show what the user entered
    print("\nYou entered:")
    for i, r in enumerate(values, start=1):       # loop for the report
        print(f"  R{i} = {r:g} ohms")

    # print the results
    print("\nResults:")
    print(f"  Total resistance in SERIES   = {r_series:g} ohms")
    print(f"  Total resistance in PARALLEL = {r_parallel:g} ohms")

    # ---------------------------------------------------------
    # NEW FEATURE: offer to save a CSV report
    # ---------------------------------------------------------
    print("\n" + "-" * 44)
    answer = input("Save this report to a CSV file? (y/n): ").strip().lower()

    if answer == "y":
        filename = ask_export_filename()
        try:
            saved_as = export_csv(values, r_series, r_parallel, filename)
        except OSError as error:                  # disk full, permission denied, ...
            print(f"  -> Could not write the file: {error}")
        else:
            print(f"  -> Report saved to '{saved_as}'.")

    elif answer == "n":
        print("  Okay — no file written.")
    else:
        print("  I'll take that as a 'no' — no file written.")


# Run main() only when the file is executed directly
if __name__ == "__main__":
    main()
  
