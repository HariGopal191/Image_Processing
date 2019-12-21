from PIL import Image, ImageDraw
import PIL
def get_colors(infile, outfile, numcolors=10, swatchsize=20, resize=150):

    image = PIL.Image.open(infile)
    image = Image.Image.resize(image,(resize, resize),resample=0)
    result = Image.Image.convert(image,'P', palette=PIL.Image.ADAPTIVE, colors=numcolors)
    result.putalpha(0)
    colors = result.getcolors(resize*resize)

    # Save colors to file

    pal = PIL.Image.new('RGB', (swatchsize*numcolors, swatchsize))
    draw = ImageDraw.Draw(pal)

    posx = 0
    for count, col in colors:
        draw.rectangle([posx, 0, posx+swatchsize, swatchsize], fill=col)
        posx = posx + swatchsize

    
    del draw
    pal.save(outfile, "PNG")

if __name__ == '__main__':
    get_colors('Harry.jpg', 'outfile.png')

