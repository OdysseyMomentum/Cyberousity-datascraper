# Cyberousity

## CyberGraph
.
CyberGraph is a visualizing tool that depicts a graph of websites and their cyber-crime relations. The WebScraper scrapes cyber-crime related words and generates a histogram per every website. These histograms will then be compared between each other and the result is a graph that shows various relations between the websites w.r.t. cyber-crime.

Usage: Download `CyberGraph.zip` to your computer, extract files and click on `CyberGraph.exe`

(Note that this visualisation serves merely as a demo and is based on fictional data)

## WebScraper
.
The WebScraper program is responsible for extracting crime-related keywords from a given website. The input is a URL link and the output is a file including a JSON line which includes:
- A histogram of the top 10 most frequently occurring crime-related words on that website
- A percentage of all crime related words used in the website text

Usage: Open the main.py in an editor and input a URL as a parameter to the execution. You MUST have the file `Keywords` in the same directory as the `main.py`.

Public Safety - Open-Source 911
