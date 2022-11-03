# Dash `pages`, demo of common input component spanning more pages

The first example [multi_page_sync_components](https://github.com/nopria/dash-persistence-test/tree/main/multi_page_sync_components) shows how to synchronize component values between pages. This example is an alternative way of synchronizing an input parameter common to many pages, obtained through persistence instead of `dcc.Store` as in https://github.com/AnnMarieW/dash-multi-page-app-demos#13-multi_page_sync_components

The second example [page_sync_with_query_strings](https://github.com/nopria/dash-persistence-test/tree/main/page_sync_with_query_strings) adds query string capabilities to the first; if you add `?year=2100` to the URL of page 1, 2 or 3, you will see the year parameter being set accordingly.

Unfortunately it seems that there is a bug in persistence management, in fact persistence works fine as in first example until you don't use query strings; but after you apply a query string, as soon as you change page (and only the first time you change page after applying a query string) **persistence is not able to keep the manually set value** and initial value comes back, even if it should come back only on page refresh (persistence is of memory type).
