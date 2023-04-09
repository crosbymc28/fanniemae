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

for i in range (291):
    tot = 0

    clean_data = pd.read_csv(r"C:\Users\kingk\Downloads\bitcamp\class8\fnma-class8-{}.csv".format(i),header=None).values
    for data in clean_data: 
        tot += data[1]

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

    sizes = [[5000000,20000000],
            [5000000,20000000],
            [5000000,20000000],
            [5000000,20000000],
            [5000000,20000000],
            [5000000,30000000],
            [5000000,30000000],
            [15000000,40000000],
            [15000000,40000000],
            [15000000,40000000]]

    
    if tot < sizes[3][0]:
        continue
        #print("you suck, go away")
    elif tot > sizes[3][1]:
        df = pd.DataFrame({"loan_id": load_id, "upb":upb,"note_rate":note_rate, "borrower_fico":borrower_fico, "coborrower_fico":coborrower_fico, "combined_fico":combined_fico, "state":state, "dti": dti, "ltv":ltv, "maturity_date":maturity_date,"loan_term":loan_term, "property_type":property_type })
        df.to_csv(r'class8\pool-8-{}'.format(i), header=None, index=None, sep='|', mode='a')

    else:
        #print("I work tho!!!--------------- " + str(i))
        df = pd.DataFrame({"loan_id": load_id, "upb":upb,"note_rate":note_rate, "borrower_fico":borrower_fico, "coborrower_fico":coborrower_fico, "combined_fico":combined_fico, 
              "state":state, "dti": dti, "ltv":ltv, "maturity_date":maturity_date,"loan_term":loan_term, "property_type":property_type })
        df.to_csv(r'class8\pool-8-{}'.format(i), header=None, index=None, sep='|', mode='a')

    #print(tot)