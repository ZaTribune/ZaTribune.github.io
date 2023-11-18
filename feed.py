import yaml

import xml.etree.ElementTree as xml_tree

with open("feed.yaml", "r") as file:
    yamlData = yaml.safe_load(file)

    rssElement = xml_tree.Element(
        "rss",
        {
            "version": "2.0",
            "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
            "xmlns:content": "http://purl.org/rss/1.0/modules/content/",
        },
    )

channelElement = xml_tree.SubElement(rssElement, "channel")

linkPrefix = yamlData["link"]

xml_tree.SubElement(channelElement, "title").text = yamlData["title"]
xml_tree.SubElement(channelElement, "format").text = yamlData["format"]
xml_tree.SubElement(channelElement, "subtitle").text = yamlData["subtitle"]
xml_tree.SubElement(channelElement, "description").text = yamlData["description"]
xml_tree.SubElement(channelElement, "language").text = yamlData["language"]
xml_tree.SubElement(channelElement, "link").text = linkPrefix

xml_tree.SubElement(channelElement, "itunes:author").text = yamlData["author"]
xml_tree.SubElement(channelElement, "itunes:image", {"href": linkPrefix + yamlData["image"]})
xml_tree.SubElement(channelElement, "itunes:category", {"test": yamlData["category"]})

for item in yamlData['item']:
    itemElement=xml_tree.SubElement(channelElement, "item")
    xml_tree.SubElement(itemElement, "title").text = item["title"]
    xml_tree.SubElement(itemElement, "itunes:author").text = yamlData["author"]
    xml_tree.SubElement(itemElement, "description").text = item["description"]
    xml_tree.SubElement(itemElement, "itunes:duration").text = item["duration"]
    xml_tree.SubElement(itemElement, "pubDate").text = item["published"]

    enclosureElement=xml_tree.SubElement(itemElement, "enclosure",{
      "url":linkPrefix+item["file"],
      "type":"audio/mpeg",
      "length":item["length"]

    })

outputree = xml_tree.ElementTree(rssElement)
outputree.write("podcast.xml", encoding="UTF-8", xml_declaration=True)
