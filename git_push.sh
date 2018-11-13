#!bin/bash

git add ./*
git rm git_push.sh
git commit -m "latest version"
git pull origin master
git push origin master
