import os, PyPDF2
from PyPDF2 import PdfReader, PdfWriter

parts = ["Vocal","Alto_1","Alto_2", "Tenor_1", "Tenor_2", "Baritone", 
         "Trumpet_1", "Trumpet_2", "Trumpet_3", "Trumpet_4",
         "Trombone_1", "Trombone_2", "Trombone_3", "Trombone_4", 
         "Rhythm"]
        
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
