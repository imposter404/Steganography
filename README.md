# Steganography

## Written In Python

<div align="left">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="50px" alt="Python" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opencv/opencv-original.svg" height="50px" alt="OpenCV" />
</div>


## Python Dependency 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pypi/pypi-original.svg" height="50px" alt="pypi" />

> ``` console
> pip install opencv-python
> pip install numpy
> ```


---
# Method
### LSB 
Least Significant Bit
- #### Righttmost bit

    In this process we change the Rightmost bit for the whole pixel it will have less impact on the final value.If we change the Rightmost bit from `0` to `1` (`00011000` to `00011001`) it will change the decimal value  from `24` to `25`.


    ***Before encoding*** <br>
    pixel1=[ 01100100, 01111000, 1000110 `0`] #RGB(100,120,140)<br>
    pixel2=[ 01100100, 01111000, 1000110 `0`] #RGB(100,120,140)<br>
    pixel3=[ 01100100, 01111000, 1000110 `0`] #RGB(100,120,140)<br>

    secret_char='A' #binary: 01000001

    ***After encoding*** <br>
    pixel1=[ 01100100, 01111000, 1000110 `0`] #RGB(100,120,140)<br>
    pixel2=[ 01100100, 01111000, 1000110 `1`] #RGB(100,120,141)<br>
    pixel3=[ 01100100, 01111000, 1000110 `0`] #RGB(100,120,140)<br>


- #### RGB

    Here we change the rightmost bit for RGB channel for each pixel
    It works similer as before but here we can hide 3 bit data in each pixel

    ***Before encoding*** <br>
    pixel1=[ 0110010`0`, 0111100`0`, 1000110 `0`] #RGB(100,120,140)<br>
    pixel2=[ 0110010`0`, 0111100`0`, 1000110 `0`] #RGB(100,120,140)<br>
    pixel3=[ 0110010`0`, 0111100`0`, 1000110 `0`] #RGB(100,120,140)<br>
    pixel3=[ 0110010`0`, 0111100`0`, 1000110 `0`] #RGB(100,120,140)<br>

    secret_char='A' #binary: 01000001

    ***After encoding*** <br>
    pixel1=[ 0110010`0`, 0111100`1`, 1000110 `0`] #RGB(100,121,140)<br>
    pixel2=[ 0110010`0`, 0111100`0`, 1000110 `0`] #RGB(100,120,140)<br>
    pixel3=[ 0110010`0`, 0111100`0`, 1000110 `0`] #RGB(100,120,140)<br>
    pixel3=[ 0110010`0`, 0111100`1`, 1000110 `0`] #RGB(100,121,140)<br>


---
### MSB 
Most Significant Bit
- #### Leftmost bit

    In this process we change the Leftmost bit for the whole pixel it will have large impact on the final value. If we change the Rightmost bit from `0` to `1` (`00011000` to `10011000`) it will change the decimal value  from `24` to `152`.

    ***Before encoding*** <br>
    pixel1=[ `0`1100100, 01111000, 10001100 ] #RGB(100,120,140)<br>
    pixel2=[ `0`1100100, 01111000, 10001100 ] #RGB(100,120,140)<br>
    pixel3=[ `0`1100100, 01111000, 10001100 ] #RGB(100,120,140)<br>

    secret_char='A' #binary: 01000001

    ***After encoding*** <br>
    pixel1=[ `0`1100100, 01111000, 10001100 ] #RGB(100,120,140)<br>
    pixel2=[ `1`1100100, 01111000, 10001100 ] #RGB(228,120,141)<br>
    pixel3=[ `0`1100100, 01111000, 10001100 ] #RGB(100,120,140)<br>

- #### RGB

    Here we change the Leftmost bit for RGB channel for each pixel
    It works similer as before but here we can hide 3 bit data in each pixel

    ***Before encoding*** <br>
    pixel1=[ `0`1100100, `0`1111000, `1`0001100] #RGB(100,120,140)<br>
    pixel2=[ `0`1100100, `0`1111000, `1`0001100] #RGB(100,120,140)<br>
    pixel3=[ `0`1100100, `0`1111000, `1`0001100] #RGB(100,120,140)<br>
    pixel3=[ `0`1100100, `0`1111000, `1`0001100] #RGB(100,120,140)<br>

    secret_char='A' #binary: 01000001

    ***After encoding*** <br>
    pixel1=[ `0`1100100, `1`1111000, `1`0001100] #RGB(100,248,140)<br>
    pixel2=[ `0`1100100, `0`1111000, `1`0001100] #RGB(100,120,140)<br>
    pixel3=[ `0`1100100, `0`1111000, `1`0001100] #RGB(100,120,140)<br>
    pixel3=[ `0`1100100, `1`1111000, `1`0001100] #RGB(100,248,140)<br>


---
# Setup
The `requirements.txt` file should list all Python libraries that your code
depend on, and they will be installed using:

```
pip install -r requirements.txt
```
---
## Run
Jupyter Notebook
``` python 
Main.ipynb
```
