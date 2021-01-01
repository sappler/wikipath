# wikipath
https://wikirace-288103.wl.r.appspot.com/

The website uses a Bi-Directional BFS to find the shortest path between two Wikipedia pages.
The starting "node" is the starting page, which performs a BFS on all of the links on the article.
The ending "node" is the ending page, which performs a BFS on all of the pages found on its "what links here" page.

I knew python and some basic HTML/CSS already, but this was my first time using Google Cloud services, Flask, JavaScript (with AJAX) together from scratch. 
Overall, I'm happy with how it came out, and I had a lot of fun making it.

The process that took the most time was deciding on what languages I wanted to use, 
and figuring out how to put it all together with a fantastic service like Google Cloud's App Engine.
