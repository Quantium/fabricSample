# Fabric Sample

I made this as a simple example of :cloud: :computer: (cloud computing). This is the python code to manage a 4-cores cluster made with :strawberry:Raspberry Pi B+, a simple switch and cables. Its made with :snake:Python 3 and Fabric. Every Raspberry is running Raspbian and its SSH port is open and tested.

![Raspberry 4 Cores Cluster](https://raw.githubusercontent.com/quantium/fabricSample/master/readme_files/raspberry4CoresCluster.jpeg)

## Getting Started

You don't need the raspberries, any linux computer with ssh access through your local network will work fine for most of the examples. But, think again! Build the cluster is so much fun.

It's better if you have some previous knowledge about:

* Python 3 :snake:
* Linux Shell :penguin:
* Computer Hardware :computer:
* Raspberry Pi :strawberry:

Just Fork or clone this project and keep reading.

### Prerequisites

If you don't have it already, [install Python 3](https://realpython.com/installing-python/) I'm using Python 3.6.5+

One you have Python 3 installed use pip to install fabric, in the console type:

```
pip install fabric
```

You will need at least 4 linux machines, you could use virtual ones if you want. This computers will need to have the SSH port open and accessible to your network from your computer

### Installing

Just clone or fork this repository and run the samples with python from a terminal.

```
python3 ls.py
```

```
ifconfig wlan0 down

crontab -e

@reboot sudo ifdown wlan0
```

## Built With

* [Python](https://www.python.org/) - The programming language
* [Fabric](https://maven.apache.org/) - The library for streamlining
* [Raspbian](https://rometools.github.io/rome/) - The Operative System for the cluster

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Andrés González Aragón** - [Quantium](https://github.com/Quantium)

See also the list of [contributors](https://github.com/Quantium/fabricSample/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Thank you to everybody in the [Python](https://www.python.org/) team.
+ Thank you to the people who program and maintain [fabric](http://www.fabfile.org/)
* Thank you very much to the guys of [Raspberry PI](https://www.raspberrypi.org/)
* The Dog Bone Case was bought [here](https://www.amazon.com/gp/product/B01LVUVVOQ)
