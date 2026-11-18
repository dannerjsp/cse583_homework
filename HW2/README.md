# HW2
A description of my work process for HW2: Learn Git Branching

## Introduction Sequence
### Introduction to Git Commits


### Branching in Git


### Merging in Git 



### Rebase Introduction - This was frustrating.
1. `git switch -c bugFix` : names C1 bugFix
2. `git commit` : makes C2 as bugFix
3. `git checkout main` : took head back to main. Tried git C1, which was wrong. C1 is not the same as main.
4. `git commit` : makes C3
5. `git checkout bugFix` : moved to C2
6. `git rebase main` : moved C2 bugFix to the end of C3 as C2' bugFix





## Ramping Up Sequence
### Detach yo' HEAD
1. `git switch --detach C1` : detached the head from C4 and attached it to C1. Not what I needed. 
2. `undo` : had to undo that because I messed that up
3. `git switch --detach C4` : detached the head from bugFix and attached it to C4? That was the solution. 

### Relative Refs (^)
Notes: Relative commits are powerful, but we will introduce two simple ones here:
* Moving upwards one commit at a time with ^
* Moving upwards a number of times with ~<num>

1. `git switch --detach C4` : detached the head from bugFix and attached it to C4? That was the solution. 
2. `git checkout bugfix^` : moves from bugFix C4 up to it's parent (C3)

### Relative Refs #2 (~)
Notes:
* `git switch --detach HEAD~4` : detaches and moves the head up to C0 from C4
* `git branch -f main HEAD~3` : forcefully reassigns the main branch to the three parents behind HEAD. 

To complete this level, move HEAD, main, and bugFix to their goal destinations shown.
1. `git switch --detach HEAD^` : detached the head and moved it to C1
2. `git branch -f main C6` : forecrully moved main branch from C4 to C6
3. `git branch -f bugFix HEAD^` : forcefully moved bugFix from C5 to the parent of Head (C1), which is C0 

### Reversing Changes in Git
Notes:
* `git reset HEAD~1` : reverses changes by moving a branch reference backwards in time to an older commit. Moves a branch backwards as if the commit had never been made in the first place.
* `git revert HEAD^` : reverse changes and share those reversed changes with others. It took (C2) and copied it to (C3) as (C2').

To complete this level, reverse the most recent commit on both local and pushed. You will revert two commits total (one per branch). 
Keep in mind that pushed is a remote branch and local is a local branch -- that should help you choose your methods.
1. `git reset HEAD~1` : moved both main, local, and the head to (C1). Almost like (C3) never even happened.
2. `git checkout pushed` : moved the head to pushed(C1) 
3. `git revert HEAD^` : added  (C1') to (C2). Not what we wanted. 
4. `undo`
5. `git revert HEAD` : added (C2') to (C2)  




## Push & Pull -- Git Remotes! Sequence
### Clone Intro
To finish this level, simply git clone the remote repository we've set up for you. The real learning will come in following lessons.
1. `git clone` - cloned the repository onto local storage

### Remote Branches
Notes:
* `git switch --detach o/main; git commit` : looks like it detached head from (C1) and then committed.

To finish this level, commit once off of `main` and once after checking out `o/main`. This will help drive home how remote branches behave differently, and they only update to reflect the state of the remote.
1. `git commit` : made (C3) after (C1)
2. `git switch --detach o/main` : detached the head and moved it to (C1)
3. `git commit` : made a new branch with the head on (C4)

### Git Fetchin'
Notes:
* `git fetch` : fetch data from a remote repository in two steps
    1. downloads the commits that the remote has but are missing from our local repository
    2. updates where our remote branches point

To finish the level, simply git fetch and download all the commits!
1. `git fetch` : downloaded the latest commits

### Git Pullin'
Notes:
* `git cherry-pick 0/main` : 
* `git rebase o/main` or `git pull --rebase` : 
* `git merge o/main` or `git pull --no-rebase` : 

Remember -- you can actually solve this level with just fetch and merge, but it will cost you an extra command :P
1. `git pull` : downloaded from the repository and merged(?) the commits

### Facking Teamwork
Notes:
* `git fakeTeamwork foo 3` : simulated a teammate pushing three commits to the foo branch on our remote.

Go ahead and clone the remote repository, fake some changes on that remote, add a local commit, and then pull down the remote changes and merge them. It's like a few lessons in one!
1. `git clone` : cloned the repository locally
2. 'git fakeTeamwork' : made a commit (C2) and (C3) on the origin repository. I made two to see if that affects anything
3. `git commit` : Committed (C4) locally
4. `git pull` : made a branch off (C1) with the downloaded fake commits (C2) and (C3) and merged it with (C4) to make (C5).

### Git Pushin'
Notes:
* `git push` : upload  changes to a specified remote and updating that remote to incorporate your new commits

To finish this level, simply share two new commits with the remote. Strap in though, because these lessons are about to get a lot harder!
1. `git commit` : New commit (C2)
2. `git commit` : new commit (C3)
3. `git push` : published (C2) and (C3) to the repository

### Diverged History
Notes:
* `git fetch; git rebase o/main; git push` : Fetched the new commit (C2) from the remote repository. Rebased the local commit (C3) to the end of the remote commit (C2) as (C3'). Then uploaded those new local commits to the remote repository.
* `git fetch` : doesn't move your work (and instead just creates a merge commit), it's a way to tell git that you have incorporated all the changes from the remote.
* `git fetch; git merge o/main; git push` : updated our local repository with the remote commits, merged the new work into our work (to reflect the new changes in the remote), and then pushed them with git push.
* `git pull --rebase; git push` :
* `git pull; git push` : 

In order to solve this level, take the following steps:
1. `git clone` : Clone your repo
2. `git fakeTeamwork` : Fake some teamwork (1 commit)
3. `git commit` : Commit some work yourself (1 commit)
4. `git pull --rebase; git push` : Publish your work via rebasing

### Locked Main
Notes: on a large collaborative team it's likely that main is locked and requires some Pull Request process to merge changes.

Create another branch called feature and push that to the remote. Also reset your main back to be in sync with the remote otherwise you may have issues next time you do a pull and someone else's commit conflicts with yours.
1. `git switch -c feature` : created a branch called feature on (C2) 
2. `git push` : pushed the local commit (C2) to the remote repository
3. `git switch main` : moved the head from (C1) to (C2)
4. `git branch -f main C1` : forcibly moved the main from (C2) to (C1)
5. `git checkout feature` : moved the head from (C1) o/main to (C2) o/feature


