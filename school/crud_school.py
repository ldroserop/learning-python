from school_db import con
import os
import bcrypt
from datetime import datetime

status_menu = True
global status_op

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_countries(op):
    os.system('clear')

    print("::: Country form :::")
    namecountry = input("Write the name of your country of origin: ")
    while True:
        abrev_input = input("Type the first three letters of your country or origin: ")
        if len(abrev_input) == 3:
            abrev = abrev_input.upper()
            break
        else:
             print("Please write only the first three letters of your country of origin.")         
    while True:
        descrip_input = input("Choose an option as appropriate (1 North America, 2 Central America, 3 South America, 4 Europe, 5 Africa, 6 Asia, 7 Oceania): ")
        if descrip_input == '1':
            descrip = "País de Norte América"
            break
        elif descrip_input == '2':
            descrip = "País de Centro América"
            break
        elif descrip_input == '3':
            descrip = "País de Sur América"
            break
        elif descrip_input == '4':
            descrip = "País de Europa"
            break
        elif descrip_input == '5':
            descrip = "País de África"
            break
        elif descrip_input == '6':
            descrip = "País de Asia"
            break
        elif descrip_input == '7':
            descrip = "País de Oceanía"
            break        
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_country = f'''
            INSERT INTO 
                countries (name, abrev, descrip, created_at, updated_at, deleted_at) 
                VALUES('{namecountry}', '{abrev}', '{descrip}', '{create}', '{update}', '{delete}')
        '''
    con.execute(new_country)
    con.commit()

    print("::: New country has been created successfully :::")
    os.system('pause')
    menu()
    # Obtener el ID del país recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_country = cur.fetchone()[0]
    cur.close()

    return id_country

def create_departments(op):
    os.system('clear')

    print("::: Department form :::")
    name = input("Write the name of your department of origin: ")
    while True:
        abrev_input = input("Type the first three letters of your department or origin: ")
        if len(abrev_input) == 3:
            abrev = abrev_input.upper()
            break
        else:
             print("Please write only the first three letters of your department of origin.")
    
    # Assuming id_country is obtained from user input or another source
    id_country = input("Enter the ID of the country: ")
    
    descrip = "Departamento/Provincia de " + name
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_department = f'''
            INSERT INTO 
                departments (name, abrev, descrip, id_country, created_at, updated_at, deleted_at) 
                VALUES('{name}', '{abrev}', '{descrip}', '{id_country}', '{create}', '{update}', '{delete}')
        '''
    con.execute(new_department)
    con.commit()

    print("::: New department has been created successfully :::")
    os.system('pause')
    menu()

    # Obtener el ID del departamento recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_department = cur.fetchone()[0]
    cur.close()

    return id_department

def create_cities(op):
    os.system('clear')

    print("::: Cities form :::")
    name = input("Write the name of your city of origin: ")
    while True:
        abrev_input = input("Type the first three letters of your city or origin: ")
        if len(abrev_input) == 3:
            abrev = abrev_input.upper()
            break
        else:
             print("Please write only the first three letters of your city of origin.")
    descrip = "Ciudad de " + name
    
    # Assuming id_department is obtained from user input or another source
    id_department = input("Enter the ID of the department: ")
    
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_city = f'''
            INSERT INTO 
                cities (name, abrev, descrip, id_dept, created_at, updated_at, deleted_at) 
                VALUES('{name}', '{abrev}', '{descrip}', '{id_department}', '{create}', '{update}', '{delete}')
        '''
    con.execute(new_city)
    con.commit()

    print("::: New city has been created successfully :::")
    os.system('pause')
    menu()

    # Obtener el ID de la ciudad recién creada
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_city = cur.fetchone()[0]
    cur.close()

    return id_city

