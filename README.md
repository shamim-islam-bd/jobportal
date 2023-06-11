
# Project Title
# ( JobPortal )

JobPortal is a Fullstack Base Project Based on Python Django Django_rest_framework.





## Screenshots

Home: 

![App Screenshot](https://i.ibb.co/m48SkrV/Home.png)

Menu: 

![App Screenshot](https://i.ibb.co/dpfMjjZ/menu.png)

My jobs: 

User can manage all things related to job.
Create, Update, delete.

![App Screenshot](https://i.ibb.co/PCF7n0X/myjobs.png)

Job Details: 

![App Screenshot](https://i.ibb.co/hyjJh4h/Jobdetails.png)

Job Update: 

![App Screenshot](https://i.ibb.co/4MJRdh0/post-updatejobs.png)

Stats or Query job by value: 

![App Screenshot](https://i.ibb.co/vVm0qXj/stats.png)

Applied Jobs: 

![App Screenshot](https://i.ibb.co/8BXt8Df/appliedjobs.png)

filter Jobs: 

![App Screenshot](https://i.ibb.co/C10KJnb/filter.png)

User Profile Manage: 

![App Screenshot](https://i.ibb.co/FqLxXjK/user-profile-update.png)

Search Jobs: 

![App Screenshot](https://i.ibb.co/9YdZwwP/search-jobs.png)

Upload Resume: 

![App Screenshot](https://i.ibb.co/2sKT5s6/resumeupload.png)



## API Reference

#### Get all Jobs

```http
  GET {DOMAIN}/api/jobs/
```
User Can filter the jobs as their needs.

| Key | Value     | Description                |
| :-------- | :------- | :------------------------- |
| `education ` | `Bachelor ` |  |
| `jobType ` | `Internship ` |  |
| `experience` | `1 Year ` |  |
| `min_salary ` | `90 ` |  |
| `max_salary ` | `10000 ` |  |
| `keyword ` | `java ` |  |
| `location ` | `Dhaka ` |  |

#### Get Job

```http
 GET {DOMAIN}/api/jobs/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of job to fetch |

#### Add New Job 

```http
 POST {{DOMAIN}}/api/jobs/
```

| Value |  attributes  | Description                |
| :-------- | :------- | :------------------------- |
| `title`  | `attributes ` | **Required**. add title|
| `description`  | `attributes ` | **Required**. add description |
| `email`  | `attributes ` | **Required**. add email |
| `address`  | `attributes ` | **Required**. add address |
| `jobType`  | `attributes ` | **Required**. add jobType |
| `education`  | `attributes ` | **Required**. add education |
| `industry`  | `attributes ` | **Required**. add industry |
| `experience`  | `attributes ` | **Required**. add experience |
| `salary`  | `attributes ` | **Required**. add salary |
| `position`  | `attributes ` | **Required**. add position |
| `company`  | `attributes ` | **Required**. add company |
| `lastDate`  | `attributes ` | **Required**. add lastDate |


#### Delete Job

```http
 GET {DOMAIN}/api/jobs/${id}
```

#### Update Job

```http
 PUT {DOMAIN}/api/jobs/${id}
```


#### Apply for a Job.

```http
 POST {{DOMAIN}}/api/jobs/1/apply/
```

| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` id ` | `Authorization` | `Bearer + {Token}` |


#### Current User Applied Jobs.
```http
 GET {{DOMAIN}}/api/me/jobs/applied/
```
| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` ` | `Authorization` | `Bearer + {Token}` |

#### Current User Applied single Job Check.
```http
 GET {{DOMAIN}}/api/jobs/1/check/
```
| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` ` | `Authorization` | `Bearer + {Token}` |


#### Current User posted Jobs.
```http
 GET {{DOMAIN}}/api/me/jobs/
```
| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` ` | `Authorization` | `Bearer + {Token}` |


#### Applied Jobs Candidates 
```http
 GET {{DOMAIN}}/api/jobs/1/candidates/
```
| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` ` | `Authorization` | `Bearer + {Token}` |


#### stats / Query jobs with name, Locations
```http
 GET {{DOMAIN}}/api/stats/java
```
| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` ` | `Authorization` | `Bearer + {Token}` |


Account Action: 

#### Signup
```http
 POST {{DOMAIN}}/api/signup/
```
| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` ` | `first_name` | `demouser` |
| ` ` | `last_name` | `demouser` |
| ` ` | `email` | `demouser@gmail.com` |
| ` ` | `password` | `112233` |


#### Login
```http
 POST {{DOMAIN}}/api/token/
```
| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` ` | `username` | `demouser` |
| ` ` | `password` | `112233` |


#### Loggin user / me
```http
 GET {{DOMAIN}}/api/me/
```
| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` ` | `Authorization` | `Bearer + {token}` |


#### Token verify
```http
 POST {{DOMAIN}}/api/token/verify/
```
| Key     | Value | Body                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Bearer + {token}` |  ` ` |

Form-data: 

| Key     | Value |               |
| :-------- | :------- | :------------------------- |
| `token` | `{token}` |  ` ` |


#### Update User
```http
 POST {{DOMAIN}}/api/update/
```
| Parameter | Key     | Value                |
| :-------- | :------- | :------------------------- |
| ` ` | `first_name` | `demouser` |
| ` ` | `last_name` | `demouser` |
| ` ` | `email` | `demouser@gmail.com` |
| ` ` | `password` | `112233` |


#### Upload Resume
```http
 POST {{DOMAIN}}/api/token/verify/
```

Body: Form-data: 

| Key     | Value |               |
| :-------- | :------- | :------------------------- |
| `resume` | `CyberSecurity.pdf` |  ` ` |

## Installation


New starter Project with python Django steps : 

```bash
1. Create project folder & open with vsCode
2. python -m venv menv         - will create a virtual environment folder
3. pip install django        - install django in a same dir where menv exist.
3. menv\Scripts\activate       - it'll active your activate your venv
4. django-admin startproject myprojectname   -it'll create a project folder
5. pip install django djangorestframework    - it'll install djando
6. python manage.py runserver                - run server
```



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`='SECRET_KEY'

`DEBUG`=True
`DB_NAME`="jobportal"
`DB_USER`=postgres
`DB_PASSWORD`=shamim
`DB_HOST`=localhost
`DB_PORT`=5432

`GEOC0DER_API`=C7Y4PMK7lA5OrflsEXrVpiqR0AT3K7OT



## Developer  :

- [@shamim-islam-bd](https://github.com/shamim-islam-bd)

- [@Portfolio](https://shamim-99728.web.app/)




## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://shamim-99728.web.app)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shamim-islam-bd/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Shamim_islam_bd)


## License

[MIT](https://choosealicense.com/licenses/mit/)






