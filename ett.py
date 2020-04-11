from ebooklib import epub
from os import mkdir,sep
import os
from bs4 import BeautifulSoup as bs
from tkinter import *
from tkinter import filedialog

#pips needed
#pip install ebooklib
#pip install bs4
if not os.path.exists(r'c:\audiobook'):
        os.makedirs(r'c:\audiobook')
class Ett:
        def __init__(self,path):
                self.book = epub.read_epub(path)
                self.title = self.book.title
        def get_pages(self):
                table_of_contents = self.book.spine
                ids = list(zip(*table_of_contents))[0]
                try:
                        mkdir("c:\\audiobook\\"+self.title)
                except FileExistsError as e:
                        return False
                i=1
                book=self.book
                for x in ids:
                        part = book.get_item_with_id(x)
                        part_text = bs(part.get_content(),"lxml").get_text()
                        try:
                            with open("c:\\audiobook\\"+self.title + sep +str(i)+".txt","w") as file:
                                    print(part_text)
                                    file.write(part_text)
                        except UnicodeEncodeError as e:
                            pass

                        i+=1
                return True

#Ett("american-god.epub").get_pages()
#make an an object of Ett class
# Ex:
book = Ett('text.epub')
#and call the get_pages() to convert epub to txt
# Ex:
book.get_pages()
#Now a folder will be created with name skyward,and each chapter of skyward will be inside it as text files
