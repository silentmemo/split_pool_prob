
import random
import matplotlib.pyplot as plt



def simulate_experiment(tag_barcode, pcr_index,input_cell,sort_cell): 
    number_of_tag_barcode = tag_barcode
    number_of_pcr_index = pcr_index
    input_cell_number = input_cell
    sort_cell_number = sort_cell

    tag_barcode_name_list = []
    for i in range(number_of_tag_barcode):
        tag_barcode_name_list.append("TAG"+str(i))

    pcr_index_name_list = []
    for i in range(number_of_pcr_index):
        pcr_index_name_list.append("PCR"+str(i))



    class cell:
        def __init__(self, cellID):
            self.cellID = cellID
        def set_tag_barcode(self, tag_barcode):
            self.tag_barcode = tag_barcode
        def set_pcr_index(self,pcr_index):
            self.pcr_index = pcr_index

        def get_tag_barcode(self):
            return self.tag_barcode
        def get_pcr_index(self):
            return self.pcr_index
        def get_cell_info(self):
            cell_info = self.tag_barcode + "|" + self.pcr_index
            return cell_info




    cell_dict={}
    cellID_count =0
    for well in range(len(tag_barcode_name_list)):
        this_well_dict = {}
        for i in range(round(input_cell_number/len(tag_barcode_name_list))):
            cellID_count = cellID_count+1
            this_cell = cell(str(cellID_count))
            chosen_tag_barcode = tag_barcode_name_list[well]
            this_cell.set_tag_barcode(chosen_tag_barcode)
            cell_dict[cellID_count] = this_cell



    second_cell_dict = {}
    for well in range(len(pcr_index_name_list)):

        this_well_dict = {}
        for k in range(sort_cell_number):
            idx = random.choice(list(cell_dict))
            chosen_cell = cell_dict[idx]
            cell_dict.pop(idx)
            chosen_index =  pcr_index_name_list[well]
            chosen_cell.set_pcr_index(chosen_index)
            
            cell_information = {"tag_barcode" : chosen_cell.get_tag_barcode(), "pcr_index" : chosen_cell.get_pcr_index(),"barcode_index" : chosen_cell.get_cell_info(),"pcr_well" : well }
            this_well_dict[idx] = cell_information 
        second_cell_dict[well] = this_well_dict.copy()


    pooled_cell_dict ={} ### pooled final dict
    for well in second_cell_dict:
        cell_in_well_dict = second_cell_dict[well]
        for cell in cell_in_well_dict:
            # print(type(cell_in_well_dict[cell]))
            pooled_cell_dict[cell] = cell_in_well_dict[cell].copy()



    import pandas as pd
    df = pd.DataFrame.from_dict(pooled_cell_dict,    orient="index")
    frequency_of_each_combination = df["barcode_index"].value_counts()
    collision_count = 0
    unique_count =0
    for item in frequency_of_each_combination:
        if item != 1:
            collision_count = collision_count + item
        else: 
            unique_count = unique_count + item
    ### collision rate as a fraction of total 
    collision_rate =  collision_count / (collision_count + unique_count)
    total_nuclei = number_of_pcr_index * sort_cell_number
    recovered_barcode = len(frequency_of_each_combination)
    cluster_per_nucleus = round(400000000/recovered_barcode)

    return {"number_of_tag_barcode" : tag_barcode,"number_of_pcr_index" : pcr_index,"input_cell_number" :input_cell,    "sort_cell_number" : sort_cell,"collision_rate" : collision_rate,"total_nuclei" : total_nuclei,"recovered_barcode":recovered_barcode,"cluster_per_nucleus":cluster_per_nucleus}


### define ranges of variable 
sort_cell_range = (1,50)
pcr_index_range=(1,96)


result_dict = {}
result_counter =0
for sim_cell in range(sort_cell_range[0],sort_cell_range[1]+1,2):
    for sim_index in range(pcr_index_range[0],pcr_index_range[1]):
        print(sim_cell,sim_index)
        result_dict[result_counter] = simulate_experiment(96,sim_index,200000,sim_cell)
        result_counter = result_counter +1
import pandas as pd 
df = pd.DataFrame.from_dict(result_dict,orient="index")
df.to_csv("96_96_simulation_result.csv",index=False)