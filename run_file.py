import os, pathlib, PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

new_dir_path = "C:\\Users\\Owner\\Downloads\\charts\\"
os.chdir(new_dir_path)

parts = ["Vocal","Alto_1","Alto_2", "Tenor_1", "Tenor_2", "Baritone", 
         "Trumpet_1", "Trumpet_2", "Trumpet_3", "Trumpet_4",
         "Trombone_1", "Trombone_2", "Trombone_3", "Trombone_4", 
         "Rhythm"]

pages1 = [0,1,1,1,1,1,
          1,1,1,1,
          1,1,1,1,
          4]

pages2 = [0,2,2,2,2,2,
          2,2,2,2,
          2,2,2,2,
          8]

pages3 = [0,3,3,3,3,3,
          3,3,3,3,
          3,3,3,3,
          12]

pdf_files = Path(new_dir_path).glob("*.pdf")
for pdf_file in pdf_files:
    reader = PdfReader(pdf_file)
    file = open(pdf_file, "rb")
    len_of_pdf = len(reader.pages)
    if len_of_pdf <= 30:
        temp_list = list(pages1)
    elif len_of_pdf > 30 and len_of_pdf <= 42:
        temp_list = list(pages2)
    elif len_of_pdf < 100:
        temp_list = list(pages3)
    else:
        #print("File ", pdf_file.name, " has too many pages.")
        continue
    #print(pdf_file.name," has ", len_of_pdf, "pages. Using page", temp_list[1])
          
    if pdf_file.name.__contains__("_v"):
        vocal_pages = pdf_file.name.split("_v")[1]
        truncated_name = pdf_file.name.split("_v")[0]
        #print("Vocal pages detected:", vocal_pages)
        vocal_pages = vocal_pages.split(".pdf")[0]
        #print("Vocal pages part 2:", vocal_pages)
        temp_list[0] = int(vocal_pages)
        #print("Using vocal pages:", temp_list[0],"for ", pdf_file.name)
    else:
        truncated_name = pdf_file.stem
    i = 0
    for j in range(len(temp_list)):
        if len(temp_list) != len(parts):
            print("Error: parts list and temp_list length do not match.")
            break
        writer = PdfWriter()
        #print("Creating PDF for ", parts[j], " from ", pdf_file.name)
        #print("starting on page ", i," adding ", temp_list[j], " pages.")
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
        
# merger
setlist = ["Oh Channukah","Christmas Time is Here","Feel So Good","Orange Colored Sky",
           "My Favorite Things","Silent Night (Clark)","Deck the Halls With All Sorts of Funky"]
performance = "Oakleaf"

new_dir_path = "C:\\Users\\Owner\\Downloads\\charts\\split\\"
os.chdir(new_dir_path)
for part in parts:
    merger = PdfWriter()
    for piece in setlist:
        file_name = f"{piece}_{part}.pdf"
        if not os.path.exists(file_name):
            print("File ", file_name, " does not exist, skipping.")
            continue
        #print("Adding ", file_name, " to ", performance, " setlist.")
        reader = PdfReader(file_name)
        for page_num in range(len(reader.pages)):
            merger.add_page(reader.pages[page_num])
    output_file_path = f"{performance}_{part}.pdf"
    with open(output_file_path, "wb") as output_pdf:
        merger.write(output_pdf)
