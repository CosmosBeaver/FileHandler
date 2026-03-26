from tkinter import *
from tkinter import ttk,simpledialog
import os
from functions import create_pdf,choose_folder,zipping

def run_task(action,status,root):

    folder_path=choose_folder()
    if not folder_path:
        status.set("Status: Folder selection cancelled. • ᴖ •")
        return
    
    base_dir = os.path.dirname(os.path.abspath(folder_path))
    input_folder = os.path.join(base_dir, "input")
    output_folder = os.path.join(base_dir, "output")

    if not os.path.exists(input_folder):
        status.set(f"Error: Could not find input folder. • ᴖ •")
        return
    
    status.set("Status: Processing files... Please wait. (╭ರ_•́)")
    root.update()
    
    all_items=os.listdir(input_folder)
    
    #functions to buttons 
    if action=="pdf":
        pdf_name=simpledialog.askstring("PDF Name", "Enter a name for the PDF ( ꈍ◡ꈍ):", parent=root)
        if not pdf_name:
            status.set("Status: Task cancelled (no name provided). • ᴖ •")
            
        if not pdf_name.lower().endswith(".pdf"):
            pdf_name+=".pdf"
        
        files=[f for f in all_items if os.path.isfile(os.path.join(input_folder,f))]
        result_message=create_pdf(input_folder,output_folder,files,pdf_name)
    elif action=="zip":
        result_message=zipping(input_folder,output_folder,all_items)
        
    status.set(result_message)

if __name__ == "__main__":
    root = Tk()
    root.title("File handler ദ്ദി◝ ⩊ ◜.ᐟ")
    
    frm = ttk.Frame(root, padding=100)
    frm.grid()

    status=StringVar()
    status.set("Status: Waiting for input... ( ╹ -╹)?")
    ttk.Label(frm, text="Beep boop why are you here? /ᐠ◣ω◢マ" ).grid(column=0, row=0,pady=(0, 10))
    ttk.Button(frm,text="I want PDF! ૮ • ﻌ - ა",command=lambda:run_task("pdf",status,root)).grid(column=0, row=1,pady=2)
    ttk.Button(frm,text="I want Archive! ૮ ᴖﻌᴖა",command=lambda:run_task("zip",status,root)).grid(column=0, row=2,pady=2)
    ttk.Button(frm, text="Quit (╥﹏╥)", command=root.destroy).grid(column=0, row=3,pady=(10, 0))
    
    status_label = ttk.Label(frm, textvariable=status, wraplength=250, justify="center", foreground="black")
    status_label.grid(column=0, row=4, pady=(20, 0))
    root.mainloop()