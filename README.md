### I'am creating a Bug tracker with Django and Bootstrap 5

### Features

* Register user
* Login
* Password reset
* Add,update,delete projects
* Add update,delete project bugs
* Add update,delete messages for project bugs
* Project detail page
* Bug detail page

![2022-03-26 12 58 41 127 0 0 1 4464cc509d53](https://user-images.githubusercontent.com/60063451/160238343-0d5d3301-07a2-43d3-ac59-7f4971c512be.jpg)

### Password reset

![2022-03-26 13 04 27 127 0 0 1 c760fe6e09a9](https://user-images.githubusercontent.com/60063451/160238733-1a2eb692-3b0c-4d34-8b73-bf1a6d148163.jpg)
![2022-03-26 13 07 29 127 0 0 1 73262c97f133](https://user-images.githubusercontent.com/60063451/160238738-35e42225-f38e-402b-8826-3b016be4d22e.jpg)
![2022-03-26 13 05 13 127 0 0 1 6c9efc7edae0](https://user-images.githubusercontent.com/60063451/160238751-02810007-5611-4581-8c1c-04b89d8ff261.jpg)
![2022-03-26 13 05 33 127 0 0 1 2f08541778f2](https://user-images.githubusercontent.com/60063451/160238752-645b68ab-2572-4550-9cda-5c20eb8beb79.jpg)

### Login validation


![2022-03-26 13 22 46 127 0 0 1 f65716f6f81c](https://user-images.githubusercontent.com/60063451/160239380-1171636b-4c5d-4027-94d0-4e8754f7b841.jpg)
![2022-03-26 13 24 07 127 0 0 1 59aa92d2cd04](https://user-images.githubusercontent.com/60063451/160239388-368c8d2c-9c0b-4a92-95d6-8d2c4a4f7ac6.jpg)

### Sign up success
![2022-03-26 13 24 44 127 0 0 1 6409ee5daf3e](https://user-images.githubusercontent.com/60063451/160239390-dd3becf8-0a1a-4f77-9e05-2b4d24708fea.jpg)


### Create project


![2022-03-26 15 42 00 127 0 0 1 25e49c257a50](https://user-images.githubusercontent.com/60063451/160244528-efaaf74c-88d1-4369-bbee-2682e517eae8.jpg)

### Project details page, add bugs

![2022-03-26 16 34 21 127 0 0 1 f8194f286174](https://user-images.githubusercontent.com/60063451/160246511-1a154b07-d201-4cae-8e4b-fe9584a9056f.jpg)

![2022-03-26 16 36 27 127 0 0 1 428bc05e863e](https://user-images.githubusercontent.com/60063451/160246641-94849edf-f6b7-43f4-8c1e-fbc4a2ed3d3e.jpg)

### I made two functions on the project model to get resolved and unresolved bugs.

``` python

def unresolved_bugs(self):
  return self.bug_set.filter(state='UN')

def resolved_bugs(self):
  return self.bug_set.filter(state='RE')

```

### To get the count of the resolved and unresolved bugs I 'am using template tags in the html template.
``` html
<h2>
  Unresolved bugs:
  {% comment %} {{ unresolved_bugs }} {% endcomment %}
  {{ project.unresolved_bugs | length }}
</h2>

```
