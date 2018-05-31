import csv

# Files to Load

filepath = "budget_data_2.csv"
output = "budget_Data_2_analysis.txt"

# Variables to store values for total months, total revenue

total_months = 0
total_rev = 0

# to calculate the change in Revenue we need to declare Two Variables which will store 
# the previous value and store it in Revenue Change  

prev_revenue = 0
revenue_change = 0


increase = ["", 0]

decrease = ["", 9999999999999999999999]

revenue_changes = []


# Read Files

with open(filepath) as revenue_data:

    reader = csv.DictReader(revenue_data)

    # for all the rows of data in excel file the loop will run through each row

    for row in reader:



        # Calculate the totals

        total_months = total_months + 1

        total_rev = total_rev + int(row["Revenue"])

        # Keep track of changes

        revenue_change = int(row["Revenue"]) - prev_revenue

        prev_revenue = int(row["Revenue"])

        
        # Determine the greatest increase

        if (revenue_change > increase[1]):

            increase[1] = revenue_change

            increase[0] = row["Date"]



        if (revenue_change < decrease[1]):

            decrease[1] = revenue_change

            decrease[0] = row["Date"]



        # Add to the revenue_changes list

        revenue_changes.append(int(row["Revenue"]))



    # Set the Revenue average

    revenue_avg = sum(revenue_changes) / len(revenue_changes)

    

    # print required summary

    print("-------------------------")
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_rev))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + str(increase[0]) + " ($" +  str(increase[1]) + ")") 
    print("Greatest Decrease: " + str(decrease[0]) + " ($" +  str(decrease[1]) + ")")


    # to create an output file as file type as "Text"

    # Output Files

with open(output, "w") as txt_file:

    txt_file.write("----------------------------------------------------")
    txt_file.write("\n")
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("----------------------------------------------------")
    txt_file.write("\n")

    txt_file.write("Total Months: " + str(total_months))

    txt_file.write("\n")

    txt_file.write("Total Revenue: " + "$" + str(total_rev))

    txt_file.write("\n")

    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))

    txt_file.write("\n")

    txt_file.write("Greatest Increase: " + str(increase[0]) + " ($" + str(increase[1]) + ")") 

    txt_file.write("\n")

    txt_file.write("Greatest Decrease: " + str(decrease[0]) + " ($" + str(decrease[1]) + ")")

