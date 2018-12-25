
# This is one of the imoportant code
# it extracts the metadata from the pdf file and can reveal important information of the system.


# it can be useful in cyber forensics 
# using new module of python pypdf

# importing the pypdf module for metadata extraction:))
import pyPdf

def main():

    # setting the location of the pdf here from which metadata is to be extracted 
    
	filen = <LOCATION_OF_THE_PDF> # provide the file location here 
	
	pdfFile = pyPdf.PdfFileReader(file(filen,'rb'))  # opening the pdf file here
  
	data = pdfFile.getDocumentInfo() # saving the metadata info in data variable using defined function 

	print "(:-------#####------Extracted Metadata of the file-------#######--------:)"
  
	for metadata in data:
		print metadata+ ":" +data[metadata]

if __name__ == '__main__': 
	main()   # calling the main driver function 
  
  
# program ends
# happy hacking 
