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
## What is Steganography ?
Steganography is a practice in which a file, image, text or video is concealed within another file, image, text or video

## Why to use Steganography over Cryptography
the main advantage of Steganography over Cryptography alone is that the intednded secrect message does not attract attention to itself. Plainly visible encrypted message, no matter how unbreakable they are, arouse interest.

---
# Method
### LSB 
**Least Significant Bit** : this method changes the Rightmost bit for the whole pixel, it will have less impact on the final value. If we change the Rightmost bit from `0` to `1` (`00011000` to `00011001`) it will change the decimal value  from `24` to `25`.

- #### Righttmost bit
    #RGB(100,120,140)<br>
    [ 01100100, 01111000, 1000110 `0`] 


- #### RGB
    #RGB(100,120,140)<br>
    [ 0110010`0`, 0111100`0`, 1000110 `0`] 

    ---
### MSB 
**Most Significant Bit** :this method changes the Leftmost bit for the whole pixel it will have large impact on the final value. If we change the Rightmost bit from `0` to `1` (`00011000` to `10011000`) it will change the decimal value  from `24` to `152`.

- #### Leftmost bit
    #RGB(100,120,140)<br>
    [ `0`1100100, 01111000, 10001100 ] 

- #### RGB
    #RGB(100,120,140)<br>
    [ `0`1100100, `0`1111000, `1`0001100] 
    
    ---


### Hybrid
this method is used for pictures. Most significat bit is taken from both picture to make a new RGB pixel
    
[ **1100**1010, **0010**0110, **1110**1110] <br>
[ **0000**1010, **1100**0001, **1111**1110] <br>
<br>
[ **1100** **0000** , **0010** **1100** , **1110** **1111**]



---
# Code

- ### Text

    `encode()` function run all the encoding method in selected image

    > ```python
    > def encode():
    >     LSB_encode()
    >     LSB_RGB_encode()
    >     MSB_encode()
    >     MSB_RGB_encode()
    > ```

    > ```python
    > encode()
    > ```

    `decode()` function run all the encoding method in selected image

    > ```python
    > def decode():
    >     LSB_decode()
    >     LSB_RGB_decode()
    >     MSB_decode()
    >     MSB_RGB_decode()
    > ```

    > ```python
    > decode()
    > ```
    ---

- ### Picture

    `image1.jpg` & `image2.jpg` is used here to encode

    > ```python
    > Hybrid_encode()
    > Hybrid_decode()
    > ```

    >[!IMPORTANT]
    > shape of `image2.jpg` < `image1.jpg`



---
# Setup
The `requirements.txt` file should list all Python libraries that your code
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

---
## Run
Pythin
```pyhton
Main.py
```

Jupyter Notebook
``` python 
Main.ipynb
```
