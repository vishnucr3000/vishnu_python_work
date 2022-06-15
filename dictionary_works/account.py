account = {"acc_no": 123456,
           "acc_name": "vishnu",
           "acc_op_date": "01-04-2022",
           "acc_type": "savings",
           "acc_nominee": "praseena",
           "acc_bal": 20001}

# print(account["acc_no"])
# print(account["acc_name"])
# print(account.get("acc_type"))
# print(account.get("acc_bal"))
#
# if "acc_branch" in account:
#     account["acc_branch"]="Kakkanad"
# else:
#     account["acc_branch"]="Kochi"

account["acc_bal"] = account.get("acc_bal") - 1000 if account.get("acc_bal") > 20000 else account.get("acc_bal") - 500

print(account)
