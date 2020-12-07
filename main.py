import csv

def finddups():

    try:
        with open('RepoData.csv', newline='', encoding="utf8") as csvfile:
            name = ""
            count = 0

            reader = csv.DictReader(csvfile)
            for row in reader:
                if name == row['repository_name_unauthorized']:
                        print(row['repository_name_unauthorized'], row['state'])
                        count = count + 1
                name = row['repository_name_unauthorized']

            print(count)
    except:
        print("Unable to open the USArchives.csv file")

def findunique():

    try:
        with open('RepoData.csv', newline='', encoding="utf8") as csvfile:
            name = ""
            count = 0

            reader = csv.DictReader(csvfile)
            for row in reader:
                if name != row['repository_name_unauthorized']:
                        print(row['repository_name_unauthorized'], row['state'])
                        count = count + 1
                name = row['repository_name_unauthorized']

            print(count)
    except:
        print("Unable to open the USArchives.csv file")

def findauthorized():

    try:
        with open('RepoData.csv', newline='', encoding="utf8") as csvfile:
            count = 0

            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['repository_name_authorized']:
                    print(row['repository_name_authorized'], row['state'])
                    count = count + 1

            print(count)
    except:
        print("Unable to open the USArchives.csv file")

findauthorized()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Let's Go")

