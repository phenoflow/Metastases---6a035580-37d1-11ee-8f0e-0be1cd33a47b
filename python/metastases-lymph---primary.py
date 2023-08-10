# Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"B560","system":"readv2"},{"code":"B5601","system":"readv2"},{"code":"B5603","system":"readv2"},{"code":"B5605","system":"readv2"},{"code":"B5606","system":"readv2"},{"code":"B5607","system":"readv2"},{"code":"B560z","system":"readv2"},{"code":"B5611","system":"readv2"},{"code":"B5612","system":"readv2"},{"code":"B5615","system":"readv2"},{"code":"B5618","system":"readv2"},{"code":"B5619","system":"readv2"},{"code":"B5620","system":"readv2"},{"code":"B5631","system":"readv2"},{"code":"B5632","system":"readv2"},{"code":"B5633","system":"readv2"},{"code":"B5642","system":"readv2"},{"code":"B5653","system":"readv2"},{"code":"B5654","system":"readv2"},{"code":"B56z","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('metastases-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["metastases-lymph---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["metastases-lymph---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["metastases-lymph---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
