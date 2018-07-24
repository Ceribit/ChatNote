# Purpose 
This is a self-done project to practice creating a website with common features found in both blogs and many social media sites.


# Upcoming updates
1) Add friend groups
2) Improve search bar to redirect to a search page if the user doesn't exist
3) Add ability to change account info and make password verification required
   to change info
4) Add a messaging system and a tag system


# Issues:
0) Clean up the code
1) Adding tags in the notes-page requires me to relabel the tags
in the query set before putting them in the context. If not done,
the html shows "Queryset <tag1, tag2>" instead of just tag1, tag2.
2) Fix up the code for managing friend requests. It works for now, but looks
unorganized and may complicate up things later on
3) One day, I may plan to rework this project with class-based views


# Implemented features:
1) Login/Registration
2) Settings page to update personal info
3) Notes with a manytomany link with tags
  a) Notes displayed with cards and can be added in the home screen
4) Basic search bar (Enter user and it brings you to their profile page)
5) Added basic friend functionality (add/remove friends)

# Completed Updates:
x) Existence of friends
x) Functionality of sending a friend request and accepting it
x) Move the notes page to its own path (change '/' path to '/notes')
  a) Notes will have an extension (eg. '/notes/edit') to edit and delete
  notes
  b) You can now edit notes
