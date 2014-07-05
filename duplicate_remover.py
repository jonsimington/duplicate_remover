from sys import argv

# First argument is input csv, second argument is output csv
# Output csv will contain no duplicate entries

with open(argv[1],'r') as input, open(argv[2],'w') as output:
    duplicates = set()    # duplicate lines

    for line in input:
        if line in duplicates:
            continue
        duplicates.add(line)
        output.write(line)
