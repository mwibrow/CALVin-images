# CALVin images

This repository contains the source SVG
images originally created for academic research use with
[CALVin](https://github.com/mwibrow/CALVin).

## Details

The SVGs were created with [Inkscape](https://inkscape.org/en/)
and then processed with [svgo](https://github.com/svg/svgo)
to remove all the Inkscape cruft.

## Converting to other formats

If PNG (or JPEG, etc.) versions of a particular image is required,
then the easiest way is to use Inkscape at the command line
(Inkscape usually does a better job of retaining transparency
for PNG files than other methods). For example:

```
inkscape -z -w 512 ball.svg -e ball.png
```

should convert the SVG file to a 512px by 512px
PNG.


|  |  |
| :---: | :---: |
| ball | peas |
| <img width=64 height=64 src="https://raw.githubusercontent.com/mwibrow/CALVin-images/master/svg/ball.svg?sanitize=true"> | <img width=64 height=64 src="https://raw.githubusercontent.com/mwibrow/CALVin-images/master/svg/ball.svg?sanitize=true"> |
| ball | peas |
| <img width=64 height=64 src="https://raw.githubusercontent.com/mwibrow/CALVin-images/master/svg/ball.svg?sanitize=true"> | <img width=64 height=64 src="https://raw.githubusercontent.com/mwibrow/CALVin-images/master/svg/ball.svg?sanitize=true"> |
