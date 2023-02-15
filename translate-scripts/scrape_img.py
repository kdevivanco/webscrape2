import requests
import bs4
 

html_element = '''<ul class="list-no-style row wrap margin-bottom-xxlarge">
            <li class="border-box width-100 large-up-width-1-3 padding-small">
                <a class="scale-on-hover block bg-white radius" style="box-shadow: 0px 0px 5px rgba(144, 216, 210, 0.7)" href="https://www.classcentral.com/report/udemy-top-courses/">
                <img class="block radius width-100" src="https://ccweb.imgix.net/https%3A%2F%2Fwww.classcentral.com%2Fimages%2Fcollections%2Fcollections-udemy-top-courses.png?auto=format&amp;ixlib=php-3.3.1&amp;w=450&amp;s=243e8b030c78e5cd68b2e3ddd8e1bc7f" alt="250 Top Udemy Courses of All Time (2021)">
                </a>
            </li>
            <li class="border-box width-100 large-up-width-1-3 padding-small">
                <a class="scale-on-hover block bg-white radius" style="box-shadow: 0px 0px 5px rgba(144, 216, 210, 0.7)" href="https://www.classcentral.com/report/india-online-degrees/">
                <img class="block radius width-100" src="https://ccweb.imgix.net/https%3A%2F%2Fwww.classcentral.com%2Fimages%2Fcollections%2Fcollection-india-ugc-approved-online-degrees.png?auto=format&amp;ixlib=php-3.3.1&amp;w=450&amp;s=0165b8c5462a88d74b09d1ec21533264" alt="500+ UGC Approved Online Degrees from India’s Top Universities">
                </a>
            </li>
            <li class="border-box width-100 large-up-width-1-3 padding-small">
                <a class="scale-on-hover block bg-white radius" style="box-shadow: 0px 0px 5px rgba(144, 216, 210, 0.7)" href="https://www.classcentral.com/report/mooc-based-masters-degree/">
                <img class="block radius width-100" src="https://ccweb.imgix.net/https%3A%2F%2Fwww.classcentral.com%2Fimages%2Fcollections%2Fcollection-earn-a-masters-degree-social.png?auto=format&amp;ixlib=php-3.3.1&amp;w=450&amp;s=b6c23348d8c869ee66cab69691933e49" alt="70+ Legit Master’s Degrees You Can Now Earn Completely Online">
                </a>
            </li>
            <li class="border-box width-100 large-up-width-1-3 padding-small">
                <a class="scale-on-hover block bg-white radius" style="box-shadow: 0px 0px 5px rgba(144, 216, 210, 0.7)" href="https://www.classcentral.com/report/list-of-mooc-based-microcredentials/">
                <img class="block radius width-100" src="https://ccweb.imgix.net/https%3A%2F%2Fwww.classcentral.com%2Fimages%2Fcollections%2Fcollection-microcredentials-social.png?auto=format&amp;ixlib=php-3.3.1&amp;w=450&amp;s=ac00a29f643507e6d6ae41dd49791dce" alt="Massive List of MOOC-based Microcredentials">
                </a>
            </li>
            <li class="border-box width-100 large-up-width-1-3 padding-small">
                <a class="scale-on-hover block bg-white radius" style="box-shadow: 0px 0px 5px rgba(144, 216, 210, 0.7)" href="https://www.classcentral.com/collection/ivy-league-moocs">
                <img class="block radius width-100" src="https://ccweb.imgix.net/https%3A%2F%2Fwww.classcentral.com%2Fimages%2Fcollections%2Fcollection-ivy-league-moocs-social.jpg?auto=format&amp;ixlib=php-3.3.1&amp;w=450&amp;s=9fd82b0b3f0af3174ed36f9701d84ba2" alt="Free Online Ivy League Corses">
                </a>
            </li>
            <li class="border-box width-100 large-up-width-1-3 padding-small">
                <a class="scale-on-hover block bg-white radius" style="box-shadow: 0px 0px 5px rgba(144, 216, 210, 0.7)" href="https://www.classcentral.com/report/most-popular-online-courses/">
                <img class="block radius width-100" src="https://ccweb.imgix.net/https%3A%2F%2Fwww.classcentral.com%2Fimages%2Fcollections%2Fcollection-most-popular-all-time-social.png?auto=format&amp;ixlib=php-3.3.1&amp;w=450&amp;s=1f90fe42cee7ab47ab240f59cfb697e1" alt="The 100 Most Popular Online Courses of All Time">
                </a>
            </li>
        </ul>'''

soup = bs4.BeautifulSoup(html_element, 'html.parser')

# Find all `img` elements in the HTML
images = soup.find_all('img')

# Extract the src attribute of each image
for image in images:
    print(image['src'])

#set counter for img name
counter =0 

for img_tag in images:
    img_url = img_tag["src"]
    response = requests.get(img_url) #request the URL
    print (response)
    counter +=1
    path = "/Users/macbookpro/Desktop/Programacion/AllStars2/www.classcentral.com/images/collections/curated"
    with open(f"{path}/coll_{str(counter).split('/')[-1]}.png", "wb") as f:
           f.write(response.content) #Save file
