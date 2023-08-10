# ACFFS
## Automation of generating a redundant folder and file structure that makes up your projects


**ACFFS** is a program developed using Python. 
It is very lightweight and allows for the **automatic creation** of a given **folder** and **file structure**. This enables the automation of generating a redundant folder and file structure that makes up your projects. 
You can also provide the content for each file, which will be transferred to the created files.

To use **ACFFS**, you need to create the desired structure within the **"files_templates"** folder.
There, you can create the folder structure and the files.
For the files to have the correct naming and proper extension, you must adhere to the following naming convention: "filename-extension-template.txt".
Only the **"-template.txt"** part should be added to each file. 
Only **underscores** will not be replaced by a period or removed.
**Hyphens** in the middle will be replaced by a period.

You can then provide the content for each file, which will remain exactly the same in the files created by the program.

Once you have created the folder and file structure, you can execute the **"create.py"** file to initiate the creation of your structure.

## Steps of usage :
1. Execute **"create.py"**

You will be prompted to:

1. Select a destination folder
2. Name the folder that will be created and will contain your folders and files.
