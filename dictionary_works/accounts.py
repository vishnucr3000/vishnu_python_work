import os

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

acc_details=[ac for ac in accounts if ac["acno"]==1002]

print(acc_details)


# print accounts of saving account type

savings_ac=[sa for sa in accounts if sa["ac_type"]=="savings"]
print(savings_ac)


# sort account based on balance order by desc

print(sorted(accounts,key=lambda ac:ac["balance"],reverse=True))


# print all transaction where transaction amount greater than 500

all_transactions=[trans for tlist in accounts for trans in tlist["transactions"] if trans["amount"]<500]

print(all_transactions)

# print all phone pay transactions

phone_pay_tran=[pp for translist in accounts for pp in translist["transactions"] if pp["method"]=="phone-pay" ]
print(phone_pay_tran)

# print all credit transactions of 1002

credit_trans=[credit_tran for credit_trans_list in accounts for credit_tran in credit_trans_list["transactions"] if credit_tran["to"]==1002]
print(credit_trans)

# aggregate transactions based on payment mode

agg={}

for slist in accounts:
    for trans in slist["transactions"]:
        t_method=trans["method"]
        t_amount=trans["amount"]
        if t_method in agg:
            agg[t_method]+=t_amount
        else:
            agg[t_method]=t_amount
print(max(agg.items(),key=lambda ag:ag[1]))

# print sum of all transactions

print(sum([t["amount"] for nlist in accounts for t in nlist["transactions"]]))

# print min of all transactions

print(min(m["amount"] for mlist in accounts for m in mlist["transactions"]))

# update a dictionary

agg.update({"g-pay":500})

print(agg)

# sort dictionary keys desc

dictionary={
    5:10,
    2:4,
    7:14,
    4:8,
    9:18
}

print(sorted((i for i in dictionary.keys()),reverse=True))

print(sorted((j for j in dictionary.values()),reverse=True))

print(sorted(dictionary.items(),key=lambda k:(k[0],k[1]),reverse=False))

# print dictionary based on keys sorted des

for i in dictionary.keys():
    print((i,dictionary[i]))

print(sorted(dictionary.items(),reverse=True))

from operator import itemgetter

lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print(sorted(lis,key=itemgetter("age")))




