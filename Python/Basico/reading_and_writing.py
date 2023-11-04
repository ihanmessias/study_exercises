from pathlib import Path
import shutil
import os

### FILES:
## COPY
# CopyFile (Pode renomear o arquivo enquanto o move):
pwd = Path(__file__).parent
file_ = pwd / 'texto.txt'
file_d = pwd / 'destino1' / 'texto2.txt'
shutil.copyfile(file_, file_d)
# Copy1 (Apenas move o arquivo):
file_d = pwd / 'destino2'
shutil.copy(file_, file_d)
# Copy2 (Mantém os metadados originais):
file_d = pwd / 'destino3'
shutil.copy2(file_, file_d)

## MOVE
# Move file:
file_ = pwd / 'texto_move.txt'
file_d = pwd / 'destino1'
shutil.move(file_, file_d)

## DELETE
# Delete file:
file_ = pwd / 'texto_rm.txt'
if file_.exists():
    os.remove(file_)

### FOLDERS:
## CREATE
pwd = Path(__file__).parent
folder_ = pwd / 'destino4'
folder_.mkdir(exist_ok=True)
## CREATE2 
folder_ = pwd / 'destino5' / 'destino5_01'
folder_.mkdir(parents=True, exist_ok=True)
## COPY FODLER
shutil.copytree(pwd / 'destino5', pwd / 'destino1' / 'destino5')
## DELETE FOLDERS VAZIAS
folder_rm = pwd / 'destino5' / 'destino5_01'
folder_rm.rmdir()
## DELETE FOLDERS -RF
folder_rm = pwd / 'destino1'
shutil.rmtree(folder_rm)