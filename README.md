# gameoflife-rgb
Game of Life compressed into the rgb channels of each pixel

## How to use
Clone the repository and enter it by using this command
```bash
git clone https://github.com/cooper-anderson/gameoflife-rgb;
cd gameoflife-rgb;
```

Now run `rgb.py` by running one of these commands
```bash
python rgb.py
```
or
```bash
./rgb.py
```

Note that for the second one, you may need to enable permissions

## How it works
The actual Game of Life that is running here is just running like normal. However, the way it is being displayed is different. Instead of having each cell on the grid correspond to one pixel, I switched it so that 3 cells correspond to one pixel, and those three cells determine if the RGB values of that pixel are on or off. Since there are only 2 states for each of the 3 bits, that gives us 8 total color combinations. Those being in order: black, blue, green, cyan, red, magenta, yellow and white.

## Screenshots
![rgb](screenshots/rgb.png "RGB Demonstation")
![glider](screenshots/glider.png "Glider Frame")

