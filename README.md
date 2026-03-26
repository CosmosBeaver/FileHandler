File Handler

--Lightweight Python GUI tool that helps with UNI assignments that often require sending a PDF of what you wrote or ZIPs of your files


--Features
PDF Compiler (I want PDF! ૮ • ﻌ - ა):
 * Takes all images in your input folder and combines them into a single .pdf.

 * Smart Formatting: Automatically rotates landscape images to portrait and ensures everything is in RGB mode.

 * Page Numbers: Automatically draws outlined page numbers (e.g., "1/5") at the bottom center of each page.


Archive Maker (I want Archive! ૮ ᴖﻌᴖა): 
 * Looks at all the subdirectories in your input folder and turns each one into a separate .zip file in your output folder, keeping the original name.

 !Requirements
This project relies on standard Python libraries (tkinter, os, shutil), but you will need to install Pillow for the image processing. (pip install Pillow)


--Required Folder Structure

Wherever you choose your "Base Folder", it must contain two sub-folders named exactly input and output:

📁 Your_Base_Folder/
├── 📁 input/    <-- Place your images (for PDF) or folders (for Zip) in here
└── 📁 output/   <-- The app will drop your finished PDFs and Zips here

--How to Use
 * Run the main.py script to open the GUI.

 * Click your desired action (PDF or Archive).

 * A folder dialog will pop up. Select your Base Folder (the one that contains the input and output folders).

 * If making a PDF: You'll be prompted to enter a name for your new file.

Watch the status text at the bottom! It will tell you when the files are processing and when they are successfully finished