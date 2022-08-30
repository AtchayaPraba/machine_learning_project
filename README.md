# machine_learning_project
My first end to end ML project.

## Software and account Resquirement
1. [Github Account] (https://github.com)
2. [Heroku Account] (https://dashboard.heroku.com/login)
3. [VS code IDE] (https://code.visualstudio.com/download)
4. [GIT cli] (https://git-scm.com/downloads)
 
## virtual environment
### Create conda environment 
```
conda create -p venv python==3.7 -y
```

### Activate conda environment
```
conda activate venv
```
OR
```
conda activate venv/
```
OR
```
conda init cmd.exe
```
AND
```
close and reopen VS code
```

## Command to install requirements.txt file
```
pip install -r requirements.txt
```  

## Add files to Git Repo
To maintain the "version control system"
```
git add <file_name>
```
OR
```
git add <file_name1>, <file_name2>, <file_name3>, ...<file_namen>
```
OR
```
git add .
```

## Check file status
```
git status
```
## Save / commit the changes for version control 
```
git commit
```
OR 
```
git commit -m "any_message"
```

## View all the versions
```
git log
```

## To send version / changes to github repo
origin --> current git repo's remote url
```
git push origin main
```

## To Check remote url
```
git remote -v
```

## To download files form remote url
```
git pull
```
OR
```
git fetch
```

## To Check branch of the repo
```
git branch
```

## To setup CI/CD pipeline we need three information form "heroku"
1. HEROKU_EMAIL = atchayapraba93@gmial.com
2. HEROKU_APP_KEY = d439ad07-f68c-4414-b355-de5bd5024e1e
3. HEROKU_APP_NAME = ml-project-pipelines-1

## Build Docker image
```
docker build -t <image_name>:<tagname> .
```
>> image_name is always "lowercase"