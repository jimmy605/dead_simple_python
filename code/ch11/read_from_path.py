from pathlib import PosixPath

path = PosixPath().joinpath(PosixPath.home(), '.bash_history')

with path.open('r') as file:
    for line in file:
        continue 
    print(line.strip())