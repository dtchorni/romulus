from ftplib import FTP
import sys


def load_file(f='data/ASTRO/2018/285/46P/FINE_POINT/NEOS_SCI_2018285081000_clean.fits'):
    global image
    image = fits.open(f)
    image.info()



def print_help(ftp=None,tokens=[]):
    print('Usage:\n\thelp : print this dialog'
          '\n\tls : list current directory'
          '\n\tcd <dir> : change into <dir>'
          '\n\tuse <dir> : use <dir> to download *clean.fits for processing'
          '\n\tq : quit')

def list_dir(ftp,tokens=[]):
    ftp.retrlines('LIST')

def change_dir(ftp,tokens):
    if len(tokens)==1:
        print('Error: missing dir')
    else:
        ftp.cwd(tokens[1])

def use_fits(ftp,tokens=[]):
    print('Using files from: ' ftp.pwd())

def quit_ftp(ftp,tokens):
    ftp.close()


def parse_input(ftp,inp):
    cmds = ['help','ls','cd','use','q']
    funcs = [print_help, list_dir, change_dir, use_fits, quit_ftp]
    tokens = inp.split(' ')
    if tokens[0] in cmds:
        func[cmds.index(tokens[0])](ftp,tokens)
        return tokens[0]
    else:
        print_help()


def handle_ftp(ftp):
    list_dir(ftp)
    while line in sys.stdin:
        parse_input(ftp, line):



def login_ftp(addr='ftp.asc-csa.gc.ca'):
    ftp = FTP(addr)
    ftp.login()
    ftp.cwd('/users/OpenData_DonneesOuvertes/pub/NEOSSAT/')
    handle_ftp(ftp)

def main():
    # load_file()
    login_ftp()

def load_file(f=r'D:\NEOSSAT Data\ASTRO\2018\033\2002_AJ129\FINE_POINT\NEOS_SCI_2018033163030_clean.fits'):
    image = fits.open(f)
    image.info()

def main():
   load_file()

if __name__ == "__main__":
    main()

