<h1 align="center" id="title">Memory Game</h1>

<p align="center"><img src="./resources/readme/memory-game.png" alt="memory-game-image"></p>

<p id="description">Memory game using a modular structure and PyGame.</p>

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Installation Step](#installation-steps)
- [The process](#the-process)
  - [Built with](#built-with)
  - [Structure](#structure)
- [Useful resources](#useful-resources)
- [License](#license)
- [Author](#author)

## Demo

<img src="./resources/readme/1.png" alt="memory-game-image-1">
<img src="./resources/readme/2.png" alt="memory-game-image-2">
<img src="./resources/readme/3.png" alt="memory-game-image-3">
<img src="./resources/readme/4.png" alt="memory-game-image-4">
<img src="./resources/readme/5.png" alt="memory-game-image-5">
  
## Features

Here're some of the project's best features:

*   Demonstrating proficiency in Python.
*   Demonstrating proficiency in Modular Structures.
*   Demonstrating proficiency in Object Oriented Programming.

## Installation Steps:

1. Clone the repository.
2. Open the project with Visual Studio Code.
3. Run the app and enjoy it.

## The process 
### Built with

Technologies used in the project:

*   PyGame
*   Python 3.9
*   Visual Studio Code 1.70.2

### Structure

``` Python
    for fila in cuadros:
        x = 0
        for cuadro in fila:
            if cuadro.descubierto or cuadro.mostrar:
                pantalla_juego.blit(cuadro.imagen_real, (x, y))
            else:
                pantalla_juego.blit(imagen_oculta, (x, y))
            x += medida_cuadro
        y += medida_cuadro
```

## Useful resources

* [PyGame](https://www.pygame.org/news) - PyGame is a set of Python language modules that allow the creation of two-dimensional video games in a simple way.
* [Python](https://www.python.org/) - High-level interpreted programming language whose philosophy emphasizes the readability of its code.
* [Visual Studio Code](https://code.visualstudio.com/) - Source code editor developed by Microsoft.

## License:

> This project is licensed under the MIT License

## Author

Made with 💚 by [R4cz](https://www.linkedin.com/in/r4cz/)
