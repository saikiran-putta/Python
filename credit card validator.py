#step1 = remove "-" or " "
#step2 = add the odd dgits
#step3 = double the even digits if sum is >10 add up the digits
#step4 = add step2 and step3
#step5 = if sum in step4 is divisible by 10 then card number is valid
sum_odd_digits = 0
sum_even_digits = 0
credit_card_number = input("Enter the card number: ")
credit_card_number = credit_card_number.replace("-","")
credit_card_number = credit_card_number.replace(" ","")

for x in credit_card_number[::2]:
    sum_odd_digits += int(x)

for x in credit_card_number[1::2]:
    x = int(x) * 2
    if x > 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

total = sum_odd_digits + sum_even_digits

if total % 10 == 0:
    print("CREDIT CARD IS VALID")
else:
    print("CREDIT CARD IS INVALID")

