
#Crawlers 

- Crawlers  and spiders can be used to search the internet from search engines to extract info . 

- Crawlers discover content through various / many means . Like one is ............. by pure discovery .

- When a url is visited by the crawler and the info regarding the content type of the website is returned to search engine .

- Another method used by crawlers is that it also follows and visits any and all urls found from the previously visited websites .

- The crawler looks for keywords in the domain's visit and then indexes these keywords in the search engine . 

- If the user searches the keyword , then that domain whose same keyboard is indexed in the search engine , will be showed to the user .

#SEO

- Search engine optimisation (SEO)  . It is the practice of enhancing your website so that a search engine prioritize that domains website at the time of a search request by the user .

- The criteria for judging which aspects matter in a website differ , search engine to search engine . Some of the common ones include , how easy it is to crawl that website . How responsive your website is to different browser and all . 

#Robots-txt

- Similar to "Sitemaps" which we will later discuss, this file is the first thing indexed by "Crawlers" when visiting a website.
- This file must be served at the root directory - specified by the web-server itself. Looking at this files extension of **.txt**, its fairly safe to assume that it is a text file.
- The text file defines the permissions the "Crawler" has to the website. For example, what type of "Crawler" is allowed to index and sometimes it also specifies what not to index . 
- This ensures that websites domains such as admin login page and other imp and sensitive websites aren't indexed and displayed in searches when requested for .


![[robot-txt-keywords.png]]


-  The "Crawler" can index every other content that isn't contained within the disallowed directory.
- The crawler also knows the difference between directories , sub-directories and files , for example : "Disallow : /not-a-secret/but-this-is/" in this the crawler will only restrict indexing in the but-this-is/ directory . 

#Regexing

- Whilst you can make manual entries for every file extension that you don't want to be indexed, you will have to provide the directory it is within, as well as the full filename. 
- Imagine if you had a huge site! What a pain...Here's where we can use a bit of [regexing(opens in new tab)](https://www.rexegg.com/regex-quickstart.html).

![[regexing.png]]

- The $ is a used for a query format used by crawlers .
-  "sitemap.xml" thats how sitemaps are defined in websites . 
