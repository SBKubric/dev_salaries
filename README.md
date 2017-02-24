# The DevSalaries Project

## Description
If you reading this you are really wanna know what is so special about it.

Ok, let's put it straight: I was given a task to code a tiny script
 so it could download data from [Superjob API](api.superjob.ru) and show to an user a pretty bar chart
 with average salaries for every programming language in the downloaded data set.

 I did this. And I even fixed that nice library that guys from Uber created a couple of years ago:
 [link](https://github.com/uber/multidimensional_urlencode)

## Installation
Nothing special. Almost. At. All.

You just need to:

 1. Fork this repo

 2. Clone it
 ```
 git clone 'ssh_link_to_forked_repo'
 ```

 3. Register your own application at [Superjob API](api.superjob.ru). Set the link to the app site as link to your fork of this repo.

 4. Export your API key as `SJ_API_KEY` environment variable:
 ```
 export SJ_API_KEY='your_api_key_here'
 ```
 Don't forget about environment variable scope, so launch script from the same environment.

 5. Oh, you probably don't want to collect garbage in your pip, so you should install a [virtual environment](docs.python-guide.org/en/latest/dev/virtualenvs/)!

 6. Nevertheless, after cloning a repo you should install requirements:
 ```
 pip install -r requirements
 ```

Aaaaaand you're done!

## Example

First of all, fetch all data from API by
```
python3 fetch_vacancies.py name_of_json_file
```

Then process the json file by
```
python3 prune_vacancies.py name_of_json_file name_for_new_json_file
```

Then draw a bar chart by
```
python3 analyze_vacancies.py name_for_new_json_file
```

Or you can just launch a one script
```
python3 just_do_it.py
```

## Disclaimer

