# Molecular Parser

Small python script and web interface to parse a given molecular formula an get result in [Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) datatype

## Installation

Install and use [docker](https://docs.docker.com/get-docker/) 

Type commands list below in a terminal with your fingers (on the keyboard)
## Usage with Docker & docker-compose
Launch pre writen formulae
```bash
make launch_for_test
```
should return 
```bash
Water : H2O -> {'H': 2, 'O': 1}
Magnesium hydroxide : Mg(OH)2 -> {'Mg': 1, 'O': 2, 'H': 2}
Fremy's salt : K4[ON(SO3)2]2 -> {'K': 4, 'N': 2, 'O': 14, 'S': 4}
Sucrose : C12H22O11 -> {'C': 12, 'H': 22, 'O': 11}
```
Launch unit-tests with unittest 
```bash
make unit-test
```
Launch linter (flake8)
```bash
make lint
```
## Bonus - BackMolecule
Launch web interface http://0.0.0.0:5000
```bash
make launch-web
```
![BackMolecule](static/images/backMolecule.png?raw=true "Interface")
## Usage without Docker
[pip](https://pypi.org/project/pip/) is required to install project locally

CLI - Parse a formula
```bash
python3 parser.py Mg1H3EO4
```

CLI - Launch pre writen formulas
```bash
python3 launch_for_test.py 
```

Launch unit-tests with unittest 
```bash
python3 -m unittest tests/unit-test.py
```


## License
[MIT](https://choosealicense.com/licenses/mit/)