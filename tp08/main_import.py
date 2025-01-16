import csv

def main():
    with open(r".\tp08\MOCK_DATA.csv") as csv_file:
        data = csv.DictReader(csv_file)
        for d in data:
            del d['id']
            print(d)
if __name__=='__main__':
    main()
