import pandas as pd

def class_filter(data, maturity_date, loan_term):
    if (maturity_date == data[9]) and (loan_term == data[10]):
        return data
    return None

##################################################################################################

for i in range(43643):
    clean_data = pd.read_csv(r"C:\Users\kingk\Downloads\bitcamp\class8\fnma-class8-leftover{}.csv".format(i),header=None).values
    unfilter_data = []
    filter_data = []

    for data in clean_data: 

        if class_filter(data, clean_data[0][9], clean_data[0][10]) is None:
            
            if len(unfilter_data) == 0: 
                unfilter_data.append([data[0]]),unfilter_data.append([data[1]]),unfilter_data.append([data[2]]),unfilter_data.append([data[3]]),unfilter_data.append([data[4]]),unfilter_data.append([data[5]]),unfilter_data.append([data[6]]),unfilter_data.append([data[7]]),unfilter_data.append([data[8]]),unfilter_data.append([data[9]]),unfilter_data.append([data[10]]),unfilter_data.append([data[11]])
            
        
            else: 
                unfilter_data[0].append(data[0])
                unfilter_data[1].append(data[1])
                unfilter_data[2].append(data[2])
                unfilter_data[3].append(data[3])
                unfilter_data[4].append(data[4])
                unfilter_data[5].append(data[5])
                unfilter_data[6].append(data[6])
                unfilter_data[7].append(data[7])
                unfilter_data[8].append(data[8])
                unfilter_data[9].append(data[9])
                unfilter_data[10].append(data[10])
                unfilter_data[11].append(data[11])
        else:
            if len(filter_data) == 0: 
                filter_data.append([data[0]])
                filter_data.append([data[1]])
                filter_data.append([data[2]])
                filter_data.append([data[3]])
                filter_data.append([data[4]])
                filter_data.append([data[5]])
                filter_data.append([data[6]])
                filter_data.append([data[7]])
                filter_data.append([data[8]])
                filter_data.append([data[9]])
                filter_data.append([data[10]])
                filter_data.append([data[11]])

            else: 
                filter_data[0].append(data[0])
                filter_data[1].append(data[1])
                filter_data[2].append(data[2])
                filter_data[3].append(data[3])
                filter_data[4].append(data[4])
                filter_data[5].append(data[5])
                filter_data[6].append(data[6])
                filter_data[7].append(data[7])
                filter_data[8].append(data[8])
                filter_data[9].append(data[9])
                filter_data[10].append(data[10])
                filter_data[11].append(data[11])
                print("hello")
        
    print(len(filter_data))
    print(len(unfilter_data))

    if(len(filter_data)):
        df = pd.DataFrame({"loan_id": filter_data[0], "upb":filter_data[1],"note_rate":filter_data[2], "borrower_fico":filter_data[3], "coborrower_fico":filter_data[4], "combined_fico":filter_data[5], 
                "state":filter_data[6], "dti": filter_data[7], "ltv":filter_data[8], "maturity_date":filter_data[9],"loan_term":filter_data[10], "property_type":filter_data[11] })
        df.to_csv(r"C:\Users\kingk\Downloads\bitcamp\class8\fnma-class8-{}.csv".format(i), mode='w', index=False, header=False)
    if(len(unfilter_data)):
        df = pd.DataFrame({"loan_id": unfilter_data[0], "upb":unfilter_data[1],"note_rate":unfilter_data[2], "borrower_fico":unfilter_data[3], "coborrower_fico":unfilter_data[4], "combined_fico":unfilter_data[5], 
                    "state":unfilter_data[6], "dti": unfilter_data[7], "ltv":unfilter_data[8], "maturity_date":unfilter_data[9],"loan_term":unfilter_data[10], "property_type":unfilter_data[11] })
        df.to_csv(r"C:\Users\kingk\Downloads\bitcamp\class8\fnma-class8-leftover{}.csv".format(i+1), mode='w', index=False, header=False)
        #temp = i+1
    #let = "fnma-class3-leftover{}.csv".format(temp)