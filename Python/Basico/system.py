from pathlib import Path
import os
caminho = Path('primeira_pasta/segunda_pasta')

for nome in ['file1.txt','file2.txt','file3.txt']:
    caminho_file = caminho / nome
    print(caminho_file)
    
Path.home()
Path.cwd()
Path.cwd().is_absolute()
Path('primeira_pasta').is_absolute()
Path('/').is_absolute()
Path('/labs').is_absolute()
(Path.cwd() / 'primeira_pasta').exists()
(Path.cwd() / 'primeira_pastaaaaa').exists()
__file__
Path(__file__).parent
Path(__file__).parents[0]
Path(__file__).parents[1]
Path(__file__).parents[2]
Path(__file__).anchor
Path(__file__).name
Path(__file__).stem
Path(__file__).suffix
Path(__file__).drive
list(Path.cwd().glob('*'))
list(Path.cwd().glob('*.py'))
list(Path.cwd().glob('*/*'))
list(Path.cwd().glob('**/*'))
list(Path.cwd().glob('**/.*')) # Pastas Ocultas
list(Path.home().glob('**/.*'))
for i in list(Path.home().glob('**/*')):
    if i.is_file():
        print(i)
list(Path.cwd().glob('**/*.txt'))
Path(__file__).is_file()
Path(__file__).is_dir()
Path(__file__).parent.is_dir()
os.path.getsize(__file__)

# Exercise:
def search_file(path, file:str) -> str:
    for f in path.glob('**/*'):         
        if f.is_file():
            if f.name == file:
                print(f)
search_file(Path.home(), 'environments.txt')

# Exercise 2:
def size_files(path):
    for d in path.glob('*'):
        if d.is_dir() and not d.name.startswith('.'):
            size=0
            for files in d.glob('**/*'):
                if files.is_file():
                    size += os.path.getsize(files)
            print(d.name, round(size / 1024 / 1024, 2), 'mb')