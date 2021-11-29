# kEvol

kEvol is a multi-program family that has implemented EA algorithms.

## Description


kEvol is a multi-program family that has been written in Python. You can use this family, whether as a single set of programs or modules imported in other programs. kEvol allows to define all the possible values of the EA algorithm's parameters and create all possible  
combinations of those parameters known as the configurations. The algorithm will test these configurations, and a report will be generated. A command line-based reporter also allows users to load the EA algorithm report(s) and query different information and plot them.


## Getting Started

### Dependencies

* OS: Windows/Linux

### Installing


* Currently, the only support is for the \*nix-based systems


To install simply
```
   git clone https://github.com/keagleV/kEvol.git
```
Then,
```
   ./install.sh
```

### Executing program

As stated before, since kEvol is not a single program, there is general structure that must be followed. However, if the prerequistis 
for each stage is qualified, you can continue and start with any stage.

Firts, create a .val file:



Then use the mkconfig program to create the configuration file:
```
mkconfig -f NAME.val
```

Now the configuration file is ready to be used by the main program:
```
kevol -f config.cfg
```

Optionally, you can use the reporter program for perform a novel analyzation:
```
reporter -f report.csv
```

## Help

For any help through using this family, you can use -h or --help command line option to get help about that specific program.
In the case of any ambiguity or software bug or any collaboration, feel free to send me an email at my email address.


## Authors

Contributors names and contact info

ex. Kiarash Sedghi 
ex. kiarash.sedghi99@gmail.com




## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
