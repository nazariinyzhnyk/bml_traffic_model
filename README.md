# Biham–Middleton–Levine traffic model

Self-organizing cellular automaton traffic flow model [wiki article](https://en.wikipedia.org/wiki/Biham–Middleton–Levine_traffic_model).

### Requirements

Project was developed in Python 3.6 using basic libraries.
See [requirements](requirements.txt) file for details.
To install all the libraries with preinstalled Python and pip cd to project's folder and run command in Terminal:

```
pip install -r requirements.txt
```

## Running

Basic examples are shown in [Jupyter Notebook](examples.ipynb).
Running simulations in terminal:

```
python main.py -fcols 50 -frows 50 -d 40 -i 100
```

where:
-fcols: number of fields' columns
-frows: number of fields' rows
-d: density
-i: number of iterations

## TODOs

- add possibility to save init and final matrix
- add experiments with different params to readme file
- add possibility to init various direction cars (+ to move left / up).
- add comments to explain program logic

## Authors

* **Nazarii Nyzhnyk** - *Initial work* - [nazariinyzhnyk](https://github.com/nazariinyzhnyk)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details
