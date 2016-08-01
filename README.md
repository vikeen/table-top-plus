# Table Top Plus

## Database Setup

```sql
CREATE DATABASE table_top_plus;
CREATE ROLE table_top_plus with PASSWORD 'password';
ALTER DATABASE table_top_plus OWNER TO table_top_plus_user; 
```

## Deployment to Heroku

```
$ git push heroku master
$ heroku run python manage.py migrate
```

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
