import os, pathlib, PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

new_dir_path = "C:\\Users\\Owner\\Downloads\\charts\\"
os.chdir(new_dir_path)

parts = ["Vocal","Alto_1","Alto_2", "Tenor_1", "Tenor_2", "Baritone", 
         "Trumpet_1", "Trumpet_2", "Trumpet_3", "Trumpet_4",
         "Trombone_1", "Trombone_2", "Trombone_3", "Trombone_4", 
         "Rhythm"]
x = 2
temp_list = [2,x,x,x,x,x,
          x,x,x,x,
          x,x,x,0,
          20]

### enter file name here ###
file_name = "Oh Channukah.pdf"
pdf_files = Path(new_dir_path)+file_name
truncated_name = pdf_files.stem
print(truncated_name)
    
for j in range(len(temp_list)):
    if len(temp_list) != len(parts):
        print("Error: parts list and temp_list length do not match.")
        break
    writer = PdfWriter()
    #print("Creating PDF for ", parts[j], " from ", pdf_file.name)
    #print("starting on page ", i," adding ", temp_list[j], " pages.")
    i = 0
    for page_num in range(i, i + temp_list[j]):
        
        #print("Adding page ", page_num, " for ", parts[j], " from ", pdf_file.name)
        if temp_list[j] == 0:
            #print("Skipping ", parts[j], " for ", pdf_file.name,", no vocal pages.")
            continue
        if page_num >= len_of_pdf:
            #print("Reached end of PDF for ", pdf_file.name)
            break
        writer.add_page(reader.pages[page_num])
        i += 1
    output_file_path = f"split\\{truncated_name}_{parts[j]}.pdf"
    with open(output_file_path, "wb") as output_pdf:
        writer.write(output_pdf)
