import csv

# reading csv file
def read_dataset(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# making list of districts
def list_districts(dataset):
    values = list()
    for i in range(0, len(dataset)):
        value = dataset[i][0]
        values.append(value)
    return values


# making a list with unique districts
def unique_districts(values):
    output = list()
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


# counting female, male and total population of a district
def district_detail(output, dataset):
    results = list()
    results.append(["District", "Female", "Male", "Total"])
    for j in range(0, len(output)):
        count = 0
        female = 0
        male = 0
        for i in range(0, len(dataset)):
            if output[j] in dataset[i][0]:
                if 'female' in dataset[i][3]:
                    female = female + 1
                else:
                    male = male + 1
                count = count + 1
        results.append([output[j], female, male, count])
    return results


# counting total number of female, male and total population
def total_count(results):
    total_Female = 0
    total_Male = 0
    total_Pop = 0
    for i in range(1, len(results)):
        total_Female = total_Female + results[i][1]
        total_Male = total_Male + results[i][2]
        total_Pop = total_Pop + results[i][3]
    results.append(["Total", total_Female, total_Male, total_Pop])
    return results


# creating table
def table(results):
    for row in results:
        print("|", row[0], " " * (13-len(row[0])), "|", row[1], " " * (7-len(str(row[1]))), "|",
              row[2], " " * (7-len(str(row[2]))), "|", row[3], " " * (7-len(str(row[3]))), "|")


filename = "survey.csv"
dataset = read_dataset(filename)
list_districts = list_districts(dataset)
unique_districts = unique_districts(list_districts)
district_detail = district_detail(unique_districts, dataset)
total_count = total_count(district_detail)

table(total_count)
