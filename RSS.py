#! /usr/bin/python

# SHEBANG GOES HERE
#############################################################################
#                               _ _                                         #
#                         /\   | | |                                        #
#                        /  \  | | |  _   _  ___  _   _ _ __                #
#                       / /\ \ | | | | | | |/ _ \| | | | '__|               #
#                      / ____ \| | | | |_| | (_) | |_| | |                  #
#                     /_/    \_|_|_|  \__, |\___/ \__,_|_|                  #
#                     | |              __/ |                                #
#                     | |__   __ _ ___|___/    __ _ _ __ ___                #
#                     | '_ \ / _` / __|/ _ \  / _` | '__/ _ \               #
#                     | |_) | (_| \__ |  __/ | (_| | | |  __/               #
#                     |_.__/ \__,_|___/\___|  \__,_|_|  \___|               #
#                     | |        | |                   | |                  #
#                     | |__   ___| | ___  _ __   __ _  | |_ ___             #
#                     | '_ \ / _ | |/ _ \| '_ \ / _` | | __/ _ \            #
#                     | |_) |  __| | (_) | | | | (_| | | || (_) |           #
#                     |_.__/ \___|_|\___/|_| |_|\__, |  \__\___/            #
#                     | | | / __|                __/ |                      #
#                     | |_| \__ \               |___/                       #
#                      \__,_|___/                                           #
#                                                                           #
#               https://www.facebook.com/AiiYourBaseRBel0ngToUs             #
#               If you have suggestions or want to get involved             #
#############################################################################

"""
This program aims to create a constant RSS feed on my third monitor
This will provide me with constant news updates

14/09/2015
AND DATE OF FINISHING HERE

If you have any suggestions or want to help
contact me at`
https://www.facebook.com/AiiYourBaseRBel0ngToUs

This program abides by the rules of presentation for
PEP-8
shown here on
https://www.python.org/dev/peps/pep-0008/

This program also abides by the Unix Philosophy

You may use this code, or any features of 22this code
in your own work, as long as you link my page
and the BSD licensing, which can be copied directly
below.

https://www.facebook.com/AiiYourBaseRBel0ngToUs
*BSD licensed*

More info can be read here
http://opensource.org/licenses/BSD-3-Clause


What is an RSS feed?
RSS stands for R S S
They can be used to import news or other sources and have a customised
news feed at your will, this reader was created to be my, the owners, customised
news feed. It will be displayed on a raspberry pi on a small monitor i have on
my desk.
An article in an RSS feed is one news piece or one object of data.
An example of this is

"BBC NEWS
Can AI take over the world?
17/09/2015
Stephen Hawkings seems to think so, according to his newest study. "

RSS feeds have multiple attributes, these are the ones i have used in this program.

TITLE - The title of the RSS article, this is normally the very first thing
you'll see, as it'll allow you to name the article it's currently working on
Using the BBC example above, this would be the title "Can AI take over the world?"
The feed title, which is "BBC NEWS" can also be considered a title,
but it isn't a title of the article, it's a title of the feed.

Description -  The description of the RSS article, this tends to either be
the whole news story of just the general gist of it, depending on what the
RSS feed owner has decided on.
An example of an RSS description is the
"Stephen Hawkings seems to think so, according to his newest study. "
in the BBC example.

Date - The date is the published date of the RSS article, when it was published.
An example of this is the 17/09/2015 in the BBC example

"""

# enable DEVMODE to get accurcate error reports and other
# cool nifty things, only use if you are debugging
DEVMODE = True

import logging
# imports the loggign module, creates a logging file called "ProgramLog.txt"
# this helps debug the program
logging.basicConfig(filename='ProgramLog.txt', level=logging.DEBUG,
					format=' %(asctime)s - %(levelname)s- %(message)s')

global_wait_time = 3
# this is a global variable, for how long each RSS article waits before renewing
# ans it also allows you to read the articles, instead of an infinite loop
# of RSS feeds
# used in conjuntuion with the Time module
if DEVMODE == False:
	logging.disable(logging.CRITICAL)
# if DEVMODE is false, turn off debugging.

import time
# imports the time module, vital so it doesn't infinitely loop every 0.002 seconds
from pyfiglet import Figlet
# figlet from linux but in python makes pretty fonts such as the one i use above
import feedparser
# feed parser is used to get the RSS feeds and parse them

logging.debug("all modules installed sucessfully")

f = Figlet(font="slant")
# uses the figlet font Slant, change Slant if you want a different font
logging.debug("Figlet set up correctly")

def main():
	logging.info("Start of Main()")

	while True:
		# infinite loop
		logging.debug("starting RSS feed loop")
		RSS()
		logging.debug("Finished RSS feed, waiting 60 seconds to refresh")
		# infinitely loops through RSS(). this is because its an infinite
		# RSS feed displayer
		time.sleep(60)
		# but waits a minute before doing it again

	logging.debug("sucessfully went to RSS")


