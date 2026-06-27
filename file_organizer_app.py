import os
import shutil
from tkinter import filedialog
import tkinter as tk


folders = {
    # Images
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.bmp': 'Images',
    '.gif': 'Images',
    '.webp': 'Images',
    '.svg': 'Images',
    '.ico': 'Images',
    '.tif': 'Images',
    '.tiff': 'Images',
    '.heic': 'Images',
    '.raw': 'Images',

    # Documents
    '.pdf': 'Documents',
    '.txt': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.rtf': 'Documents',
    '.odt': 'Documents',
    '.pages': 'Documents',
    '.md': 'Documents',
    '.tex': 'Documents',

    # Spreadsheets
    '.xls': 'Spreadsheets',
    '.xlsx': 'Spreadsheets',
    '.csv': 'Spreadsheets',
    '.ods': 'Spreadsheets',

    # Presentations
    '.ppt': 'Presentations',
    '.pptx': 'Presentations',
    '.odp': 'Presentations',

    # Music
    '.mp3': 'Music',
    '.wav': 'Music',
    '.flac': 'Music',
    '.aac': 'Music',
    '.ogg': 'Music',
    '.m4a': 'Music',
    '.wma': 'Music',
    '.aiff': 'Music',
    '.mid': 'Music',
    '.midi': 'Music',

    # Videos
    '.mp4': 'Videos',
    '.mkv': 'Videos',
    '.avi': 'Videos',
    '.mov': 'Videos',
    '.wmv': 'Videos',
    '.flv': 'Videos',
    '.webm': 'Videos',
    '.mpeg': 'Videos',
    '.mpg': 'Videos',
    '.3gp': 'Videos',
    '.m4v': 'Videos',

    # Archives
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.7z': 'Archives',
    '.tar': 'Archives',
    '.gz': 'Archives',
    '.bz2': 'Archives',
    '.xz': 'Archives',
    '.iso': 'Archives',
    '.cab': 'Archives',

    # Code
    '.py': 'Code',
    '.pyw': 'Code',
    '.java': 'Code',
    '.c': 'Code',
    '.cpp': 'Code',
    '.cc': 'Code',
    '.cs': 'Code',
    '.h': 'Code',
    '.hpp': 'Code',
    '.js': 'Code',
    '.jsx': 'Code',
    '.ts': 'Code',
    '.tsx': 'Code',
    '.html': 'Code',
    '.htm': 'Code',
    '.css': 'Code',
    '.scss': 'Code',
    '.php': 'Code',
    '.rb': 'Code',
    '.go': 'Code',
    '.rs': 'Code',
    '.swift': 'Code',
    '.kt': 'Code',
    '.lua': 'Code',
    '.luau': 'Code',
    '.r': 'Code',
    '.m': 'Code',
    '.pl': 'Code',
    '.sh': 'Code',
    '.bat': 'Code',
    '.ps1': 'Code',
    '.sql': 'Code',
    '.json': 'Code',
    '.xml': 'Code',
    '.yaml': 'Code',
    '.yml': 'Code',
    '.toml': 'Code',
    '.ini': 'Code',
    '.cfg': 'Code',

    # Executables
    '.exe': 'Applications',
    '.msi': 'Applications',
    '.apk': 'Applications',
    '.appx': 'Applications',
    '.deb': 'Applications',
    '.rpm': 'Applications',

    # Fonts
    '.ttf': 'Fonts',
    '.otf': 'Fonts',
    '.woff': 'Fonts',
    '.woff2': 'Fonts',

    # eBooks
    '.epub': 'Books',
    '.mobi': 'Books',
    '.azw3': 'Books',

    # Torrents
    '.torrent': 'Torrents',

    # Disk Images
    '.img': 'Disk Images',
    '.dmg': 'Disk Images',
    '.vhd': 'Disk Images',
    '.vhdx': 'Disk Images',

    # Backups
    '.bak': 'Backups',
    '.backup': 'Backups',

    # Logs
    '.log': 'Logs',

    # Shortcuts
    '.lnk': 'Shortcuts',

    # Misc
    '.tmp': 'Temp',
    '.temp': 'Temp',
    '.crdownload': 'Downloads',
    '.part': 'Downloads',
}


def selected_folder():
    folder_path = filedialog.askdirectory()
    label.config(text=folder_path)
    window.update()
    for file in os.listdir(folder_path):
    
        if not os.path.isfile(os.path.join(folder_path, file)):
            continue
    
        ext = os.path.splitext(file)[1]
        folder = folders.get(ext, 'Misc')
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
        
        try:
          shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, folder))
        except shutil.Error:
            pass #already there skips
        
    label.config(text='Done!')
            
        
window = tk.Tk()
window.title("File Organizer")
window.geometry("380x200")
window.configure(bg='#3305a6')

label = tk.Label(window,  text="select folder", font=('Segoe UI', 15, 'bold'), fg='#a60505', bg='#0590a6' )
label.pack()

button = button = tk.Button(window, text="click me to select folder", bg='#4CAF50', fg='white', font=('Arial', 11), relief='flat', padx=10, pady=5, command=selected_folder)
button.pack()

window.mainloop()