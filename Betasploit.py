#!/usr/bin/env python3

imp = __import__

req = imp("requests")

time = imp("time")

pl = imp("platform")

os = imp("os")

sys = imp("sys")

web = imp("webbrowser")

socket = imp("socket")

cl = imp("colorama")

random = imp("random")

google = imp("googlesearch")


f = cl.Fore 

os.system("")

bs = "}"
s = "{"

print(f"""

                 ___      _        ___      _     _ _
                | _ ) ___| |_ __ _/ __|_ __| |___(_) |_
                | _ \/ -_)  _/ _` \__ \ '_ \ / _ \ |  _|
                |___/\___|\__\__,_|___/ .__/_\___/_|\__|
                                        |_|
                    
        {f.YELLOW}{bs}==============[      {f.CYAN}Host1let{f.YELLOW}        ]=============={s}
        {f.YELLOW}{bs}==============[    {f.CYAN}Version 1.0.0{f.YELLOW}     ]=============={s}
        {f.YELLOW}{bs}==============[{f.CYAN}Powered By Python 3.11{f.YELLOW}]=============={s}
{f.RESET}""")


dorklist = ["category", "id", "name", "Id", 'query', 'cat', 'page', 'view', 'data', 'page_code', 'mode', 'code', 'typeboard', 'prodID', 'no', 'ps_db', 'uid', 'act', 'bd', 'board', 'lan', 'show', 'item_ID', '']
dorkpath = ["/dork/id", "/dork/category", '/dork/query', '/dork/name', '/dork/cat', '/dork/page', '/dork/view', '/dork/data', '/dork/page_code', '/dork/mode', '/dork/code', '/dork/typeboard', '/dork/prodID', '/dork/no', '/dork/ps_db', '/dork/uid', '/dork/act', '/dork/bd', '/dork/board', '/dork/LAN', '/dork/show', '/dork/item_id', '/dork/item_ID', '/dork/Item_id', '/dork/Item_ID']


class HELP:
    
    def usage(numberDict):
        dictX = {
            'commands' : [
                {
                    '1' : 'help',
                    'info' : 'show this message',
                    'usage' : 'type " help "'
                },
                {
                    '1' : 'plus',
                    'info' : 'plus two number together',
                    'usage' : 'plus x:y => x , y are 1 2 3 ...'
                },
                {
                    '1' : 'search',
                    'info' : 'search a Query on Google',
                    'usage' : 'search Python Book (pdf) For H4ckers'
                },
                {
                    '1' : 'dork',
                    'info' : 'find websites for sql injection',
                    'usage' : {
                        'arg1' : 'local > local=true => choose something from " dorklist " variable and searching for that',
                        'arg2' : 'dorkPath > dorkPath=/dork/{} => search a special Dork by user, you can see dork paths options by typing " pathdork "'
                    }
                },
                {
                    '1' : 'open',
                    'info' : 'open an link by default system Browser => actually work at Windows and Linux Desktop',
                    'usage' : 'open #<link> => open https://www.example.com'
                },
                {
                    '1' : 'read',
                    'info' : 'read an file or pathfile',
                    'usage' : 'read #<file or path> => " read numbers.txt " or " read /home/usr/bin/nmap " or " read C:\\User\\SYSNAME\\Desktop\\Something.txt "'
                },
                {
                    '1' : 'sys',
                    'info' : 'You can use system commands by sys',
                    'usage' : 'sys ... #<Commands> => sys ls && echo Hi'
                },
                {
                    '1' : 'osinfo',
                    'info' : 'Give the OS information',
                    'usage' : {
                        'arg1' : 'clear > clear=true => Print Better'
                    }
                },
                {
                    '1' : 'alexa',
                    'info' : 'Use Request Polling > first try to get json data, if cannot try to get status code else continue the program',
                    'usage' : {
                        'arg1' : 'url > url=https://www.example.com => set url',
                        'arg2' : 'method > method=<GET - POST> => set method, if you dont call the method arg, its GET by default'
                    }
                },
                {
                    '1' : 'exit',
                    'info' : 'finish program',
                    'usage' : 'type " exit "'
                }
            ]
        }
        
        return dictX['commands'][numberDict]

