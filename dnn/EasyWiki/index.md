---
layout: sidebar
categories: dnn
title: EasyWiki
subtitle: A simple wiki module for DNN
description: An extensible Wiki module for DotNetNuke built upon XsltDb.
---

<h1>{{page.title}}</h1>
<h2>{{ page.subtitle }}</h2>

EasyWiki is an extensible Wiki module for DotNetNuke built upon [XsltDb](http://xsltdb.codeplex.com/).
XsltDb is powerful XSLT module for DotnetNuke. It allows you to do much more than standard XML/XSL module with much less code. XsltDb offers safe database access, AJAX support, visitor interactions, environment integration (dnn properties, request, cookie, session and form values), regular expressions, etc.


## WikiCreole 1.0
EasyWiki adopts WikiCreole 1.0 markup, please visit [http://www.wikicreole.org](http://www.wikicreole.org) for details. EasyWiki then extends markup with Extensions, and also supports DNN-Token-Replace tokens.
Here under the cheat-sheet for WikiCreole 1.0 markup.

## DNN Integration Features
EasyWiki is naturally integrated in DotNetNuke, since it is a DNN module.

### DNN Module
As with any other DNN module you'll configure module through **module settings**, you will add EasyWiki module instances to pages and be able to assign **view and edit permissions** (on the whole module instance, that is not at page level, at the moment).

### Token-Replace
EasyWiki markup engine also supports DNN tokens. That is you can include DNN tokens within markup, for example:

<blockquote><span>Hello world, it is now [date:now]</span></blockquote>

will be rendered as:

<blockquote class="style2"><span>Hello world, it is now 21/11/2014 04.48</span></blockquote>

### Search-Engine
EasyWiki implements ISearchable, that is all EasyWiki pages are automatically indexed by DNN's built-in searchengine, and searchable through the standard search functions.

## Store in DNN
The first release of EasyWiki adopts an easy storage mechanism: one file for each page. Every page is saved to an XML file in module's storage folder (which you choose in module settings). 

### Sample page XML
An EasyWiki page is stored as XML with the format:

	<easywiki>
	<page title="Page Title" name="PageName">
	<content> WIKI MARKUP HERE </content>
	</page>
	</easywiki>

## markItUp! Editor
[markItUp](http://markitup.jaysalvat.com/) is a powerful, lightweight, customizable and flexible editor engine. markItUp is the only EasyWiki editor: there's no WYSIWYG editor, but several keystrokes and plugins are used. 

![markItUp]({{ site.baseurl }}/images/markitupeditor.png)


## Extensions
EasyWiki Extensions allow you to extend EasyWiki markup syntax with custom tags, that are automatically and dynamically associated with implementation sources in the form of XSLT resource files. 

In other words: each extension is represented by a macro (a custom tag) and implemented in a correspoding EasyWiki plugin, where plugins consist of XSLT files. EasyWiki plugins support XsltDb mdo extensions in main xslt template only. 

### Placeholder
Extensions have a special markup tag: three angle less-than signs followed by the extension name, a blank and optional extension parameters followed by three greater-than signs.

<blockquote><span>
<pre>&lt;&lt;&lt;extension param1="value" ... paramN="value"&gt;&gt;&gt;
</pre>
</span></blockquote>

### Special Extensions
Special extensions are built-in extensions, that is extensions whose code is nested within EasyWiki - there's no external xslt file.

**Extension** |  **Description** |  **Syntax**
---------------|------------------|---------------|
include | Includes another page in current one | ``` <<<include page="IncludedPage">>> ```
layout	| allows to use another page as the layout frame for impaginating current page; layout page must include the special tag $page$ to be replaced with current page content |	``` <<<layout page="LayoutPage">>> ```


### XSLT Extensions
EasyWiki extensions consist of XSLT files you can publish at two different levels:
- shared, module-level, extensions are placed under EasyWiki module folder and shared between all EasyWiki instances
- local, wiki-level, extensions are placed under the specific wiki root folder and are only valid for that specific wiki.

Local extensions have priority, that is if a local extension exists with the same name of a shared extensions, the local one will be used.

**Extension** |  **Description** |  **Syntax**
---------------|------------------|---------------|
sql2table	| Executes an SQL query showing results as a wiki table |  ``` <<<sql2table select="">>> ```
sql2htmltable |	Executes an SQL query showing results as an Html table	|  ``` <<<sql2htmltable select="">>> ```
sql2radgrid |	Executes an SQL query showing results within a Telerik RadGrid | ```	<<<sql2radgrid select="[SQL]" skin="[SKIN]" filter="[true|false]">>> ```
swfobject |	Embeds a video with SWFObject and JWPlayer	| ``` <<<swfobjectid="video1" url="url-to-video" autostart="false">>> ```
embed |	Embeds a video with JWPlayer | ```	<<<embed id="video1" url="url-to-video" autostart="false">>> ```
file |	Inserts a link to the specified file, with an icon depending on file type |	 ``` <<<file url="/files/pippo.pdf" title="Pippo!">>> ```
filelist |	Inserts a list of files from the specified portal folder.  | ```	<<<filelist folder="[FOLDER]" mode="[table|ul]">>> ```
bq |	Generates blockquote styled element	 | ``` <<<bq text="content of blockquote" class="style1">>> ```
toc |	Generates Topic Of Contents |	``` <<<toc level="n">>> ```
allpages |	Generates index of all pages in Wiki |	``` <<<allpages mode="listmenu">>> ```
code |	Adds SyntaxHighlighter to page |	``` <<<code lang="all">>> ```
page2pdf |	Convert page to PDF |	``` <<<page2pdf>>> ```
xmenu |	Embed a DDRMenu in a wiki page | ```	<<<xmenu ProviderName="[ProviderName]" MenuStyle="[MenuStyle]" NodeSelector="[NodeSelector]" IncludeNodes="[IncludeNodes]" ExcludeNodes="[ExcludeNodes]">>> ```
thumbs |	Embed a simple image gallery in a wiki page | ```	<<<thumbs folder="[FOLDER]">>> ```

## Custom Layouts
EasyWiki allows you to use any page as the layout for another page: just include a tag in the layout page, and specify the wanted layout in your page.

### Layout extension
The layout extension (a core extension) allows you to declare the layout you want to load for your page. In order to activate a layout, you MUST include a layout extension declaration referencing the wanted layout page. That is write:

```
<<<layout page="MyLayout">>>
```

### Layout pages
The above declaration is a reference to a page called "MyLayout", that must exist in your wiki. Such page is a normal wiki page, except it - in order to become a Layout Page - MUST contain the special tag 

![$page$]({{ site.baseurl }}/images/easiwiki_pages.png)

which acts as the placeholder for your page content. That is:
- the layout page dictates the structure of the published page
- the placeholder will be substituted with your wiki page content.


## Download / Fork
Download or Fork this project at Github [https://github.com/trapias/EasyWiki](https://github.com/trapias/EasyWiki).

## Comments
{% include disqus.html disqus_identifier=page.disqus_identifier %}
