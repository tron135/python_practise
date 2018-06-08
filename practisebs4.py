from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
	<html>
		<head>
			<meta charset="utf-8"/>
			<title>Anime Rocks</title>
			
			<link rel="stylesheet" href="main2.css"/>
			
		</head>
		<body >
			<div class="container">
				<header>
						<h1>Anime Rocks</h1>
						<form class="column">
							<input class="search" type="text" placeholder="Search..." required>
		                    <input class="button" type="button" value="Search">
						</form>	
						<nav class="top_nav">
							<ul>
								<li><a href="myweb.html">Home</a></li>
								<li><a href="genres.html">Genres</a></li>
								<li><a href="list.html">Anime List</a></li>
								<li><a href="">Contact</a></li>
								<li><a href="">About</a></li>
							</ul>
						</nav>
						<div class="clear"></div>
				</header>
				<section class="left_side">
				</section>
				<aside class="right_side">
					<div>
						<h3>Upcoming Animes</h3>
						<br/>
					</div>
					<div>
						<h3> Social Links</h3>
						<br/>
						<ul>
							<li><a href="">Facebook</a></li>
							<li><a href="">Twitter</a></li>
							<li><a href="">Youtube</a></li>
						</ul>
					</div>
				</aside>
				<footer class="page_footer">
					<br/>
					&copy; Copyright tron135.ihostfull.com
					<br/>
				</footer>
			</div>	
		</body>
	</html>"""

soup = BeautifulSoup(html, "html.parser")
# print(soup.body.div)
# d = soup.find("div")
# print(type(d))
print(soup.find(class_ = "right_side"))