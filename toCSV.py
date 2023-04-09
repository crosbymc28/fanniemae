import pandas as pd 
number = 0 
max_num = 16
file_name = "fnma-dataset-0{}".format(number)
load_id = []
upb = [] 
note_rate = []
borrower_fico = [] 
coborrower_fico = []
combined_fico = []
state = [] 
dti = [] 
ltv = [] 
maturity_date = [] 
loan_term = []
property_type = [] 

"""
loan_id|
upb|
note_rate|
borrower_fico|
coborrower_fico|
combined_fico|
state|
dti|
ltv|
maturity_date|
loan_term|
property_type

"""
while number < max_num: 
    file_name = "fnma-dataset-0{}.txt".format(number)
    if number > 9: 
        file_name = "fnma-dataset-{}.txt".format(number)

    with open(file_name) as file: 
        for line in file: 
            data = str(line).rstrip().split("|")
            if data[6] == "" or data[3] == ""  or data[0] == ""  or data[2] == "" or data[7] == "" or data[8]  == "" or data[9] == "" or data[10] == "":
                continue 
            load_id.append(data[0])
            upb.append(data[1])
            note_rate.append(data[2])
            borrower_fico.append(data[3])
            coborrower_fico.append(data[4])
            combined_fico.append(data[5])
            state.append(data[6])
            dti.append(data[7])
            ltv.append(data[8])
            maturity_date.append(data[9])
            loan_term.append(data[10])
            property_type.append(data[11])
    number+=1 
df = pd.DataFrame({"loan_id": load_id, "upb":upb,"note_rate":note_rate, "borrower_fico":borrower_fico, "coborrower_fico":coborrower_fico, "combined_fico":combined_fico, 
              "state":state, "dti": dti, "ltv":ltv, "maturity_date":maturity_date,"loan_term":loan_term, "property_type":property_type })
df.to_csv("./fnma-clean-dataset.csv", mode='a', index=False, header=False)