-- CREATE TYPE pavilion_name as ENUM ('asia', 'europe', 'north america', 'south america', 'australia');
-- CREATE TYPE item_type as ENUM ('toy', 'furniture', 'treat', 'medicine');

CREATE TABLE IF NOT EXISTS items (
    id SERIAL ,
    cost DECIMAL,
    weight DECIMAL ,
    type item_type ,
    expiraton_date DATE
);
CREATE TABLE IF NOT EXISTS aviary (
    id SERIAL ,
    size decimal ,
    pavilion pavilion_name,
    outdoors boolean ,
    construction_date DATE ,
    cleaning_stuff_size INT
);
CREATE TABLE IF NOT EXISTS animals (
    id SERIAL ,
    aviary_id INT,
    species VARCHAR (20),
    weight decimal ,
    height decimal ,
    endangered boolean ,
    age INTEGER
);

CREATE TABLE IF NOT EXISTS items_to_animals (
    id SERIAL ,
    animal_id INT,
    item_id INT,
    availability boolean
);
