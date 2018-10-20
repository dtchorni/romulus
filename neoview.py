from astropy.io import fits


def load_file(f='data/ASTRO/2018/285/46P/FINE_POINT/NEOS_SCI_2018285081000_clean.fits'):
    image = fits.open(f)
    image.info()


def main():
    load_file()

if __name__ == "__main__":
    main()




