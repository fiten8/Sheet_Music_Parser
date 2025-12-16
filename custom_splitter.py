import os, pathlib
from PyPDF2 import PdfReader, PdfWriter

parts = ["Vocal","Alto_1","Alto_2", "Tenor_1", "Tenor_2", "Baritone", 
         "Trumpet_1", "Trumpet_2", "Trumpet_3", "Trumpet_4",
         "Trombone_1", "Trombone_2", "Trombone_3", "Trombone_4",
         "Guitar","Piano","Bass","Aux_Percussion","Drums"]
x = 2
temp_list = [0,x,x,x,x,x,
          x,x,x,x,
          x,x,x,x,
          x,2*x,x,0,x]

### enter file name here ###
truncated_name = "Deck the Halls With All Sorts of Funky"

script_dir = pathlib.Path().absolute()
output_dir = os.path.join(script_dir, "split")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print("Created output directory: ", output_dir)
file_name = truncated_name + ".pdf"
file_path = f"../charts/{file_name}"
#print(truncated_name)

with open(file_path, "rb") as pdf_file:
    reader = PdfReader(pdf_file)
    len_of_pdf = len(reader.pages)
    #print("Total pages in PDF: ", len_of_pdf)

    i = 0
    for j in range(len(temp_list)):
        if len(temp_list) != len(parts):
            print("Error: parts list and temp_list length do not match.")
            break
        writer = PdfWriter()
        if temp_list[j] == 0:
                print("Skipping ", parts[j], " for ", pdf_file.name,", no pages.")
                continue
        #print("Creating PDF for ", parts[j], " from ", pdf_file.name)
        #print("starting on page ", i," adding ", temp_list[j], " pages.")
        for page_num in range(i, i + temp_list[j]):
            #print("Adding page ", page_num, " for ", parts[j], " from ", truncated_name)
            if page_num >= len_of_pdf:
                print("Reached end of PDF for ", pdf_file.name)
                break
            writer.add_page(reader.pages[page_num])
            i += 1
        output_file_path = f"{output_dir}\\{truncated_name}_{parts[j]}.pdf"
        with open(output_file_path, "wb") as output_pdf:
            writer.write(output_pdf)
