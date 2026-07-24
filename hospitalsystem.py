patients={}

#Function for registration
def patient_register():
    patient_id = int(input("Enter patient ID:"))
    name = input("Enter patients name:")
    age =int(input("Enter patients age:"))
    weight = float(input("Enter patients weight"))
    gender= patient_gender()
    phone = int(input("Enter contact no"))
    address = patient_address()

    
   

    patients[patient_id]={
    "Consultation":[],
    "Name":name,
    "Age":age,
    "Weight":weight,
    "Gender":gender,
    "Phone":phone,
    "Address":address,
    }
    print("Registered Successfully")


def patient_consultation():
    patient_id=int(input("Enter patient id"))
    if patient_id in patients:
        Disease = input("disease")
        Severity = severity_level()
        Temperature =input("temperature level")
        Blood_group= blood_group()
        Doctor = doctor_selection()
        Prescription = input("Prescription")
        Fees = input("Enter fees")
        Follow_up_date = input("Enter follow up date")
        print("Get Well Soon")

        Consultation ={
            "Disease":Disease,
            "Severity":Severity,
            "Temperature":Temperature,
            "Blood_group":Blood_group,
            "Doctor": Doctor,
            "Prescription":Prescription,
            "Fees" : Fees,
            "Follow up date" : Follow_up_date
        }
        patients[patient_id]["Consultation"].append(Consultation)


#Function for searching
def patient_search():
    patient_id=int(input("Enter patient id:"))
    if patient_id in patients:
        print("Patient detail already exist")
    else:
        print("Patient Not Found") 


#Function to delete patientt record
def patient_delete():
    patient_id=int(input("Enter patients id:"))
    if patient_id in patients:
        del patients[patient_id]
        print("Patients record deleted successfully")
    else:
        print("Patient detail Not Found")


#Function to update patients detail
def patient_update():
    patient_id = int(input("Enter patient id"))
    if patient_id in patients:
        patients[patient_id]["Name"]=input("Enter New Name")
        patients[patient_id]["Age"]=int(input("Enter New Age"))
        patients[patient_id]["Weight"]=int(input("Enter New Weight"))
        patients[patient_id]["Gender"]=patient_gender()
        patients[patient_id]["Phone"]=input("Enter New PhoneNO")
        patients[patient_id]["Address"]=patient_address()


def patient_gender():
    print("\nPatient Gender")
    print("1. MALE")
    print("2. FEMALE")
    print("3. OTHER")

    select = int(input("Select Gender:"))

    if select == 1:
        return "MALE"
    elif select == 2:
        return "FEMALE"
    elif select == 3:
        return "OTHER"
    else:
        print("INVALID CHOICE")
        return None

def doctor_selection():
    print("\nAvailable Doctors")
    print("1. Dr. Ghosh - Endocrinologist")
    print("2. Dr. Fernandez - Cardiologist")
    print("3. Dr. Khan - Orthopedic")
    print("4. Dr. Mehta - Neurologist")
    print("5. Dr. Mishra - Dentist")
    print("6. Dr. Singh - Dermatologist")
    print("7. Dr. Jadhav - ENT Specialist")
    print("8. Dr. Choudhary - Oncologist")
    print("9. Dr. Patel - Radiologist")
    print("10. Dr. Ganguly - Gynecologist")

    choice = int(input("Select Doctor: "))

    if choice == 1:
        return "Dr. Ghosh"

    elif choice == 2:
        return "Dr. Fernandez"

    elif choice == 3:
        return "Dr. Khan"

    elif choice == 4:
        return "Dr. Mehta"
    
    elif choice == 5:
        return "Dr. Mishra"
    
    elif choice == 6:
        return "Dr. Singh"
    
    elif choice == 7:
        return "Dr. Jadhav"
    
    elif choice == 8:
        return "Dr. Kamble"
    
    elif choice == 9:
        return "Dr.Patel"
    
    elif choice == 10:
        return "Dr.Ganguly"

    else:
        print("Invalid Choice")
        return None 

def doctor_information():

    print("=" * 50)
    print("        DOCTOR INFORMATIONS")
    print("=" * 50)

    print("\nDr. Ghosh - Endocrinologist\n"
      "Treats diabetes,hormone and endocrine related disorders.\n")

    print("Dr. Fernandez - Cardiologist\n"
      "Treats heart and cardiovascular related conditions.\n")

    print("Dr. Khan - Orthopedic Specialist\n"
      "Treats bones,joints,muscles and injuries.\n")

    print("Dr. Mehta - Neurologist\n"
      "Treats disorders related to the brain,spinal cord and nervous system.\n")

    print("Dr. Mishra - Dentist\n"
      "Treats dental and oral health problems,including cavities and gum disorders.\n")

    print("Dr. Singh - Dermatologist\n"
      "Treats skin,hair and nail related conditions.\n")

    print("Dr. Jadhav - ENT Specialist\n"
      "Treats conditions related to the ear,nose and throat.\n")

    print("Dr. Choudhary - Oncologist\n"
      "Specializes in the diagnosis and treatment of cancer.\n")

    print("Dr. Patel - Radiologist\n"
      "Uses medical imaging such as X-rays,CT scans,MRI and ultrasound for diagnosis.\n")

    print("Dr. Ganguly - Gynecologist\n"
      "Treats women's reproductive health and gynecological conditions.\n")
    

