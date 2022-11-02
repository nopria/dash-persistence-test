# Dash `pages` multi-page app demos

This repo contains minimal examples of multi-page apps using the `pages` feature available in dash>=2.5.1

__See the :new: Dash Documentation [Multi-Page Apps and URL Support](https://dash.plotly.com/urls)__  

__:movie_camera: Don't miss the video tutorials:__
 - [Introducing Dash `pages` --  A better way to make multi-page apps`](https://youtu.be/pJMZ0r84Rqs) by Adam Schroeder and Chris Parmer.  
 - Charming Data Videos by Adam Schroeder:
      - [Creating Multi Page Apps - Part I ](https://youtu.be/Hc9_-ncr4nU) Getting Started
      - [Creating Multi Page Apps - Part II](https://www.youtube.com/watch?v=MtSgh6FOL7I) Sidebar and Layout Enhancements


This feature was developed in dash-labs.  For background, see the thread on the [Dash Community Forum.](https://community.plotly.com/t/introducing-dash-pages-a-dash-2-x-feature-preview/57775/)
If you have a multi-page app using the `pages` plugin from dash-labs, see the post on [how to migrate to dash>=2.5.1.](https://community.plotly.com/t/introducing-dash-pages-a-dash-2-x-feature-preview/57775/132?u=annmariew) 


__Example Apps__

The examples are listed by their folder name.

 13. [multi_page_sync_components/](#13-multi_page_sync_components) - syncs components between pages using [MultiplexerTransform from dash-extensions](https://www.dash-extensions.com/pages/transforms/multiplexer-transform) to update a dcc.Store from multiple callbacks.


__Other tutorials or examples using `pages`:__  


1. Adding a Blog to your Dash app.  See  this [Dash Community Forum post](https://community.plotly.com/t/adding-a-blog-to-your-dash-app/65955). It describes how to do this and includes [this repo](https://github.com/bradley-erickson/dash-blog-page) from @bradley-erickson. 

2. See the [Dash Webb Compare](https://dash-webb-compare.herokuapp.com/ ) app live.  This app shows the first images from the James Webb Space Telescope. Compare before and after images of Hubble vs Webb. The Github repo has 2 versions of the app using `pages`.  
    - [app_pages.py](https://github.com/AnnMarieW/webb-compare/blob/master/app_pages.py) - Creates an multi-page app without using the `pages` folder.
    - [app_pages_no_assets.py](https://github.com/AnnMarieW/webb-compare/blob/master/app_pages_no_assets.py) - This multi-page app uses images that are hosted on GitHub so it doesn't use either the `pages` or the `assets` folder.  
   
__Tips and Tricks__
1. [Pretty print dash.page_registry](#1-print_registry-from-dash-labs-110) - with the `print_registry()` function from dash-labs
2. [How to use dcc.Link in Markdown](#2-tada-use-dcclink-in-dccmarkdown)  - for high performance page navigation from a link in a dcc.Markdown component.
3. [Avoiding duplicate ids](#3-avoiding-duplicate-ids) - Strategies for handling ids in a large multi-page app.
--------
---------

# Example Apps


## 13. [multi_page_sync_components/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_sync_components)

This example shows how to synchronize component values between pages. It uses [MultiplexerTransform from the dash-extensions](https://www.dash-extensions.com/pages/transforms/multiplexer-transform) library to update a `dcc.Store` component from multiple callbacks.

![sync](https://user-images.githubusercontent.com/72614349/175389756-bf064f6d-edd1-4107-9764-1373c260451f.gif)
---
