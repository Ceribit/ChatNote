# Purpose
This is a self-done project to practice creating a website with common features found in both blogs and many social media sites. All features included were made from scratch


# Implemented features:
1) Login/Registration
2) Settings page to update personal info
3) Notes with a manytomany link with tags
  a) Notes displayed with cards and can be added in the home screen
4) Basic search bar (Enter user and it brings you to their profile page)
5) Added basic friend functionality (add/remove friends)
6) Added a simple private messaging system

## Afterthoughts (Of making this)
As I've gone through the process of building this, I've discovered aspects that I wished I had programmed differently. Such prospects include:
- Using a class-based view
- Dividing the project amongst many other apps, some of which could've been built independent from another to make the project much simpler
- Kept a consistent naming convention (I've mostly kept this except for one variable I never took the time to rename)
- Having the program kept clean from the start so I wouldn't have to clean it afterwards
I still plan to update this small experiment in the future, but for a more different learning experience, I may create a different website altogether in a new repository

# Upcoming updates
1) Add friend groups
2) Improve search bar to redirect to a search page if the user doesn't exist
3) Add ability to change account info and make password verification required to change info
4) Improve the messaging system html/javascript to allow the user to scroll through messages

# Issues:
* Clean up the code
* Adding tags in the notes-page requires me to relabel the tags
in the query set before putting them in the context. If not done,
the html shows "Queryset <tag1, tag2>" instead of just tag1, tag2.
* Fix up the code for managing friend requests. It works for now, but looks
unorganized and may complicate up things later on
* Improve the html
