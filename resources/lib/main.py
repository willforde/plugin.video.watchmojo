"""
	Copyright: (c) 2013 William Forde (willforde+xbmc@gmail.com)
	License: GPLv3, see LICENSE for more details
	
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Call Necessary Imports
from xbmcutil import listitem, urlhandler, plugin
import parsers

BASEURL = u"http://www.sciencefriday.com%s"
class Initialize(listitem.VirtualFS):
	@plugin.error_handler
	def scraper(self):
		# Fetch Video Content
<<<<<<< HEAD
		url = u"%s/video/theme/" % BASEURL
		sourceCode = urlhandler.urlread(url, 604800) # TTL = 1 Week
		videoItems = parsers.CategorysParser().parse(sourceCode)
		
		# Add Extra Items
		icon = (plugin.getIcon(),0)
		self.add_youtube_channel("watchmojo", hasHD=False)
		self.add_item(u"-%s" % plugin.getuni(32941), thumbnail=icon, url={"action":"Videos", "url":"/video/cat/home/1"})
		self.add_item(u"-%s" % plugin.getuni(30101), thumbnail=icon, url={"action":"Themes", "url":"/video/theme/"})
		
		# Set Content Properties
		self.set_sort_methods(self.sort_method_video_title)
		self.set_content("files")
		
		# Return List of Video Listitems
		return videoItems

class Themes(listitem.VirtualFS):
	@plugin.error_handler
	def scraper(self):
		# Fetch Video Content
		url = BASEURL + plugin["url"]
		sourceCode = urlhandler.urlread(url, 604800) # TTL = 1 Week
		videoItems = parsers.ThemesParser().parse(sourceCode)
		
		# Set Content Properties
		self.set_sort_methods(self.sort_method_video_title)
		self.set_content("files")
		
		# Return List of Video Listitems
		return videoItems

class SubCat(listitem.VirtualFS):
	@plugin.error_handler
	def scraper(self):
		# Fetch Video Content
		url = u"%s/video/theme/" % BASEURL
		sourceCode = urlhandler.urlread(url, 604800) # TTL = 1 Week
=======
		url = BASEURL % "/about/about-science-friday.html"
		sourceCode = urlhandler.urlread(url, 604800) # TTL = 1 Week
		
		# Add Extra Items
		icon = (plugin.getIcon(),0)
		self.add_youtube_channel("SciFri", hasPlaylist=True, hasHD=True)
		self.add_item(u"-%s" % plugin.getuni(30101), thumbnail=icon, url={"action":"Recent", "url":"/video/index.html#page/full-width-list/1", "type":"video"})
		self.add_item(u"-%s" % plugin.getuni(30102), thumbnail=icon, url={"action":"Recent", "url":"/audio/index.html#page/full-width-list/1", "type":"audio"})
>>>>>>> origin/master
		
		# Set Content Properties
		self.set_sort_methods(self.sort_method_video_title)
		self.set_content("files")
		
		# Fetch and Return VideoItems
		return self.regex_scraper(sourceCode)
	
	def regex_scraper(self, sourceCode):
		# Create Speed vars
		results = []
		additem = results.append
		localListitem = listitem.ListItem
		mainTitle = plugin["title"]
		import re
		
<<<<<<< HEAD
		# Add Current Category
		self.add_item(label=u"-%s" % mainTitle, url={"action":"Videos", "url":plugin["url"]})
		mainTitle = mainTitle.lower()
		
		for catID in plugin["idlist"].split(u","):
			# Fetch Title and Set url & action
			url = u"/video/id/%s/1" % catID
			title = re.findall('<a href="%s">(.+?)</a>' % url, sourceCode)[0]
			if title.lower() == mainTitle: continue
			
			# Create listitem of Data
			item = localListitem()
			item.setLabel(title)
			item.setParamDict(action="Videos", url=url)
			
			# Store Listitem data
=======
		# Deside on content type to show be default
		if plugin.getSetting("defaultview") == "0": # Video
			menuItem = plugin.getuni(30002)
			contentType = ("video-list", "segment-list")
		
		else: # Audio
			menuItem = plugin.getuni(30003)
			contentType = ("segment-list", "video-list")
		
		# Loop each topic
		for url, title in re.findall('<li><a\shref="(/topics/\S+?\.html)">(.+?)</a></li>', sourceCode):
			# Create listitem of Data For Video
			item = localListitem()
			item.setLabel(title)
			item.setParamDict(action="ContentLister", url="%s#page/bytopic/1" % url, type=contentType[0])
			item.addContextMenuItem(menuItem, "XBMC.Container.Update", action="ContentLister", url="%s#page/bytopic/1" % url, type=contentType[1])
>>>>>>> origin/master
			additem(item.getListitemTuple(False))
			
		# Return list of listitems
		return results

class ContentLister(listitem.VirtualFS):
	@plugin.error_handler
	def scraper(self):
		# Fetch Video Content
<<<<<<< HEAD
		url = BASEURL + plugin["url"].replace(u" ",u"%20")
		sourceCode = urlhandler.urlread(url, 14400) # TTL = 4 Hours
		videoItems = parsers.VideosParser().parse(sourceCode)
=======
		url = BASEURL % plugin["url"]
		sourceCode = urlhandler.urlread(url, 14400) # TTL = 4 Hours
		videoItems = parsers.VideosParser().parse(sourceCode, plugin["type"])
		
		# Set Content Properties
		self.set_sort_methods(self.sort_method_date, self.sort_method_video_title)
		self.set_content("episodes")
		
		# Return List of Video Listitems
		return videoItems

class Recent(listitem.VirtualFS):
	@plugin.error_handler
	def scraper(self):
		# Fetch Video Content
		url = BASEURL % plugin["url"]
		sourceCode = urlhandler.urlread(url, 14400) # TTL = 4 Hours
		videoItems = parsers.RecentParser().parse(sourceCode)
>>>>>>> origin/master
		
		# Set Content Properties
		self.set_sort_methods(self.sort_method_date, self.sort_method_video_title)
		self.set_content("episodes")
		
		# Return List of Video Listitems
		return videoItems

class PlayVideo(listitem.PlayMedia):
	@plugin.error_handler
	def resolve(self):
		# Create url for oembed api
<<<<<<< HEAD
		url = BASEURL + plugin["url"]
=======
		url = BASEURL % plugin["url"]
		sourceCode = urlhandler.urlread(url, 14400)# TTL = 4 Hours
		
		# Search for Internal Video Source url
		if "video-permalink-player" in sourceCode and "video-permalink-player" in sourceCode and ("data-videosrc" in sourceCode or "data-flashvideosrc" in sourceCode):
			import re
			plugin.debug("Found Internal Link")
			for part1, part2 in re.findall('data-videosrc="(\S*?)"|data-flashvideosrc="(\S*?)"', sourceCode):
				if part1: return part1
				elif part2: return part2
			return url[0]
		else:
			# Atempt to Find External Video Source
			return self.sources(sourceCode)

class PlayAudio(listitem.PlayMedia):
	@plugin.error_handler
	def resolve(self):
		# Create url for oembed api
		url = BASEURL % plugin["url"]
>>>>>>> origin/master
		sourceCode = urlhandler.urlread(url, 14400)# TTL = 4 Hours
		import re
		
		# Search sourceCode for audo file
		stitcher = re.findall('<a\sclass="stitcher-ll"\shref="(http://app\.stitcher\.com\S+?)"\starget="_blank">', sourceCode)[0]
		return plugin.parse_qs(stitcher[stitcher.find("?")+1:])["url"]
