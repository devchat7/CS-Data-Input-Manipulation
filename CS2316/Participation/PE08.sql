#SELECT * FROM employees WHERE salary <= 30000;
#SELECT name,num_employees,total_revenue FROM stores WHERE name LIKE "c%" and total_revenue > 5000000 and total_revenue < 8000000
#SELECT name,total_revenue FROM stores ORDER BY total_revenue DESC LIMIT 5
#SELECT store_id , COUNT(salary) FROM stores,employees GROUP BY store_id;
#SELECT store_id , COUNT(salary) FROM stores,employees WHERE SUM(salary) > 50000
#SELECT * FROM students WHERE fname LIKE "b%";
#SELECT store_id, sum(salary) from stores join employees using (store_id) group by store_id having sum(salary)>50000'
#SELECT store_id,sum(salary) FROM stores JOIN employees USING (store_id) GROUP BY store_id HAVING sum(salary)>50000;
#SELECT store_id,count(*) FROM stores JOIN products USING (store_id) WHERE store_id> %s GROUP BY store_id having count(*)>%s
SELECT stores.store_id, COUNT(stores.store_id) FROM stores JOIN products on products.store_id =stores.store_id WHERE stores.store_id >"%s" GROUP BY stores.store_id HAVING COUNT(stores.store_id)>"%s" 