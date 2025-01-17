from CustomerDAO import CustomerDAO

def main():
    dao = CustomerDAO(r'.\tp08\customers_db.db')
    customers = dao.find_all()
    print(customers)
    
    c1 = next(customers)
    print(c1)
    c1 = next(customers)
    print(c1)
    # for customer in customers:
    #     print(customer)
        
        
if __name__=='__main__':
    main()
