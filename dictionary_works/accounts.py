accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]

# print details of account 1002

acdetails = [ac for ac in accounts if ac["acno"] == 1002]

print(acdetails)

# print accounts of saving account type

saving_acc = [ac["acno"] for ac in accounts if ac["ac_type"] == "savings"]

print(saving_acc)

# sort account based on balance order by desc

accounts.sort(reverse=True, key=lambda ac: ac["balance"])
print(accounts)

sort_acc = sorted(accounts, reverse=True, key=lambda ac: ac["balance"])

print(sort_acc)

# print all transaction where transaction amount greater than 500

for acc in accounts:
    trans = [tr for tr in acc["transactions"] if tr["amount"] > 500]
    print(trans)

# print all phone pay transactions

all_tran=[ac["transactions"] for ac in accounts]
p_tran=[trans for tlist in all_tran for trans in tlist if trans["method"]=="phone-pay"]
print(p_tran)

# print all credit transactions of 1002

amt=[amount for tlist in all_tran for amount in tlist if amount["to"]==1002]

print(amt)

# aggregate transactions based on payment mode
agg={}
ag_tran=[tran for at in all_tran for tran in at]
for mtd in ag_tran:
    p_method=mtd["method"]
    p_amt=mtd["amount"]
    if p_method in agg:
        agg[p_method]+=p_amt
    else:
        agg[p_method]=p_amt
max_tran=max(agg.items(),key=lambda item:item[1])
print(max_tran)






