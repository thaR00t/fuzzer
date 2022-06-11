#import libs
from rich import print
import requests
import argparse
import textwrap


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
args = parser.parse_args()

print("""
dirfuzzer.py -u and -w missing check the [-h] or [--help] to display the help command

""")

display = """"
[italic blue]
============================================
WEB DIRECTORY FUZZER, HOPE YOU ENJOY 
WITH THIS SCRIPT,
REPORT ANY ISSUES AND ANY ADVICE.
============================================
Ctrl ^C to interrupt the script
 status code:        url:

[/italic blue]

"""

#Creating var
url = args.url
wlist = args.wordlist
ext= args.extension
out = args.output


try:
        
        
        #Analyze the wordlist 
        if wlist:
            print(display)
            wordlistline = open(wlist, 'r').readlines()                                             
            for i in range(0,len(wordlistline)):                                                                #For loop

                enumeration=wordlistline[i].replace("\n",(ext or ""))                                                                                                                                                            # 
                r = requests.get(url+"/"+enumeration)                                                           #send a request                                                                                                        # 

                if  r.status_code != 404 and 400:                                                               #if the request is not 404 and 400 it's correct!
                    output = ("    "+str(r.status_code)+"              "+url+'/'+enumeration)                   #r.status_code record the status of the server which is 404 is no available                    
                                                                                                                #then if is 200 is availabl, and print the output
                    print(f"[bold orange_red1]{output}[/bold orange_red1]")
                    if out:
                        outfile = (str(r.status_code)+" "+ url+'/'+enumeration)
                        with open(out,'a') as f:
                            f.write(outfile+"\n")
                            f.close()
            
        

except KeyboardInterrupt:
        print("[italic red][!]Script interrupt by user[/italic red]")
