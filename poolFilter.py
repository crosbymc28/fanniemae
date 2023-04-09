import pandas as pd
"""
loan_id,upb,note_rate,borrower_fico,coborrower_fico,coborrower_fico,state,dti,ltv,maturity_date,loan_term,property_type

Pool 1
Fico - 640 -745 
if 5 is none use 3

Note Rate 
between 5.0 -7.0 

DTI 35-50 

LTV 
75-85 
[400,850,1.5,6.5,20,60,70,99]
[730,770,1.5,9.0,35,45,90,95]
[550,740,1.5,7.0,20,45,0,85]
[720,850,2.0,5.0,10,45,70,80]
[690,790,3.0,7.0,15,35,70,85]
[675,780,3.0,7.0,30,55,60,85]
[670,750,3.0,7.0,47,52,35,80]
[600,700,3.0,7.0,,45,55,60,95]
[600,770,4,6,40,45,70,90]
[640,745,5.0,7.0,35,50,75,85]
"""

pool_needs = [[640,745,5.0,7.0,35,50,75,85],
              [600,770,4.0,6.0,40,45,70,90],
              [600,700,3.0,7.0,45,55,60,95],
              [670,750,3.0,7.0,47,52,35,80],
              [675,780,3.0,7.0,30,55,60,85],
              [690,790,3.0,7.0,15,35,70,85],
              [720,850,2.0,5.0,10,45,70,80],
              [550,740,1.5,7.0,20,45,0,85],
              [730,770,1.5,9.0,35,45,90,95],
              [400,850,1.5,6.5,20,60,70,99]]
def pool_filter(data,pool):
    #print(data) 
    #print(pool)
    #load_id = [],upb = [], note_rate = [],borrower_fico = [] ,coborrower_fico = [],combined_fico = [],state = [] ,dti = [] ,ltv = [] ,maturity_date = [] ,loan_term = [],property_type = [] 
    if data[5] == "nan" and data[3] == "nan": return None 
    fico = 0 
    if data[5] != "Nan": fico = int(data[3])
    else: fico = int(data[5]) 
    note_rate = float(data[2]) 
    
    DTI = int(data[7])
    LTV = int(data[8]) 
    #print(fico)
    #print(note_rate)
    #print(LTV)
    #print(DTI)
    

    
    #print(pool[0])
    #print(pool[1])
    #print(pool[2])
    #print(pool[3])
    #print(pool[4])
    #print(pool[5])
    #print(pool[6])
    #print(pool[7])
    #print("\n")
    # print("\n")

    # print((fico >= pool[0] and fico <= pool[1]))
    # print((note_rate >= pool[2] and note_rate <= pool[3] ))
    # print((LTV >= pool[4] and LTV <=pool[5]  ))
    # print((DTI >=pool[6]  and DTI <=pool[7]))

    if fico >= pool[0] and fico <= pool[1] and note_rate >= pool[2] and note_rate <= pool[3] and LTV >= pool[4] and LTV <=pool[5] and DTI >=pool[6]  and DTI <=pool[7]:
        print("Here")
        return data 
    #print("I am below")
    return None 

for i in range(9):
    clean_data = pd.read_csv("./fnma-leftover{}.csv".format(i), header=None).values
    unfilter_data = []
    filter_data = []
    for data in clean_data: 

        if pool_filter(data, pool_needs[i]) is None:
            
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
        df.to_csv("./fnma-class{}-hit.csv".format(i+1), mode='a', index=False, header=False)

    df = pd.DataFrame({"loan_id": unfilter_data[0], "upb":unfilter_data[1],"note_rate":unfilter_data[2], "borrower_fico":unfilter_data[3], "coborrower_fico":unfilter_data[4], "combined_fico":unfilter_data[5], 
                "state":unfilter_data[6], "dti": unfilter_data[7], "ltv":unfilter_data[8], "maturity_date":unfilter_data[9],"loan_term":unfilter_data[10], "property_type":unfilter_data[11] })
    df.to_csv("./fnma-leftover{}.csv".format(i+1), mode='a', index=False, header=False)