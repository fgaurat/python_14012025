import csv
import sqlite3

def main():
    con = sqlite3.connect(r'.\tp08\customers_db.db')
    sql = """INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) 
    VALUES(?,?,?,?,?)"""
    with open(r".\tp08\MOCK_DATA.csv") as csv_file:
        data = csv.DictReader(csv_file)
        for d in data:
            del d['id']
            print(d)
            values = list(d.values())
            con.execute(sql,values)
    
    con.commit()
    con.close()
if __name__=='__main__':
    main()
