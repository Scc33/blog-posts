---
title: "Delete Duplicate Emails"
datePublished: Sat Sep 09 2023 19:45:03 GMT+0000 (Coordinated Universal Time)
cuid: clmcfqybv000108l26wr8gwmh
slug: delete-duplicate-emails
tags: python, pandas, sql, data-cleaning, leetcode

---

## The Problem

With this article, I will be covering the [delete duplicate emails Leetcode problem](https://leetcode.com/problems/delete-duplicate-emails/).

Leetcode describes this problem as easy. That's a super reasonable evaluation as the solution requires only basic SQL or Pandas knowledge.

The problem description is as follows:

> Write a solution to **delete** all duplicate emails, keeping only one unique email with the smallest `id`.
> 
> For SQL users, please note that you are supposed to write a `DELETE` statement and not a `SELECT` one.
> 
> For Pandas users, please note that you are supposed to modify `Person` in place.
> 
> After running your script, the answer shown is the `Person` table. The driver will first compile and run your piece of code and then show the `Person` table. The final order of the `Person` table **does not matter**.
> 
> ```plaintext
> +-------------+---------+
> | Column Name | Type    |
> +-------------+---------+
> | id          | int     |
> | email       | varchar |
> +-------------+---------+
> id is the primary key (column with unique values) for this table.
> Each row of this table contains an email. 
> The emails will not contain uppercase letters.
> ```

## The Solution

### Pandas

[Pandas](https://en.wikipedia.org/wiki/Pandas_(software)) is a great Python tool for data analysis and manipulation. Built into that library is the [drop duplicates](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html) function. Please note that the problem statement asks us to do this [in place](https://en.wikipedia.org/wiki/In-place_algorithm).

Using the Pandas library this can be achieved by first in-place sorting by the `id` field and then dropping the duplicates from `email`. We want to keep at least the first duplicated element.

```python
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)
```

Voila! I love these simple questions.

### SQL

In SQL we want to run a delete query. We will grab two copies of the `person` table and match them based on the `email`. To keep at least one of the solutions we only delete the entry with the higher `id` value. This keeps the `email` associated with the smallest `id`.

```sql
DELETE p1 
FROM person p1, person p2 
WHERE p1.email = p2.email AND p1.id > p2.id;
```

As with many problems, there are multiple ways to solve them. These Pandas and SQL solutions are but one way of approaching the delete duplicate question.