def patient_address():

    house_no = input("House No: ")
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    pincode = input("Pincode: ")

    return {
        "House No": house_no,
        "Street": street,
        "City": city,
        "State": state,
        "Pincode": pincode,
    }

def severity_level():

    print("1.Mild")
    print("2.Moderate")
    print("3.Severe")
    print("4.Critical")

    choice=int(input("Enter level"))

    if choice == 1:
        return "Mild"
    elif choice == 2:
        return "Moderate"
    elif choice == 3:
        return "Severe"
    elif choice == 4:
        return "Critical"
    
    else:
        print("Invalid selection")
        return None


def blood_group():

    print("\nBlood Group")
    print("1. A+")
    print("2. A-")
    print("3. B+")
    print("4. B-")
    print("5. AB+")
    print("6. AB-")
    print("7. O+")
    print("8. O-")

    choice = int(input("Select Blood Group: "))

    if choice == 1:
        return "A+"
    elif choice == 2:
        return "A-"
    elif choice == 3:
        return "B+"
    elif choice == 4:
        return "B-"
    elif choice == 5:
        return "AB+"
    elif choice == 6:
        return "AB-"
    elif choice == 7:
        return "O+"
    elif choice == 8:
        return "O-"
    else:
        print("Invalid Choice")
        return None


def patient_display():
    patient_id = int(input("Enter patient ID"))
    if patient_id not in patients:
        print("No Records available for the patient")
        return

    details = patients[patient_id]
    print("\n" + "="*50)
    print("     PATIENT DETAILS")
    print("="*50)


    print(f"Patient ID : {patient_id}")
    print(f"Name       : {details['Name']}")
    print(f"Age        : {details['Age']}")
    print(f"Weight     : {details['Weight']}")
    print(f"Gender     : {details['Gender']}")
    print(f"Phone      : {details['Phone']}")
    
    print("\n" + "="*50)
    print("         ADDRESS")
    print("="*50)

    address = details["Address"]
    
    print("\nAddress")
    print("-" * 30)
    print("House No :", address["House No"])
    print("Street   :", address["Street"])
    print("City     :", address["City"])
    print("State    :", address["State"])
    print("Pincode  :", address["Pincode"])

    if details["Consultation"]:

        consultation = details["Consultation"][-1]

        print("\n" + "=" * 50)
        print("        CONSULTATION")
        print("=" * 50)

        print("Disease        :", consultation["Disease"])
        print("Severity       :", consultation["Severity"])
        print("Temperature    :", consultation["Temperature"])
        print("Blood Group    :", consultation["Blood_group"])
        print("Doctor         :", consultation["Doctor"])
        print("Prescription   :", consultation["Prescription"])
        print("Fees           :", consultation["Fees"])
        print("Follow up date :", consultation["Follow up date"])

        print("\n="*50)

    else:
        print("\nNo consultation details available.")


def hospital_information():
    print("="*50)
    print("     HEALTH FIRST HOSPITAL")
    print("="*50)

    print("\n Established : 2026")
    print("\n Address : Mumbai")
    print("\n Contact : 7506589580")
    print("\n Email : healthfirsthospital123@gmail.com")
    print("\n Emergency: 102")
    print("\n Working hours : 24/7")
    print("\n YOUR HEALTH,OUR FIRST PRIORITY.")

def health_awareness():

    print("=" * 50)
    print("           HEALTH AWARENESS")
    print("=" * 50)

    print(" *Wash your hands regularly.")
    print(" *Drink at least 3-4 litres of water daily.")
    print(" *Eat a balanced and nutritious diet.")
    print(" *Exercise for at least 30 minutes every day.")
    print(" *Sleep for 7-8 hours every night.")
    print(" *Avoid smoking and tobacco.")
    print(" *Avoid alcohol consumption.")
    print(" *Get regular health check-ups.")
    print(" *Stay up-to-date with vaccinations.")
    print(" *Manage stress through meditation or yoga.")
    print(" *Avoid processed or junk foods.")

    print("=" * 50)
    print("        YOUR HEALTH, OUR FIRST PRIORITY")
    print("=" * 50)


while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Register Patient")
    print("2. Patient Consultation")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Display Patients")
    print("7. About Hospital")
    print("8. Doctor Information")
    print("9. Health Awareness")
    print("10. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        patient_register()

    elif choice == 2:
        patient_consultation()

    elif choice == 3:
        patient_search()

    elif choice == 4:
        patient_update()

    elif choice == 5:
        patient_delete()

    elif choice == 6:
        patient_display()

    elif choice == 7:
        hospital_information()

    elif choice == 8:
        doctor_information()

    elif choice == 9:
        health_awareness()
    
    
    
    elif choice == 10:
        print("\nThankyou for choosing\n"
        "HEALTH FIRST HOSPITAL\n"
        "We Wish You and Your Family\n" 
        "Good Health!\n")
        break

        
    else:
        print("Invalid Choice")

