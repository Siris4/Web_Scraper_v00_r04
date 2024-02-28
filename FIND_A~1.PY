from bs4 import BeautifulSoup
import requests
# import chardet

response = requests.get("https://news.ycombinator.com/news")    # removed: , verify=False)
webpage_html_document = response.text

# PRINT THE WHOLE HTML DOC ONLY IF YOU NEED IT (will take up a lot of space in the console)
# print(webpage_html_document)

# NOW: dig in, and find the parts that we want out of the html doc.

# print(soup.title)  # For example, if we want the tab Title name, use print(soup.title)

  # what if we wanted to get a hold of the text that is the title of the first story link?

# article_upvote_tag = soup.find('span', id=score_id)

soup = BeautifulSoup(webpage_html_document, "html.parser")  # we want to pass the html document that we want to parse (yc_webpage), then we provide the Method of which we are going to parse it with.
articles = soup.find_all(name="a", class_="titlelink")   # removed: href="https://overkill.wtf/nintendo-sue-yuzu-emulator/")

article_texts = []  # to add data into the Lists
article_links = []  # to add data into the Lists

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(article_text)
    link = article_tag.get("href")  #looking for the Value: href
    article_links.append(article_link)
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]  #need to remove: .getText() because we can't use getText on Lists    # also removed: article_upvote_tag.getText()
                    # creating a new list (using List Comprehension)
        # this above is the same as:
        # for article_tag in articles:
        #     text = article_tag.getText()
        #     article_texts.append(article_text)


# article_upvotes = soup.find(name="span", class_="score")  # <span class="score" id="score_39530203">480 points</span>

# print(f"The <a> tag line is: {article_tag_first_yc_story_link}")    # the <a> tag line:  <a href="https://overkill.wtf/nintendo-sue-yuzu-emulator/">Nintendo is suing the creators of Switch emulator Yuzu</a>
# print(f"The .getText Method of article_tag_first_yc_story_link is: {article_tag_first_yc_story_link.getText()}\n")  # to GET the Text INSIDE/WITHIN the anchor tag:

# print(f"The Title of the article is: {article_tag_first_yc_story_link.text}")   # text of the article title itself: Nintendo is suing the creators of Switch emulator Yuzu

print(f"The Title of the article is: {article_texts}")
print(f"The article URL Link itself is: {article_links}")
print(f"The article Upvote Score is: {article_upvotes}")

# print(article_text)

# print(f"The Upvote point score.text is currently: {article_upvote.text}")
# print(f"The Upvote point score.getText() is currently: {article_upvote.getText()}")

# OR:

# article_upvote = soup.find(name="span", class_="score").getText()  # <span class="score" id="score_39530203">480 points</span>
# print(f"Using a different Method of .getText(), the article_upvote is: {article_upvote}")


