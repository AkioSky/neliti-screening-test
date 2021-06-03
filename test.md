<!-- Compile with: pandoc -s test.md -c pandoc.css -o test.html --metadata pagetitle="Neliti Developer Screening Test" -->

<center>
![Neliti logo](neliti.svg){ width=300px }\ 

# Neliti Developer Screening Test
</center>

Welcome to Neliti! This is a brief screening test so we can get an idea of your knowledge of our stack - Python, Django and ES6. Submit your answer by email to `anton@neliti.com` in whatever form you think is best.

 - All answers should include a short explanation of your answer alongside the code.
 - If something is ambiguous, make a reasonable assumption, state the assumption in your answer and continue.
 - Use of external libraries is OK - use your judgement.
 - Code efficiency, clarity and style are all important.

**Recommended time: 90 minutes**

Good luck!
</center>

# Part 1 - Programming

## Question 1: Python

Complete the following function:

```python
def word_frequencies(url):
    """
    Downloads the content from the given URL and returns a dict {word -> frequency}
    giving the count of each word on the page. Ignores HTML tags in the response.
    :param url: Full URL of HTML page
    :return: dict {word -> frequency}
    """
    pass
```

## Question 2: Django ORM
Neliti is primarily a website that hosts academic publications. We record views and downloads of these publications in order to give statistics to our customers. This question is about analysing view and download data to produce some meaningful insights. Here is an excerpt of two models:

```python
class Hit(models.Model):

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    action = models.CharField(max_length=2, choices=ACTIONS)


class Publication(models.Model):

    title = models.CharField(max_length=200)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    # ... remaining fields omitted
```

A `Publication` represents a single journal article on our website ([example](https://www.neliti.com/publications/66008/)). Each time a user accesses a publication, we create a new `Hit` instance. A `Hit` represents either a single view or a single download of a publication. Publications are arranged into collections called journals - a `Journal` is a collection of publications of similar subject matter.

Your task is to write a function `get_journal_statistics()` that returns a `dict` mapping journals to summary statistics:
```python
def get_journal_statistics():
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    return summary
```

The return value should be a `dict` giving summary statistics for all journals in the form

```
{journal_id -> (total_views, total_downloads)}
```

where

* `journal_id` is the primary key of the journal instance in the `Journal` table
* `total_views` is the total number of `Hit` instances for all publications in that journal and all time with `action == Hit.PAGEVIEW`
* `total_downloads` is the total number of `Hit` instances for all publications in that journal and all time with `action == Hit.DOWNLOAD`.

All journals should be present in the result, and your code should correctly handle cases where there are no hits of the given type.

## Question 3: Django project

The specification of this task is vague - as most of the tasks in the real life. 🙂 You need to balance your time and imagination. If you are out of time, feel free to provide a very basic solution, but for bonus points, add any feature, UX or functional.
The task is simple: Create a small weather app in Django. 
The app can use the met.no service to acquire data via a GET call: https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25 - you need to pass the coordinates only. In the application you need to create a way to input the location and then using that information to display weather information. The whole UX is up to you. (Hint: you will only use fraction of the data from this service!) 

Please create a git repo and update it with your code - as it develops. Try to commit as frequently as possible - with meaningful comments - just as you would do in a real project. At the end of the task, please share the link to your repo.


## Question 4: Algorithms

Given a list of integers and a target integer, write a function that expresses the target integer by inserting `+` and `-` operations between the list items. For example:

```
>>> f([1, 2, 3, 4, 5], 9)
'9 = 1 + 2 - 3 + 4 + 5'
>>> f([2, 5, 60, -5, 3], 69)
'69 = 2 + 5 + 60 - -5 - 3'
>>> f([2, 5, 10], 50)
None
```

- All list items must be used in the solution, they cannot be skipped.
- If there are multiple ways to express the target integer, return any.
- If there is no way to express the target integer, return `None`.
- Your algorithm should be as efficient as possible.

Analyse the running time of your algorithm and discuss whether it is optimal.


# Part 2 - Other questions

Choose one of the following questions and tell us something interesting!

 1. Tell us one thing you are very opinionated about as a developer and why.
 2. Based on your understanding of our company, what do you think our biggest challenge is?
 3. What's one cool feature or idea you'd like to implement if you came to work for us?

# That's it! 🚀


