SELECT d.search_type_id, s.name, Count(d.*)
INNER JOIN SearchType as s ON d.search_type_id = s.id
FROM StopandSearchData as d
GROUP BY date_of_operation ASC