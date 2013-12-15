import praw
import Skype4Py

r = praw.Reddit(user_agent='Find_Top_Post');
submissions = r.get_subreddit('all').get_hot(limit=1);
top = [str(x) for x in submissions];
top = top[0];
top = top[8:];
print "Current top post: " + top;

skype = Skype4Py.Skype();

skype.Attach();

skype.SendMessage("YOUR SKYPE CONTACT HERE", top);
