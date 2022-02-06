import csv

def write_into_csv(info_list):
    with open('stu_info.czv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Roll No.", "Email ID"])
            
        writer.writerow(info.list)
        
if _name_ == '_main_':
    condition = True
    stu_num = 1
    
    while(condition):
        stu_info = input("Enter student information for student #{} in the format (Name Age Roll No. Email ID):")
        
        stu_info_list = stu_info.split("")
        
        print("\nThe entered information is -\nName: {}\nAge: {}\nRoll No.: {}\nEmail ID: {}".format(stu_info_list[0], stu_info_list[1], stu_info_list[2],stu_info_list[3]))
              
        choice_check = input("Is the enetered information correct? (yes/no)")
        
        if choce_check == "yes":
            write_into_csv(stu_info_list)
            
            condition_check = input("Enter (yes/no) if you want to enter information for another student:")
            if condition == "yes":
                stu_num = stu_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("\nPlease enter the correct information")