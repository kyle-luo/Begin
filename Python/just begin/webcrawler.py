def getnexttarget(page):
    startlink = page.find('<a href=')
    if startlink == -1:
        return None, 0
    startquote = page.find('"', startlink)
    endquote = page.find('"', startquote + 1)
    url = page[startquote + 1 : endquote]
    return url, endquote
    
def getalllinks(page):
    while True:
        url, endpos = getnexttarget(page)
        links = []
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
        
def crawlall(page):
    alllinks = getalllinks(page)
    crawled = []
    while True:   
        if alllinks[0] not in crawled:
            alllinks.append(getalllinks(alllinks[0]))
            crawled.append(alllinks[0])
            alllinks.remove(alllinks[0])
    return crawled
    
print getalllinks('https://udacity.github.io/cs101x/index.html')