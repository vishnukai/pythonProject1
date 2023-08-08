import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='newpassword@97', database='python')

while True:

    print('Choose a option')
    print('1.Create a account')
    print('2.Account Login')
    print('3.Exit')


    try:
        login = int(input('Enter a choice:'))
        if login == 1:
            name = input('Enter the user_name')
            login_password = input('Enter the login password:')
            transaction_password = input('Enter the transaction password:')
            check_name = "SELECT * FROM BANK WHERE name = %s"
            cur = mydb.cursor()
            cur.execute(check_name, (name,))
            fetch_name = cur.fetchone()
            if fetch_name is None:
                cur = mydb.cursor()
                s = 'INSERT INTO bank(NAME,LOGIN_PASSWORD,TRANSACTION_PASSWORD) VALUES(%s,%s,%s)'
                t = (name, login_password, transaction_password)
                cur.execute(s, t)
                mydb.commit()
                to_get_account_no = "SELECT * FROM BANK WHERE NAME= %s and LOGIN_PASSWORD = %s and TRANSACTION_PASSWORD=%s"
                cur.execute(to_get_account_no, (name, login_password, transaction_password))
                nr = cur.fetchall()[-1]

                print(f"Account created Sucessfully,'Account number is :{nr[0]}")
            else:
                print(f'The user name already exists{name}.Please enter anotehr user name')

        elif login == 2:
            n = input('Enter your account number:')
            l = input('Enter your login password')

            sql_query = "SELECT * FROM BANK WHERE ACCOUNT_NO= %s and LOGIN_PASSWORD = %s;"
            cur = mydb.cursor()
            cur.execute(sql_query, (n, l))
            row = cur.fetchone()
            if row:
                print(f'LOGGED IN SUCESSFULLY \nWelcome to K banking {row[1]} ')
                while True:

                    print('Choose a option')
                    print('1.Deposit')
                    print('2.Transfer')
                    print('3 Check balance')
                    print('4.Logout')
                    c = int(input('Enter your choice:'))
                    if c == 1:
                        amount = int(input('Enter the amount'))
                        upi_id = input('Enter the upi_id to send the request')
                        sql_query_new = "SELECT * FROM Account_transaction WHERE account_no =%s;"
                        cur.execute(sql_query_new, (row[0],))
                        row_n = cur.fetchone()

                        if row_n:
                            amount_new = row_n[3] + amount
                            a_c_n = 'INSERT INTO ACCOUNT_TRANSACTION(ACCOUNT_NO,UPID,AMOUNT) VALUES(%s,%s,%s)'
                            t_a_n = (row[0], upi_id, amount_new)
                            cur.execute(a_c_n, t_a_n)

                            mydb.commit()
                            print(f'The amount has been credited to your account {row[0]} balance is {amount_new}')
                        else:
                            a_c = 'INSERT INTO ACCOUNT_TRANSACTION(ACCOUNT_NO,UPID,AMOUNT) VALUES(%s,%s,%s)'
                            t_a = (row[0], upi_id, amount)
                            cur.execute(a_c, t_a)
                            mydb.commit()
                            print(f'The amount has been credited to your account{row[0]}')
                    elif c == 2:
                        amount = int(input('Enter the amount:'))
                        upi_id = input('Enter the upi_id to transfer the amount:')
                        transaction_password=input('Enter the transaction password:')
                        print(row[3])
                        if transaction_password==row[3]:
                            sql_query_new = "SELECT * FROM Account_transaction WHERE account_no =%s;"
                            cur.execute(sql_query_new, (row[0],))
                            row_n = cur.fetchone()

                            if row_n:
                                amount_new = row_n[3] - amount
                                a_c_n = 'INSERT INTO ACCOUNT_TRANSACTION(ACCOUNT_NO,UPID,AMOUNT) VALUES(%s,%s,%s)'
                                t_a_n = (row[0], upi_id, amount_new)
                                cur.execute(a_c_n, t_a_n)

                                mydb.commit()
                                print(f'The amount has been debited from your account {row[0]} balance is {amount_new}')
                            else:
                                print('Your bank balance is zero! Please deposit some amount')
                        else:
                            print('The password doesnt match')

                    elif c == 3:
                        sql_query_new = "SELECT * FROM Account_transaction WHERE account_no =%s;"
                        cur.execute(sql_query_new, (row[0],))
                        row_n = cur.fetchone()
                        if row_n:
                            print(f'Your current balance is {row_n[3]}')
                        else:
                            print('Balance is zero')


                    elif c == 4:
                        print('Logging out.....')
                        break
                    else:
                        print('Invalid choice. Please choose again.')

            else:
                print(f"The account number {n} and password doesn't exist")
        elif login == 3:
            print('Exiting........')
            break


        else:
            print('invalid choice.Please choose again')
    except:
        print('Enter a valid choice')