def create_idtype(op):
    os.system('clear')

    print("::: Identification Type form :::")
    while True:
        id_input = input("Select your Id type (1 for Cédula de Ciudadanía, 2 for Tarjeta de Identidad or 3 for Pasaporte): ")
        if id_input == '1':
            name = "Cédula de Ciudadanía"
            abrev = "CC"
            descrip = "Documento de identificación nacional en Colombia para mayores de edad"
            break
        elif id_input == '2':
            name = "Tarjeta de Identidad"
            abrev = "TI"
            descrip = "Documento de identificación nacional en Colombia para menores de edad"
            break
        elif id_input == '3':
            name = "Pasaporte"
            abrev = "PASS"
            descrip = "Documento internacional de identificación"
            break
        else:
            print("Invalid option, please write only 1, 2 or 3.") 
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_idtype = f'''
        INSERT INTO 
            identification_types (name, abrev, descrip, created_at, updated_at, deleted_at) 
            VALUES('{name}', '{abrev}', '{descrip}', '{create}', '{update}', '{delete}')
    '''
    con.execute(new_idtype)
    con.commit()

    print("::: New identification type has been created successfully :::")
    os.system('pause')
    menu()

    # Obtener el ID del tipo de identificación recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_idtype = cur.fetchone()[0]
    cur.close()

    return id_idtype

def create_user(op):
    os.system('clear')

    print("::: Signup form :::")
    email = input("Your email: ")
    passwd = input("Your password: ")
    passwd_hashed = hash_password(passwd)
    while True:
        stt_input = input("Your status (1 for active or 2 for inactive): ")
        if stt_input == '1':
            stt = True
            break
        elif stt_input == '2':
            stt = False
            break
        else:
            print("Invalid option, please write only 1 or 2.") 
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_user = f'''
        INSERT INTO 
            users (email, password, status, created_at, updated_at, deleted_at) 
            VALUES('{email}', "{passwd_hashed}", '{stt}', '{create}', '{update}', '{delete}')
    '''
    con.execute(new_user)
    con.commit()

    print("::: New user has been created successfully :::")
    os.system('pause')
    menu()

    # Obtener el ID del usuario recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_user = cur.fetchone()[0]
    cur.close()

    return id_user

def create_student(op):
    os.system('clear')

    print("::: Student form :::")
    code = input("Your student code: ")
    id_person = input("Your ID: ")
    while True:
        stt_input = input("Your status (1 for active or 2 for inactive): ")
        if stt_input == '1':
            stt = True
            break
        elif stt_input == '2':
            stt = False
            break
        else:
            print("Invalid option, please write only 1 or 2.") 
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_student = f'''
        INSERT INTO 
            students (code, id_person, status, created_at, updated_at, deleted_at) 
            VALUES('{code}', '{id_person}', '{stt}', '{create}', '{update}', '{delete}')
    '''
    con.execute(new_student)
    con.commit()

    print("::: New student has been created successfully :::")
    os.system('pause')
    menu()

    # Obtener el ID del estudiante recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_student = cur.fetchone()[0]
    cur.close()

    return id_student

def create_persons(op):
    fname = input("Write your first name: ")
    lname = input("Write your last name: ")
    id_ident = input("Enter the ID of the identification type: ")
    ident_number = input("Write your ID number: ")
    id_exp_city = input("Enter the ID of the city of experience: ")
    address = input("Write your address: ")
    mobile = input("Write your mobile number: ")
    id_user = input("Enter the ID of the user: ")    
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_person = f'''
        INSERT INTO 
            persons (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_user, created_at, updated_at, deleted_at) 
            VALUES('{fname}', '{lname}', '{id_ident}', '{ident_number}', '{id_exp_city}', '{address}', '{mobile}', '{id_user}', '{create}', '{update}', '{delete}')
    '''
    con.execute(new_person)
    con.commit()

    print("::: New person has been created successfully :::")
    os.system('pause')
    menu()

    # Obtener el ID de la persona recién creada
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_person = cur.fetchone()[0]
    cur.close()

    return id_person

def menu(): 
    global opt
    status_opt = True
    while status_menu: 
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create country")
        print("[2]. Create department")
        print("[3]. Create city")
        print("[4]. Create identification type")
        print("[5]. Create user")
        print("[6]. Create person")
        print("[7]. Create student")
        print("[8]. Exit")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '8':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_countries(opt)
        elif opt == '2':
            create_departments(opt)
        elif opt == '3':
            action = create_cities(opt)
            if action != 'cities':
                break
        elif opt == '4':
            action = create_idtype(opt)
            if action != 'idtype':
                break
        elif opt == '5':
            action = create_user(opt)
            if action != 'user':
                break
        elif opt == '6':
            create_persons(opt)
        elif opt == '7':
            create_student(opt)
        else:
            print("::: See you soon :::")
            break
    
#Call main menu
menu()

#Close connection
con.close()

