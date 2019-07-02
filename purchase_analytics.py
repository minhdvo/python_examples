""" Problem
Instacart has published a dataset(https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders.
For this challenge, we want you to calculate, for each department, the number of times a product was requested, number of times a 
product was requested for the first time and a ratio of those two numbers.
"""

# code
# load csv package for I/O
import csv

def main():
   # Load files
   ## 'products.csv' file
    with open('./input/products.csv',encoding="utf8") as product_file:
        df = csv.reader(product_file)
        department_id_pro = []
        product_id_pro = []
    
        # skip the first row
        next(df)
    
        for row in df:        
            department_id_pro.append(int(row[3]))
            product_id_pro.append(int(row[0]))

    ## 'order_products.csv' file
    with open('./input/order_products.csv') as order_file:
        df = csv.reader(order_file)
        order_id = []
        product_id_order = []
        reorder = []
    
        # skip the first row
        next(df)
    
        for row in df:        
            order_id.append(int(row[0]))
            product_id_order.append(int(row[1]))
            reorder.append(int(row[3]))

    # Determine 'department_id' for each product in order_products file
    department_id_order = list(map(lambda i: department_id_pro[product_id_pro.index(i)],product_id_order))

    # a. For each department, the number of times a product was requested
    df_1 = unique_value_count(department_id_order)        

    # b. Number of times a product was requested for the first time
    x = [i*j for i,j in zip(department_id_order,reorder)]
    
    df_2 = unique_value_count(x)
    del df_2[0]

    # write results
    department = set(department_id_pro)

    f = open('./output/report.csv','w')
    f.write('department_id,number_of_orders,number_of_first_orders,percentage\n')
    
    for i in department:
        data = str(i) + ' , ' + str(df_1[i]) + ' , ' + str(df_1[i]-df_2[i]) + ' , ' + str((df_1[i]-df_2[i])/df_1[i])
        f.write(data)
        f.write('\n')
    f.close() 



# function for determining the number of occurence for each unique element in list
# return the dict 
def unique_value_count(a):
    ret = {}
    for i in set(a):
        ret[int(i)] = a.count(i)        
    return ret


if __name__== "__main__":
  main()