class GNU(object):

    inf = {}

    inf["system"] = pl.system()
    inf["node"] = pl.node()
    inf["release"] = pl.release()
    inf["version"] = pl.version()
    inf["machine"] = pl.machine()
    inf["python_version"] = sys.version
    inf["sys_time"] = "{}".format(time.strftime("%H:%M:%S"))
    inf["sys_date"] = "{}".format(time.strftime("%y.%m.%d"))

    def allInfo():
        return GNU.inf

    def betterView():
        print("{:<25} {:<}".format("Key", "Value"))
        print("-"*40)
        for k, v in GNU.inf.items():
            print("{:<25} {:<}".format(k, v))




class Box:

    def __init__(self, msg: str):
        self.msg = str(msg)

    @property
    def postive(self):
        return f"\n{f.RESET}[{f.GREEN}+{f.RESET}] {self.msg}"

    @property
    def negative(self):
        return f"\n{f.RESET}[{f.RED}!{f.RESET}] {self.msg}"

    @property
    def action(self):
        return f"\n{f.RESET}[{f.BLUE}*{f.RESET}] {self.msg}"


class SearchBox(object):

    def __init__(self, query: str = None):

        self.q = str(query)

    def start(self):

        print(Box(f"Start Searching for '{f.RED} {self.q}{f.RESET} ' ...").action)
        print()

        try:

            for url in google.search(self.q):
 
                print(Box(url).postive)

        except Exception as e:
            print(Box("[{}] Error: {}".format(time.strftime("%H:%M:%S"), e)).negative)
            pass


