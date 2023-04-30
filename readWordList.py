WORD_LIST_FILE_PATH = "/Users/omar/obsidian/post-grad"
WORD_LIST_FILE_NAME = "words.md"

f = open(WORD_LIST_FILE_PATH + "/" + WORD_LIST_FILE_NAME, "r")
for x in f:
    print(x)


