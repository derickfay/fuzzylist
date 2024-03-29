# fuzzylist
Fuzzy, self-updating list filter workflow for Alfred 4

v.  0.3 (2022-03-30) now uses Python 3 and runs on MacOS 12.3

This is a workflow template - it does nothing as is.  It includes sample data and icons which you'll want to replace.

## Usage:
- create a csv file like you would for an [Alfred List Filter](https://www.alfredapp.com/help/workflows/inputs/list-filter/), with an optional fourth field containing the path to an icon file for that result.
- name the file *list.csv* and add it to the workflow directory

On the initial run, the workflow will create a file list.json for output to the fuzzy search.  If list.csv is modified, it will update list.json .  

You can also create multiple instances by changing the file name from list.csv in a copy of the Script Filter object.

More details can be found in the [Alfred forum post](https://www.alfredforum.com/topic/11094-fuzzy-self-updating-list-filter-workflow-template/?tab=comments#comment-57706)

## Credits
- uses [fuzzy.py by Dean Jackson](https://github.com/deanishe/alfred-fuzzy)

