---
layout: post
title: My Pre-Sales Workflow with OmniOutliner
permalink: /blog/my-presales-workflow-with-omnioutliner
tags: presales omnioutliner trello workflow node.js mac opml
---

Pre-sales is part of my job, and thus is estimating projects and activities, tasks.
Since about the past Xmas I'm a Mac user, and in the last months I embraced [OmniOutliner](https://www.omnigroup.com/omnioutliner), a great outliner - and much much more - for the Mac and iOS devices.

As a presales engineer, with OmniOutliner I can quickly put down an outline of any project, organize it and estimate tasks just by adding a 'duration' column and filling in values. Fast, easy, effective.

Where OmniOutliner lacks something, in my workflow, is about giving estimates, expressed as [FTE](https://en.wikipedia.org/wiki/Full-time_equivalent), an economic value. And doing some easy calc on given estimates, or being able to export to [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) (I've got the standard version, but neither the pro version does this afaik).

## Requisites
I wanted to be able to:

- convert human-friendly durations to a computable numeric format (work Hours, FTE)
- export basic task info and estimates to Numbers
- export the project outline to Pages, so to quickly compile a document suitable to be given to Customers
- export tasks to a [Trello](https://trello.com) board, by which to later trace work.

## Workflow
Basically my workflow looks like this:

1. Begin a project writing an outline in OmniOutliner
2. export tasks to a spreadsheet for economics and other calculations based on estimates
3. export tasks to a word processor document where I can format and extend the project's outline into a technical proposition suitable to be presented to a Customer
4. export tasks to Trello to manage and track the project while I'm working on it.

### Economics
In OmniOutliner I can add a "duration" column to express the estimated effort in terms of work hours, like "4 hours", "5 days" and so on.

I needed to convert such duration to an FTE value: "5 days" means to me 40 work-hours (5 days of 8-hours working days). 
And I needed to make calculations on my estimates, I needed to put them in a spreadsheet.

40 work hours then becomes x euros for my Customer, based on selling price. E.g. if cost to Customer is 10 euros per hour, 40 hours means 400 euros. That simple. Hopefully we all charge something more than that ;)

### Presentation
OmniOutliner can export to a variety of formats, but only the Pro version recently added the capability to export Word documents. 
I wanted to export my outlines into something simple and effective, and choose [Markdown](https://en.wikipedia.org/wiki/Markdown). But OmniOutliner cannot export Markdown.

### Project management & tracking
I love [Trello](https://trello.com). I won't explain what it is here, if you don't know it... just go try it, it's free!
Being able to automatically export a task list to Trello was mandatory for me. Once my tasks are in Trello I can track working time with tools like [Plus for Trello](https://www.plusfortrello.com/p/about.html), an excellent Chrome extension (mobile apps are coming too) or [Toggl](https://www.toggl.com).

## Tools
**Recap**: I use OmniOutliner to begin my project, a spreadhseet like Numbers or Ecel to do calcs, a word processor like Pages or Word to write documents, and Trello to work on the project.

I was missing something to let my tools "communicate", I needed a way to bring my outlines from the former to the others. No, copy&paste was not an option, althought I actually do copy from Omnioutliner and paste into Omnifocus, since I don't have the pro versions of both (Omnifocus Pro has interesting scripting capabilities).

So I decided to build myself the missing tool I needed. Luckily, OmniOutliner can export to [OPML](https://en.wikipedia.org/wiki/OPML), an XML format for outlines: I just had to write some simple code to read that XML and transform it to something useful, like CSV for economic, Markdown for presentation and to easily export to Trello.

## OpmlParser
So I started writing a simple node.js script to do that. My OpmlParser script does:

- read an OPML file (exported from OmniOutliner)
- extract the project outline
- read estimated work time for each task
- produce a simple CSV file with task name and estimate 
- produce an MD file with all text
- allow me to automatically publish my tasks onto a Trello board

It's a very raw script, but it does the trick. Here's how does it work.

### 1. Outline
A sample outline looks like this in OmniOutliner: a column named "EH", of type "Duration", MUST be present to get estimates.

![ProjectOutline.png]({{ site.baseurl }}/images/ProjectOutline.png)

### 2. OPML
Once exported to OPML, the outline looks like:

![ProjectOutline.opml.png]({{ site.baseurl }}/images/ProjectOutline.opml.png)

### 3. OpmlParser: build md and csv
It's now time to launch the script to build our output files.
If you launch it without arguments it tells you what commands are available:

	 OpmlParser ./oop.js 
	Unknown command
	USAGE: ./oop.js cmd args
	COMMANDS: outline, trello, setupdb, json

So let's build our output files, starting from the OPML file exported at step 2:

	 OpmlParser ./oop.js outline ./ProjectOutline.opml
	Outline to csv and markdown
	OpmlToCsvAndMd ./ProjectOutline.opml
	TOPIC: Project Name
	Saved file ./ProjectOutline.opml.md
	Saved file ./ProjectOutline.opml.csv
	Done.

The two files look like this:

![ProjectOutline.opml.md.png]({{ site.baseurl }}/images/ProjectOutline.opml.md.png)

![ProjectOutline.opml.csv.png]({{ site.baseurl }}/images/ProjectOutline.opml.csv.png)

Note that the last column in the csv is the parsed estimate, that is the duration converted to working hours (8 per day, 40 per week). What I need to make calcs.

Also note that the csv uses a semicolon (;) as column separator: that's because in Italy we normally use this, just change the separator to whatever character you want by modifyng the OpmlToCsvAndMd() function in source.

### 4. OpmlParser: export to Trello
In order to export the outline to a Trello board we have to perform two steps: first get access to Trello APIs, and then reuse our opml to put data in a Trello board of choice.

You must first compile the script configuration file **config.js** by putting in your Trello application key and token.

See [https://trello.com/docs/gettingstarted/](https://trello.com/docs/gettingstarted/) to understand how to get yours, then put them in config.json into **key** and **token** respectively.
In the same file you then have to fill:

- **idList**, the id of the list into which to create cards (one card for each task will be created)
- **idLabel**, optional id of label(s) you want to associate to your new cards, or null if you don't want any.

Then we can publish to a Trello board:

	 OpmlParser ./oop.js trello ./ProjectOutline.opml
	Setup Trello board
	SetupTrelloBoard ./ProjectOutline.opml
	TOPIC: Project Name
	NEW CARD: {"name":"Task 1 (0/4)","desc":"First task desription","due":null,"idList":"5093ab9b31a9186173004580","idLabels":null,"urlSource":null}
	NEW CARD: {"name":"Task 2 (0/8)","desc":"Another task in project","due":null,"idList":"5093ab9b31a9186173004580","idLabels":null,"urlSource":null}
	Done.
	CARD created: {"id":"558d113cf683ba464a08ad96","badges":{"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"comments":0,"attachments":0,"description":true,"due":null},"checkItemStates":[],"closed":false,"dateLastActivity":"2015-06-26T08:45:48.238Z","desc":"First task desription","descData":{"emoji":{}},"due":null,"email":"trapias+508fe2f791808fea59005084+558d113cf683ba464a08ad96+3a3b473a0275a066c9e2d5b878d9ee208b990a3d@boards.trello.com","idBoard":"5093ab9b31a918617300457f","idChecklists":[],"idLabels":[],"idList":"5093ab9b31a9186173004580","idMembers":[],"idShort":85,"idAttachmentCover":null,"manualCoverAttachment":false,"labels":[],"name":"Task 1 (0/4)","pos":81919,"shortUrl":"https://trello.com/c/gq5VbG6X","url":"https://trello.com/c/gq5VbG6X/85-task-1-0-4","stickers":[]}
	CARD created: {"id":"558d113cd46983ffcc207362","badges":{"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"comments":0,"attachments":0,"description":true,"due":null},"checkItemStates":[],"closed":false,"dateLastActivity":"2015-06-26T08:45:48.253Z","desc":"Another task in project","descData":{"emoji":{}},"due":null,"email":"trapias+508fe2f791808fea59005084+558d113cd46983ffcc207362+8f09a132fcf99ab8af7af44b14afcc567a2ea797@boards.trello.com","idBoard":"5093ab9b31a918617300457f","idChecklists":[],"idLabels":[],"idList":"5093ab9b31a9186173004580","idMembers":[],"idShort":86,"idAttachmentCover":null,"manualCoverAttachment":false,"labels":[],"name":"Task 2 (0/8)","pos":98303,"shortUrl":"https://trello.com/c/7gbh4fU2","url":"https://trello.com/c/7gbh4fU2/86-task-2-0-8","stickers":[]}

Estimate is added to the card title in the format (Spent/Estimate), which is the original format Plus for Trello did use - you can easily remove that.

![ProjectOutline.opml.Trello.png]({{ site.baseurl }}/images/ProjectOutline.opml.Trello.png)

#### 5. OpmlParser: further improvements
Some ideas to extend OmniParser could be:

- export to a json file, which might be useful to sync with other apps (I have code ready for that, but it's not inclued in this release since it uses custom conventions to identify a project's and customer's identifiers - ask me if you're interested)
- export to a database: I also have partial code to export outlines (tasks and estimates) to a Postgres database, which might be used for a number of custom integrations (say a custom time tracking system)
- exporting with a Github repository
- exporting to OmniFocus (but Omnifocus Pro version would be required)
- dynamically handle columns
- manage multiple FTE columns, like minimum and maximum estimates
- export to xlsx, which would allow to introduce formulas and dynamic data
- export to html with custom formatting / templates.

#### 6. OpmlParser: download
You can download the script at Github from the dedicated [OpmlParser Repository](https://github.com/trapias/opmlparser).


## Credits
Partially inspired by [node-opmlparser](https://github.com/danmactough/node-opmlparser).
