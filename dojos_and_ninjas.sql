SELECT * FROM dojos;
INSERT INTO dojos (name)
VALUES ('Seattle'), ('San Jose'), ('Burbank'), ('OC'), ('Dallas'), ('Boise'), ('Chicago');
SELECT * FROM dojos;

SELECT* FROM dojos;


INSERT INTO ninjas(dojo_id, first_name, last_name, age)
VALUES (1, 'Margaret', 'Lasseter', 40);

select * from ninjas;


INSERT INTO ninjas(dojo_id, first_name, last_name, age)
VALUES (1, 'Daniel', 'Murcia', 30), (1, 'Pachito', 'McLekkerson', 8);

SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id;