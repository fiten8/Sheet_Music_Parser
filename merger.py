import os, pathlib
from PyPDF2 import PdfReader, PdfWriter

parts = ["Vocal","Alto_1","Alto_2", "Tenor_1", "Tenor_2", "Baritone", 
         "Trumpet_1", "Trumpet_2", "Trumpet_3", "Trumpet_4",
         "Trombone_1", "Trombone_2", "Trombone_3", "Trombone_4", 
         "Guitar","Piano","Bass","Aux_Percussion","Drums"]
        
# merger
setlist = ["Oh Channukah","Christmas Time is Here","Feels So Good","Orange Colored Sky",
           "My Favorite Things","Silent Night (Clark)","Deck the Halls With All Sorts of Funky"]
performance = "Oakleaf"

script_dir = pathlib.Path().absolute()
part_index = 0
while part_index <= len(parts):
    merger = PdfWriter()
    for piece in setlist:
        file_name = f"{piece}_{parts[part_index]}.pdf"
        if not os.path.exists(file_name):
            if part_index == 0:
                print("File ", file_name, " does not exist, skipping.")
                continue
            print("File ", file_name, " does not exist, trying previous part to ",parts[part_index],", ",parts[part_index-1])
            file_name = f"{piece}_{parts[part_index-1]}.pdf"
            if not os.path.exists(file_name):
                print("File ", file_name, " does not exist, skipping.")
                continue
        print("Adding ", file_name, " to ", performance, " setlist.")
        reader = PdfReader(file_name)
        for page_num in range(len(reader.pages)):
            merger.add_page(reader.pages[page_num])
    output_file_path = f"{performance}_{parts[part_index]}.pdf"
    with open(output_file_path, "wb") as output_pdf:
        merger.write(output_pdf)
        part_index += 1