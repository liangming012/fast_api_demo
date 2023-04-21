## FASTAPI
  
- ### 环境安装

    - ##### 单独安装每个库

            pip3 install fastapi
    
            pip3 install "uvicorn[standard]" 

            或安装所有依赖 pip3 install "fastapi[all]"
            
            pip3 install "python-jose[cryptography]"
    
            pip3 install "passlib[bcrypt]"
        
    - ##### 或批量安装requirements.txt里的内容
  
            pip3 install -r requirements.txt

- ### 运行程序

        uvicorn main:app --reload

- ### API 文档

    - 访问[交互式API 文档](http://127.0.0.1:8000/docs) ，
如果端口和host不同请自行修改 http://127.0.0.1:8000/docs

    - 访问[备选 API 文档](http://127.0.0.1:8000/redoc) ，
如果端口和host不同请自行修改 http://127.0.0.1:8000/redoc

## Alembic

- #### 环境安装

        pip3 install alembic

- #### 创建迁移环境
    
        alembic init alembic   (第二个 alembic为创建的迁移环境目录)

- #### 列出环境模板列表

        alembic list_templates

- #### 提交数据库迁移

        alembic revision -m "init"

- #### 数据库迁移升级到最新版本 （将最新版本真正映射到数据库）
  
        alembic upgrade head

- #### 查看当前版本数据库迁版本
  
        alembic current

- #### 数据库迁移历史版本
  
        alembic history --verbose

- #### 数据库迁移降级到最早版本  （将最早版本真正映射到数据库）
  
        alembic downgrade base

- #### 自动生成数据库迁移 （需要先配置env.py里的target_metadata和alembic.ini里的sqlalchemy.url）

        alembic revision --autogenerate -m "Added account table"

- #### 检查是否有新的操作

        alembic check

- #### 生成指定版本SQL语句

        alembic upgrade ae1027a6acf --sql > migration.sql

- #### 生成初始化版本SQL语句 （使用 start_version:end_version）

        alembic upgrade 1975ea83b712:ae1027a6acf --sql > migration.sql
