#! /bin/bash
# 初始化环境脚本
clear

init_venv(){
  if [ ! -d venv ]; then
    python3 -m venv venv
  fi
  . venv/bin/activate #加载自己python的虚拟环境
  pip3 install -r ./requirements.txt
  if [ ! -d alembic ]; then
    alembic init alembic
  fi
}



init_venv