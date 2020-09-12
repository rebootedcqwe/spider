#!/bin/bash
#git提交
if [ `whoami` != "root" ];then
 echo "root is no"
 exit 0
else
 echo "root is ok"
fi

directory=".git"
if [ ! -d "$directory" ]; then
  echo ".git does not exist,need git init  "
  exit 0
else
  echo ".git directory   is  exist!!!"
fi
read -p "Please input your directory: " name
cd $name
git add -A
git status
read -p "Please input your commit: " name2
git commit -m "$name2"   
git push origin master
