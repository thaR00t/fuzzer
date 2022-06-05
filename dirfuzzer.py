#import libs
import requests
import argparse
import textwrap




# Creating an interface
parser = argparse.ArgumentParser(description="Welcome this is a simple web fuzzer enjoy fuzzing!",
formatter_class = argparse.RawDescriptionHelpFormatter,
epilog=textwrap.dedent('''EXAMPLE:


dirfuzzer.py -u http://example.com/ -w <wordlist> # Simple fuzzin
dirfuzzer.py -u http://example.com/ -w <wordlist> -o output.txt # Save the fuzzing's output 
'''))

parser.add_argument('-u','--url',type=str, help='Specified an url.')
parser.add_argument('-w','--wordlist', help='Insert a wordlists.')
parser.add_argument('-o','--output',help='Save the output into a file.')
args = parser.parse_args()


#Wrote by shortcu7 aka thaR00t
print('''

============================================

 SIMPLE WEB DIRECTORY FUZZER, HOPE YOU ENJOY 
WITH THIS SIMPLE SCRIPT,
REPORT ANY ISSUES AND ANY ADVICE.

 ============================================
Ctrl ^C to interrupt the script

 status code:        url:
''')

#Creating var
url = args.url
wlist = args.wordlist
out = args.output

#Analyze the wordlist
wordlistline = open(wlist, 'r').readlines()

try:
    for i in range(0,len(wordlistline)):      # For loop
        enumeration=wordlistline[i].replace("\n",'')    #check the line then go on the next 
        r = requests.get(url+"/"+enumeration)           #send a request
        if r.status_code != 404:                        #if the request is not 404 it's correct!
            output = ("    "+str(r.status_code)+"                 "+url+'/'+enumeration)                #r.status_code record the status of the server which is 404 is no available
            print(output)                                                                               #if is 200 is availabl, then print the output
except KeyboardInterrupt:
        print("Script interrupt by user")
        

outfile = (str(r.status_code)+" | "+ url+'/'+enumeration )
f= open(out,'a')
f.write(outfile+"\n")
f.close()
