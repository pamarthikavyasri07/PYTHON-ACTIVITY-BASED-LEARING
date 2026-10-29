Progressive Electricity Billing System
1. Problem Statement
The Progressive Electricity Billing System calculates household electricity bills based on the number of units consumed. It applies different electricity rates for different consumption slabs, along with fixed charges, surcharges, and rebates.
The program also compares bills for several months and identifies unusual increases in electricity bills. This helps households understand their electricity usage and manage their expenses.
2. Objectives
- Calculate electricity charges using multiple slabs.
- Add fixed charges and surcharges.
- Apply rebates to the bill.
- Compare electricity bills across multiple months.
- Identify unusual increases in monthly bills.
3. Algorithm
1. Start the program.
2. Enter the number of months.
3. For each month, enter the electricity units consumed.
4. Calculate charges using progressive slabs:
   - First 100 units: ₹2 per unit.
   - Next 100 units: ₹3 per unit.
   - Above 200 units: ₹5 per unit.
5. Add fixed charges of ₹50.
6. Add a surcharge of 5% on the energy charges.
7. Apply a 10% rebate on energy charges if consumption is below 100 units.
8. Calculate the final bill.
9. Compare each month's bill with the previous month's bill.
10. If the bill increases by more than 30%, display an unusual increase warning.
11. Display monthly bills and stop.
12. 
 4 flowchart 
   '''MERMAID A([Start]) --> B[/Enter units consumed/]
    B --> C[Calculate electricity charges]
    C --> D[Add fixed charges]
    D --> E[Apply surcharge and rebate]
    E --> F[Calculate final bill]
    F --> G[/Display bill/]
    G --> H([Stop])'''
6. Sample Input
Enter number of months: 3
Enter units for month 1: 80
Enter units for month 2: 120
Enter units for month 3: 250
7. Sample Output
Month 1 Bill: Rs. 202.00
Month 2 Bill: Rs. 323.00
Month 3 Bill: Rs. 837.50

Monthly Bill Comparison
Month 1 to Month 2: 59.90% change
Warning: Unusual bill increase!
Month 2 to Month 3: 159.29% change
Warning: Unusual bill increase!
Billing completed.


8. Expected Result
The program successfully calculates household electricity bills using progressive slabs, fixed charges, surcharges, and rebates. It compares consecutive monthly bills and displays a warning when the bill increases by more than 30%.
9. Sources / References
1. Python Software Foundation — Python Official Documentation
2. Python Tutorial — Control Flow Statements
3. Mermaid — Flowchart DocumentatioN

   
