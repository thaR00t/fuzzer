#help
def help():
    help=("\n[bold]dirfuzzer.py -u and -w missing check the [-h] or [--help] to display the help command[bold]")
    return help


#display
def display():
    banner=( """
[bold blue]
            _ _      __                               
 __| (_)_ _ / _|_  _ _________ _ _  _ __ _  _ 
/ _` | | '_|  _| || |_ /_ / -_) '_|| '_ \ || |
\__,_|_|_| |_|  \_,_/__/__\___|_|(_) .__/\_, |
                                   |_|   |__/ [/bold blue]""")        
    return banner

def status():
    stat=(""" 
    _______________________________
    \n   [!]Ctrl ^C to interrupt the script
    _______________________________
        status          url
    """)
    return stat