def RSS():

	#file = open("fb.txt", 'w')
	#facebook(feedparser)
	# uncomment to allow facebook notifs

	# these are all the RSS feeds i've gathered so far
	bbc(feedparser)
	# Goes to BBC RSS feed
	lifehacker(feedparser)
	# goes to Lifehacker RSS feed
	makeuseof(feedparser)
	# goes to makeuseof RSS feed
	wired(feedparser)
	# goes to wired RSS feed
	OMGUbuntu(feedparser)
	# goes to OMGUbuntu RSS feed
	howtogeek(feedparser)
	# goes to Howtogeek RSS feed

def makeuseof(feedparser):
	Makeuseof_feed = feedparser.parse("http://feeds.feedburner.com/makeuseof")
	# gets the feed url to parse into the RSS reader
	print("\n\n")
	# prints 2 new lines, for readabillity
	print(f.renderText(Makeuseof_feed['feed']['title']))
	# makes a massive logo of the RSS feed using Figlet
	articles = Makeuseof_feed['entries']
	# puts all the entires into a list

	counter = 0
	# creates a counter starting at 0
	for i in articles:
		# for every item in articles

		print(articles[(counter)].title)
		# print the title
		# the rough description of it
		print(articles[(counter)].link)
		# and a link to it
		print("\n")
		# and then a new line
		time.sleep(global_wait_time)
		# wait 2 seconds
		counter = counter + 1
		# add 1 to counter and loop over again

def wired(feedparser):
	Wired_feed = feedparser.parse("http://feeds.wired.com/wired/index")
	print("\n\n")
	print(f.renderText(Wired_feed['feed']['title']))
	# using Figlet, print the title of the RSS feed

	articles = Wired_feed['entries']
	#Get all the articles in a list form

	counter = 0
	# creates a counter starting at 0
	for i in articles:
		# for every item in articles

		print(articles[(counter)].title)
		# print the title
		print(articles[(counter)].link)
		# and a link to it
		print("\n")
		# and then a new line
		time.sleep(global_wait_time)
		# wait 2 seconds
		counter = counter + 1
		# add 1 to counter and loop over again

def OMGUbuntu(feedparser):
	OMGUbuntu_feed = feedparser.parse("http://feeds.feedburner.com/d0od")
	print("\n\n")
	print(f.renderText(OMGUbuntu_feed['feed']['title']))
	# using Figlet, print the title of the RSS feed

	articles = OMGUbuntu_feed['entries']
	#Get all the articles in a list form

	counter = 0
	# creates a counter starting at 0
	for i in articles:
		# for every item in articles

		print(articles[(counter)].title)
		# print the title
		print(articles[(counter)].link)
		# and a link to it
		print("\n")
		# and then a new line
		time.sleep(global_wait_time)
		# wait 2 seconds
		counter = counter + 1
		# add 1 to counter and loop over again

def howtogeek(feedparser):
	HowToGeek_feed = feedparser.parse("http://feeds.feedburner.com/HowToGeek")
	print("\n\n")
	print(f.renderText(HowToGeek_feed['feed']['title']))
	# using Figlet, print the title of the RSS feed

	articles = HowToGeek_feed['entries']
	#Get all the articles in a list form

	counter = 0
	# creates a counter starting at 0
	for i in articles:
		# for every item in articles

		print(articles[(counter)].title)
		# print the title
		print(articles[(counter)].link)
		# and a link to it
		print("\n")
		# and then a new line
		time.sleep(global_wait_time)
		# wait 2 seconds
		counter = counter + 1
		# add 1 to counter and loop over again

def lifehacker(feedparser):
	Lifehacker_feed = feedparser.parse("http://feeds.gawker.com/lifehacker/full.xml")
	print("\n\n")
	print(f.renderText(Lifehacker_feed['feed']['title']))
	# using Figlet, print the title of the RSS feed

	articles = Lifehacker_feed['entries']
	#Get all the articles in a list form

	counter = 0
	# creates a counter starting at 0
	for i in articles:
		# for every item in articles

		print(articles[(counter)].title)
		# print the title
		print(articles[(counter)].link)
		# and a link to it
		print("\n")
		# and then a new line
		time.sleep(global_wait_time)
		# wait 2 seconds
		counter = counter + 1
		# add 1 to counter and loop over again

def bbc(feedparser):
	BBC_feed = feedparser.parse('http://feeds.bbci.co.uk/news/'
									 'technology/rss.xml?edition=uk')
	print("\n\n")
	print(f.renderText(BBC_feed['feed']['title']))
	articles = BBC_feed['entries']
	counter = 0
	for i in articles:

		print(articles[(counter)].title)
		print(articles[(counter)].description)
		print(articles[(counter)].link)
		print("\n")
		time.sleep(2)
		counter = counter + 1



# required in all programs, if the name "main" is called, run main()
# i do this instead of main() at the bottom so this can
# still be imported as a module
if __name__ == '__main__':
	main()
