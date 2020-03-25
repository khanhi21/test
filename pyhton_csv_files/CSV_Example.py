# This lesson includes
# CSV uses
# importing csv in python
# managing data from csv
# import  csv
#
#
# with open("user_details.csv", newline='') as csvfile:
#      csvreader = csv.reader(csvfile, delimiter=",")


    # print(csvreader)
    #
    # for row in csvreader:
    #     print(row)

    # iterable_csv = iter(csvreader)
    # next(iterable_csv) # to skip the next line
    # for row in iterable_csv:
    #     print(row[-1])

# import csv
# def transform_user_details(csv_file_name):
#     new_user_data = []
#     with open(csv_file_name, newline='') as csvfile:
#         user_details_csv = csv.reader(csvfile, delimiter=",")
#         for user in user_details_csv:
#             transformation = []
#             transformation.append(user[1])
#             transformation.append(user[2])
#             transformation.append(user[-1])
#             new_user_data.append(transformation)
#     return new_user_data
# #
# # print(transform_user_details("user_details.csv"))
# def create_new_user_data_csv(old_user_data_file="user_details.csv", new_file_name='new_user_data.csv'):
#     new_user_data = transform_user_details(create_new_user_data_csv)
#     new_file = open(new_file_name, 'w')
#     with new_file:
#         csv_writer = csv.writer(new_file)
#         csv_writer.writerows(new_user_data)
# create_new_user_data_csv()

# 2 min challenge - print the columns of this file and last row

# replace any information in csv file
