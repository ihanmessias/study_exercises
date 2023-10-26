from pathlib import Path

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