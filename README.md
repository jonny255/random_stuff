# random_stuff
Pretty random files in here... Really is for me to get more familiar with and learn CI/CD techniques and git in general. I did make it public in case anyone somehow stumbles upon this repo and is lucky enough to win the lottery but instead wasted that luck on finding the source code/solution they've been searching for.






You can prune more aggressively, discarding some safeties, by using git gc --prune=now, or the low-level git prune. But take care that you don't remove safeties and backups (like reflog) that you need one minute after compacting.


Perhaps what enlarges your repository are some untracked files in the working directory. There "make clean" or "git clean" might help (but take care that you don't remove some important files).

Most safe of all those suggestions: you can try to pack more aggressively, using --depth and --window option of low-level git-repack. See also Git Repack Parameters blog post by Pieter de Bie on his DVCS Comparison blog, from June 6, 2008. Or "git gc --aggressive".

as an addendum to point 2, the Git BFG Repo Cleaner is a much faster alternative to git filter-branch.


25

Depending on what you want to do with your repository, you might also consider using the following git clone option:

   --depth <depth>
       Create a shallow clone with a history truncated to the specified
       number of revisions. A shallow repository has a number of
       limitations (you cannot clone or fetch from it, nor push from nor
       into it), but is adequate if you are only interested in the recent
       history of a large project with a long history, and would want to
       send in fixes as patches.







it clone now has a --single-branch option that allows you to check out a single branch without pulling in the Git history of the other branches. If Git is consuming a lot of disk space, because you have a lot of branches, you can delete your current checkout and reclone the repository using this option to regain some disk space. For example:

cd ../
rm -rf ./project
git clone -b master --single-branch git@github.com:username/project.git
Also, if your current master has a long history and you don't have any outstanding branches that need to be merged back into master, you can create an archive branch off of master and create a new orphan master without any Git history:

git checkout -b master_archive_07162013  # Create and switch to the archive branch
git push origin master_archive_07162013  # Push the archive branch to the remote and track it
git branch -D master                     # Delete local master
git push --delete origin master          # Delete remote master
git remote prune origin                  # Delete the remote tracking branch
git checkout --orphan master             # Create a new master branch with no history
git commit -m "initial commit"           # Re-establish the files in the repository
git push origin master                   # Push the new master to the remote
The new master branch's tree will not be related to the old archived master branch, so only do this when you are truly archiving the branch.

If you archive your master branch and then git clone master with single-branch, your checkout should be a lot smaller.






7

If you do not need to keep all of the commit history locally, you could use a shallow clone:

git clone --depth=1 [url_of_repo]
I frequently use this when cloning GitHub projects, if I am only interested in the latest set of files and not in the history.

I think it is easier to start with a fresh clone as shown above, but others have shown how to trim an existing local repo.

Concerns: Apparently fetching and pushing is/was not support on shallow clones, but I have been able to successfully push and pull changes to GitHub repositories with it, so it might work in your case too. (But no doubt you will run into difficulties if you want to merge branches but don't have the base commit in history.)

You can always get the entire history later, by using:

git fetch --unshallow


Git gc will remove unused objects. That is about everything you can do.

You could consider splitting up your repositories if they become too big.


You can repack your repository. However, I think it's called by git gc

git repack -ad


2

git prune might be a hint. It cleans the repository from unreachable commits (git gc does not call it).


From the git-prune manpage: "In most cases, users should run git-gc, which calls git-prune."



well, for me my git repositories get smaller by a few mb when calling git prune after git gc (measured with du -sh .git). maybe git gc only prunes older commits, and git prune prunes every object which is not reachable

IIRC git gc offers some extra security (not deleting some objects) that git prune lacks.

Before 'git prune' ~900 Mb. After 'git prune' ~150 Mb.




Worth once after cloning if the savings really matter:

git repack -adf --depth 100 --window 500 --window-memory 1G
For instance, that'll repack the linux history down to 2.1G. The -f flag in particular is a one-shot deal for when you really really care, you do that only when it's actually worth the time it'll take to lop another 10% off the repo size, and it only works once on any clone, for reruns just set up your config so the auto-gcs look wider and deeper for opportunities.

but be warned: these are chosen to take something like an hour to run on a modern half-decent midrange, do not try this on a cheap ec/linode, it'll take for-frikken-ever. For those, do the repack on a beefier rig and just scp the repo instead of cloning.



You might have a lot of git projects cloned on your computer, but only a few of them you are actively working on today.

In those idle projects, the checked out working files can consume a significant amount of disk space. (Sometimes even larger than git's history, because history gets compressed.)

So one way to save disk space is to remove the working files from idle projects you are not working on. A nice way to do that is to create an empty branch which you can switch to when you are not working on the project.

Another more drastic thing you can do is to delete absolutely everything except for the .git/config file. That file contains the repostory's URL, which you can use to git clone the project again in future.

Before doing this, you should ensure that you have committed and pushed all your work (including other local branches) to the remote repository, if you don't want to lose it.


https://gitbetter.substack.com/p/how-to-clean-up-the-git-repo-and
How to clean up the git repo and reduce its disk size
Clean large git repo and reduce repo size


If you are working in a Git repo for a very long time then you can cleanup your repo to gain disk space.

Git has an internal garbage collection tool that takes care of most of the things but there are few things that we can also do to clean up the repo.

Let’s see some techniques to clean up the repo.

Before applying these techniques to git, make sure you get the size of the .git directory using

du -sh .git
Deleting local reference of the remote branch
It’s always a good practice to delete a branch after it is merged. Github provides an option to delete the branch once you merged the PR. But this one will delete that branch only in the remote.

Even after the branch is deleted in the remote, it will still have the reference in the local.

To delete all the local references of the remote branch

git remote prune origin
git repack
Packs are Git internal representations that used to combine all individual objects into packs.

Without going much deeper, Packs are used to reduce the load on disk spaces, mirror systems, etc.

git repack
This will create new packs that are not packed yet in the repo. This helps in reducing disk sizes.

git prune-packed
Git will have some pack files. This command will help you to reduce extra objects that are already present in the pack files. This will help you to reduce the size of the pack file itself.

git prune-packed
git reflog expire
Git has a feature called reflog that helps to track Git refs in the local repo. Git has an internal garbage collection mechanism to remove old refs in Git. But there is also a manual mechanism to remove old refs.

git reflog expire --expire=1.month.ago
The above command will remove all refs that are older than one month. I think one month is safer. But if you can mention whatever value you feel safe.

git gc
gc stands for garbage collection. This command will help Git to remove unwanted data in the current repo.

git gc --aggressive
The above command will remove all refs and inaccessible commits in the repo which are older than two weeks. —aggressive will help more time optimizing it.

Combining all command
git remote prune origin && git repack && git prune-packed && git reflog expire --expire=1.month.ago && git gc --aggressive
We have combined all the commands. You can have it as an alias and run it weekly once to have a clean repo.

And don’t forget to see the .git directory size after cleaning up your repo.

Running it across all the repos in your machine will definitely help you reduce some disk space.
















































