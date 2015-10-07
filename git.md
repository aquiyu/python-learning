Git / Github
=========

[github](http://github.com)

[python repo](https://github.com/aquiyu/python-learning)



## Basic use

##### Initialize a repo
  + in the directory, execute `git init`

###### Associate the repo with github
  * Find / Create the repository on github.com
  * On the right side of the page, find the Clone URL (Copy the SSH)
    * For example: `git@github.com:aquiyu/python-learning.git`
  * Execute `git remote add origin git@github.com:aquiyu/python-learning.git`


###### View status of working directory
  + `git status`

###### Mark changes for commitment / upload
  + `git add _file_name`
  + or `git add _dir_name_`
  + or `git add .` - adds everything

###### Comitting changes
  + `git commit -m 'Message for the changeset'`
  + This will only include files you've already added as per the previous step

###### Uploading changes
  + `git push origin master`
    + if it fails, it may be that you're not synchronized, try `git pull origin master` and  give it another go

###### Downloading changes
  + `git pull origin master`
