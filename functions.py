import os
from PIL import Image, ImageDraw, ImageFont 
from tkinter import filedialog
import shutil


def choose_folder():
    folder_path=filedialog.askdirectory(title="Select a directory (っº - ºς)")
    return folder_path


def zipping(input_folder,output_folder,files):
    zipped_count=0
    
    if not files:
        return "Warning: There are no folders to zip. • ᴖ •"
    
    for f in files:
        full_file_path=os.path.join(input_folder,f)
        if os.path.isdir(full_file_path):
            
            zip_output_base=os.path.join(output_folder,f)
            shutil.make_archive(zip_output_base,'zip',full_file_path)
            zipped_count+=1
            
    if zipped_count > 0:
        return f"Success: Created {zipped_count} zip files in the output folder! (˶ᵔ ᵕ ᵔ˶)"
    else:
        return "Warning: No valid files were found to zip. • ᴖ •"
    
#force landscape
#add indexing
def procces_one_image(image_path,index,total_pages):
    img=Image.open(image_path)
    
    if img.width > img.height:
        img = img.transpose(Image.ROTATE_90)
    if img.mode != 'RGB':
        img = img.convert('RGB')
        
    draw = ImageDraw.Draw(img)
    fontsize = int(img.height * 0.03) 
    try:
        font = ImageFont.truetype("arial.ttf", fontsize)
    except OSError:
        font = ImageFont.load_default()
        
    page_num_text=f"{index+1}/{total_pages}"
    bbox = draw.textbbox((0, 0), page_num_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (img.width - text_width) / 2
    y = img.height - text_height - (img.height * 0.05)

    outline_thickness = max(1, int(fontsize / 15))

    draw.text(
        (x, y), 
        page_num_text, 
        fill="white",                
        font=font, 
        stroke_width=outline_thickness, 
        stroke_fill="black"             
    )
    
    return img

#orders the files 1,2.. or alphabeticaly
def create_pdf(input_folder,output_folder,files,pdf_name):
    output_filename=os.path.join(output_folder,pdf_name)
    
    if os.path.exists(output_filename):   
        return f"Error: {pdf_name} already exists! Please delete or rename it. • ᴖ •"
    if not files:
        return "Warning: There are no images in the input folder to process. • ᴖ •"
    
    try:
        files.sort(key=lambda x: int(x.split('.')[0]))
    except ValueError:
        files.sort()
        
    total_pages=len(files)
    
    #sequential for optimized RAM usage
    def image_generator():
        for i,filename in enumerate(files):
            yield procces_one_image(os.path.join(input_folder,filename),i,total_pages)
    img_gen=image_generator()
    
    try:
        first_image = next(img_gen)
        first_image.save(
            output_filename, 
            "PDF", 
            resolution=100.0, 
            save_all=True, 
            append_images=img_gen
        )
        return f"Success! PDF compiled and saved as {pdf_name} (˶ᵔ ᵕ ᵔ˶)"
    except StopIteration:
        return "Error: Could not process any images. • ᴖ •"
    except Exception as e:
        return f"Error creating PDF • ᴖ • : {str(e)}"