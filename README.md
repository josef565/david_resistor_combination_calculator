# david_resistor_combination_calculator

What it does
Reads the resistor values you type in and calculates the total resistance
when they are connected in series and in parallel. It also saves the result
to a CSV file for you.

How to run it
Install Python 3, then run: Resistor_calculator.py 
 
Sample output. 
Enter how many resistors you have? 3 Enter value of resistor 1 (ohms)?  100 Enter value of resistor 2 (ohms)?  220 Enter value of resistor 3 (ohms)? 470

Result 
Total resistance in SERIES = 790 ohms 
Total resistance in PARALLEL = 60.1128 ohms 
Save this report to a CSV file? (y/n): y
Report saved to ‘resistor_report.csv’


 My own twist
The program can export a timestamped CSV report of your resistor list and
both totals, ready to open in Excel.

What I learned
I learned how to write to a file using Python's `csv` module, and how to
catch `OSError` so the program does not crash if the file cannot be saved.

Author 
JOSEPH DAVID OLUWATOBI , ND II MECHATRONICS ENGINEERING,
YABA COLLEGE OF TECHNOLOGY.
