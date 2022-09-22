""" ****GUI***************************************************************
- Want a GUI that lets user select the desired folder to be organized.
- Can create custom sorting folders
    - Can choose file types associated with each folder
- Can run organization once or choose to have the program monitor 
  folder/folders for changes and keep them organized.
    - can set interval for checking the folder
"""

""" **********************************************************************
Get path to folder that needs to be organized(selected using GUI)
    - make sure that directory exists
        - if it does not exist return popup window error
        - if it does set target path variable to equal path entered
"""

""" **********************************************************************
Check target folder for folders used to sort files
    - ie. Videos, Pictures, Zips, Drivers, Setup Files
        - [Pictures, Videos, Audio, Misc., Zip/Rar, Drivers, Installers]
    - check for each folder specified by the GUI
        - if folder does not exist create the folder
    - add custom folders with custom filetype associations
    - create file association per folder
    - can add custom filetypes and associate them or choose from list of known filetypes
"""

""" **********************************************************************
Check each file in target directory for filetype
    - if filetype is not equal to a filetype associated with a folder for sorting skip it
    - if filetype is associated with a folder move that file to it's associated folder
        - probably use a list of file types to compare the list of files to
"""

""" **********************************************************************

"""

""" **********************************************************************

"""

""" **********************************************************************

"""