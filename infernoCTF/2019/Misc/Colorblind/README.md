# Color Blind
## 139

What do the colors mean?

Author : nullpxl

file: `colorblind.png`


# Solution

Nothing special with this challenge, we are given a 64x1 sized png, and we just need to read the pixels rgb vaules as ascii characters.

```py
from PIL import Image

im = Image.open('colorblind.png') 
pix = im.load()
print(im.size)  


for x in range(im.size[0]):
	for y in range(im.size[1]):
		for z in range(3):
			print(chr(pix[x,y][z]), end='')
```

Data extracted from the script:
```
blahblahblah_hello_how_are_you_today_i_hope_you_are_not_doing_this_manually_infernoCTF{h3y_100k_y0u_4r3_n07_h3x_bl1nD_:O}_doing_this_manually_would_be_a_bad_idea_you_shouldnt_do_it_manually_ok
```

flag: `infernoCTF{h3y_100k_y0u_4r3_n07_h3x_bl1nD_:O}`