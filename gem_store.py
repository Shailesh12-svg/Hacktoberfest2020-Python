gems_list = ["Emrald","Ivory","Jasper","Ruby","Garnet"]
price_list=[2760,2119,1599,3920,3999]

reqd_gems=["Ivory","Emrald","Garnet"]
reqd_quantity=[2,3,5]

def calculate_bill(gems_list,price_list,reqd_gems,reqd_quantity):
    price_dict=dict(zip(gems_list,price_list))
    reqd_dict=dict(zip(reqd_gems,reqd_quantity))

    try:
        bill=sum(price_dict[gem] * reqd_dict[gem] for gem in reqd_dict)
    except KeyError:
        return -1

    if bill>3000:
        bill=0.95*bill
        return bill

bill_amount=calculate_bill(gems_list,price_list,reqd_gems,reqd_quantity)
print(bill_amount)


