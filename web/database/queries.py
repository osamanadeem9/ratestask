"""
Some key points in our SQL query:
    -   Generate_dates ensures we get data for the complete date range, even if no route rate exist on a particular day.
    -   Recursive subqueries ensure that we get data from all region codes if user has requested data for a larger region.
        For example, querying north_europe_main region returns the data from region codes lying in
        both north_europe_main and uk_main region.
    -   Most of the querying has been done using SQL (rather than using python loops or conditions, which are rather
        simpler) to demonstrate SQL expertise as demanded in the task (inferenced from GitHub Readme file).
"""

RATES_QUERY = """with generate_dates as (
	SELECT generate_series(timestamp %(date_from)s
                     ,timestamp %(date_to)s
                     ,interval  '1 day')::date AS date
)
select date, avg_price from generate_dates
left join
	(Select pr.day as day,
	  case
		when COUNT(pr.price) < 3 then null
	  else
		ROUND(AVG(pr.price))
	  end as avg_price
	from prices pr
	Join ports po ON pr.orig_code = po.code
	Join ports po2 on pr.dest_code = po2.code
	where (pr.orig_code = %(origin)s or po.parent_slug in (WITH RECURSIVE subregions AS (
		SELECT slug FROM regions
		WHERE slug = %(origin)s
		UNION
		SELECT r.slug FROM regions r
		INNER JOIN subregions s ON s.slug = r.parent_slug) SELECT * FROM subregions))

	and (pr.dest_code = %(destination)s or po2.parent_slug IN (WITH RECURSIVE subregions AS (
		SELECT slug FROM regions
		WHERE slug = %(destination)s
		UNION
		SELECT r.slug FROM regions r
		INNER JOIN subregions s ON s.slug = r.parent_slug) SELECT * FROM subregions))

	GROUP by pr.day
	Order by pr.day) as daily_average_prices
on date = daily_average_prices.day;"""