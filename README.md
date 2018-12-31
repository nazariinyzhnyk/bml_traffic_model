# Biham–Middleton–Levine traffic model

Self-organizing cellular automaton traffic flow model
 ([wiki article](https://en.wikipedia.org/wiki/Biham–Middleton–Levine_traffic_model)). <br />

###Simple example:
Initial matrix:<br />
![alt text](results/2018-12-31 14/11/11.png)

Resulting matrix:<br />
![alt text](results/2018-12-31 14/11/19.png)

### Requirements

Project was developed in Python 3.6 using basic libraries.<br />
See [requirements](requirements.txt) file for details.<br />
To install all the libraries with preinstalled Python and pip cd to project's folder and run command in Terminal:

```
pip install -r requirements.txt
```

## Running

Basic examples are shown in [Jupyter Notebook](examples.ipynb).
Running simulations in terminal:

```
python main.py -fcols 50 -frows 50 -d 40 -i 100 -p 1
```

where:<br />
-fcols: number of fields' columns<br />
-frows: number of fields' rows<br />
-d: density<br />
-i: number of iterations<br />
-p: save plot flag

## TODOs

- add possibility to init various direction cars (+ to move left / up);
- pass args to plot_matrix function to  save plots with normal names.

## Authors

* **Nazarii Nyzhnyk** - *Initial work* - [nazariinyzhnyk](https://github.com/nazariinyzhnyk)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details
