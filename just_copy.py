import glob
import os
import shutil

dir_7007 = "C:/FTP/7007"
dir_7020 = "C:/FTP/7020"
dir_7166 = "C:/FTP/7166"
dir_5959 = "C:/FTP/5959"
dir_7011 = "C:/FTP/7011"
dir_7167 = "C:/FTP/7167"
dir_7549 = "C:/FTP/7549"
dir_7594 = "C:/FTP/7594"
backup_7007 = "C:/FTPBackup/7007"
backup_7020 = "C:/FTPBackup/7020"
backup_7166 = "C:/FTPBackup/7166"
backup_5959 = "C:/FTPBackup/5959"
backup_7011 = "C:/FTPBackup/7011"
backup_7167 = "C:/FTPBackup/7167"
backup_7549 = "C:/FTPBackup/7549"
backup_7594 = "C:/FTPBackup/7594"
src = "Z:/export/DESADV/"

for file in glob.glob(r'Z:/export/DESADV/codenudat_7007*.xml'):
    print(file)    
    shutil.copy(file, backup_7007)
    shutil.move(file, dir_7007)

     
for file in glob.glob(r'Z:/export/DESADV/codenudat_7020*.xml'):
    print(file)
    shutil.copy(file, backup_7020)
    shutil.move(file, dir_7020)
    

for file in glob.glob(r'Z:/export/DESADV/codenudat_7166*.xml'):
    print(file)
    shutil.copy(file, backup_7166)
    shutil.move(file, dir_7166)    
    
for file in glob.glob(r'Z:/export/DESADV/codenudat_5959*.xml'):
    print(file)
    shutil.copy(file, backup_5959)
    shutil.move(file, dir_5959) 
    
for file in glob.glob(r'Z:/export/DESADV/codenudat_7011*.xml'):
    print(file)
    shutil.copy(file, backup_7011)
    shutil.move(file, dir_7011)     
    
for file in glob.glob(r'Z:/export/DESADV/codenudat_7167*.xml'):
    print(file)
    shutil.copy(file, backup_7167)
    shutil.move(file, dir_7167) 
    
for file in glob.glob(r'Z:/export/DESADV/codenudat_7549*.xml'):
    print(file)
    shutil.copy(file, backup_7549)
    shutil.move(file, dir_7549)  
    

for file in glob.glob(r'Z:/export/DESADV/codenudat_7594*.xml'):
    print(file)
    shutil.copy(file, backup_7594)
    shutil.move(file, dir_7594) 
    




