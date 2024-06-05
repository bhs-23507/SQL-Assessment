# Import the company database into this code
import sqlite3

# What the database is
DATABASE = "company.db"

def print_table_header():
    print(f"company name                 market cap          foun.year    foun.name               sector")

# Functions
# Function to print all companies ordered by company id in ascending order
def print_all_companies():
    "print all companies sorted by id in ascending order"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company ORDER BY id ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print_table_header()
    for company in results:
        print(f"{company[1]:<29}{company[2]:<20}{company[3]:<13}{company[4]:<24}{company[5]:<10}")
    db.close()

# Function to print all the tables and information of the first company
def print_all_info_of_first_company():
    "print all information on first company"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company ORDER BY id ASC LIMIT 1;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print_table_header()
    for company in results:
        print(f"{company[1]:<29}{company[2]:<20}{company[3]:<13}{company[4]:<24}{company[5]:<10}")
    db.close()

# Function to print all the information of the top three companies
def print_all_info_of_top_three_companies():
    "print all information of the top three companies"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company ORDER BY id ASC LIMIT 3;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print_table_header()
    for company in results:
        print(f"{company[1]:<29}{company[2]:<20}{company[3]:<13}{company[4]:<24}{company[5]:<10}")
    db.close()

# Function to print all the companies sorted by the founding year in descending order
def print_all_companies_sorted_by_founding_year():
    "print all companies sorted by founding year"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company ORDER BY founding_year DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print_table_header()
    for company in results:
        print(f"{company[1]:<29}{company[2]:<20}{company[3]:<13}{company[4]:<24}{company[5]:<10}")
    db.close()

# Function to print all the companies with the sector, Technology
def print_all_companies_with_sector_Technology():
    "print all companies with the sector Technology"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company WHERE sector = 'Technology';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print_table_header()
    for company in results:
        print(f"{company[1]:<29}{company[2]:<20}{company[3]:<13}{company[4]:<24}{company[5]:<10}")
    db.close()

# Function to print all the companies sorted by market cap in descending order
def print_all_companies_sorted_by_market_cap():
    "print all companies sorted by market cap"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company ORDER BY market_cap DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print_table_header()
    for company in results:
        print(f"{company[1]:<29}{company[2]:<20}{company[3]:<13}{company[4]:<24}{company[5]:<10}")
    db.close()

# Function to print all the information of the top five companies
def print_all_info_of_top_five_companies():
    "print all information of the top five companies"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company ORDER BY id ASC LIMIT 5;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print_table_header()
    for company in results:
        print(f"{company[1]:<29}{company[2]:<20}{company[3]:<13}{company[4]:<24}{company[5]:<10}")
    db.close()

# Function to print all the companies with a market cap more than a trillion
def print_all_companies_with_market_cap_more_than_trillion():
    "print all companies with more than a trllion, market cap"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM company WHERE market_cap > 1000000000000;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print_table_header()
    for company in results:
        print(f"{company[1]:<29}{company[2]:<20}{company[3]:<13}{company[4]:<24}{company[5]:<10}")
    db.close()

# Main code
while True:
    # The user can choose options given, 1-10
    user_input = input("\n1. Print all companies\n2. Print all information of the first company\n3. Print all information of the top three companies\n4. Print all companies sorted by founding year\n5. Print all companies with the sector Technology\n6. Print all companies sorted by market cap\n7. Print all information of the top five companies\n8. Print all companies with market cap more than a trillion\n9. Exit\n\n")
    # If the user inputted 1, print all companies
    if user_input == "1":
        print_all_companies()
    # If the user inputted 2, print all the information of the first company
    elif user_input == "2":
        print_all_info_of_first_company()
    # If the user inputted 3, print all the information of the top three companies
    elif user_input == "3":
        print_all_info_of_top_three_companies()
    # If the user inputted 4, print all the companies sorted by founding year in descending order
    elif user_input == "4":
        print_all_companies_sorted_by_founding_year()
    # If the user inputted 5, print all the companies with the sector, Technology
    elif user_input == "5":
        print_all_companies_with_sector_Technology()
    # If the user inputted 6, print all the companies sorted by market cap in descending order
    elif user_input == "6":
        print_all_companies_sorted_by_market_cap()
    # If the user inputted 7, print all the information of the top five companies
    elif user_input == "7":
        print_all_info_of_top_five_companies()
    # If the user inputted 8, print all the market cap with more than a trillion
    elif user_input == "8":
        print_all_companies_with_market_cap_more_than_trillion()
    # If the user inputted 9, stop the loop and exit
    elif user_input == "9":
        break
    # Else if the user enters any other number or alphabet, tell them that it's not an option.
    else:
        print("That was not an option\n")