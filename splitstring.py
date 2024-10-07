# test = 'new Array("0000429","CPP122156505","random name","Grp","RB","random name","9/12/2024","","0001148248","01","")'
with open('rawtabledata.txt', 'r') as file:
    fileText = file.read()

delText = 'new Array('
lines = fileText.splitlines()
processedLines = []
for line in lines:  
    # Remove unwanted parts
    line = line.lstrip(',').strip()
    if delText in line:

        line = line.strip().strip(delText).strip('new Array(').strip(')').strip('"')
        fields = line.split('","')

        if len(fields) >= 8:
            del fields[7]
        if len(fields) >= 9:
            fields[8] = fields[8].split('"')[0]

        line = '","'.join(fields)
        line = f'"{line}"'
        line = line[:-4]
        processedLines.append(line)

# Join all processed lines
res = "\n".join(processedLines)

with open('newtabledata.txt', 'w') as file:
    # Write headers and data to the new file
    file.write('"Agent","Document Number","Insured Name","LOB","Desc","Description","Date Produced","Group Number","Specialist","Location"\n')
    file.write(res)
    print("Done. Open newtabledata.txt in Excel")



