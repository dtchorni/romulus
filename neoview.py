from astropy.io import fits

def load_file(f=r'D:\NEOSSAT Data\ASTRO\2018\033\2002_AJ129\FINE_POINT\NEOS_SCI_2018033163030_clean.fits'):
    image = fits.open(f)
    image.info()

def main():
   load_file()

if __name__ == "__main__":
    main()

##Hi this is to track changes
