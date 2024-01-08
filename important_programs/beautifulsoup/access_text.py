sample_html= '''<html>
<head>
    <title>CoderzColumn : Developed for Developers by Developers for the betterment of Development.</title>
    <script src="static/script1.js"></script>
    <script src="static/script2.js"></script>
    <link rel="stylesheet" href="static/stylesheet.css" type="text/css" />
</head>
<body>
    <p id='start'>Welcome to CoderzColumn</p>
    <p id='main_para'>We regularly publish tutorials on various topics 
    (Python, Machine learning, Data Visualization, Digital Marketing, etc.) regularly explaining 
    how to use various Python libraries.</p>
    <p id='sub_para'>Below are list of Important Sections of Our Website : </p>
        <ul>
            <li><a href='https://coderzcolumn.com/blogs'>Blogs</a></li>
            <li><a href='https://coderzcolumn.com/tutorials'>Tutorials</a></li>
            <li><a href='https://coderzcolumn.com/about'>About</a></li>
            <li><a href='https://coderzcolumn.com/contact-us'>Contact US</a></li>
        </ul>
    <p id='end'>Please feel free to send us mail @ coderzcolumn07@gmail.com if you need any 
    information about any article or want us to publish article on particular topic.</p>
</body>
</html>'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(sample_html, 'html.parser')
whole_page_src = soup.html
print(soup.text)
print("=====================Title Text+++++++++++++++++++++")
print(soup.title.text)
print("=====================Body Text+++++++++++++++++++++")
print(soup.body.text.strip())
print("====================P text +++++++++++++++++++++++++")
print(soup.p.text)
print("====================UL text +++++++++++++++++++++++++")
print(soup.ul.get_text().strip())

# stripped_strings - It works like strings property only but removes newlines characters.
print(list(soup.ul.stripped_strings))