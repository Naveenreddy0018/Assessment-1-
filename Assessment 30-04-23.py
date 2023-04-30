"""Question 1 - 
Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 
Book - Introduction to Python Programming : Rs 499.00
Book - Python Libraries Cookbook : Rs. 855.00
Book - Data Science in Python : Rs. 645.00
Taxes and additional charges are described as details - 
GST : 12%
Delivery Charges : Rs. 250.00   """

print("1.Book - Introduction to Python Programming : Rs 499.00")
print("2.Book - Python Libraries Cookbook : Rs. 855.00")
print("3.Book - Data Science in Python : Rs. 645.00")

book1 = int(input("Enter how many Introduction to Python Programming books you need: "))
price1 = 499.00 * book1

book2 = int(input("Enter how many Python Libraries Cookbook books you need: "))
price2 = 855.00 * book2

book3 = int(input("Enter how many Data Science in Python books you need: "))
price3 = 645.00 * book3

book_prices = price1 + price2 + price3
print("GST will be included i.e., 12%")
print("Delivery charges will be Rs. 250.00")
total_price = book_prices + book_prices * 0.12 + 250.00

print("The Total Invoice amount for all the purchases: ", total_price)



"""Question 2 - 
Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.

Input : string1 = "India"
Output : uniqueLetters = i,n,d,a

Input : string1 = "Dedication"
Output : uniqueLetters = d,e,i,c,a,t,o,n            """

st = input("Enter the string: ")
st = st.lower()
final_st = []
for i in st:
    if i not in final_st:
        final_st.append(i)
    else:
        pass

a = ",".join(final_st)
print(a)