import html2markdown as h2m
import urllib.request
import re
from sys import argv, exit

if __name__ == '__main__':
    if len(argv) not in (2, 3): exit(1)

    day = argv[1]
    if int(day) not in range(1, 24):
        exit(1)
    destinationFilePath = argv[2]

    url = "https://adventofcode.com/2020/day/" + day
    response = urllib.request.urlopen(url)
    content = str(response.read())
    


    taskBegin = '<article class="day-desc">'
    taskEnd = '</article>'
    htmlTask = content[content.index(taskBegin) + len(taskBegin):content.index(taskEnd)]
    
    print(htmlTask)
    markdownTask = h2m.convert(htmlTask)
    markdownTask = markdownTask.replace('\\n', '\n\t')
    markdownTask = markdownTask.replace("\\\\'", "'")
    markdownTask = re.sub('<em.*?>', '**', markdownTask)
    markdownTask = re.sub('</em>', '**', markdownTask)
    markdownTask = re.sub('(\[.*?\]\()/(.*?\))', r'\1https://adventofcode.com/\2', markdownTask)
    
    markdownTask = re.sub('<.*?>', '', markdownTask)



    destinationFile = open(destinationFilePath, "w")
    destinationFile.write(format(markdownTask))
    destinationFile.close()

