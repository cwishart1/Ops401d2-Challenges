#!/usr/bin/env python3

# Script Name:                  Challenge37-cookieMonster
# Class Name:                   Ops 401
# Author Name:                  Cody Wishart
# Date of latest revision:      5/25/21
# Purpose:                      Capture cookies

# Import Lib
import requests, os, webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

cookies = dict(name="cookieMonster")
response = requests.get(targetsite, cookies=cookies)
print("\nHTTP Respons\n" + str(response))
with open("response.html", "w") as file:
    file.write(str(response))



#filePath = 'file:///path/to/your/file/testdata.html'
#webbrowser.open("file://./response.html", new=2)  # open in new tab
#os.system("start response.html")
#os.system(f"firefox {response}")
