from ftplib import FTP
import sys
import os


# def load_file(f='data/ASTRO/2018/285/46P/FINE_POINT/NEOS_SCI_2018285081000_clean.fits'):
#     global image
#     image = fits.open(f)
#     image.info()



def print_help(ftp=None,tokens=[]):
    print('\nUsage:\n\thelp : print this dialog'
          '\n\tls : list current directory'
          '\n\tcd <dir> : change into <dir>'
          '\n\tuse <dir> : use <dir> to download *clean.fits for processing'
          '\n\tq : quit\n\n')

def list_dir(ftp,tokens=[]):
    ftp.retrlines('LIST')
    #[print(f) for f in ftp.nlst()]

def change_dir(ftp,tokens):
    if len(tokens)==1:
        print('Error: missing dir')
    else:
        tokens[1]=tokens[1][:-1]
        print(tokens[1])
        ftp.cwd(tokens[1])

def use_fits(ftp,tokens=[]):
    print('\n\nUsing clean fits files from: ' + ftp.pwd()+'\n\n')
    files = ftp.nlst()
    for f in files:
        if 'clean.fits' in f:
            print(f)
            ftp.retrbinary('RETR '+f, open('input_data/'+f, 'wb').write)


def quit_ftp(ftp,tokens):
    ftp.close()


def parse_input(ftp,inp):
    cmds = ['help\n','ls\n','cd','use\n','q\n']
    funcs = [print_help, list_dir, change_dir, use_fits, quit_ftp]
    tokens = inp.split(' ')
    print(tokens)
    if tokens[0] in cmds:
        funcs[cmds.index(tokens[0])](ftp,tokens)
    else:
        print_help()
    return tokens[0]


def handle_ftp(ftp):
    list_dir(ftp)
    print(':' + ftp.pwd() + '$ ',end='',flush=True)
    while 1:
        try:
            line =sys.stdin.readline()
        except KeyBoardInterrupt:
            break
        if not line:
            break

        if(parse_input(ftp, line)=='q\n'):
            return
        print(':'+ftp.pwd()+'$ ',end='',flush=True)



def login_ftp(addr='ftp.asc-csa.gc.ca'):
    ftp = FTP(addr)
    ftp.login()
    ftp.cwd('/users/OpenData_DonneesOuvertes/pub/NEOSSAT/')
    handle_ftp(ftp)

def main():
    # load_file()
    login_ftp()

##TODO: Integrate the asteroid finder through program

if __name__ == "__main__":
    main()

