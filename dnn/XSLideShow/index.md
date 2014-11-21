---
layout: sidebar
categories: dnn
title: XSLideShow
subtitle: A free DotNetNuke slideshow module
description: A free DotNetNuke module to publish photo-galleries / slideshows. 
---

<h1>{{page.title}}</h1>
<h2>{{ page.subtitle }}</h2>

XSLideShow is a free DotNetNuke module to publish photo-galleries / slideshows. 
XSLideShow is built with [XsltDb](http://xsltdb.codeplex.com/), a great DotNetNuke module that uses XSLT transformations to build dynamic and feature-rich DNN modules very quickly. 

<div class="addthis_native_toolbox"></div>

## Intro
**XSLideShow is an old project and is no more actively maintained**, it was an experiment to build a slideshow module on top of XsltDb: module logic is all in the XSLT, there are no external dependencies apart the assets needed to build the different views. 

There is no live demo anymore. This page just references the project, so that if you're interested you can get the code and play with it.

## Visualization Plugins
XSLideShow has several visualization plugins, most of which based on freely avaiable jQuery plugins and a couple using Flash. See Credits to find details for each.  

 **Plugin** |  **Credits** |  **Description**
--------|----------|----------------------|
thumbnails + Lightbox | [Lightbox](http://leandrovieira.com/projects/jquery/lightbox/)  | This plugin builds a classic view with thumbnails of images, clicking on which you can see the full photos inside Lightbox.
thumbnails + FancyBox | [Fancybox](http://fancybox.net/)  | This plugin builds a classic view with thumbnails of images, clicking on which you can see the full photos inside FancyBox.  
Galleria Classic Theme | [Galleria](http://galleria.aino.se/) | This plugin builds a nice framed album with thumbnails 
thumbnails + Lightbox + fullscreen slideshow with JBGallery | [Lightbox](http://leandrovieira.com/projects/jquery/lightbox/) + [JBGallery](http://maxb.net/scripts/jbgallery-2.0/) | This plugin adds a fullscreen visualization, based on JBGallery, to a classic thumbnails view
thumbnails + FancyBox + slideshow with JBGallery |  [Fancybox](http://fancybox.net/) + [JBGallery](http://maxb.net/scripts/jbgallery-2.0/) | This plugin adds a fullscreen visualization, based on JBGallery, to a classic thumbnails view. 
ShineTime | [ShineTime](http://addyosmani.com/blog/shinetime/) | A nice plugin
jQuery Cycle plugin | [Malsup jQuery Cycle](http://malsup.com/jquery/cycle/) | A single frame slideshow with several transition effects 
LongTail JW Player (flash player) | [JW Player](http://www.longtailvideo.com/players/jw-player/) | A slideshow built with the great JW Player 
LongTail JW Image Rotator | [Image Rotator](http://www.longtailvideo.com/players/jw-image-rotator/) | A flash gallery, real full screen with transition effects
SlidesJS | [SlidesJS](http://slidesjs.com/) | A nice sliding panel with effects
Supersized | [Supersized](http://www.buildinternet.com/project/supersized/) | A fullscreen gallery
ContentFlow | [ContentFlow](http://www.jacksasylum.eu/ContentFlow/) | A configurable gallery with multiple view modes
prettyPhoto | [prettyPhoto](http://www.no-margin-for-errors.com/projects/prettyphoto-jquery-lightbox-clone/)  |prettyPhoto is a nice lightbox clone.

## Media Sources
Images may come from different media sources:

<ul class="uldisc">
<li>the RSS feed of a Picasa Web Album,</li>
<li>a DNN site folder,</li>
<li>a Twitpic user feed (from version 01.00.04),</li>
<li>a DNN site folder with automatic generation of high-quality png thumbnails</li>
<li>a local XML file in XSLideShow MediaSource format</li>
<li>a remote XML file in XSLideShow MediaSource format (allows to build dynamic galleries; new for version 01.00.08).</li>
</ul>

### XSLideShow XML format
XSLideShow can load album definitions from external resources (e.g. a local or remote, static or dynamically generated XML file). An album is defined like:

	<?xml version="1.0" encoding="utf-8" ?>
	<album>
	<media filename="d:\inetpub\wwwroot\albe.ihnet.it.dnn\Portals\0\Img\TestJP\20101014 K-Idea 01.jpg" extension="jpg" href="/Portals/0/Img/TestJP/20101014 K-Idea 01.jpg" width="" height="" title="Prima" description="Prima foto" medium="image" size="" timestamp="">
	</media>
	<media filename="d:\inetpub\wwwroot\albe.ihnet.it.dnn\Portals\0\Img\Arcobaleno\DSC_0120.jpg" extension="jpg" href="/Portals/0/Img/Arcobaleno/DSC_0120.jpg" width="" height="" title="Arcobaleno 1" description="Arcobaleno al balcone 1" medium="image" size="" timestamp="">
	</media>
	<media filename="d:\inetpub\wwwroot\albe.ihnet.it.dnn\Portals\0\Img\Arcobaleno\DSC_0134.jpg" extension="jpg" href="/Portals/0/Img/Arcobaleno/DSC_0134.jpg" width="" height="" title="Arcobaleno 2" description="Arcobaleno al balcone 2" medium="image" size="" timestamp="">
	</media>
	<media filename="http://lh3.ggpht.com/_R4m4nm04fxg/SNGXUnxDguI/AAAAAAAABwQ/C1cCIWhMUnY/s720/Img0322.jpg" extension="jpg" href="http://lh3.ggpht.com/_R4m4nm04fxg/SNGXUnxDguI/AAAAAAAABwQ/C1cCIWhMUnY/s720/Img0322.jpg" width="" height="" title="Img0322" description="Img0322" medium="image" size="" timestamp="">
	</media>
	<media filename="http://lh4.ggpht.com/_R4m4nm04fxg/SNGXXniEXSI/AAAAAAAABw8/NHPxzXlObRc/s720/Img0870.jpg" extension="jpg" href="http://lh4.ggpht.com/_R4m4nm04fxg/SNGXXniEXSI/AAAAAAAABw8/NHPxzXlObRc/s720/Img0870.jpg" width="" height="" title="Img0870" description="Img0870" medium="image" size="" timestamp="">
	</media>
	<media filename="http://lh3.ggpht.com/_R4m4nm04fxg/TAwYbWitt5I/AAAAAAAASyE/RWFh5BF4P20/DSC_1046.JPG" extension="jpg" href="http://lh3.ggpht.com/_R4m4nm04fxg/TAwYbWitt5I/AAAAAAAASyE/RWFh5BF4P20/DSC_1046.JPG" width="" height="" title="Ale&amp;Andrea" description="Ale&amp;Andrea" medium="image" size="" timestamp="">
	</media>
	<media filename="http://lh5.ggpht.com/_R4m4nm04fxg/SQJvzRfdaEI/AAAAAAAABtc/CKQz1qLSocE/113_1359.JPG" extension="jpg" href="http://lh5.ggpht.com/_R4m4nm04fxg/SQJvzRfdaEI/AAAAAAAABtc/CKQz1qLSocE/113_1359.JPG" width="" height="" title="Ale&amp;Andrea" description="Ale&amp;Andrea" medium="image" size="" timestamp="">
	</media>
	</album>


## Installation
Since version 01.00.10 XSLideShow is packaged as a normal DNN module, and can thus be installed like any other module.

### Prerequisites
XSLideShow depends on XsltDb: you have to install XsltDb first. Get it at [Codeplex](http://xsltdb.codeplex.com/) and install as with any DNN module. 
XSLideShow 01.00.10 has been tested with XsltDb 02.00.75 (latest currently available).

### Manual Installation
Previous versions needed a manual install procedure which is no more necessary. Also note there are no conflicts between the old and the new, packaged, version, since server-side code is now integrated in the module source code.

After downloading the module, extract the contents of the zip file (zip contains both the xsl script and jQuery plugins). Install jQuery plugins under /Portals/_default/js of your DotNetNuke host, or choose a location you prefer by adjusting the paths in xsl file. Copy the files XSLideShow.cs and Trapias.cs in /App_Code/XsltDb.
Then create a new XsltDb instance on a page, click on "edit XSLT" and paste the contents of the xsl file in the editor. Save and publish.
Then click on the Edit Configuration button, or go to module settings, and proceed with configuration.

If you wish to install on a DNN host with virtual root (e.g. http://localhost/dotnetnuke), you have to modify the function HTTPAlias() in trapias.cs. Modify it to:


	public string HTTPAlias()
	{
	       string protocol = "http://";
	 
	       if(HttpContext.Current.Request.IsSecureConnection)
	              protocol = "https://";
	 
	       string url = protocol + HttpContext.Current.Request.Url.Host; // + HttpContext.Current.Request.ApplicationPath;
	       if (url.EndsWith("/"))
	              return url.Substring(0, url.Length - 1);
	       else
	              return url;
	}


That is comment out ApplicationPath. This is due to a previous XsltDb bug, solved since release 2.0.33, with virtual folders (ApplicationPath was added to get around the bug, and is no more necessary). The fix will be included in next release.

## Configuration
XSLideShow can be configured like any other DNN module, by choosing the "Settings" module action. Go to "XsltDb Settings" to find XSLideShow configuration values. 

First of all you have to choose a media source, that is the source of your images: they may come from a Picasa web album, a local folder, a Twitpic account or an XML file (local or remote).Depending on the media source you select, you have to provide specific configuration. 

Then you must configure the aspect of your slideshow: choose a Visualization Plugin and set its options as per your needs. 

Finally save module configuration, and enjoy your new slideshow! 

## Fork
Fork this project at Github [https://github.com/trapias/XSLideShow](https://github.com/trapias/XSLideShow).

## Comments
{% include disqus.html disqus_identifier=page.disqus_identifier %}
