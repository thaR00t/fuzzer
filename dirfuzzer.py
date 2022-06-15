#import libs
from rich import print
import requests
import argparse
import textwrap
import time
from format import help,display,status

# Creating an interface
parser = argparse.ArgumentParser(description="Welcome this is a simple web fuzzer enjoy fuzzing!",
formatter_class = argparse.RawDescriptionHelpFormatter,
epilog=textwrap.dedent('''EXAMPLE:\n
dirfuzzer.py -u http://example.com -w <wordlist> # Simple fuzzin
dirfuzzer.py -u http://example.com -w <wordlist> -x .txt # Add extension
dirfuzzer.py -u http://example.com -w <wordlist> -o output.txt # Save the fuzzing's output
'''))

parser.add_argument('-u','--url',type=str, help='Specified an url.')
parser.add_argument('-w','--wordlist', help='Insert a wordlists.')
parser.add_argument('-x','--extension',type=str,help='Select an extension for the fuzzin')
parser.add_argument('-o','--output',help='Save the output into a file.')
parser.add_argument('-b','--banner',help='If you want you can spawn the banner')
args = parser.parse_args()



#Creating var

url = args.url
wlist = args.wordlist
ext= args.extension
out = args.output
ban = args.banner

try:
    if ban:
        print(display())
    else:
        if url and wlist:
            print(display())
            print(status())
            wordlistline = open(wlist, 'r').readlines()
            #for loop to analyze the wordlist
            for i in range(0,len(wordlistline)):                                                                
                enumeration=wordlistline[i].replace("\n",(ext or ""))

                #Send a request                                                                                                                                                   
                r = requests.get(url+"/"+enumeration)                                                           
                #Check the status of the page if is 404 is not available then don't print it                                                                                           
                if  r.status_code != 404:                                                                       
                    output = ("         ("+str(r.status_code)+")        "+url+"/"+enumeration)                                         

                    print(f"[bold orange_red1]{output}[/bold orange_red1]")
                    time.sleep(0.1)
                    if out:                
                        outfile = (str(r.status_code)+"   "+url+'/'+enumeration)
                        with open(out,'a') as f:
                            f.write(outfile+"\n")
                            f.close()

        else:

            print(help())

except KeyboardInterrupt:
        print("[bold red] [!]Script interrupt by user[!][/bold red]")