class Console(object):

    def _():
        while 1:
            user = str(input("\nBetasploit > "))
            text = user.split()

            if user == "help":
                numsx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                
                for n in numsx:
                    main = HELP.usage(n)
                    com = main.get('1')
                    info = main.get('info')
                    use = main.get('usage')
                    print(Box('''Command: {}
Info: {}
Usage: {}'''.format(com, info, use)).postive)

            if user.startswith("plus"):
                nums = [int(num) for num in user.replace("plus ", "").split(":")]
                #for i in nums:
                print(Box(nums[0]+nums[-1]).postive)

            if user.startswith("search"):
                query = user.replace("search ", "")

                try:
                    SearchBox(query).start()
                except KeyboardInterrupt:
                    print(Box('Close SearchBox Class').action)
                    pass

            if user.startswith("dork"):
                local = text[text.index("dork")+1].replace("local=", "")
                if local == "true":
                    something = random.choice(dorklist)
                    SearchBox(f"inurl:*.php?{something}=").start()

                else:
                    if len(text) == 2:
                        dork = text[text.index("dork")+1].replace("dorkPath=", "")
                        if dork.startswith('/dork/'):
                            _dork = dork.replace('/dork/', '')
                            if not f"/dork/{_dork}" in dorkpath:
                                print(Box("Invalid Path`s ID Dork").negative)
                                
                            else:
                                try:
                                    SearchBox(f'inurl:*.php?{_dork}=').start()
                                except KeyboardInterrupt:
                                    print(Box('Close SearchBox Class').action)
                                    pass
                            
                        else:
                            print(Box("Invalid Path`s Dork").negative)

            if "pathsdork" in text:
                print(Box(dorkpath).postive)

            if user.startswith("sys"):
                order = user.replace("sys ", "")
                try:
                    os.system(order)
                except Exception as es:
                    print(Box(es).negative)
                    pass

            if "osinfo" in text:
                if len(text) >= 2 and text[text.index("osinfo")+1].replace("clear=", "") == "true":
                    print()
                    GNU.betterView()
                    print()
                else:
                    print()
                    print(GNU.allInfo())
                    print()

            if "open" in text:
                url = text[text.index("open")+1]
                print(Box(f"Try to open ' {f.YELLOW}{url}{f.RESET} ' ...").action)

                try:
                    web.open(url)
                    print(Box(f"Live View in ' {f.GREEN}{url}{f.RESET} '").postive)
                except Exception as ew:
                    print(Box("[{}] Error: {}".format(time.strftime("%H:%M:%S"), ew)).negative)


            if 'read' in text:
                print(Box('Try to Open ...').action)
                try:
                    fileToRead = text[text.index('read')+1]
                    print(Box(f"File Openned ' {f.RED}{fileToRead}{f.RESET} '").postive)
                    print(Box('Try To Read ...').action)
                    file = open(fileToRead, 'r').read()
                    print(Box(f"File Readed ' {f.RED}{fileToRead}{f.RESET} '\n").postive)
                    print(file)
                except Exception as ETR:
                    print(Box('[{}] Error: {}'.format(time.strftime('%H:%M:%S'), ETR)).negative)
                    pass
                
            if 'alexa' in text:
                print(Box('Try to process information').action)
                if len(text) >= 3:
                    try:
                        urlx = text[text.index('alexa')+1].replace('url=', '')
                        print(Box(f"Url: ' {f.RED}{urlx}{f.RESET} '").postive)
                        method = text[text.index('alexa')+2].replace('method=', '')       
                        print(Box(f"Method: ' {f.RED}{method}{f.RESET} '").postive)
                        if method == "GET":
                            try:
                                respone = req.get(urlx).json()
                                print(Box(respone).postive)
                            except:
                                print(Box("Cannot Get Json Data").negative)
                                print(Box('Try To Get STATUS_CODE').action)
                                try:
                                    respone = req.get(urlx).status_code
                                    print(Box(respone).postive)
                                except Exception as EMAIN:
                                    print(Box('[{}] Error: {}'.format(time.strftime('%H:%M:%S'), EMAIN)).negative)
                                    pass
                                
                        elif method == "POST":
                            try:
                                respone = req.post(urlx).json()
                                print(Box(respone).postive)
                            except:
                                print(Box("Cannot Get Json Data").negative)
                                print(Box('Try To Get STATUS_CODE').action)
                                try:
                                    respone = req.post(urlx).status_code
                                    print(Box(respone).postive)
                                except Exception as EMAIN:
                                    print(Box('[{}] Error: {}'.format(time.strftime('%H:%M:%S'), EMAIN)).negative)
                                    pass
                                    
                    except Exception as EMAIN2:
                        print(Box('[{}] Error: {}'.format(time.strftime('%H:%M:%S'), EMAIN2)).negative)
                        pass
                
                else:
                    try:
                        urlx = text[text.index('alexa')+1].replace('url=', '')
                        print(Box(f"Url: ' {f.RED}{urlx}{f.RESET} '").postive)
                        method = "GET"       
                        print(Box(f"Method: ' {f.RED}{method}{f.RESET} '").postive)
                        try:
                            respone = req.get(urlx).json()
                            print(Box(respone).postive)
                        except:
                            print(Box("Cannot Get Json Data").negative)
                            print(Box('Try To Get STATUS_CODE').action)
                            try:
                                respone = req.get(urlx).status_code
                                print(Box(respone).postive)
                            except Exception as EMAIN:
                                print(Box('[{}] Error: {}'.format(time.strftime('%H:%M:%S'), EMAIN)).negative)
                                pass
                                    
                    except Exception as EMAIN2:
                        print(Box('[{}] Error: {}'.format(time.strftime('%H:%M:%S'), EMAIN2)).negative)
                        pass
                    

            if user == "exit":
                print(Box("Finish").action)
                exit()


if __name__ == "__main__":
    try:
        Console._()

    except Exception as EMain:
        print(Box(EMain).negative)
        pass
