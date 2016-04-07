import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORS = []

PHRASE = {
	"class %%%(%%%):": "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)": "class has-a __init__ takes self and *** parameters.",

}