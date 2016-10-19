#!/usr/bin/env python

"""
Extract all links from a web page
=================================
Author: Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://pythonadventures.wordpress.com/2011/03/10/extract-all-links-from-a-web-page/
GitHub: https://github.com/jabbalaci/Bash-Utils

Given a webpage, extract all links.

Usage:
------
./get_links.py <URL>
"""

import sys
import urllib
import urlparse
import re

from BeautifulSoup import BeautifulSoup


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


def process(url):
    myopener = MyOpener()
    #page = urllib.urlopen(url)
    page = myopener.open(url)

    text = page.read()
    page.close()

    soup = BeautifulSoup(text)

    urls = []

    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        urls.append(tag['href'])

    return urls
    
# process(url)


def main():


    # Store the urls we were given
    urls_queue = sys.argv[1:] 
    urls_found = []
    urls_done = []

    site_roots = []

    # Get the domains to keep us on the same domain (don't follow external links)
    for url in urls_queue:
        mre = re.match('^https?://[^/]*',url,re.IGNORECASE)
        if mre:
            site_roots.append( mre.group(0) )

    urls_queue = [url for inurl in sys.argv[1:] for url in process(inurl) if any([url.startswith(sr) for sr in site_roots])]
    urls_queue = list( set(urls_queue) )

    while len(urls_queue) > 0:

        # Get url off the top of the queue
        url = urls_queue.pop()
        urls_done.append(url)

        found = process(url)

        for uf in found:
            # I'd suggest checking to make sure it's on the same domain here
            if not any( [ uf.startswith( site_root ) for site_root in site_roots ] ):
                continue # Next url, this is off site

            if uf not in urls_found:
                urls_found.append(uf) 

            # If we don't have it in the queue, queue it up
            if uf not in urls_queue and uf not in urls_done:
                urls_queue.append(uf)
    
        print "Done %d; Queued %d; Found %d (%s)" % ( len(urls_done), len(urls_queue), len(urls_found), url )

    print urls_found
# main()

#############################################################################

if __name__ == "__main__":
    main()

        
        
